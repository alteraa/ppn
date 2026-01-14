import os
import argparse
import subprocess
import tempfile
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert deb packages to zip files.",
    )
    parser.add_argument(
        "input",
        help="Path to deb file or dir containing deb files.",
        type=Path,
    )
    parser.add_argument(
        "output",
        help="Path to output file or dir.",
        type=Path,
        nargs="?",
        default=Path.cwd() / "setup.zip",
    )
    return parser.parse_args()


def clone_setup_repo():
    try:
        repo_url = "https://github.com/atasoglu/ask2api"
        # branch = "debian"
        branch = "main"
        repo_dir = Path(tempfile.mkdtemp())
        subprocess.run(
            [
                "git",
                "clone",
                "--branch",
                branch,
                repo_url,
                repo_dir,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        shutil.rmtree(
            repo_dir / ".git",
            onerror=lambda func, path, exc: (os.chmod(path, 0o777), func(path)),
        )
        return repo_dir
    except Exception as ex:
        _exit(f"Failed to clone repo: {ex}")


def _exit(mssg):
    raise SystemExit(mssg)


def main():
    args = parse_args()
    if not args.input.exists():
        _exit(f"{args.input} does not exist!")
    deb_files = []
    if args.input.is_dir():
        deb_files = list(args.input.glob("*.deb"))
        if not deb_files:
            _exit(f"No .deb files found in {args.input}")
    else:
        if args.input.suffix != ".deb":
            _exit(f"{args.input} is not a .deb file!")
        deb_files = [args.input]
    if args.output.is_dir():
        args.output.mkdir(parents=True, exist_ok=True)
        output_path = args.output / "setup.zip"
    else:
        if args.output.suffix != ".zip":
            _exit(f"{args.output} is not a .zip file!")
        output_path = args.output
    repo_dir = clone_setup_repo()
    for deb_file in deb_files:
        shutil.copy2(deb_file, repo_dir)
    shutil.make_archive(
        base_name=output_path.with_suffix(""),
        format="zip",
        root_dir=repo_dir,
    )
    shutil.rmtree(repo_dir)


if __name__ == "__main__":
    main()
