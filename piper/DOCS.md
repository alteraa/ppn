# Checkpoint Loading Fix for Piper Fine-tuning

## Problem
The fine-tuning script failed with error:
```
error: Subcommand 'fit' does not accept option 'model.sample_bytes'
Parsing of ckpt_path hyperparameters failed!
```

## Root Cause
The checkpoint file contains hyperparameters (`sample_bytes`, `channels`, etc.) that are not recognized by the current VitsModel class. Lightning CLI tries to parse these unknown parameters and fails.

## Solution

### 1. Filter Checkpoint Hyperparameters
Created a script to remove unknown hyperparameters from the checkpoint:

```python
# filter_checkpoint.py - removes unknown hyperparameters
python filter_checkpoint.py input.ckpt output_filtered.ckpt
```

### 2. Update VitsModel (Alternative)
Modified the VitsModel class to ignore unknown parameters:

```python
# In lightning.py
self.save_hyperparameters(ignore=['sample_bytes'])
```

### 3. Update Fine-tune Script
Changed the checkpoint path to use the filtered version:

```bash
--ckpt_path /workspace/voices/tr/turkish_model_filtered.ckpt
```

## Files Modified
- `/workspace/filter_checkpoint.py` - New script to filter checkpoints
- `/workspace/fine_tune.sh` - Updated to use filtered checkpoint
- `/workspace/piper1-gpl/src/piper/train/vits/lightning.py` - Added ignore parameter
- `/workspace/piper1-gpl/src/piper/train/__main__.py` - Added PosixPath to safe globals

## Usage
1. Filter the checkpoint: `python filter_checkpoint.py original.ckpt filtered.ckpt`
2. Run fine-tuning: `./fine_tune.sh`

--- 

```bash
root@31a0cf5afef8:/workspace/piper1-gpl# git diff 
diff --git a/src/piper/train/__main__.py b/src/piper/train/__main__.py
index a2713d8..debe345 100644
--- a/src/piper/train/__main__.py
+++ b/src/piper/train/__main__.py
@@ -6,6 +6,8 @@ from lightning.pytorch.cli import LightningCLI
 from .vits.dataset import VitsDataModule
 from .vits.lightning import VitsModel
 
+from pathlib import PosixPath
+
 _LOGGER = logging.getLogger(__package__)
 
 
@@ -26,6 +28,7 @@ def main():
     torch.backends.cuda.matmul.allow_tf32 = True
     torch.backends.cudnn.allow_tf32 = True
     torch.backends.cudnn.deterministic = False
+    torch.serialization.add_safe_globals([PosixPath])
     _cli = VitsLightningCLI(  # noqa: ignore=F841
         VitsModel, VitsDataModule, trainer_defaults={"max_epochs": -1}
     )
diff --git a/src/piper/train/vits/lightning.py b/src/piper/train/vits/lightning.py
index 1c5f2e1..824246a 100644
--- a/src/piper/train/vits/lightning.py
+++ b/src/piper/train/vits/lightning.py
@@ -76,7 +76,7 @@ class VitsModel(L.LightningModule):
         **kwargs,
     ):
         super().__init__()
-        self.save_hyperparameters()
+        self.save_hyperparameters(ignore=['sample_bytes'])
 
         if isinstance(self.hparams.resblock_kernel_sizes, str):
             self.hparams.resblock_kernel_sizes = ast.literal_eval(
root@31a0cf5afef8:/workspace/piper1-gpl# 
```

---

