# 6. Gün: Doping — p-n Ekleminin Kurulması

*Elinizde silikon bir levha tutuyorsunuz. 170 mikrometre inceliğinde, her iki tarafı da cilalanmış, testere hasarından temiz bir şekilde kazınmış; kusursuz elmas kübik simetriye göre düzenlenmiş kabaca 5 × 10²² atom içeren mükemmel bir kristal silikon dilimi. Ve elektriksel açıdan konuşursak, neredeyse tamamen işe yaramaz. Oda sıcaklığında saf silikon, santimetre küp başına yaklaşık 1,5 × 10¹⁰ serbest elektronluk bir içsel taşıyıcı konsantrasyonuna sahiptir. Aynı hacimde 5 × 10²² atom olduğunu fark edene kadar bu kulağa çok fazla geliyor. Trilyonda bir atomdan daha azı mobil yük taşıyıcısına katkıda bulunuyor. Direnç 230.000 ohm-santimetre civarındadır; tam bir yalıtkan olmasa da bir iletken veya güneş hücresi olarak kullanışlı değildir. Bugün, inert silikonu gerçekten güneş ışığını toplayabilen bir şeye dönüştüren hassas şekilde kontrol edilen safsızlıkları ekleyerek bu sorunu çözüyoruz.*

---

## Kasıtlı Kirlenme Paradoksu

Bu kursta şu ana kadar yaptığımız her şey yabancı maddeleri *ortadan kaldırmakla* ilgiliydi. Siemens işlemi silikonu %99,9999'a (altı-dokuz) kadar saflaştırdı. Czochralski kristal büyümesi bu saflığı mükemmel bir kafeste korudu. Milyar başına parça kontaminasyon seviyelerine takıntılıydık. Ve şimdi, tüm bu kahramanca arınmadan sonra, onu kasıtlı olarak kirleteceğiz.

Bu bir çelişki değil. Bütün mesele bu. Silikonu saflaştırdık, böylece tam olarak hangi yabancı maddelerin nereye, tam olarak hangi konsantrasyonlarda gideceğini *bizim* seçebiliyoruz. Değersiz bir kirli silikon yığını ile çalışan bir güneş hücresi arasındaki fark, temizlik değil, *kontrollü* kirliliktir. Yarı iletken fiziği, özünde safsızlıkların istediğinizi yapmasını sağlama bilimidir.

Silisyumun içine kasıtlı olarak yabancı maddeler katma işlemine **doping** denir ve bu, bir levhayı güneş hücresine dönüştürmenin en önemli adımıdır. Doping olmadan p-n bağlantısı olmaz. P-n bağlantısı olmadan yerleşik bir elektrik alanı yoktur. Bu alan olmadan, foto-oluşturulmuş elektronlar ve delikler yeniden birleşene kadar rastgele dolaşırlar ve çok az miktarda ısıdan başka bir şey üretmezler. Doping, bir güneş hücresine yönlülüğünü veren şeydir; rastgele yük oluşumunu yararlı akıma dönüştüren asimetri.

---

## Doping Nasıl Çalışır: Atomik Resim

Silikon periyodik tablonun 14. Grubunda yer alır: dört değerlik elektronu, atom başına dört kovalent bağ, herkes memnun. Her elektronun hesabı verilir. Hiçbir şey kalmadı ve hiçbir şey eksik değil. Saf silikonun bu kadar zayıf bir iletken olmasının nedeni budur; her elektron bir bağa kilitlenmiştir.

Şimdi bir silikon atomunun bir **fosfor** atomuyla değiştirildiğini hayal edin. Fosfor Grup 15'tedir: beş değerlik elektronu. Silikon kafese gayet iyi bir şekilde yerleşerek komşularıyla dört kovalent bağ oluşturuyor ancak geriye bir elektronu kalıyor. Bu ekstra elektron herhangi bir kovalent bağa bağlı değildir. İletim bandının sadece 0,045 eV altında sığ bir enerji durumunda bulunur (bunu tam 1,12 eV bant aralığıyla karşılaştırın). Oda sıcaklığında, termal enerji (kT ≈ 0,026 eV) onu serbest bırakmak için fazlasıyla yeterlidir. Bu elektron doğumdan itibaren fiilen özgürdür.

