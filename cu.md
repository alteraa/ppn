🎓 NVIDIA CUDA: Derinlemesine Teknik Rehber (A'dan Z'ye)
CUDA, sadece bir yazılım kütüphanesi değil, donanımla yazılımın kusursuz bir senfonisidir. Bu rehber, sizi bir kullanıcıdan bir GPU Geliştiricisine dönüştürmeyi hedefler.
1. Donanım Mimarisi: GPU'nun İçinde Ne Oluyor?
GPU, binlerce küçük çekirdekten oluşur; ancak bu çekirdekler rastgele dizilmemiştir. Hiyerarşiyi anlamak, performanslı kod yazmanın anahtarıdır.
Streaming Multiprocessors (SM)
Her GPU, birden fazla Streaming Multiprocessor (SM) biriminden oluşur. Bir SM içinde:
 * CUDA Cores: Temel matematiksel işlemleri yapan birimler.
 * Tensor Cores: AI ve matris çarpımları için özelleşmiş birimler.
 * Warp Scheduler: İş parçacıklarını (threads) yöneten kontrolcü.
Warp ve SIMT Yapısı
CUDA, SIMT (Single Instruction, Multiple Threads) modelini kullanır.
 * 32 thread bir araya gelerek bir Warp oluşturur.
 * Bir Warp içindeki tüm thread'ler aynı anda aynı komutu çalıştırır ancak farklı veriler üzerinde işlem yaparlar.
 * Warp Divergence: Eğer bir if-else bloğunda bazı thread'ler farklı yola girerse, performans düşer (donanım her iki yolu da sırayla çalıştırmak zorunda kalır).
2. CUDA Programlama Modeli: Threads, Blocks, Grids
Kodunuzu GPU'ya gönderdiğinizde, onu bir hiyerarşiye oturtmanız gerekir:
 * Thread: En küçük işlem birimi.
 * Block (Blok): Thread'lerden oluşan grup. Bir blok içindeki thread'ler birbirleriyle Shared Memory üzerinden haberleşebilir. (Genellikle blok başına 256 veya 512 thread önerilir).
 * Grid: Bloklardan oluşan tüm yapı. Ekran kartının tamamına yayılan iş yüküdür.
3. Bellek Hiyerarşisi (Hız vs. Kapasite)
CUDA'da en büyük darboğaz bellek transferidir. Veriyi nereye koyduğunuz, kodun hızını 100 kat değiştirebilir.
| Bellek Tipi | Lokasyon | Hız | Kapsam |
|---|---|---|---|
| Registers | Çip Üstü | En Hızlı | Sadece ilgili Thread |
| Shared Memory | Çip Üstü (SM) | Çok Hızlı | Blok içindeki tüm Thread'ler |
| Global Memory | VRAM (DRAM) | Yavaş | Tüm Grid (Herkes erişebilir) |
| Constant Memory | VRAM (Cache'li) | Hızlı (Read-only) | Tüm Grid |
> Altın Kural: Veriyi mümkün olduğunca Shared Memory'de tutun ve Global Memory'ye (VRAM) erişimi minimize edin.
> 
4. RTX 5000 Serisi (Blackwell) ve CUDA 12.8 Yenilikleri
2026 itibarıyla en güçlü donanım olan Blackwell mimarisi, hesaplama limitlerini zorluyor:
 * FP4 Desteği: 4-bit kayan nokta hassasiyeti. Bu, AI modellerinin (LLM) bellek kullanımını devasa oranda azaltırken hızı 2.5 kat artırıyor.
 * 5. Nesil Tensor Core: Transformer modelleri için özel donanımsal hızlandırma.
 * GDDR7 Bellek: Veri yolu genişliği saniyede 1.5 TB'ı aşarak veri darboğazını (bottleneck) büyük ölçüde çözüyor.
 * NVLink 5.0: Birden fazla GPU arasındaki iletişim hızını saniyede 1.8 TB'a çıkararak devasa cluster kurulumlarını kolaylaştırıyor.
5. Profesyonel Kurulum: Docker ve NVIDIA Container Runtime
Bir işletim sistemini kirletmeden en güvenli CUDA kurulumu şöyledir:
 * Sürücü Yükle: Sadece güncel NVIDIA Driver'ı yükleyin (Toolkit'e gerek yok).
 * Docker & Toolkit Kur: ```bash
   Linux (Ubuntu) örneği
   curl -fsSL https://www.google.com/search?q=https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
   sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
   
 * Konteyner Başlat:
   # PyTorch ile Blackwell mimarisi uyumlu çalışma
docker run --gpus all -it --rm pytorch/pytorch:2.5.1-cuda12.8-cudnn9-devel

6. CUDA Koduna Giriş: İlk Kernel (C++)
Basit bir vektör toplama işlemi üzerinden GPU'nun nasıl düşündüğünü anlayalım:
// Bu fonksiyon GPU üzerinde çalışacak (__global__)
__global__ void vectorAdd(const float *A, const float *B, float *C, int numElements) {
    // Thread index'ini hesapla
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < numElements) {
        C[i] = A[i] + B[i]; // Paralel toplama
    }
}

int main() {
    // 1. Host (CPU) ve Device (GPU) belleklerini ayır
    // 2. Veriyi CPU'dan GPU'ya kopyala (cudaMemcpy)
    // 3. Kernel'ı başlat (Launch)
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, n);
    // 4. Sonucu GPU'dan geri al
}

7. Bakım ve Optimizasyon (Best Practices)
CUDA ile çalışan bir sistemi "maintain" etmek için şu araçları ve yöntemleri kullanmalısınız:
 * Profiling (Nsight Systems): Kodunuzun nerede yavaşladığını (CPU/GPU transferi mi, işlem mi?) görsel olarak görün.
 * Unit Testing: GPU kodlarını test etmek zordur. GTest gibi kütüphaneleri kullanarak küçük kernel testleri yazın.
 * Memory Coalescing: Thread'lerin bitişik bellek adreslerine erişmesini sağlayın. Bu, Global Memory hızını dramatik şekilde artırır.
 * Unified Memory: cudaMallocManaged kullanarak bellek yönetimini CUDA'ya bırakın; ancak yüksek performans için manuel yönetime (cudaMalloc) geçiş yapmayı öğrenin.
8. Yazılım Portatifliği
Yazdığınız bir CUDA kodu sadece sizin kartınızda mı çalışacak?
 * PTX (Parallel Thread Execution): Kodunuzu derlerken -gencode bayraklarını kullanarak hem eski (Ampere) hem yeni (Blackwell) kartlar için optimize edilmiş ikili dosyalar (binaries) oluşturun.
 * Cross-platform: Windows (WSL2) ve Linux arasında CUDA kodları Docker sayesinde %100 taşınabilir durumdadır.
CUDA dünyası sürekli genişliyor. Bir sonraki adımda, Blackwell (RTX 5000) serisinin sunduğu FP4 veri tipini kullanarak bir LLM (Büyük Dil Modeli) optimizasyonu yapmak ister misin? Yoksa doğrudan C++ ile ilk kernel'ımızı derleyip performans testleri mi yapalım?