# filter_checkpoint.py
```python
#!/usr/bin/env python3
import torch
import sys

def filter_checkpoint(input_path, output_path):
    # Load checkpoint
    ckpt = torch.load(input_path, weights_only=False, map_location="cpu")
    
    # Define known parameters
    known_params = {
        'batch_size', 'sample_rate', 'num_symbols', 'num_speakers',
        'resblock', 'resblock_kernel_sizes', 'resblock_dilation_sizes',
        'upsample_rates', 'upsample_initial_channel', 'upsample_kernel_sizes',
        'filter_length', 'hop_length', 'win_length', 'mel_channels',
        'mel_fmin', 'mel_fmax', 'inter_channels', 'hidden_channels',
        'filter_channels', 'n_heads', 'n_layers', 'kernel_size',
        'p_dropout', 'n_layers_q', 'use_spectral_norm', 'gin_channels',
        'use_sdp', 'segment_size', 'learning_rate', 'learning_rate_d',
        'betas', 'betas_d', 'eps', 'lr_decay', 'lr_decay_d',
        'init_lr_ratio', 'warmup_epochs', 'c_mel', 'c_kl', 'grad_clip',
        'dataset'
    }
    
    # Filter hyperparameters
    if "hyper_parameters" in ckpt:
        filtered_hparams = {k: v for k, v in ckpt["hyper_parameters"].items() 
                          if k in known_params}
        ckpt["hyper_parameters"] = filtered_hparams
        print(f"Filtered out {len(ckpt['hyper_parameters']) - len(filtered_hparams)} unknown parameters")
    
    # Save filtered checkpoint
    torch.save(ckpt, output_path)
    print(f"Filtered checkpoint saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filter_checkpoint.py <input_checkpoint> <output_checkpoint>")
        sys.exit(1)
    
    filter_checkpoint(sys.argv[1], sys.argv[2])
```

---

## Why torch <=2.2.x need?

This error is **not because your checkpoint is “bad”**, but because **PyTorch ≥ 2.4 (including 2.5.1)** changed the default checkpoint loading behavior for **security reasons**.

### What changed in PyTorch 2.4+

* `torch.load(..., weights_only=True)` is now **strict**
* It **refuses to unpickle non-tensor objects** (like `pathlib.PosixPath`)
* Lightning CLI **forces `weights_only=True`** internally
* Older checkpoints (including many Piper / Lightning VITS checkpoints) **contain metadata objects**, so they fail

That’s exactly what this line means:

```
Unsupported global: pathlib.PosixPath
```

---

## Best Torch Version for Piper / VITS Training

### ✅ **Recommended (most compatible)**

**PyTorch 2.1.x or 2.2.x**

These versions:

* Load legacy Lightning checkpoints without issues
* Are widely tested with Piper, VITS, Lightning
* Do **not** enforce strict `weights_only` loading

📌 **Best choice:**

```
torch==2.1.2
```

or

```
torch==2.2.2
```

---

## Versions to Avoid (for now)

❌ **PyTorch 2.4.x**
❌ **PyTorch 2.5.x**

Unless you:

* Patch Lightning internals, or
* Manually allowlist globals, or
* Resave the checkpoint

---

## Quick Fix Options (Choose One)

### 🔹 Option 1 — Downgrade PyTorch (EASIEST & SAFEST)

```bash
pip uninstall torch -y
pip install torch==2.1.2
```

This is what most Piper users do.

---

### 🔹 Option 2 — Allowlist PosixPath (Advanced)

If you **trust the checkpoint source**:

```python
from pathlib import PosixPath
import torch.serialization

torch.serialization.add_safe_globals([PosixPath])
```

⚠️ This must run **before** Lightning loads the checkpoint
(not trivial with LightningCLI).

---

### 🔹 Option 3 — Resave the Checkpoint (One-time fix)

Load once with `weights_only=False`, then resave:

```python
ckpt = torch.load("model.ckpt", weights_only=False)
torch.save(ckpt["state_dict"], "weights_only.pt")
```

But Piper / Lightning expects full checkpoints, so this is usually not ideal.

---

## ✅ Final Recommendation

**Use this combo for Piper training:**

* **torch 2.1.2**
* **lightning < 2.2**
* **python 3.10 or 3.11**

This avoids **all checkpoint loading issues** and matches upstream Piper expectations.

If you want, tell me:

* Piper version
* Lightning version
* Whether this is training or inference

and I’ll give you an exact `requirements.txt` that works.