Fosfora **verici** safsızlığı diyoruz çünkü serbest bir elektron bağışlıyor. Fosfor katkılı silikon **n tipi**'dir (negatiftir, çünkü çoğunluk taşıyıcıları elektronlardır). Fazladan elektronunu kaybeden fosfor atomu kafeste sabit bir pozitif iyon haline gelir ancak hareket edemez. Yalnızca elektron hareketlidir.

Ayna görüntüsü: bir silikon atomunu Grup 13'ten **bor** ile değiştirin. Borun yalnızca üç değerlik elektronu vardır. Kolayca üç kovalent bağ oluşturur, ancak dördüncü bağ eksiktir; eksik bir elektron, bir **delik** vardır. Bu deliğin iyonizasyon enerjisi değerlik bandının sadece 0,045 eV üzerindedir, bu da oda sıcaklığında termal olarak aktif olduğu anlamına gelir. Komşu bir elektron, kendi bağını eksik bırakarak bu boş bağa atlayabilir ve böylece delik *hareket eder*. Tam olarak kafes içinden akan pozitif yük taşıyıcısı gibi davranır.

Bor bir **alıcı** safsızlıktır (bir elektronu kabul ederek bir delik oluşturur). Bor katkılı silikon **p tipi**'dir (pozitif çoğunluk taşıyıcıları). Bir elektron kazanan bor atomu sabit bir negatif iyon haline gelir.

İşte insanları şaşırtan kısım: İlgili konsantrasyonlar *küçük*. Tipik bir güneş hücresi tabanı, santimetre küp başına yaklaşık 1 × 10¹⁶ atom olacak şekilde bor katkılıdır. Bu, her 5 milyon silikon atomuna karşılık bir bor atomu demektir; kabaca %0,00002 bor. Ancak bu küçük kirlilik silikonun iletkenliğini yaklaşık 15.000 kat artırıyor. 230.000 Ω·cm'den yaklaşık 1-10 Ω·cm'ye kadar. Dopingin gücü budur: Her biri %100 verimlilikle ücretsiz bir taşıyıcıya katkıda bulunduğunda çok fazla yabancı maddeye ihtiyacınız yoktur.

---

## P-N Kavşağı: Sihrin Gerçekleştiği Yer

Bir p-tipi silikon tabakası alın (bor katkılı taban, çoğu güneş hücresinin başlangıç malzemesi) ve yüzeye ince bir n-tipi silikon tabakası ekleyin (içine fosfor yayarak). Az önce bir **p-n bağlantısı** oluşturdunuz; fotovoltaikleri mümkün kılan yapı.

Sınırda yaşananlar çok güzel. N tarafındaki serbest elektronlar ve p tarafındaki delikler birbirine yakındır. Elektronlar sınır boyunca p tarafına yayılır; delikler n tarafına yayılır. Ancak burada çok önemli bir gelişme var: Bir elektron n tarafını terk ettiğinde arkasında sabit bir fosfor iyonu (pozitif yük) bırakır. Bir delik p tarafını terk ettiğinde, arkasında sabit bir bor iyonu (negatif yük) bırakır. Bu hareketsiz iyonlar, n tarafından p tarafına doğru bir elektrik alanı oluşturur.

Açığa çıkan iyonların bu bölgesine **tükenme bölgesi** (ya da uzay yükü bölgesi) denir; difüzyon yoluyla hareketli taşıyıcılardan arındırılmıştır. Tipik bir güneş hücresinde yaklaşık 0,1 ila 1 mikrometre genişliğindedir. İçindeki elektrik alanı oldukça büyüktür: kabaca 10.000 ila 100.000 V/cm, her ne kadar silikon p-n bağlantısı için toplam voltaj (**yerleşik potansiyel**) yalnızca 0,6-0,7 volt olsa da.

