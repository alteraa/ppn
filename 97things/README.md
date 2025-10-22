---
marp: true
title: Her Programcının Bilmesi Gereken 97 Şey
theme: default
class:
  - lead 
paginate: true
style: |
  section {
    font-size: 28px;
    padding-top: 85px;
  }
  section h3 {
    position: fixed;
    top: 10px;
    left: 30px;
    width: 100%;
    padding: 10px 0 20px 0;
    z-index: 1;
  }
  section h3::after {
    content: '';
    display: block;
    margin-top: 15px;
    margin-left: 0;
    width: 96%;
    border-bottom: 1px solid #ccccccaa;
    opacity: 0.7;
  }
  header {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, 1150%);    
    width: auto;
    text-align: center;
    z-index: 2;
  }
  
---

## :bulb: Her Programcının Bilmesi Gereken 97 Şey

---

<!-- footer: 23.10.2025 -->
<!-- header: :bulb: Her Programcının Bilmesi Gereken 97 Şey -->

### Giriş

<div style="display: flex; align-items: center; gap: 32px; min-height: 320px;">
  <div style="flex: 1; min-width: 180px;">
    <img src="cover.jpg" alt="97 Things Every Data Engineer Should Know kapak görseli" style="max-width: 100%; height: auto; border-radius: 10px;">
  </div>
  <div style="flex: 2;">
    Bu sunum, <em>97 Things Every Data Engineer Should Know: Collective Wisdom from the Experts</em> (O'Reilly) kitabının yapay zeka tarafından özetlenip derlenmiş bir versiyonudur. İçerikte hata veya eksiklikler bulunabilir; lütfen bu özeti okurken dikkatli yaklaşınız.
  </div>
</div>


---

### 1. İhtiyatlı Davran

- **Teknik borç**, kısa vadede fayda sağlasa da uzun vadede **faiz** ödemesi gerektiren bir yük oluşturur.
- **Doğru yapmak** ile **hızlı yapmak** arasında seçim yaparken, teknik borç birikmesine neden olacak hızlı çözümlerden kaçınılmalıdır.
- Teknik borç alındığında, bu borç **izlenmeli** ve **hızla geri ödenmelidir**; aksi takdirde proje değeri olumsuz etkilenir.
- Teknik borcun **faizini takip etmek**, projenin iş değeri üzerindeki etkisini görünür kılar ve geri ödeme önceliklendirmesini sağlar.

---

### 2. Fonksiyonel Programlama Prensiplerini Uygula

- **Fonksiyonel programlama** paradigmasını derinlemesine anlamak, yazdığınız kodun kalitesini önemli ölçüde artırabilir.
- **Referans şeffaflığı**, aynı girdilerle her zaman aynı sonuçları veren fonksiyonlar anlamına gelir ve bu, kodun hata oranını azaltır.
- **Değişkenlerin aşırı mutasyonu**, hataların başlıca nedenidir ve bu durum, test odaklı tasarım ile azaltılabilir.
- Fonksiyonel programlama dillerini öğrenmek, bu prensiplerin içselleştirilmesine yardımcı olur ve diğer programlama alanlarına uygulanabilir.

---

### 3. "Kullanıcı Ne Yapardı?" Diye Sor (Sen Kullanıcı Değilsin)

- **Kullanıcılar** programcılar gibi düşünmez, bu yüzden yazılım geliştirirken onların bakış açısını anlamak için onları izlemek önemlidir.
- **Görevleri** kullanıcıların nasıl tamamladığını gözlemlemek, tasarım kararlarını kullanıcıların gerçek davranışlarına göre şekillendirmeye yardımcı olur.
- **Kullanıcılar** sıkıştıklarında odaklarını daraltır, bu yüzden yardım metinleri ve araç ipuçları sorunlu alanların hemen yanında olmalıdır.
- **Kullanıcıların** söyledikleri ile yaptıkları arasında fark olabilir, bu yüzden kullanıcı gereksinimlerini anlamanın en iyi yolu onları izlemektir.

---

### 4. Kodlama Standartlarını Otomatikleştir

- **Kodlama standartlarını** otomatikleştirerek, projenin başından sonuna kadar tutarlı bir kod yapısı sağlanabilir.
- **Kod formatlama işlemlerini** derleme sürecinin bir parçası haline getirerek, her derlemede otomatik olarak çalıştırılmasını sağlayın.
- **Statik kod analizi araçları** kullanarak istenmeyen antipattern'leri tarayın ve bulunduklarında derlemeyi durdurun.
- Kodlama standartlarını **dinamik** tutarak, projenin ihtiyaçlarına göre güncellenmesini sağlayın.

---

### 5. Güzellik Sadelikte Yatar

- **Güzel kod** yazmak için **sadelik** en önemli unsurdur ve bu, kodun okunabilirliğini, sürdürülebilirliğini ve geliştirme hızını artırır.
- Kodun her bir parçası, **tek bir sorumluluğa** sahip basit objeler ve açıklayıcı isimlere sahip odaklanmış yöntemlerle **basit** tutulmalıdır.
- **Kısa yöntemler** (5-10 satır) yazmak, bazılarına aşırı gelebilir ama bu, kodun temiz ve test edilebilir kalmasını sağlar.
- **Sadelik**, sistemlerin zamanla sürdürülebilir ve hızlı geliştirilmesini sağlayarak, kodun güzelliğini ve etkinliğini artırır.

---

### 6. Yeniden Yapılandırmadan Önce

- **Mevcut kod tabanını ve testleri değerlendirmek**, kodun güçlü ve zayıf yönlerini anlamanıza yardımcı olur, böylece hatalardan kaçınarak güçlü yönleri koruyabilirsiniz.
- **Her şeyi yeniden yazma cazibesinden kaçının**; mevcut kodun test edilmiş ve gözden geçirilmiş olduğunu unutmayın, bu yüzden mümkün olduğunca yeniden kullanın.
- **Birçok küçük değişiklik yapmak**, sistem üzerindeki etkileri daha kolay değerlendirmeye olanak tanır ve büyük değişikliklerin getirdiği baskı ve hatalardan kaçınır.
- **Kişisel tercihler ve yeni teknolojiler**, yeniden yapılandırma için yeterli sebepler değildir; maliyet-fayda analizi yapmadan bu tür değişikliklere gitmekten kaçının.

---

### 7. Paylaşımdan Sakının

- **Yeniden kullanım** her zaman iyi bir şey değildir; **bağlamı** dikkate almak önemlidir.
- **Bağımlılıkları** artırmak, sistemin bakım maliyetlerini ve karmaşıklığını artırabilir.
- **Paylaşılan kod** oluştururken, bu kodun sistemin diğer bölümleri üzerindeki etkilerini dikkatlice değerlendirin.
- **Bağlamı kontrol edin** ve yalnızca uygun olduğunda kod paylaşımına gidin.

---

### 8. İzci Kuralı

- **Kodunuzu** her kontrol ettiğinizde, modülü bulduğunuzdan daha temiz bir şekilde geri bırakmayı hedefleyin.
- **Küçük iyileştirmeler** yaparak yazılım sistemlerinizin zamanla daha iyi hale gelmesini sağlayın.
- **Takım çalışması** ve sistemin bütününe olan özen, bireysel kod parçalarına olan ilgiden daha önemlidir.
- Kodda **dağınıklık bırakmak**, sosyal olarak kabul edilemez bir davranış olarak görülmelidir.

---

### 9. Başkalarını Suçlamadan Önce Kendi Kodunuzu Kontrol Edin

- **Kendi kodunuzun hatalı olabileceğini kabul edin** ve hatayı önce kendi kodunuzda arayın.
- **Derleyici hatalarının nadir olduğunu unutmayın** ve enerjinizi kodunuzdaki hatayı bulmaya harcayın.
- **Farklı araçların ve sürümlerin varsayımlarını sorgulayın** ve başkalarının sorunlarını anlamaya çalışın.
- **Çoklu iş parçacıklı sistemlerde basitliği tercih edin**, çünkü bu tür sistemlerde hata ayıklamak daha zordur.

---

### 10. Araçlarınızı Dikkatli Seçin

- **Modern uygulamalar** genellikle sıfırdan inşa edilmez, mevcut araçlar ve kütüphaneler kullanılarak oluşturulur, bu da geliştiricilerin zamanını daha verimli kullanmalarını sağlar.
- **Araç seçimi** yaparken, farklı araçların farklı varsayımlara dayanabileceğini ve bu durumun mimari uyumsuzluklara yol açabileceğini göz önünde bulundurmalısınız.
- **Araçların yaşam döngüleri** farklılık gösterebilir ve bir aracın güncellenmesi diğer araçlarla uyumsuzluklara neden olabilir, bu da bakım zorluklarını artırır.
- **Dış araçları** iş alanı nesnelerinden arayüzler ve katmanlar aracılığıyla izole etmek, gerektiğinde aracı değiştirmeyi kolaylaştırır ve uygulamanın daha küçük ve yönetilebilir kalmasını sağlar.

---

### 11. Alanın Dilinde Kod Yazın

- **Alan** terimleriyle kod yazmak, kodun anlaşılabilirliğini ve bakımını kolaylaştırır.
- **Kullanıcı tanımlı türler** kullanarak, alan kavramlarını ve ilişkilerini doğrudan modelleyebilirsiniz.
- **Gizli anlaşmalar** yerine, iş kurallarını açıkça kodda ifade etmek, gelecekteki geliştiricilerin işini kolaylaştırır.
- **Kapsülleme** ile birlikte alan modelini açıkça tanımlamak, kodun evrimleşmesini ve bakımını kolaylaştırır.

---

### 12. Kod Tasarımdır

- **Kod tasarımdır** ve bu, yazılım geliştirme sürecinin yaratıcı bir süreç olduğunu vurgular.
- **Yazılım krizi**, tasarım krizine dönüşmüştür; çünkü kaliteli ve doğrulanmış tasarımlar talebi, yaratma kapasitemizi aşmaktadır.
- **Otomatik testler**, yazılım tasarımının tamamlanması için gereklidir ve bu testlerin etkinliğini artırmak için büyük sistemlerin durum alanını kontrol altına alıyoruz.
- **Büyük tasarımlar**, kendilerini zanaatlarının ustalığına adayan büyük tasarımcılar tarafından üretilir; bu, kod için de geçerlidir.

---

### 13. Kod Düzeni Önemlidir

- **Kod düzeni**, kodun okunabilirliğini ve anlaşılabilirliğini artırarak hata yapma olasılığını azaltır.
- **Kodun taranabilir olması**, geliştiricilerin kodu daha hızlı anlamasına ve değişiklik yapacağı yeri daha kolay bulmasına yardımcı olur.
- **İfade edici bir düzen**, kodun amacını daha iyi yansıtır ve otomatik formatlayıcıların ötesinde elle yapılan düzenlemelerle desteklenmelidir.
- **Kompakt bir format**, ekran alanını verimli kullanarak geliştiricinin kodu daha iyi anlamasına ve bağlamdan kopmadan çalışmasına olanak tanır.

---

### 14. Kod İncelemeleri

- **Kod incelemeleri**, kod kalitesini artırır ve hata oranını düşürür, ancak asıl amaç hataları düzeltmek yerine bilgi paylaşımı ve ortak kodlama yönergeleri oluşturmaktır.
- İncelemeler sırasında yapıcı ve nazik olunmalı, farklı roller tanımlanarak takım içindeki hiyerarşik etkiler azaltılmalıdır.
- Haftalık düzenli kod inceleme günleri düzenleyerek, her toplantıda farklı bir takım üyesinin kodu incelenmeli ve roller değiştirilmeli, böylece inceleme yükü takım üyeleri arasında dağıtılmalıdır.
- Kod incelemelerini eğlenceli hale getirmek, başarı için önemlidir; toplantılar bilgi paylaşımı odaklı olmalı ve resmi olmayan bir ortamda yapılmalıdır.

---

### 15. Mantıkla Kod Yazın

- **Kodun doğruluğunu** elle ispatlamak yerine, kodu kısa bölümlere ayırarak ve her bölümün doğruluğunu tartışarak yarı resmi bir şekilde değerlendirin.
- **Kodun okunabilirliğini** artırmak için yatay ve dikey boşluklar kullanarak, ilişkili yapıları hizalayın ve bölümleri ayırmak için boş satırlar ekleyin.
- **Fonksiyonlarınızı** kısa ve tek bir göreve odaklanmış tutun, 24 satır sınırını aşmamaya çalışın ve dört parametreyi geçmeyecek şekilde tasarlayın.
- **Kapsülleme** ilkesine sadık kalarak, dar arayüzler oluşturun ve iç durumu döndüren getter'lar yerine, nesnenin kendi bilgileriyle çalışmasını sağlayın.

---

### 16. Yorumlar Üzerine Bir Yorum

- **Yorumlar**, programlamanın temel yapıları kadar gereklidir ve kodun ne yaptığını açıklamalıdır.
- **Javadoc** gibi araçlar API belgeleri oluşturmak için iyi bir başlangıçtır, ancak kodun içindeki açıklamalar da önemlidir.
- Yorumlar, kodu **açıklayıcı** olmalı ancak **karmaşıklaştırmamalıdır**; kodun amacını net bir şekilde belirtmelidir.
- Başlık yorumları, kodu okumadan kullanabilmek için yeterli bilgi sağlamalı, satır içi yorumlar ise kodu genişletmek veya düzeltmek isteyen geliştiricilere yardımcı olmalıdır.

---

### 17. Sadece Kodun Söyleyemediğini Yorumla

- **Yorumlar**, kodun söyleyemediği şeyleri ifade etmeli ve kodun zaten ifade edebileceği şeyleri tekrarlamamalıdır.
- **Yanlış veya gereksiz yorumlar**, kod tabanında dikkat dağıtıcı ve yanıltıcı bir unsur olarak kalır ve bu tür yorumlar genellikle göz ardı edilir.
- **Yorumlar**, kod gibi değerlendirilmelidir; her biri okuyucuya değer katmalı, aksi takdirde kaldırılmalı veya yeniden yazılmalıdır.
- Kodun yapısını veya adlandırma kurallarını değiştirerek kodun kendisinin daha açık olmasını sağlamak, **yorumların gereksizliğini** azaltır.

---

### 18. Sürekli Öğrenme

- **Sürekli öğrenme**, yazılım geliştiriciler için piyasa değerini korumanın anahtarıdır ve bu sorumluluk bireyin kendisine aittir.
- **Mentorluk** almak, daha deneyimli kişilerden öğrenmek için önemli bir yoldur; eğer bir mentor bulamazsanız, sanal mentorlar edinin.
- **Yeni teknolojiler** ve araçlar öğrenmek, mevcut teknoloji yığınınıza yeni fikirler katabilir ve her yıl yeni bir dil veya teknoloji öğrenmek önerilir.
- **Hatalardan ders almak** ve bu hataların nedenlerini anlamak, problem çözme becerilerinizi geliştirir ve benzer sorunlarla karşılaşan diğer kişilerin deneyimlerinden faydalanmanızı sağlar.

---

### 19. Kolaylık Bir -ility Değildir

- **İyi bir API tasarımı**, tutarlı bir soyutlama seviyesi izlemeli ve **ifadeli bir dil** oluşturmalıdır.
- **Kolaylık adına** yapılan API tasarımı, genellikle kodun okunabilirliğini azaltır ve **kullanıcı yerine geliştiricinin konforunu** ön planda tutar.
- API'ler, **verimlilik, tutarlılık ve zarafet** ile karmaşıklığı gizlemeli, bu da iyi bir API tasarımının çaba gerektirdiği anlamına gelir.
- API'ler, **ifade gücü yüksek bir dil** sunmalı ve kullanıcıların beklenmedik şekillerde API'yi kullanabilmelerine olanak tanıyan **çeşitli bir kelime dağarcığı** sağlamalıdır.

---

### 20. Erken ve Sık Dağıtın

- **Kurulum ve dağıtım süreçlerini** projenin başında başlatmak, bu süreçlerin gelişmesine ve uygulama kodunun kurulumunu kolaylaştıracak şekilde değiştirilmesine olanak tanır.
- **Dağıtım sürecini** sona bırakmak, kodda yapılan varsayımlar nedeniyle daha karmaşık hale gelebilir ve bu nedenle erken aşamada tüm değiş tokuşları bilmek daha iyidir.
- **Hedef ortamda uygulamayı** gösterebilene kadar iş değeri sunulamaz, bu yüzden dağıtım sürecini ertelemek yerine deney, değerlendirme ve yeniden yapılandırma yaparak ilerleyin.
- **Kurulum/dağıtım süreci**, müşteri veya profesyonel hizmetler ekibinizin verimliliği için önemlidir; bu nedenle, bu süreci test etmeli ve proje boyunca yeniden yapılandırmalısınız.

---

### 21. İş İstisnalarını Teknik İstisnalardan Ayırın

- **Teknik sorunlar** ve **iş mantığı sorunları** farklıdır ve aynı istisna hiyerarşisinde karıştırılmamalıdır.
- **Teknik istisnalar**, programlama hataları veya çevresel sorunlar nedeniyle ortaya çıkar ve genellikle genel bir istisna yönetim mekanizması tarafından ele alınmalıdır.
- **İş mantığı istisnaları**, sözleşmenin bir parçası olan olağandışı durumları temsil eder ve istemci kodu tarafından ele alınmalıdır.
- İki tür istisnayı ayırmak, **kodun netliğini** artırır ve her birinin uygun şekilde ele alınmasını sağlar.

---

### 22. Çok Bilinçli Pratik Yapın

- **Bilinçli pratik**, bir görevi tamamlamak için değil, o görevdeki beceri ve tekniğinizi geliştirmek için yapılır.
- Uzmanlık kazanmanın anahtarı, **10,000 saat** boyunca odaklanmış ve bilinçli pratik yapmaktır.
- Doğuştan gelen yetenek, başarı için bir eşik oluşturur, ancak asıl farkı yaratan, **sıkı çalışmadır**.
- Bilinçli pratik, zaten iyi olduğunuz şeyleri değil, **zorlandığınız alanları** geliştirmeyi hedefler.

---

### 23. Alan-Spesifik Diller

- **Alan**a özgü diller (DSL), belirli bir alana yönelik özel bir dil kullanarak, alan uzmanlarının okuyabileceği ve yazabileceği ifadeler sunar.
- **İç** DSL'ler, genel amaçlı bir programlama dilinin sözdizimini doğal dile benzeterek, mevcut API'leri veya iş kodlarını daha erişilebilir hale getirir.
- **Dış** DSL'ler, metinsel veya grafiksel ifadeler kullanarak, genellikle bir araç zinciri ile işlenir ve iç modellere dönüştürülür.
- **DSL** tasarımında hedef kitleyi dikkate alarak, dilin teknik seviyesini ve kullanılabilirliğini bu kitleye göre uyarlamak önemlidir.

---

### 24. Şeyleri Kırmaktan Korkmayın

- **Kodu değiştirmekten korkmayın**, çünkü bu korku projeyi daha da kötü hale getirir ve refaktör yapmak uzun vadede projeye değer katar.
- **İçsel arayüzleri yeniden tanımlayın**, modülleri yeniden yapılandırın ve tasarımınızı basitleştirerek bağımlılıkları azaltın.
- **Büyük refaktörleri küçük adımlarla** gerçekleştirin ve her adımda test yaparak ilerleyin.
- **Kodun sağlığına önem verin** ve yönetimi, bu tür temizlik projelerinin uzun vadede maliyetleri azaltacağına ikna edin.

---

### 25. Test Verilerinizde Sevimli Olmayın

- **Test verilerinde mizahi veya uygunsuz içerik kullanmaktan kaçının**, çünkü bu veriler beklenmedik bir şekilde halka açık hale gelebilir.
- **Kodunuzda yazdığınız her metin** (yorumlar, günlükler, diyaloglar veya test verileri) kamuya açık hale gelirse nasıl görüneceğini düşünün.
- **Yanlışlıkla halka açık hale gelen içerikler**, kişi, ekip veya şirket için ciddi sonuçlar doğurabilir.
- **Kodunuzu ve test verilerinizi dikkatle gözden geçirin**, çünkü bunlar beklenmedik bir şekilde yayılabilir ve itibarınıza zarar verebilir.

---

### 26. O Hatayı Görmezden Gelmeyin!

- **Hataları** görmezden gelmek, kodunuzu daha kırılgan ve güvenlik açıklarına yatkın hale getirir, bu yüzden her hatayı kontrol edin ve ele alın.
- **Hata işleme** kodun akışını karmaşıklaştırabilir, ancak bu, gelecekteki sorunları önlemek için gereklidir.
- **İstisnalar** gibi yapılandırılmış hata işleme yöntemlerini kullanarak hataları göz ardı etmeyin ve her zaman ele alın.
- **Arayüzlerinizdeki** potansiyel hata koşullarını gizlemeyin; bunları açıkça belirtin ve kullanıcıların hataları yönetmesine olanak tanıyın.

---

### 27. Sadece Dili Değil, Kültürünü de Öğrenin

- **Programlama dili öğrenirken**, sadece dilin sözdizimini değil, dilin **kültürünü** de anlamak önemlidir.
- **Farklı diller öğrenmek**, bildiğiniz dilleri yeni ve yaratıcı şekillerde kullanmanıza olanak tanır.
- **Tasarım desenlerini** daha iyi anlamak için farklı diller arasında geçiş yapın ve her dilin kendine özgü uygulamalarını keşfedin.
- Yeni diller öğrenerek, mevcut dilinizde yazdığınız kodun **güzelliğini ve etkinliğini** artırabilirsiniz.

---

### 28. Programınızı Dik Pozisyona Çivilemeyin

- **Hatalı exception yönetimi**, uygulamanın kararlı bir şekilde çalışmasını engelleyebilir ve sorunların izlenmesini zorlaştırır.
- **Aşırı karmaşık exception handling** yapıları, yazılımın bakımını zorlaştırabilir ve hataların tespit edilmesini engelleyebilir.
- **Kullanıcıdan hataları gizlemek**, sorunların çözümünü daha da zorlaştırabilir ve kullanıcı deneyimini olumsuz etkileyebilir.
- **Basit ve sağlam bir hata raporlama mekanizması** oluşturmak, uygulamanın güvenilirliğini ve sürdürülebilirliğini artırır.

---

### 29. "Sihirli Oluyor"a Güvenmeyin

- **Programlamada** görünmeyen ve takdir edilmeyen düşünme süreci, en zor ve önemli kısımdır.
- **Yazılım geliştirmeyi** basitleştirme çabaları genellikle naif bir yaklaşım olup, bu süreçlerin karmaşıklığı göz ardı edilmemelidir.
- **Projelerde** "sihirli" olarak görülen süreçlerin anlaşılmaması, sorunlar ortaya çıktığında projeyi tehlikeye atabilir.
- **Projelerdeki** sihirli süreçlerin nasıl çalıştığını anlamak veya bu süreçleri anlayan kişilere değer vermek, sorunları çözmede kritik öneme sahiptir.

---

### 30. Kendinizi Tekrarlamayın

- **DRY prensibi**, yazılım geliştirme süreçlerinde gereksiz tekrarı önleyerek daha temiz ve bakımı kolay kod yazmayı teşvik eder.
- Kod tabanındaki **tekrarlar**, hata olasılığını artırır ve sistemin karmaşıklığını gereksiz yere büyütür.
- **Otomasyon**, tekrarlayan süreçleri hızlandırır ve hata riskini azaltır; bu nedenle manuel işlemler mümkün olduğunca otomatikleştirilmelidir.
- **Soyutlama ve tasarım kalıpları**, koddaki mantıksal tekrarları azaltmak için kullanılmalı ve DRY prensibi diğer yazılım ilkeleriyle birlikte uygulanmalıdır.

---

### 31. O Koda Dokunmayın!

- **Geliştiriciler**, geliştirme sunucusunun ötesine erişim sağlamamalıdır; bu, kodun düzgün bir şekilde test edilip entegre edilmesini sağlar.
- **Sürüm yöneticisi**, kodu aşamalı sunucuya taşımaktan sorumlu olmalı ve geliştiriciler bu süreçte sadece izleyici olmalıdır.
- **Üretim sunucusuna** geliştiricilerin erişimi kesinlikle yasaklanmalıdır; sorunlar destek ekibi tarafından çözülmeli veya geliştiriciden düzeltme istenmelidir.
- **Üretim ortamında** sorun çözmekten kaçınılmalı, bunun yerine kod kontrol sistemine yama eklenmelidir.

---

### 32. Sadece Durumu Değil, Davranışı da Kapsülleyin

- **Davranışları kapsülleyin**, sadece durumu değil, çünkü bu, nesne yönelimli tasarımın gücünü tam olarak kullanmanızı sağlar.
- **Kapsülleme**, büyük ve karmaşık sistem yapılarıyla başa çıkmak için önemli bir yapıdır ve programlama dillerinde modüller, paketler, sınıflar gibi yapılarla desteklenir.
- Nesneler, **hem durumu hem de davranışı kapsüller**, bu da tasarım sürecini basitleştirir ve sorumlulukların nesneler arasında dağıtılmasına olanak tanır.
- **Kapsüllemeyi bozmayın**; iş kurallarını merkezi bir nesne yerine ilgili sınıflara dağıtarak, kodun bakımını ve genişletilebilirliğini artırın.

---

### 33. Kayan Nokta Sayıları Gerçek Değildir

- **Kayan nokta** sayılar, matematiksel anlamda **gerçek sayılar** değildir ve sınırlı hassasiyetleri nedeniyle sürekli ve kayıpsız değildirler.
- **IEEE kayan nokta** sayıları, **sabit hassasiyetli** sayılar olup, çevredeki sayıların aralıklarını bilmek, klasik sayısal hatalardan kaçınmanıza yardımcı olabilir.
- **Yuvarlama hataları**, neredeyse eşit sayılar çıkarıldığında **önemli basamakların** iptaline yol açarak, algoritmalarınızda **felaket iptallerini** önlemek için dikkatli olmanız gerektiğini gösterir.
- **Kayan nokta** sayılar, finansal uygulamalar için uygun değildir; bunun yerine **decimal sınıfları** kullanılmalı ve **doğruluk** her zaman **verimlilikten** önce gelmelidir.

---

### 34. Açık Kaynakla Hayallerinizi Gerçekleştirin

- **Açık kaynak projeleri**, yazılım geliştirme hayallerinizi gerçekleştirmek için mükemmel bir fırsat sunar ve farklı alanlarda deneyim kazanmanızı sağlar.
- Açık kaynak projelerine katkıda bulunmak, **başkalarının kodlarını inceleyerek** ve kendi kodlarınızı ekleyerek öğrenme fırsatı sunar.
- Bu projeler sayesinde, aynı yazılım tutkusuna sahip insanlarla **kalıcı dostluklar** kurabilir ve gerçek dünya deneyimi kazanabilirsiniz.
- Katkıda bulunmak için, projelerin kullandığı araçları öğrenin ve **test kodu yazarak** projelere dahil olun; bu, hızlı öğrenmenin en etkili yollarından biridir.

---

### 35. API Tasarımının Altın Kuralı

- **API tasarımı** yaparken, gelecekteki değişikliklerin müşteri kodunu bozup bozmayacağını düşünmek önemlidir.
- **API'yi kilitlemek**, sınıfları ve yöntemleri final veya sealed yaparak, gelecekteki değişiklikleri sınırlayabilir.
- **Birim testleri**, API tasarımında önemli bir kullanım durumu olarak görülmeli ve API'yi kullanan kodlar için de testler yazılmalıdır.
- **Statik, final ve sealed** yapılar faydalı olabilir, ancak test edilebilirlik sorunlarını anlamak ve çözmek için bu yapıları deneyimlemek önemlidir.

---

### 36. Guru Miti

- Yazılım endüstrisinde "guru" miti, sorunların kanıta dayalı analiz yerine sihirli bir şekilde çözüleceği beklentisini yaratır.
- Gerçek "gurular" da herkes gibi mantık ve sistematik analiz kullanır, sadece yıllar boyunca öğrenme ve düşünce süreçlerini geliştirmişlerdir.
- "Guru" miti ortadan kalktığında, daha zeki biriyle çalışırken yeterli bağlam sağlamak ve kendi gelişim yolumuzu görmek daha kolay hale gelir.
- Yazılım dünyasında, "guru" miti yerine uzmanların diğer uzmanları yetiştirmesi gerektiği vurgulanmalıdır.

---

### 37. Sıkı Çalışma Ödüllendirilmez

- **Az çalışarak daha fazlasını başarmak** için haftalık 30 saatten fazla çalışmanın verimliliği düşürebileceğini unutmayın.
- **Sürekli öğrenme** sürecinin bir parçası olarak, yaptığınız işi gözlemlemek, üzerinde düşünmek ve davranışlarınızı buna göre değiştirmek için zaman ayırın.
- **Sürdürülebilir bir tempo** tutturmak ve yeni bilgiler ışığında rotanızı ayarlamak, uzun soluklu yazılım projelerinde başarının anahtarıdır.
- **Kendinizi güncel tutmak** için kitap okuyun, konferanslara katılın ve yeni tekniklerle deney yapın; bu, mesleki gelişiminizin ayrılmaz bir parçasıdır.

---

### 38. Hata Takip Sistemini Nasıl Kullanacağınızı Öğrenin

- **Hata raporları** yazarken, hatanın nasıl yeniden üretileceğini ve ne sıklıkla ortaya çıktığını açıkça belirtin.
- Hatanın ne olması gerektiğini ve gerçekte ne olduğunu detaylı bir şekilde açıklayın.
- Hata raporları, raporu yazan kişinin profesyonelliğini yansıtır; bu yüzden öfkeyle yazılmış raporlardan kaçının ve kapsamlı bilgi sağlayın.
- **Hata takip sistemi** kullanırken, hata durumlarını ve önceliklerini değiştirirken açıklamalar ekleyin ve herkesin aynı sorguları kullandığından emin olun.

---

### 39. Kodu Kaldırarak İyileştirin

- **Az kod, daha fazla performans**: Gereksiz kodları kaldırarak yazılımın performansını artırabilir ve kod karmaşıklığını azaltabilirsiniz.
- **YAGNI prensibini uygulayın**: Şu anda ihtiyaç duymadığınız kodları yazmaktan kaçının; gelecekte gerekirse ekleyebilirsiniz.
- **Ekstra kod maliyetlidir**: Küçük görünen ek kodlar zamanla büyüyerek bakım yükünü artırır, bu yüzden müşteriyle iletişim kurarak gereksinimleri netleştirin.
- **Gereksinimleri doğru belirleyin**: Programcılar sistem gereksinimlerini belirlemez; bu, müşteri tarafından yapılmalıdır.

---

### 40. Beni Kur

- **Kullanıcı deneyimi** önemlidir; yazılımınızın kurulumu ve kullanımı kolay olmalıdır.
- **Hızlı başlangıç kılavuzları** sağlayarak kullanıcıların yazılımınızı hızlıca deneyimlemesine olanak tanıyın.
- **Kapsamlı ve anlaşılır bir eğitim** sunarak kullanıcıların yazılımınızı etkili bir şekilde öğrenmesini sağlayın.
- Kullanıcı geri bildirimlerini dikkate alarak yazılımınızı **sürekli iyileştirin** ve kullanıcı memnuniyetini artırın.

---

### 41. Yanıt Süresi

- **Uygulama yanıt süresi**, yazılım kullanılabilirliği için kritik bir faktördür ve genellikle uzak **interprocess iletişimlerin** sayısına bağlıdır.
- **Ripple loading** gibi durumlar, ardışık veritabanı çağrılarıyla yanıt süresini uzatabilir ve bu da kullanıcı deneyimini olumsuz etkiler.
- Yanıt süresini iyileştirmek için, **paralelleştirme**, **önbellekleme** ve **parsimony** ilkesi gibi stratejiler uygulanabilir.
- Uygulama tasarımı sırasında, her uyaran için gereken **interprocess iletişimlerin** sayısını en aza indirmek önemlidir.

---

### 42. Derlemeyi Temiz Tutun

- **Uyarıları** göz ardı etmeyin; her birini ele alarak kod tabanınızın temiz kalmasını sağlayın.
- **Sıfır tolerans** politikası uygulayarak, önemsiz görünen uyarıları bile çözün veya politika değişiklikleri yapın.
- **Zihinsel yükü** azaltmak için gereksiz uyarıları temizleyin ve böylece önemli olanları daha kolay fark edin.
- **Kod hijyenini** sağlamak için derleme sürecinde uyarıları dikkate alın ve hemen çözüm üretin.

---

### 43. Komut Satırı Araçlarını Kullanmayı Öğrenin

- **Komut satırı araçlarını** kullanarak, yazılım geliştirme sürecinde kullanılan araçların ne yaptığını daha iyi anlayabilirsiniz.
- **Komut satırı araçları**, otomasyon ve görevlerin daha verimli gerçekleştirilmesi için **scripting** desteği sunar.
- **IDE'ler**, geliştirme sürecini kolaylaştırsa da, komut satırı araçları kullanarak **derleme sürecini** daha iyi kontrol edebilirsiniz.
- **Komut satırı araçlarını** öğrenmek, IDE'lerin sunduğu işlevlerin arka planını anlamanızı ve bu işlevleri daha etkin kullanmanızı sağlar.

---

### 44. İkiden Fazla Programlama Dilini İyi Bilin

- **Birden fazla programlama dili** bilmek, programcının düşünme biçimini genişletir ve yazılım geliştirme yetkinliğini artırır.
- **Farklı programlama paradigmaları** öğrenmek, algoritma uygulama ve problem çözme becerilerini geliştirir.
- **Deklaratif yaklaşımlar**, genellikle daha kısa ve anlaşılır programlar yazmayı sağlar ve bu, farklı diller arasında bilgi aktarımını teşvik eder.
- **İşverenler**, çalışanlarının yeni diller öğrenmelerine olanak tanıyarak mevcut dillerin daha sofistike kullanımını teşvik etmelidir.

---

### 45. IDE'nizi Bilin

- **IDE'yi etkili kullanmak**, programcıların üretkenliğini artırır ve kod düzenleme, derleme ve hata ayıklama işlemlerini kolaylaştırır.
- **Klavye kısayollarını ezberlemek**, fareyle menüler arasında gezinmek yerine kod yazarken akışın kesilmesini önler.
- **Stil kurallarını IDE'de uygulamak**, kodun tutarlılığını sağlar ve olası hataları tespit etmeye yardımcı olur.
- **Unix araçlarını kullanmak**, kod manipülasyonunu kolaylaştırır ve programcıların daha verimli çalışmasını sağlar.

---

### 46. Sınırlarınızı Bilin

- **Kaynaklarınızı** ve **sınırlamalarınızı** bilmek, yazılım geliştirme sürecinde verimli çalışmanın anahtarıdır.
- **Zaman** ve **uzay karmaşıklığı** gibi algoritmaların ve veri yapılarının performans özelliklerini anlamak, sistemlerinizi optimize etmenize yardımcı olur.
- **Önbellek** ve **bakış ileri** gibi teknikler, sistem performansını artırabilir ancak yalnızca erişim öngörülebilir olduğunda etkilidir.
- **Algoritma** ve **veri yapısı** seçiminde ölçüm yapmak, hangi yöntemin daha etkili olduğunu belirlemenin en güvenilir yoludur.

---

### 47. Bir Sonraki Commit'inizi Bilin

- **Bir sonraki commit'inizi bilin**: Eğer bitiremiyorsanız, değişikliklerinizi atın ve edindiğiniz bilgilerle yeni bir görev tanımlayın.
- **Spekülatif kodlamadan kaçının**: Tahminlere dayalı kodu depoya eklemeyin, bunun yerine öğrenme amacıyla deneysel çalışmalar yapın.
- **Görevlerinizi küçük ve yönetilebilir parçalara ayırın**: İki saatten fazla sürecek görevleri fark ettiğinizde, değişiklikleri atın ve daha küçük görevler tanımlayın.
- **Kodu öğrenmek için deney yapın**: Yapılandırılmamış gibi görünen kodlama oturumları bile, kodu anlamak ve üretken adımlar tanımlamak için bir amaca hizmet eder.

---

### 48. Büyük, Bağlantılı Veriler Veritabanına Aittir

- **Büyük ve kalıcı veri kümeleri** için ilişkisel veritabanı kullanmak, veri yönetimini kolaylaştırır ve performansı artırır.
- **Açık kaynaklı RDBMS** sistemleri, maliyet sorununu ortadan kaldırır ve uygulamanıza kolayca entegre edilebilir.
- **SQL öğrenmek**, veritabanı merkezli uygulamalar yazmayı keyifli hale getirir ve karmaşık veri işlemlerini basit sorgularla çözmenizi sağlar.
- **Veritabanı kullanımı**, veri tutarlılığı ve çoklu uygulama erişimi gibi avantajlar sunarak uygulamanızın ölçeklenebilirliğini ve güvenliğini artırır.

---

### 49. Yabancı Dilleri Öğrenin

- **Programcılar**, makinelerle iletişim kurmanın yanı sıra, farklı **soyutlamaları** öğrenerek ifade güçlerini artırmalıdır.
- **İyi programcılar**, günlük rutinlerinin dışına çıkarak, farklı amaçlar için ifade gücü yüksek olan diğer **dillerin** farkında olmalıdır.
- **Büyük projeler**, sadece programlama sanatı değil, aynı zamanda sosyal bir çaba olduğundan, programcılar **meslektaşları** ve diğer paydaşlarla etkili iletişim kurabilmelidir.
- **Programcılar**, projedeki farklı paydaşların dünyasını anlamak için onların **alan dillerini** öğrenmeli ve bu dillerde akıcı olmalıdır.

---

### 50. Tahmin Etmeyi Öğrenin

- **Tahmin**, geçmiş deneyim ve veriler üzerine kurulu, yaklaşık bir hesaplama veya yargıdır ve kesinlik içermez.
- **Hedef**, iş hedefi olarak belirlenen arzu edilen bir durumu ifade eder ve tahminlere dayandırılmalıdır.
- **Taahhüt**, belirli bir tarihe kadar belirli bir işlevselliği sağlamayı vaat eder ve sağlam tahminlere dayanmalıdır.
- Tahmin, hedef ve taahhüt kavramlarını netleştirerek, projelerin daha başarılı yönetilmesini ve planlanmasını sağlayabilirsiniz.

---

### 51. "Merhaba Dünya" Demeyi Öğrenin

- **Küçük kod parçalarını test etmek için** büyük projelerden bağımsız, basit ve hızlı denemeler yapabileceğiniz küçük programlar yazın.
- **IDE'ye bağımlı kalmadan**, metin düzenleyiciler ve komut satırı araçları kullanarak kodu hızlıca derleyip çalıştırmayı öğrenin.
- **Kodunuzu test etmek için** basit ve doğrudan yöntemler kullanarak, karmaşık projelerden soyutlanmış bir şekilde çalışın.
- **Kendi çalışma şeklinizi sorgulayarak**, daha verimli ve etkili yöntemler keşfetmeye açık olun.

---

### 52. Projenizin Kendi Adına Konuşmasına İzin Verin

- **Sürekli entegrasyon** sunucunuza **statik kod analizi araçları** ekleyerek kod metriklerini izleyin ve zaman içindeki evrimlerini değerlendirin.
- Projenizin **sesini duyurmak** için e-posta veya anlık mesajlaşma kullanarak geliştiricilere metriklerdeki değişiklikleri bildirin.
- **Aşırı geri bildirim cihazları (XFD)** kullanarak fiziksel bir cihazın, otomatik analiz sonuçlarına göre durumunu değiştirmesini sağlayarak projeyi ofiste somutlaştırın.
- Projenizi **kişiselleştirerek** ve ses sentezi yazılımı kullanarak, projenizin geliştiricilere doğrudan geri bildirim vermesini sağlayın.

---

### 53. Linker Büyülü Bir Program Değildir

- **Linker** işlemi, kaynak koddan yürütülebilir dosyaya geçişte **büyülü** bir adım olarak algılanmamalıdır; aslında sadece sembolleri tanımlarla eşleştirir ve yürütülebilir dosya oluşturur.
- Bir sembolün **birden fazla tanımı** olduğunda, linker hata verir; bu nedenle her sembol için yalnızca bir tanım olmalıdır.
- Eğer bir sembol yalnızca **bildirim** olarak kalırsa ve tanımı yapılmazsa, linker bu sembolü çözümsüz olarak işaretler.
- Yürütülebilir dosyanın boyutunu anlamak için **harita dosyası** kullanarak hangi modüllerin eklendiğini ve boyutlarını inceleyin; gereksiz modülleri belirlemek için modülleri geçici olarak kaldırarak yeniden bağlayın.

---

### 54. Geçici Çözümlerin Uzun Ömürlülüğü

- **Geçici çözümler**, acil bir problemi çözmek için oluşturulur ve genellikle kalıcı hale gelir çünkü faydalıdırlar.
- Geçici çözümler, **proje kültürü** ve **yönetim kararları** nedeniyle kalıcı hale gelebilir ve bu da sistemin karmaşıklığını artırabilir.
- Geçici çözümlerden kaçınmak zordur; bu yüzden daha iyi ve **daha zarif çözümler** geliştirmek en iyi yoldur.
- **Değişim** için cesaret, kabul için bilgelik ve değiştirilemeyecekleri kabul etmek için sükunet gereklidir.

---

### 55. Doğru Kullanımı Kolay, Yanlış Kullanımı Zor Yapın

- **Arayüzler**, kullanıcıların doğru kullanmasını kolaylaştırmalı ve yanlış kullanmasını zorlaştırmalıdır.
- **İyi tasarlanmış arayüzler**, kullanıcıların doğal olarak doğru seçimler yapmasını sağlayarak hataları önler.
- **Arayüz tasarımında**, kullanıcıların yapabileceği hataları öngörmek ve bu hataları önlemek için arayüzü test etmek önemlidir.
- **Arayüzler**, kullanıcıların ihtiyaçlarına göre tasarlanmalı ve gerektiğinde kullanıcı geri bildirimlerine göre değiştirilmelidir.

---

### 56. Görünmeyeni Daha Görünür Yapın

- **Görünmezlik** yazılım geliştirme sürecinde tehlikeli olabilir, çünkü somut bir şeyle ilişkilendirilen düşünce daha net olur.
- **Birim testleri** yazmak, kodun düşük bağlılık ve yüksek uyum gibi geliştirme niteliklerini ortaya çıkarır.
- **Bülten panoları ve kartlar** kullanmak, ilerlemeyi görünür ve somut hale getirir, gizli proje yönetim araçlarına ihtiyaç duyulmaz.
- **Artımlı geliştirme**, geliştirme ilerlemesinin görünürlüğünü artırır ve tamamlanan yazılım, tahminlerden daha gerçekçi bir tablo sunar.

---

### 57. Paralel Sistemlerde

- **Paylaşılmış bellek** kullanımı, eşzamanlılık sorunlarının kökeninde yer alır ve bu sorunlar, mesaj geçişi ile önlenebilir.
- **Mesaj geçişi** ve süreç modelleri, eşzamanlı ve paralel sistemler için daha iyi ölçeklenebilirlik sağlar.
- **Veri akışı sistemleri**, senkronizasyon problemlerini ortadan kaldırarak kontrol akışını veri hazır olduğunda başlatır.
- **Kütüphane ve çerçeveler** kullanarak, paylaşılmış değişken bellek yerine süreç modelleri ve mesaj geçişi ile sistemler geliştirilmelidir.

---

### 58. Geleceğe Mesaj

- **Kodunuzu** gelecekteki birine, örneğin küçük kardeşinize, bir mesaj olarak düşünün ve onun anlamasını kolaylaştıracak şekilde yazın.
- **Zor problemler** için çözümler geliştirirken, kodunuzu anlaşılır ve bakımı kolay olacak şekilde tasarlayın.
- **Gelecekteki** programcıların kodunuzu okuduğunda hayran kalacağı ve kolayca anlayacağı bir güzellikte yazmaya çalışın.
- **Kodunuzu** sadece çalıştırmak için değil, aynı zamanda estetik ve anlaşılabilir olması için yazın.

---

### 59. Polimorfizm Fırsatlarını Kaçırmayın

- **Polimorfizm**, nesne yönelimli programlamanın temel kavramlarından biri olup, farklı sınıf veya yöntem biçimlerini kullanarak daha az ve daha okunabilir kod yazmamıza olanak tanır.
- **İf-then-else** blokları yerine polimorfizmi kullanarak, kodun bağlamını daha iyi yakalayabilir ve kodun karmaşıklığını azaltabiliriz.
- **Komut ve Çift Dağıtım** gibi tasarım desenleri, polimorfizm ile birlikte kullanıldığında, kodun daha esnek ve bakımı kolay hale gelmesini sağlar.
- **Polimorfik bir kodlama stili**, genellikle daha küçük, daha okunabilir ve daha az kırılgan bir kod tabanı oluşturur, bu nedenle if-then-else bloklarının sayısını azaltmak için fırsatları değerlendirmek önemlidir.

---

### 60. Garip Haberler: Test Uzmanları Arkadaşınızdır

- **Test uzmanları**, yazılım hatalarını bulup düzeltmenize yardımcı olarak müşterilerin memnuniyetini artırır.
- Küçük hataları önemsiz görmeyin; **test uzmanları** bu hataları bulduğunda, genel yazılım kaliteniz yükselir.
- **Test uzmanları** ile iyi ilişkiler kurarak, yazılımınızın güvenilirliğini ve itibarını artırabilirsiniz.
- **Test uzmanlarının** eleştirilerini kişisel algılamayın; onların amacı, ürününüzü daha iyi hale getirmektir.

---

### 61. Tek Binary

- **Tek bir binary** oluşturun ve bunu sürüm hattındaki tüm aşamalarda tanımlayıp terfi ettirin; ortamla ilgili detayları ortamda saklayın.
- **Kodla hedef ayarlarını saklamak**, uygulamanın çekirdek özellikleri ile platforma özgü özellikleri ayırt edememekten kaynaklanır.
- **Ortam bilgilerini de versiyonlayın**; böylece bir ortam yapılandırması bozulduğunda neyin değiştiğini anlamak kolaylaşır.
- **Dağıtık sürüm kontrol sistemleri** kullanarak, üretim ortamında yapılan değişiklikleri depoya geri itmek daha kolay hale gelir.

---

### 62. Sadece Kod Gerçeği Söyler

- **Kaynak kodu**, bir programın gerçek anlamını ve işleyişini en doğru şekilde ifade eden tek unsurdur.
- **Yorumlar**, kodun işleyişini açıklamak için yeterli değildir ve yanlış bilgi içerebilir; bu nedenle, kodun kendisi anlaşılır olmalıdır.
- **Kodunuzu** daha anlaşılır hale getirmek için iyi isimlendirme, işlevsel bütünlük, bağımsızlık ve otomatik testler kullanın.
- **Kodunuzu** bir kompozisyon gibi özenle yazın ve bakım programcılarının işini kolaylaştıracak şekilde açık ve net hale getirin.

---

### 63. Yapıyı Sahiplenin (ve Yeniden Yapılandırın)

- **Yapı süreçlerini** ihmal etmek, kötü yapılandırılmış kod kadar sorun yaratabilir; bu nedenle, yapı süreçlerini anlamak ve sahiplenmek önemlidir.
- **Yapı betikleri** de kodun bir parçasıdır ve bu nedenle, doğru diller ve yöntemlerle yazılmalı ve düzenli olarak gözden geçirilmelidir.
- **Geliştirme ekibi**, yapı sürecini sahiplenmeli ve otomatikleştirerek yeni geliştiricilerin projeye hızlı başlamasını sağlamalıdır.
- **Yapı sürecini** anlamak, geliştirme döngüsünü basitleştirir, maliyetleri düşürür ve kod kalitesini artırarak erken sorun tespiti sağlar.

---

### 64. Çift Programlama Yapın ve Akışı Hissedin

- **Çift programlama**, geliştiricilerin **akış** durumunu sürdürmelerine yardımcı olur ve bilgi paylaşımını teşvik eder.
- Takım üyeleri arasında **görev rotasyonu** yaparak, bilgi ve becerilerin daha geniş bir şekilde dağıtılmasını sağlayabilirsiniz.
- **Çift programlama**, sorunları daha etkili çözmenizi sağlar ve **kesintiler** sırasında işin devam etmesine olanak tanır.
- Yeni takım üyeleri, çift programlama ve görev rotasyonu sayesinde **hızla adapte** olabilir ve kod tabanını öğrenebilir.

---

### 65. İlkel Türler Yerine Alan-Spesifik Türleri Tercih Edin

- **Alan türlerine** göre daha **alan-spesifik türler** kullanmak, yazılım hatalarını önleyebilir ve kod kalitesini artırabilir.
- **Alan-spesifik türler**, kodun daha **okunabilir** ve **test edilebilir** olmasını sağlar, çünkü bu türler bir alanın kavramlarını ifade eder.
- **Statik** ve **dinamik** olarak yazılan dillerde, alan-spesifik türler kullanılarak kodun yeniden kullanılabilirliği artırılabilir.
- **Kaliteli yazılım geliştirmek** için, alan-spesifik türleri keşfetmeye başlamak önemlidir.

---

### 66. Hataları Önleyin

- **Hata mesajları**, kullanıcı ve sistem arasındaki en kritik etkileşimlerdir ve kullanıcı hatalarını önlemek için sistemin iletişimini "debug" etmek mümkündür.
- Kullanıcıların **format hatalarını** önlemek için, tarih gibi alanlarda kullanıcıya sadece izin verilen seçenekleri sunarak hatalı girişleri engelleyin.
- **İpuçları** ve **varsayılan değerler** kullanarak kullanıcıları hatalardan uzaklaştırabilir ve kullanıcı deneyimini iyileştirebilirsiniz.
- Sistemler, kullanıcı hatalarına karşı **toleranslı** olmalı ve geri alma işlemleri sunarak kullanıcıların veri kaybını önlemelidir.

---

### 67. Profesyonel Programcı

- **Profesyonel programcılar**, kariyerlerinden ve mesleki gelişimlerinden kişisel olarak sorumludur; bu, sürekli öğrenme ve güncel kalmayı içerir.
- **Kodlarının sorumluluğunu alarak**, QA'nın sorun bulmasını beklemeden kodlarını titizlikle test ederler.
- **Takım oyuncusu olarak**, sadece kendi işlerinden değil, tüm takımın çıktısından sorumludurlar ve gerektiğinde birbirlerine destek olurlar.
- **Temiz ve düzenli kod yazmaya özen gösterirler**; büyük hata listelerine ve düzensizliğe tahammül etmezler, en iyi uygulamaları takip ederler.

---

### 68. Her Şeyi Versiyon Kontrolü Altına Alın

- **Tüm projelerinizi** versiyon kontrolü altına alarak, kod geçmişini izleme ve cesur değişiklikler yapma imkanı elde edersiniz.
- **Versiyon kontrol sistemleri**, geliştiriciler arasında sürtüşmeyi en aza indirir ve proje ilerlemesi hakkında ortak bir anlayış sağlar.
- **Proje varlıklarınızı** (kaynak kodu, dokümantasyon, araçlar, testler vb.) versiyon kontrolüne dahil ederek veri kaybı riskini azaltırsınız.
- **Her mantıksal değişikliği** ayrı bir işlem olarak taahhüt edin ve açıklayıcı bir mesaj ekleyerek, projeyi kıracak kodları taahhüt etmekten kaçının.

---

### 69. Fareyi Bırakın ve Klavyeden Uzaklaşın

- **Zorlu bir problemle karşılaştığınızda**, çözüm bulmak için klavyeden uzaklaşıp başka bir aktivite yapmak, yaratıcı düşünceyi tetikleyebilir.
- **Kodlama sırasında beynin mantıksal kısmı aktif olduğundan**, yaratıcı tarafın devreye girmesi için ara vermek önemlidir.
- **Kodunuzu yeniden gözden geçirip sadeleştirmek**, daha okunabilir ve etkili çözümler üretmenizi sağlar.
- **Problemi anlamak için zaman ayırdıktan sonra**, yaratıcı aktivitelerle uğraşmak, daha iyi çözümler bulmanıza yardımcı olabilir.

---

### 70. Kod Okuyun

- **Kod okumak**, yazılım becerilerinizi geliştirmek için önemli bir adımdır ve başkalarının kodunu okuyarak kendi hatalarınızdan kaçınabilirsiniz.
- **Kodun okunabilirliğini** değerlendirirken, biçimlendirme, adlandırma ve dil seçiminin etkilerini göz önünde bulundurun.
- **Açık kaynak projeleri**, iyi ve kötü kod örnekleri sunarak öğrenme fırsatları sağlar.
- **Kendi eski kodunuzu** incelemek, gelişiminizi görmek ve kodlama alışkanlıklarınızı değerlendirmek için faydalı olabilir.

---

### 71. Beşeriyatı Okuyun

- **Yazılım geliştirme** sürecinde, insanlar için yazılım yazarken, insanlarla birlikte çalışmanın önemini kavrayın.
- **Wittgenstein**'in felsefesi, dilin düşünceleri tam olarak aktaramayacağını ve ortak deneyimlerin anlamayı sağladığını vurgular, bu yüzden gereksinim toplarken yanlış anlamalara karşı dikkatli olun.
- **Lakoff ve Johnson**'un metaforlar üzerine çalışmaları, dilin büyük ölçüde metaforik olduğunu ve bu metaforların sistem tasarımına olan etkilerini anlamanızı önerir.
- **Heidegger**'in araç kullanımı üzerine çalışmaları, araçların kullanımda görünmez hale geldiğini ve sadece çalışmadıklarında dikkat çektiğini belirtir, bu da kullanılabilirlik tartışmalarında dikkate alınmalıdır.

---

### 72. Tekerleği Sık Sık Yeniden İcat Edin

- **Var olan kodu kullanmak**, genellikle yeniden icat etmekten daha verimli ve güvenilirdir çünkü zaten test edilmiş ve başarılı bir şekilde kullanılmaktadır.
- **Tekerleği yeniden icat etmek**, mevcut bileşenlerin iç işleyişini anlamak ve derinlemesine bilgi edinmek için değerli bir deneyim sunar.
- **Deneme yanılma yoluyla öğrenilen dersler**, teknik kitaplardan edinilen bilgilerden daha kalıcı ve öğreticidir.
- **Deneyim kazanmak**, bir programcının eğitimi ve beceri gelişimi için teorik bilgilerin toplanması kadar önemlidir.

---

### 73. Singleton Deseninin Cazibesine Karşı Direnin

- **Singleton deseni**, test edilebilirliği engelleyip, bakımı zorlaştırarak genellikle daha fazla zarar verir.
- **Tek örnek gereksinimi** çoğunlukla varsayımsaldır ve gereksinimlerin değişmesiyle sorunlara yol açabilir.
- **Singletonlar**, bağımsız kod birimleri arasında gizli bağımlılıklar ve gereksiz bağlantılar oluşturarak birim testlerini zorlaştırır.
- **Çoklu iş parçacığı** kullanımı, singleton desenini daha da karmaşık hale getirir ve temizleme işlemleri sırasında sorunlara neden olabilir.

---

### 74. Kirli Kod Bombalarıyla

- **Performans iyileştirmesi** sırasında karmaşık veya yüksek bağlı kod parçaları, tahminlerinizi zorlaştıran "kirli kod bombaları" olarak karşınıza çıkabilir.
- **Fan-in** ve **fan-out** gibi yazılım metrikleri, kodun karmaşıklığını ve bağımlılığını ölçerek, hangi kod parçalarının daha yüksek risk taşıdığını belirlemenize yardımcı olabilir.
- **İstikrarsızlık faktörü** (I = fo / (fi + fo)) kullanılarak, bir paketin ne kadar kararlı veya kararsız olduğu değerlendirilebilir ve refaktörleme hedefi I değerini 0'a yaklaştırmaktır.
- Yazılım metrikleri, karmaşık görünebilir ancak **temiz kod** elde etme mücadelesinde kirli kod bombalarını önceden tespit etmenize yardımcı olabilir.

---

### 75. Sadelik Azaltmadan Gelir

- **Kötü kodu kurtarmaya çalışmak yerine** hızlıca vazgeçip yeniden başlamak daha verimli olabilir.
- **Kodun basit olması gerektiği** ve gereksiz değişkenler, fonksiyonlar veya satırların hemen temizlenmesi gerektiği vurgulanmaktadır.
- **Kodun yeniden yazılması**, gereksiz karmaşıklığı azaltarak daha temiz ve anlaşılır bir yapı sağlayabilir.
- **Kodu acımasızca yeniden düzenlemek**, kötü kodu düzeltmenin en etkili yollarından biridir.

---

### 76. Tek Sorumluluk İlkesi

- **Tek Sorumluluk İlkesi (SRP)**, bir sistemin bileşenlerini farklı nedenlerle değişen unsurları ayırarak tasarlamanın temel prensiplerinden biridir.
- Bir sınıfın birden fazla değişim nedeni olmamalı; örneğin, iş kuralları, raporlama ve veritabanı işlemleri farklı sınıflara ayrılmalıdır.
- **Bağımsız dağıtılabilir bileşenler** oluşturmak, sistemdeki bir bileşeni değiştirdiğinizde diğerlerini yeniden dağıtmak zorunda kalmamanızı sağlar.
- SRP'yi dikkatlice uygulamak, bağımsız dağıtılabilir bir bileşen yapısı oluşturmanın anahtarlarından biridir.

---

### 77. Evet ile Başlayın

- **"Evet" ile başlamak**, teknik liderlikte önemli bir yaklaşımdır ve talepleri reddetmek yerine çözüm odaklı düşünmeyi teşvik eder.
- Bir isteği anlamak için **"Neden?"** sorusunu sormak, isteğin arkasındaki gerçek ve geçerli nedeni keşfetmeye yardımcı olabilir.
- Talepleri mevcut ürünle uyumlu hale getirmenin yollarını aramak, **yeni fırsatlar** yaratabilir ve bazen hiç iş yapmadan çözüm sunabilir.
- **İşbirliği** yaparak ve diğer karar vericileri sürece dahil ederek, hem ekip hem de ürün için en iyi çözümleri bulmak mümkündür.

---

### 78. Geri Adım Atın ve Otomatikleştirin, Otomatikleştirin, Otomatikleştirin

- **Otomasyon**, tekrar eden görevleri daha hızlı ve güvenilir hale getirir ve bu nedenle sadece testler için değil, sürüm kontrolü, derleme ve dağıtım gibi birçok proje görevi için kullanılmalıdır.
- **IDE'ler**, tüm ekip üyelerinin aynı yapılandırmalara sahip olmasını garanti edemez, bu yüzden Ant veya Autotools gibi yapı otomasyon sistemleri kullanarak kontrol ve tekrarlanabilirlik sağlanmalıdır.
- **Egzotik araçlar** öğrenmeye gerek yoktur; bash veya PowerShell gibi kabuk dilleri ve iMacros veya Selenium gibi araçlarla otomasyon sağlanabilir.
- **Dosya formatları** otomasyonu zorlaştırabilir, ancak süreçte küçük değişiklikler yaparak düz metin veya XML gibi daha kolay işlenebilir formatlar kullanılabilir.

---

### 79. Kod Analizi Araçlarının Avantajından Yararlanın

- **Kod analizi araçları**, yazılım geliştirme sürecinde testlerin yanı sıra kod kalitesini artırmak için kullanılmalıdır.
- **Statik analiz araçları**, stil rehberi ihlalleri ve potansiyel hataları tespit edebilir, bu nedenle yapılandırılabilir araçlar kullanarak uyarıları özelleştirin.
- **Kendi statik kontrol aracınızı** oluşturmak, düşündüğünüzden daha kolay olabilir ve dilin standart kütüphanelerindeki araçları keşfetmek faydalı olabilir.
- **Testler**, kalite güvencesinin sonu değil, analiz araçları ile birlikte kullanılmalıdır.

---

### 80. Gerekli Davranışı Test Edin, Tesadüfi Davranışı Değil

- **Testler**, uygulamanın gereksinim duyulan davranışını değil, **tesadüfi davranışını** test etmemelidir.
- **Uygulama detaylarına bağlı testler**, gereksinimlerle uyumlu değişikliklerde bile hatalı sonuçlar verebilir.
- **Testler**, uygulamanın ne yaptığını değil, ne yapması gerektiğini **sözleşme** olarak belirtmelidir.
- **Whitebox testler**, kodun yapısını tekrar etmek yerine, **siyah kutu** yaklaşımıyla gereksinimlere odaklanmalıdır.

---

### 81. Kesin ve Somut Test Edin

- **Testler**, bir kod biriminin istenen ve temel davranışını hedef almalı, uygulamanın tesadüfi davranışlarını değil.
- **Testler**, hem doğru hem de kesin olmalıdır; bu, somut örnekler kullanarak karmaşıklığı azaltır.
- **Somut örnekler**, genel davranışı erişilebilir ve net bir şekilde gösterir, böylece yanlış anlamaları önler.
- **Davranış belirtimi**, sadece doğru değil, aynı zamanda kesin olmalı ve testler anlaşılır ve basit olmalıdır.

---

### 82. Uyurken Test Edin (ve Hafta Sonları)

- **Test sunucularını** gece ve hafta sonları kullanarak, iş saatleri dışında testleri otomatikleştirip sonuçları sabah alabilirsiniz.
- **Uzun süreli testler**, bellek sızıntıları ve kararlılık sorunlarını tespit etmek için önemlidir ve gece veya hafta sonu boyunca çalıştırılabilir.
- **Performans testleri** için gece veya hafta sonları, sunucuların ve ağın daha az yoğun olduğu ideal zamanlardır.
- **Otomatik testler**, farklı platform ve protokoller üzerindeki kombinasyonları daha sık test etmenizi sağlar ve bu süreçleri gece veya hafta sonu çalıştırarak kaynakları verimli kullanabilirsiniz.

---

### 83. Yazılım Geliştirmenin

- **Yazılım geliştirme**, köprü yapımı gibi "zor" mühendislik disiplinlerinden farklıdır ve bu farklılık, yazılımın doğasında yatan esneklikten kaynaklanır.
- **Test etme**, yazılım geliştirmede mühendislik titizliğini sağlamak için birincil doğrulama mekanizması olarak benimsenmelidir.
- Yazılım geliştiriciler, **birim testleri**, **mock objeler** ve **test araçları** gibi araçları kullanarak, test etmeyi kaliteli mühendislik uygulamalarının bir parçası haline getirmelidir.
- Test etmenin yazılımın kalitesini ve tekrarlanabilirliğini sağladığı kabul edilerek, geliştiriciler test sürecinin atlanmasını talep eden yönetimlere karşı profesyonelce direnmelidir.

---

### 84. Durumlarda Düşünün

- **Durum makinelerini** anlamak ve kullanmak, yazılımda **durum yönetimini** doğru yapmanın temelidir.
- Kodunuzu **test ederek**, geçerli ve geçersiz durumları ve geçişleri belirleyin ve bunları doğru tutun.
- **Durum desenini** inceleyin ve **Design by Contract** yaklaşımını kullanarak her bir metodun giriş ve çıkışında durumu doğrulayın.
- Durum kontrollerinin karmaşık hale gelmesini önlemek için **araçlar, kod üretimi veya yönlendirme** gibi yöntemlerle bu kontrolleri gizleyin.

---

### 85. İki Kafa Genellikle Bir Kafadan Daha İyidir

- **Programlamada derin düşünce** gereklidir, ancak bu yalnız çalışma gerektirmez; **işbirliği** kalite, verimlilik ve iş tatminini artırır.
- **Çift programlama**, geliştiricilerin birbirlerinden öğrenmelerini sağlayarak hem teknik hem de alan bilgilerini artırır.
- **İşbirliği**, sadece soru sormak ya da toplantılara katılmak değil, birlikte çalışarak sorunları çözmektir.
- **Çift programlama**, kaliteyi artırır ve "piyango riski" gibi sorunları azaltır; yeni başlayanlar, deneyimli ekip üyeleriyle eşleşerek hızla öğrenebilirler.

---

### 86. İki Yanlış Bir Doğru Yapabilir (ve Düzeltilmesi Zordur)

- **Kodda birbiriyle çelişen hatalar**, tek bir görünür hata olarak ortaya çıkabilir ve bu durum, geliştiricilerin doğru çözümleri göz ardı etmesine neden olabilir.
- **Yazılım hataları**, yalnızca kodda değil, aynı zamanda yazılı gereksinim belgelerinde de bulunabilir ve bu hatalar, kullanıcılar arasında yanlış anlamaların yayılmasına yol açabilir.
- **Tek bir hata** genellikle kolayca tespit edilip düzeltilebilirken, **birden fazla nedenin** olduğu sorunlar daha karmaşıktır ve çözülmesi daha zordur.
- **Çelişkili hataları çözmek** için basit bir çözüm yoktur; bunun yerine, farkındalık, açık bir zihin ve tüm olasılıkları değerlendirme istekliliği gereklidir.

---

### 87. Arkadaşlarınız İçin Ubuntu Kodlama

- **Kodunuzu** yazarken, diğer geliştiricilerin de kullanacağını ve genişleteceğini unutmadan, sosyal bir sorumluluk bilinciyle hareket edin.
- **Ubuntu felsefesi**, "Bir geliştirici, diğer geliştiriciler aracılığıyla geliştiricidir" anlayışını benimseyerek, takım çalışmasının önemini vurgular.
- **Kod kaliteniz**, başkalarının kod kalitesini etkiler; bu yüzden kodunuzu yazarken takım arkadaşlarınızı düşünün.
- **Ubuntu kodlama**, sadece iyi ve temiz kod yazmak değil, aynı zamanda takım değerlerini yaşatmak ve ilkeleri güçlendirmektir.

---

### 88. Unix Araçları Arkadaşınızdır

- **Unix araçları**, metin tabanlı her türlü veri ile çalışabilir ve bu nedenle yeni dillerin hızla ortaya çıktığı günümüz geliştirme ortamında **kalıcı bir yatırım** sağlar.
- Unix araçları, **kendi komutlarınızı** oluşturmanıza olanak tanıyan küçük ama çok yönlü Lego blokları gibidir ve bu sayede herhangi bir görevi gerçekleştirebilirsiniz.
- **Unix araçları**, büyük veri setlerini verimli bir şekilde işleyebilir ve **çok çekirdekli CPU'larda** doğal olarak yük dağılımı yapabilir.
- Eğer mevcut araçlar ihtiyaçlarınızı karşılamıyorsa, **Unix araçlarını genişletmek** kolaydır; sadece belirli kurallara uyan bir program yazmanız yeterlidir.

---

### 89. Doğru Algoritma ve Veri Yapısını Kullanın

- **Doğru algoritma ve veri yapısını kullanmak**, yazılım performansını önemli ölçüde artırabilir ve gereksiz hesaplama maliyetlerini önleyebilir.
- **Kodunuzu optimize etmeden önce çalışmasını sağlamak** önemli olsa da, gereksiz karmaşıklıklardan kaçınmak için algoritmaların ve veri yapıların nasıl ölçeklendiğini anlamak gerekir.
- **Mevcut kütüphaneleri yeniden kullanmak**, tekerleği yeniden icat etmekten kaçınmanıza yardımcı olur, ancak ne zaman, neyi ve nasıl yeniden kullanacağınızı bilmek için algoritmalar ve veri yapıları hakkında bilgi sahibi olmalısınız.
- **Algoritmaların ve veri yapıların doğru seçimi**, kullanıcı deneyimini doğrudan etkileyebilir; bu nedenle, problem alanınızı iyi anlamak ve doğru kararlar vermek önemlidir.

---

### 90. Aşırı Ayrıntılı Loglama Uykunuzu Kaçıracak

- **Aşırı ayrıntılı loglama**, sistemin kontrolünü zorlaştırır ve gereksiz uyarılarla sizi rahatsız edebilir.
- **Hata logları**, sistemde bir sorun olduğunun ilk göstergesi olabilir; bu yüzden, bu loglar önemli ve dikkatle yönetilmelidir.
- **Dağıtık sistemlerde**, dış bağımlılıkların başarısızlıklarına karşı loglama politikanızı dikkatlice belirleyin.
- **INFO seviyesindeki loglar**, önemli uygulama olayları için yeterli olmalı ve sistemin düzgün çalıştığını gösteren bir işaret olmalıdır.

---

### 91. WET Performans Darboğazlarını Seyreltir

- **DRY** (Don't Repeat Yourself) prensibi, sistemdeki her bilgi parçasının tek bir temsilinin olması gerektiğini belirtir ve bu, performans sorunlarını daha kolay tespit etmeyi sağlar.
- **WET** (Write Every Time) kodlama, aynı bilginin birden fazla yerde uygulanmasıyla performans darboğazlarını gizleyebilir ve çözülmesi gereken daha fazla kod parçası yaratır.
- Koleksiyonların yanlış kullanımı, **enkapsülasyonu** ihlal ederek kodun yeniden kullanılabilirliğini ve DRY prensibini zedeler; bu durum, API'den ham koleksiyonları kaldırarak ve alan-spesifik koleksiyon tipleri oluşturarak düzeltilebilir.
- DRY prensibine bağlı kalmak, performans darboğazlarını daha kolay tespit etmeyi ve çözmeyi sağlar, çünkü kodun tek bir yerde merkezi bir şekilde yönetilmesine olanak tanır.

---

### 92. Programcılar ve Testçiler İş Birliği Yaptığında

- **Testçiler ve programcılar iş birliği yaptığında**, hata takibi yerine daha fazla kaliteli yazılım geliştirmeye odaklanılır.
- **Kabul testi odaklı geliştirme (ATDD)** ile testler kodlamadan önce hazırlanır ve bu testler regresyon süitinin bir parçası olur.
- **Programcılar ve testçiler birlikte çalışarak**, test otomasyon projelerinin başarısız olmasını önleyebilir ve daha iyi test kapsamı sağlayabilirler.
- **İş birliği sayesinde**, test edilebilirlik doğal bir yan ürün haline gelir ve ekip daha fazla regresyon testini otomatikleştirebilir.

---

### 93. Hayatınız Boyunca

- **Kodunuzu**, hayatınız boyunca desteklemek zorunda kalacakmış gibi yazın, bu sizi daha iyi bir programcı yapacaktır.
- **Değişken ve metod isimlerini** daha iyi seçmeye çalışarak, uzun kod bloklarından kaçının ve tasarım kalıplarını öğrenip kullanın.
- **Kodunuzu test edin, yorumlar yazın ve sürekli olarak yeniden yapılandırın**; bu, kodunuzu ölçeklenebilir ve sürdürülebilir hale getirir.
- Yazdığınız her kod, kariyeriniz üzerinde kalıcı bir etki bırakır; bu yüzden her satırı, kariyerinize, müşterilerinize ve kullanıcılarınıza değer katacak şekilde yazın.

---

### 94. Örnekler Kullanarak Küçük Fonksiyonlar Yazın

- **Küçük fonksiyonlar** yazmak, kodun doğruluğunu kanıtlamak ve hataları önlemek için önemlidir.
- Fonksiyonların **matematiksel boyutunu** düşünmek, kodun karmaşıklığını azaltabilir.
- **Problem alanına** özgü türler kullanmak, fonksiyonları daha yönetilebilir hale getirir ve test edilebilirliği artırır.
- **Örnekler üzerinden** fonksiyon tasarımı yapmak, kodun doğruluğunu daha kolay kanıtlamaya yardımcı olur.

---

### 95. İnsanlar İçin Test Yazın

- **Testler**, kodunuzu anlamaya çalışan insanlar için **belgeleme** işlevi görmelidir.
- Her test, yazılımın nasıl çağrıldığını ve beklenen sonuçları açıkça **tanımlamalıdır**.
- Testlerdeki gereksiz detaylar, anlamlı metod çağrılarıyla **saklanmalı** ve her test, senaryoyu açıklayan anlamlı bir isimle adlandırılmalıdır.
- Testlerinizi, hataları doğru bir şekilde tespit ettiklerinden emin olmak için **test edin** ve başkalarının testlerinizi anlamasını sağlayarak geri bildirim alın.

---

### 96. Koda Önem Vermelisiniz

- **İyi kod** yazmak, şansa bırakılmamalı ve bu, kodun kalitesine gerçekten önem vererek mümkün olabilir.
- **Kodun anlaşılabilir, sürdürülebilir ve doğru** olması için diğer programcılarla iş birliği yaparak çalışmak önemlidir.
- Her kod parçasını elden geçirdiğinizde, onu daha iyi bir durumda bırakmaya çalışmalısınız.
- **Sürekli öğrenme** ve yeni teknikleri uygun şekilde uygulama, iyi bir programcı olmanın anahtarıdır.

---

### 97. Müşterileriniz Ne Demek İstediklerini Söylemez

- **Müşterilerle** sık sık etkileşim kurarak, onların gerçekten ne istediklerini anlamaya çalışın.
- **Müşteri taleplerini** kendi kelimelerinizle tekrar ifade edin ve onların tepkilerini gözlemleyin.
- **Görsel araçlar** kullanarak, iletişimi güçlendirin ve projeyi daha iyi anlamalarına yardımcı olun.
- **Farklı kişilerle** aynı konuyu tartışarak, çelişkili bilgileri ortaya çıkarın ve bu farklılıkları çözün.

---

Teşekkürler!