Tükenme bölgesi kendi kendini düzenler. Daha fazla taşıyıcı yayılmaya çalışırsa daha fazla iyon açığa çıkar, bu da alanı güçlendirerek onları geri iter. Nanosaniyeler içinde dengeye ulaşır. Ortaya çıkan sistem, yük taşıyıcıları için tek yönlü bir valftir: elektrik alanı elektronları n tarafına, delikleri ise p tarafına doğru sürükler. Kavşak yakınındaki bir foton tarafından üretilen herhangi bir elektron-delik çifti, yeniden birleşmeden önce bu alan tarafından ayrılacaktır. Elektron n tarafındaki kontağa itilir, dış devre boyunca akar (iş yapar) ve p tarafındaki bir delikle yeniden birleşir. Bu bir güneş hücresi.

Bir an için bunun anlaşılmasına izin verin: Fotovoltaik etkinin tamamı, kırmızı kan hücresinden daha ince bir bölgedeki 0,7 voltluk elektrik alanına dayanır. Geriye kalan her şey - yansıma önleyici kaplamalar, metal kaplama, kapsülleme - bu fısıltı kadar ince arayüzü desteklemek için mevcuttur.

---

## Difüzyon Dopingi: Fosforun Silikona Dönüştürülmesi

Peki fosforu p-tipi bir levhanın yüzeyine nasıl aktarabiliriz? Modern güneş hücresi üretiminde baskın yöntem **fosfor oksiklorür (POCl₃) difüzyonudur**.

İşlem, 800-900°C'ye ısıtılan, yaklaşık 2-3 metre uzunluğunda yatay bir silindir olan kuvars tüplü bir fırında gerçekleşir. Gofretler, modern bir üretim fırınında parti başına yaklaşık 1.200 gofret olacak şekilde kuvars teknelere dikey olarak yüklenir. Anahtar adımlar:

1. **POCl₃ dağıtımı.** Sıvı POCl₃ (oda sıcaklığında saklanan berrak, dumanlı bir sıvı), nitrojen taşıyıcı gazla kabarcıklandırılır ve oksijenle birlikte sıcak fırın tüpüne verilir. Fırın sıcaklığında reaksiyona girer:

   4 POCl₃ + 3 O₂ → 2 P₂O₅ + 6 Cl₂

2. **Fosfosilikat cam (PSG) oluşumu.** P₂O₅ levha yüzeyinde birikir ve silikonla reaksiyona girerek genellikle 20-40 nanometre kalınlığında ince bir fosfosilikat cam tabakası oluşturur. Bu cam sürekli bir fosfor atomu kaynağı görevi görür.

3. **İçeriye yayılma.** 850-900°C'de, PSG katmanındaki fosfor atomları silikon kütlesine yayılır. Katı maddelerdeki difüzyon, Fick yasalarına tabidir; bu, bir damla mürekkebin suda çok daha yavaş yayılmasını tanımlayan matematiğin aynısıdır. 880°C'de fosforun yayılımı silikonda kabaca 3 × 10⁻¹⁴ cm²/s'dir. 20-30 dakikalık bir girişten sonra, yaklaşık 0,3-0,5 mikrometre derinliğinde fosfor katkılı bir katman (**yayıcı**) elde edersiniz.

4. **PSG çıkarma.** Fosfosilikat cam tabakası seyreltik hidroflorik asit (HF) içinde sıyrılır.

Ortaya çıkan fosfor profili düz değil; yaklaşık 10²⁰-10²¹ atom/cm³ (neredeyse %1 fosfor!) yüzey konsantrasyonlarının yarım mikrometrenin üzerinde arka plan seviyelerine katlanarak düştüğü dik bir eğimdir. Bu yüksek yüzey konsantrasyonu aslında birazdan tartışacağımız bir sorundur.

Başlıca fırın üreticileri arasında **Tempress** (Hollanda), **centrotherm** (Almanya) ve **Laplace Solar** (Çin) bulunmaktadır. Modern bir difüzyon fırını saatte yaklaşık 5.000 gofreti işleyebilir ve maliyeti 500.000 ila 1.000.000 ABD Doları arasındadır. 10 GW/yıl kapasiteyle çalışan tipik bir hücre fabrikasında aynı anda çalışan 20-30 fırın bulunabilir.

---

## Ölü Katman Sorunu

İşte günün mantığa aykırı gerçeği: **yüzeyi daha iletken hale getirmek aslında güneş hücresini daha da kötüleştirir.**

Yüzeydeki bu ultra yüksek fosfor konsantrasyonu (>5 × 10²⁰/cm³), **ölü katman** veya "aşırı katkılı yayıcı" adı verilen bir bölge oluşturur. Bu bölgede fosfor konsantrasyonu katı çözünürlük sınırını aşıyor; silikon kafesin elektriksel olarak etkinleştirebileceğinden daha fazla fosfor atomu var. Fazla fosfor atomları ara bölgelerde bulunur veya çökeltiler oluşturur ve elektron bağışlamak yerine **rekombinasyon merkezleri** gibi davranırlar. Bunlar, fotojenlenmiş elektron deliği çiftlerinin öldüğü tuzaklardır.

Bu, hücre performansı açısından yıkıcıdır çünkü tam yüzeydedir; tam olarak kısa dalga boylu (mavi ve UV) fotonların emildiği yerdedir. Mavi ışık (400-500 nm), silikonun ilk 0,1-1 μm'sinde elektron-delik çiftleri üretir. Eğer o bölge bir rekombinasyon mezarlığı ise mavi tepkiyi tamamen kaybedersiniz. Ağır katkılı yayıcılara sahip ilk güneş pilleri, 500 nm'nin altında korkunç kuantum verimliliği göstererek mevcut güneş enerjisinin %15-20'sini boşa harcayacaktır.

Çözüm **seçici emitör**: yalnızca metal kontakların altında yoğun katkılama (düşük temas direncine ihtiyaç duyduğunuz yerde) ve kontaklar arasında daha hafif katkılama (iyi pasifleştirmeye ve düşük rekombinasyona ihtiyaç duyduğunuz yerde). Pratikte bu, gümüş şebeke çizgileri altındaki fosfor konsantrasyonunun iyi ohmik temas için ~10²¹/cm³ olduğu, alan bölgelerinin ise iyi taşıyıcı toplama için ~10¹⁹/cm³ katkılı olduğu anlamına gelir.

Seçici yayıcılar karmaşık desenleme adımları (lazer katkılama, dağlama işlemleri veya çoklu difüzyon maskeleri) gerektirirdi. Bu, maliyeti ve karmaşıklığı artırdı. Modern PERC hücreleri sorunu büyük ölçüde farklı bir yolla ele aldı: katkıyı mekansal olarak değiştirmek yerine, katkı seviyesinden bağımsız olarak yüzey rekombinasyonunu nötralize etmek için **pasivasyon katmanlarını** (SiNₓ, AlOₓ) kullanıyorlar. En yeni TOPCon hücrelerinde ise ağır katkı maddesi tamamen arka tarafa taşınarak ön taraftaki yüzey sorunu ortadan kaldırılıyor.

---

## Bor: Daha Hileli Katkı Maddesi

Fosfor difüzyonu nispeten basit olsa da (POCl₃ onlarca yıldır endüstrinin en büyük beygir gücü olmuştur), **bor katkılaması** daha zordur ve hücre mimarileri geliştikçe daha önemli hale gelmektedir.

Geleneksel bir güneş hücresinde, taban plakasına bor katkısı kristal büyümesi sırasında yapılır. Czochralski çektirmesindeki silikon eriyiğine kontrollü miktarda bor eklersiniz ve büyüyen kristal onu eşit bir şekilde içine alır. Tipik baz direnci 1-3 Ω·cm'dir ve yaklaşık 5 × 10¹⁵ ila 1,5 × 10¹⁶/cm³ bor konsantrasyonuna karşılık gelir.

Ancak **TOPCon** (Tünel Oksit Pasifleştirilmiş Kontak) gibi modern yüksek verimli hücre tasarımları yapıyı tersine çevirdi. TOPCon, üstünde n tipi emitör bulunan p tipi taban yerine, ön tarafında **bor katkılı emitör** bulunan **n tipi baz** (kristal büyümesi sırasında fosfor katkılı) kullanır. Bu tasarımın önemli avantajları vardır; n-tipi silikon, güneşe maruz kalmanın ilk saatlerinde p-tipi hücre çıkışını %2-3 oranında azaltabilen kötü şöhretli bir kusur kompleksi olan bor-oksijen ışığının neden olduğu bozulmaya (LID) maruz kalmaz.

N-tipi bir plaka üzerinde bor yayıcı oluşturmak, 900-1.050°C sıcaklıklarda, tipik olarak kaynak gaz olarak **BBr₃** (bor tribromür) kullanılarak bor difüzyonunu gerektirir. Bor difüzyonunun kontrolü çeşitli nedenlerden dolayı fosfordan daha zordur:

- **Daha yüksek sıcaklıklar gerekir.** Bor silikonda daha yavaş yayılır, bu nedenle 50-100°C daha yüksek sıcaklıklara ve daha uzun sürüş sürelerine ihtiyacınız vardır (fosfor için 20-30'a karşılık 30-60 dakika).
- **Bor açısından zengin katman (BRL) oluşumu.** PSG'ye benzer şekilde yüzeyde bir borosilikat cam oluşur, ancak daha karmaşıktır ve temiz bir şekilde aşındırılması daha zordur.
- **Oksijene karşı hassasiyet.** BBr₃ difüzyonu sırasında eser miktarda oksijen bile doping profilini bozan sorunlu SiO₂ katmanları oluşturabilir.

Bu zorluklara rağmen BBr₃ bor difüzyonu artık TOPCon hatlarında standarttır. **S.C New Energy Technology** (Wuxi, Çin) ve **centrotherm** gibi şirketler, tekdüzelik ve tekrarlanabilirlik sorunlarını büyük ölçüde çözen özel BBr₃ difüzyon fırınları tedarik ediyor. 2025 itibarıyla TOPCon, baskın yeni üretim teknolojisi olarak PERC'yi geride bıraktı; bu da bor difüzyon kapasitesinin büyük oranda arttığı anlamına geliyor; küresel olarak kurulu yıllık fırın kapasitesinin 300 GW'inden fazlası olduğu tahmin ediliyor.

---

## İyon İmplantasyonu: Hassas Alternatif

Silikonu katkılamanın çok daha fazla kontrol sunan ikinci bir yolu var: **iyon implantasyonu**. Plakayı sıcak bir gazla yıkamak ve atomların içeri yayılmasını beklemek yerine, katkı iyonlarını bir parçacık ışınında yüksek enerjiye hızlandırır ve onları doğrudan silikon yüzeyine fırlatırsınız.

İyon implantörü aslında küçük bir parçacık hızlandırıcıdır. Katkı kaynağını iyonize eder (örneğin, fosfor için PH₃, bor için BF₃), istenen türleri manyetik olarak ayırır, bunları 5-200 keV'ye hızlandırır ve levha boyunca ışını tarar. İyonlar silikon kafese çarpıyor ve enerjileri tarafından kontrol edilen bir derinliğe (güneş hücresi uygulamaları için genellikle 0,1-0,5 μm) gömülüyor.

Avantajları ikna edicidir:

- **Hassas doz kontrolü.** Işın akımını doğrudan ölçersiniz, böylece cm² başına kaç atom implante ettiğinizi tam olarak bilirsiniz. Difüzyon için ±%5-10'a kıyasla ±%1'lik doğruluk rutindir.
- **Yüzeyde cam tabakası yok.** Çıkarılacak PSG veya BSG yok.
- **Maskeler olmadan seçici katkılama.** Doğrudan seçici yayıcılar oluşturmak için ışını şekillendirebilirsiniz.
- **Düşük sıcaklık işlemi.** İmplantasyonun kendisi oda sıcaklığında gerçekleşir (ancak kafes hasarını onarmak ve katkı maddelerini etkinleştirmek için daha sonra yine de 900-1.000°C'de tavlamaya ihtiyacınız vardır).

Güneş enerjisi için iyon implantasyonuna öncülük eden şirket, ENERGi sistemi saatte 2.400 levha işleyebilen **Intevac**'tır (Santa Clara, California). **Kingstone Semiconductor** ve **Wanye Semiconductor** gibi Çinli şirketler o zamandan beri pazara daha düşük maliyetli araçlarla girdi.

Peki neden tüm endüstri iyon implantasyonunu kullanmıyor? **Maliyet.** Güneş enerjisi için bir iyon implanterinin maliyeti 3-5 milyon dolardır; bu, bir difüzyon fırınından 5-10 kat daha fazladır. Verim rekabetçidir (2.000-3.000 plaka/saat), ancak sermaye harcamaları ve bakım maliyetleri (yüksek vakum sistemleri, periyodik olarak değiştirilmesi gereken iyon kaynakları), difüzyonu standart hücre mimarileri için ekonomik olarak tercih edilen seçenek haline getirir. İyon implantasyonu, hassasiyetin maliyeti haklı çıkardığı yüksek verimli hücrelerde kendine yer buluyor; **Maxeon** (eski adıyla SunPower) gibi şirketlerin birbirine entegre arka temaslı (IBC) hücreleri, implantasyonu yaygın olarak kullanıyor.

---

## Önemli Sayılar

Tamamlanmış bir güneş hücresinin katkılama profiline bazı gerçek boyutlar koyalım, çünkü sayılar dikkat çekicidir:

| Katman | Kalınlık | Doping konsantrasyonu | Katkı maddesi |
|----------|-----------|----------|-----------|
| Ön verici (PERC) | 0,3-0,5 mikron | 10¹⁹-10²⁰/cm³ | Fosfor |
| Baz (p-tipi PERC) | ~170 mikron | 10¹⁶/cm³ | Bor |
| Arka BSF (PERC) | 5-10 mikron | 10¹⁸-10¹⁹/cm³ | Alüminyum |

Yayıcı, hücre kalınlığının yaklaşık %0,2'si kadardır ancak hacim başına bazdan 1.000-10.000 kat daha fazla katkı maddesi içerir. Doping konsantrasyonu 170 mikrometre boyunca dört büyüklük mertebesine yayılıyor. Bu profili doğru bir şekilde oluşturmak ve bunu yılda bir milyar levhada doğru şekilde tutmak, üretimdeki temel zorluktur.

Bahsetmediğimiz bir doping adımı daha var: **arka yüzey alanı (BSF)**. PERC hücrelerinde, arka tarafa alüminyum macunu basılır ve ~800°C'de ateşlenir, bu da alüminyum atomlarının silikonun içine yayılmasına ve bir p⁺ katmanı (yoğun katkılı p tipi) oluşturmasına neden olur. Arkadaki bu yüksek-alçak bağlantı, azınlık taşıyıcılarını (elektronları) ön bağlantı noktasına doğru iten bir alan yaratarak arka yüzeydeki rekombinasyonu azaltır. Bu, özel bir yayılma adımı yerine metalizasyon yoluyla yapılan dopingdir.

---

## Dopingden Bitmiş Yüzeye

Doping, pasif bir silikon levhayı aktif bir elektronik cihaza dönüştürür; ancak yeni katkılanmış bir levha hâlâ korkunç optik özelliklere sahiptir. Silikon parlaktır. Gelen ışığın yaklaşık %35'ini yansıtır. Eğer fotonların üçte birinden fazlası elektron-delik çifti oluşturamadan yüzeyden sekerse, hiçbir akıllıca katkılama sizi kurtaramaz.

Yarın, bu yansıma sorununa yönelik iki yönlü saldırıyı ele alacağız: yansımayı bastırmak için ince film girişimini kullanan **yansımayı önleyici kaplamalar** ve silikon yüzeye kazınmış mikroskobik piramitler kullanarak ışığı yakalayan **yüzey dokulandırma**. Birlikte, ön yüzey yansımasını %35'ten %2'nin altına düşürecekler; bu, güneş hücresi tarihindeki en büyük gelişmelerden biri.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-06.toml}}
