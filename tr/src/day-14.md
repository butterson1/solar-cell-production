# 14. Gün: Hücreden Modüle - Enkapsülasyon ve Montaj

*Dün üretim hattındaki her hücrenin bir saniyeden kısa sürede "vesikalığı" çekildi: IV eğrileri, elektrolüminesans görüntüleri, fotolüminesans taramaları. Elinizde artık akımına, voltajına ve dolum faktörüne göre titizlikle ayrılmış, test edilmiş ve sınıflandırılmış hücre kasaları var. Fakat çıplak bir güneş hücresi, açık havada çıplak bir CPU kadar işe yarar. 150 mikrometre kalınlığında, katkılanmış silikon bir yapraktır; metal temasları açıktadır. Yağmur onu aşındırır, rüzgar kırar, UV ışınımı yüzey pasivasyonunu aylar içinde bozar. Antalya'daki bir çatıya ya da Arizona'daki arazi tipi bir kuruluşa 25-30 yıl dayanabilmesi için bu kırılgan parçayı küçük bir mühendislik harikasının içine gömmek gerekir. Bugün tam olarak bunu yapıyoruz: insanın çatısına vidaladığı gerçek ürünü, yani modülü inşa ediyoruz. Ve süreç, "hücreleri camın arasına koymaktan" çok daha ilginç.* 

## Kimsenin Düşünmediği Sandviç

Bitmiş bir güneş modülü özünde lamine bir sandviçtir. Ancak buna "sandviç" demek, içerdiği hassasiyeti hafife alıyor; bu daha çok, 85°C çöl sıcağında pişirirken ve -40°C Kuzey Kutbu kışlarında donarken, otuz yıl boyunca hiç kimsenin onu bakım için açmadan hava geçirmez şekilde mühürlü kalması gereken bir zaman kapsülü inşa etmeye benziyor.

Önden arkaya standart modül yığını şöyle görünür:

1. **Ön cam** — 3,2 mm temperlenmiş, düşük demirli, yansıma önleyici kaplamalı
2. **Ön kapsülleyici sayfa** — 0,45–0,5 mm EVA veya POE
3. **Hücre dizileri** — birbirine bağlı güneş pilleri
4. **Arka kapsülleyici sayfa** — 0,45–0,5 mm EVA veya POE
5. **Arka sayfa** (veya iki yüzeyli/cam-cam modüller için arka cam)

Her katman belirli, tartışılamaz nedenlerden dolayı mevcuttur. Bir araya getirilme sırası ve nasıl bağlandıklarının fiziği, modülün 30 yıl boyunca güvenilir bir şekilde güç üretip üretmeyeceğini veya beş yıl içinde kabarcıklar, tabakalara ayrılma ve korozyon oluşturup oluşturmayacağını belirler.

## Adım 1: Tabbing ve Stringing — Hücreleri Birbirine Bağlamak

Herhangi bir katmanlama ya da laminasyon başlamadan önce hücrelerin elektriksel olarak bağlanması gerekir. **Tabbing** ve **stringing** burada devreye girer; tüm modül hattında en fazla hücrenin çatladığı adım da budur.

İşte kurulum. Her hücrenin ön yüzeyinde metal parmaklar ve baralar (8. Günde ele aldığımız serigrafi metalizasyon adımından) ve tam veya desenli alüminyum arka kontak bulunur. Hücreleri seri olarak bağlamak için (her hücre yalnızca yaklaşık 0,6-0,7 volt ürettiğinden ve modülden 30-50 volt istediğinizden bunu yapmanız gerekir), bir hücrenin ön baralarından bir sonraki hücrenin arka kontağına ince bir bakır şerit lehimlersiniz.

Bu bakır şeritlere **tabbing ribbon** denir: genellikle 0,22–0,25 mm kalınlığında, 0,9–1,5 mm genişliğinde düz bakır şeritlerdir ve önceden kalay-kurşun ya da kurşunsuz lehim alaşımıyla kaplanırlar. Hücre tasarımları 4 baradan 5, 9, 12 hatta 16 baraya geçtikçe (çoklu bara veya MBB tasarımları), bu şeritlerin genişliği de yıllar içinde küçülmüştür. Bara sayısının artması, hücre yüzeyindeki akım yolunu kısaltır; bu da direnç kayıplarını azaltır ve daha ince şeritlerin bara başına daha düşük akımı taşımasına izin verir.

**Stringing makinesi**, modül hattındaki mekanik açıdan en karmaşık ekipmanlardan biridir. Hücre başına yaklaşık 2-3 saniyede olanlar şunlardır:

1. Bir hücre, bir vakumlu kıskaç ile tasnif edilmiş silodan alınır ve ısıtılmış bir konveyöre veya platforma yerleştirilir.
2. Sekme şeritleri makaralardan beslenir, boylarına göre kesilir ve eritilir (lehimin uygun şekilde ıslanmasını sağlamak için kimyasal bir eritken püskürtülür veya batırılır).
3. Şeritler hücrenin ön baralarına milimetrenin altında bir doğrulukla yerleştirilir.
4. Kızılötesi bir lamba, sıcak hava jeti veya lazer, şerit-bara arayüzünü geleneksel kalay-kurşun lehim için yaklaşık 180–220°C'ye veya kurşunsuz alternatifler için 230–260°C'ye ısıtır (SnBiAg popülerdir). Lehim erir, bara metalizasyonunu ıslatır ve bir bağ oluşturur.
5. Bir sonraki hücre, arka teması önceki hücredeki şeritlerin arka uçlarıyla aynı hizada olacak şekilde yerleştirilir ve aynı ısıtma döngüsü, şeridi arkaya bağlar.

Sonuç, modül formatına bağlı olarak genellikle seri olarak bağlanmış 10-12 hücreden oluşan bir **dizi** olur. Standart bir 72 hücreli modül, her biri 12 hücreden oluşan altı diziye sahip olabilir.

İşte bu adımın üreticiler için neden korkutucu olduğu: 150 mikrometrelik bir silikon levhaya 200°C+ ısı uygularken aynı anda üzerine metal bir şerit bastırıyorsunuz. Bakırın termal genleşme katsayısı (17 × 10⁻⁶ /°C), silikonun (2,6 × 10⁻⁶ /°C) kabaca üç katıdır. Lehim soğuduğunda şerit silikondan çok daha fazla büzülür, hücreyi hafif bir eğriye doğru eğir ve termal strese neden olur. Stres bir kusur üzerinde yoğunlaşırsa (wafering işleminden kaynaklanan bir mikro çatlak, lazerle çizilmiş bir oluk, bir işleme çentiği) çatlak yayılır ve 0,15-0,20 dolar değerindeki bir hücreyi yok etmiş olursunuz.

Modern kiriş makineleri, kontrollü soğutma rampaları, optimize edilmiş lehim alaşımı formülasyonları (bazıları yalnızca 139°C'de düşük erime noktalı indiyum-bizmut alaşımları kullanır) ve geleneksel düz şeritlerin yerini 12-16 ince yuvarlak telin aldığı **çoklu bara (MBB) tasarımları** ile bu durumu hafifletir. Yuvarlak teller stresi daha eşit bir şekilde dağıtır ve beklenmedik bir şekilde hücre yüzeyinin optik olarak daha iyi kullanılmasını sağlar çünkü dairesel kesitleri ışığı düşük açılarla hücreye doğru geri yansıtır.

## Adım 2: Dizi Düzeni ve Veri Yolu Şeridi Ara Bağlantısı

Dizelerinizi (örneğin, 12 hücreden oluşan altı dizi) elde ettikten sonra, bunların modül düzenine yerleştirilmesi ve birbirine bağlanması gerekir. Diziler tipik olarak iki veya üç grup halinde düzenlenir ("alt diziler" olarak adlandırılır), her bir alt dizi, seri olarak bağlanmış eşit sayıda hücre içerir. Alt diziler arasında, daha kalın **veri yolu şeritleri** (2–4 mm genişliğinde, bazen kalaylı bakır örgü) dizileri bağlar ve akımı bağlantı kutusu konumuna yönlendirir.

Bu düzen adımı giderek daha fazla otomatik hale geliyor. Robotlar tamamlanmış telleri alıp camın veya kapsülleyici katmanın üzerine milimetrik hassasiyetle yerleştiriyor. Teller arasındaki boşluk önemlidir; çok yakınsanız kurdelenin kısa devre yapması riskiyle karşı karşıya kalırsınız; çok uzağa giderseniz modül alanını boşa harcarsınız. Tipik bir teller arası boşluk 2-3 mm'dir.

Alt dizi mimarisi yalnızca montaj kolaylığı sağlamaz; daha sonra tartışacağımız bypass diyot stratejisi için **elektriksel açıdan kritiktir**. Tipik bir 72 hücreli modül, her biri bir bypass diyotu tarafından korunan 24 hücrelik üç alt diziye sahiptir. 24 hücreli bir alt dizideki bir hücre gölgelenirse, bypass diyotu etkinleştirilir ve yalnızca o alt diziyi kısa devre yaparak modülün çıkışının 2/3'ünü korur. Bu bölünme olmadan, bir hücrenin gölgelenmesi tüm modülün devre dışı kalmasına neden olabilir.

## Adım 3: Cam — Herhangi Bir Cam Değil

Güneş modülünün ön kapağı ilk savunma hattıdır ve mutfak pencerenizdeki cam değildir. Güneş camı **düşük demirli temperli camdır** ve "düşük demir" kısmı son derece önemlidir. Sıradan soda-kireç camı, silikon hücrelerin hala yanıt verdiği yakın kızılötesi bölgedeki ışığı emen yaklaşık %0,1 demir oksit (Fe₂O₃) içerir. Güneş camı, demir içeriği %0,01'in altında (bazen %0,008 kadar düşük) olan hammadde kullanır; bu da standart cam için yaklaşık %89'a kıyasla güneş spektrumu boyunca geçirgenliğini %91,5'in üzerine çıkarır.

Bu yüzde 2,5 puanlık fark önemsiz görünebilir. Öyle değil. 550 watt üreten 2 metrekarelik bir modüle uygulandığında yaklaşık 14 watt'ı temsil eder ve uygun bir güneş enerjisi konumunda 30 yıllık kullanım ömrü boyunca bu yaklaşık 500 kWh enerji anlamına gelir. Şebeke ölçeğindeki fiyatlarla, düşük demirli cam ilk yıl içinde kendini amorti eder.

Cam **temperleniyor** - 620°C'ye ısıtılıyor ve daha sonra hava jetleri ile hızlı bir şekilde söndürülüyor - bu da ona tavlanmış camın yaklaşık dört katı mekanik mukavemet kazandırıyor ve kırılırsa (mesela bir dolu tanesinden) keskin parçalar yerine küçük, nispeten zararsız granüllere parçalanmasını sağlıyor. IEC 61215, modüllerin 23 m/s hızla çarpan 25 mm'lik bir buz topuna (şiddetli dolu fırtınasına eşdeğer) dayanabilmesini gerektirir. 3,2 mm temperli cam bu testi rutin olarak geçmektedir.

Çoğu ön cam ayrıca, ön yüzey yansımasını ~%4'ten ~%2'ye azaltan, tipik olarak yaklaşık 120 nm kalınlığında gözenekli bir silika sol-jel tabakası olan **yansımayı önleyici bir kaplama** (ARC) alır. Bazı premium modüller, yansımayı daha da azaltan ve modülün gün boyunca açıya daha az duyarlı olmasını sağlayan piramidal yüzey desenli **dokulu cam** kullanır.

## Adım 4: Enkapsülan — EVA ve Rakipleri

Eğer cam zırhsa, kapsülleyici de mumyalama sıvısıdır. Görevi, hücreleri optik olarak cama bağlamak, hücreleri mekanik strese karşı tamponlamak, nem girişini engellemek ve elektrik yalıtımını onlarca yıl boyunca korumaktır.

**Etilen-vinil asetat (EVA)** 1980'lerden beri bu role hakimdir. Yaklaşık %28-33 vinil asetat içeriğine sahip, yaklaşık 0,45 mm kalınlığında ön dökümlü film olarak sağlanan bir kopolimerdir. EVA, teslim edildiği haliyle yumuşak, hafif yapışkan bir termoplastiktir. Laminasyon sırasında erir, hücrelerin ve şeritlerin etrafından akar, her boşluğu ve yarığı doldurur ve daha sonra - kritik olarak - peroksitin başlattığı serbest radikal reaksiyonu yoluyla **çapraz bağlar** oluşturur. Peroksit (tipik olarak tert-butil peroksi-2-etilheksanoat, bazen TBEC olarak adlandırılır), 140°C'nin üzerindeki sıcaklıklarda ayrışır ve EVA polimer zincirleri arasında kovalent bağlar oluşturan radikaller oluşturur. EVA termoplastikten (yeniden eriyebilen) termoset (ermeyen) haline dönüşür. Bu çapraz bağlanma geri döndürülemez ve yeterli uzun vadeli performans için en az %65-85 jel içeriği elde edilmelidir.

EVA ile ilgili şaşırtıcı gerçek şu: **asetik asit üreterek bozunur.** Yıllar boyunca UV ışığa ve ısıya maruz kaldığında, vinil asetat grupları hidrolize olur ve asetik asit (sirkeye kokusunu veren kimyasalın aynısı) açığa çıkarır. Bu asit, hücre metalizasyonunu aşındırır, bazı hücre tasarımlarındaki kalay oksit şeffaf iletken okside saldırır ve eski modüllerin meşhur **esmerleşmesine** (sararma) neden olur. Asetik asit aynı zamanda kapsülleyicinin hacim direncini de azaltır; bu da hücreleri yok edebilen, voltaja bağlı bir kaçak akım olan **potansiyel kaynaklı bozulmayı (PID)** tetikleyebilir.

Bu nedenle endüstri, vinil asetat içermeyen ve bu nedenle asetik asit üretemeyen **poliolefin elastomerlere (POE)** giderek daha fazla yöneliyor. POE çok daha düşük nem buharı iletim hızlarına (EVA'nin ~1/10'u), daha iyi hacim direncine (>10¹⁴ Ω·cm'ye karşı EVA'nin ~10¹³) ve üstün PID direncine sahiptir. Yakalama mı? POE, EVA'dan kabaca %15-25 daha pahalıdır ve farklı laminasyon parametreleri gerektirir (daha düşük çapraz bağlanma sıcaklıkları, farklı yapışma arttırıcılar). Pek çok üretici artık hibrit bir yaklaşım kullanıyor: **EPE** — daha iyi cam yapışması için dış tarafta EVA kullanırken, neme karşı koruma için POE'yi hücre yüzeyine yerleştiren üç katmanlı EVA/POE/EVA ortak kalıptan çekilmiş film.

## Adım 5: Laminasyon — Kritik 15 Dakika

Laminasyon, yap ya da boz adımıdır. Bu noktaya kadar her şey tersine çevrilebilir; yanlış hizalanmış bir ipi çıkarıp düzeltebilirsiniz. Laminasyondan sonra işlem tamamdır. O sandviçin içinde ne varsa 30 yıl boyunca içeride kalır.

Modül yığını (cam, ön kapsülleyici, hücre dizileri, arka kapsülleyici, arka tabaka) genellikle temiz oda veya yarı temiz ortamda çalışan robotik kollar tarafından bir **yerleştirme masası** üzerinde monte edilir (laminatta sıkışan toz parçacıkları görünür kusurlara ve potansiyel sıcak noktalara neden olur). Daha sonra tüm yerleştirme bir **vakumlu laminatöre** aktarılır.

Laminatör aslında esnek bir silikon membranla iki bölgeye ayrılmış, ısıtılmış bir odadır. İşte adım adım süreç:

**Aşama 1 — Tahliye (3–5 dakika):** Hem üst hem de alt odalar yaklaşık 0,5–1,0 mbar'a kadar pompalanır. Bu, katmanlar arasındaki tüm havayı uzaklaştırır. Hava kalırsa, kalıcı kusurlara dönüşen kabarcıklar oluşturur; beyaz noktalar halinde görünür ve stres yoğunlaştırıcı ve nem tutucu olarak işlev görür.

**Aşama 2 — Isıtma ve presleme (8–12 dakika):** Aşağıdaki ısıtılmış merdane, laminat sıcaklığını 135–150°C'ye yükseltir. EVA yumuşayıp akmaya başladığında (yaklaşık 70°C), alt oda vakum altında kalırken üst oda atmosferik basınca havalandırılır. Bu, esnek membranı yaklaşık 1 atmosfer basınçla (~100 kPa) modülün üzerine doğru iter; bu, modülün üzerine park edilmiş küçük bir araba ile aynı kuvvettir. Basınç, erimiş kapsülleyiciyi her hücrenin, şeridin ve telin etrafında eşit şekilde sıkıştırır. Sıcaklık 140°C'nin üzerine çıktıkça EVA içindeki peroksit başlatıcı ayrışır ve çapraz bağlanma başlar.

**Aşama 3 — Sertleşme (5–8 dakika):** Çapraz bağlanma reaksiyonunu tamamlamak için laminat 145–150°C'de tutulur. Hedef genellikle >%65 jel içeriğidir ve solvent ekstraksiyon testleriyle doğrulanır (kürlenmiş EVA örneğini toluen içinde çözersiniz ve çözünmeyeni tartarsınız; bu sizin çapraz bağlı fraksiyonunuzdur). Yetersiz kürlenme, EVA'nin zamanla katmanlara ayrılabileceği veya kayabileceği anlamına gelir. Aşırı kürleme döngü süresini boşa harcar ve UV stabilizatörlerinin termal bozunmasından dolayı aşırı sararmaya neden olabilir.

Toplam laminasyon döngüsü genellikle 15-22 dakikadır ve bu da onu modül montajındaki **en büyük tek darboğaz** yapar. Bir laminatör tipik olarak bir seferde 1-2 modül tutar; bu, döngü başına 18 dakikada bir laminatörün saatte yaklaşık 3,3 modül işlemesi anlamına gelir. Yılda 2 GW modül (yaklaşık 3,5 milyon modül) üreten bir fabrikanın paralel çalışan 20-30 laminatöre ihtiyacı vardır ve her birinin maliyeti 300.000 ila 500.000 ABD Dolarıdır. Bürkle, Robert Bürkle GmbH, NPC ve 3S Swiss Solar gibi şirketler, döngüyü birkaç dakika kısaltmak için laminatör tasarımlarını optimize etmek için onlarca yıl harcadılar; çünkü tasarruf edilen her dakika, doğrudan milyonlarca sermaye ekipmanı maliyetine dönüşüyor.

## Adım 6: Arka Sayfa (veya Arka Cam)

Arka kapsülleyicinin arkasında, modülün neme, UV ve arkadan gelen mekanik hasara karşı son bariyeri olan **arka tabaka** bulunur. Klasik arka tabaka, 1970'lerde DuPont tarafından geliştirilen **TPT** laminat — Tedlar (polivinil florür) / PET (polyester) / Tedlar —tır. Floropolimer Tedlar katmanları olağanüstü UV direnci ve nem bariyeri özellikleri sağlarken PET çekirdeği mekanik dayanıklılık ve elektrik yalıtımı sağlar.

Ancak Tedlar pahalıdır (metrekare başına 5-8 ABD doları) ve sektör giderek daha ucuz alternatiflere doğru ilerlemektedir: **KPE** (Kynar PVDF / PET / EVA), **PPE** (PET / PET / EVA) ve hatta **birlikte çekilmiş poliolefin** arka sayfalar. En ucuz seçenekler (PPE) metrekare başına 2-3 dolar kadar düşük bir maliyete sahip olabilir, ancak tarihsel olarak sıcak, nemli iklimlerde daha hızlı bozulma göstermiştir — PVEL'nın modül güvenilirlik puan kartındaki verilere göre, arka tabaka çatlaması, bağlantı kutusu sorunlarından sonra ikinci en yaygın saha arıza modu olmuştur.

Işığı her iki taraftan da yakalayan iki yüzeyli modüller için, arka tabaka genellikle 2,0-2,5 mm kalınlığında (ağırlık tasarrufu için ön camdan daha ince) ikinci bir cam tabakasıyla değiştirilir. **Cam modüller** daha ağırdır (72 hücreli modül için ~28–32 kg, cam arka tabaka için ~22–24 kg) ancak üstün nem koruması, daha iyi yangın derecelendirmeleri ve daha uzun garantili ömürler sunarlar; bazı üreticiler artık cam arka tabaka için 25 yıla karşılık cam cam tasarımlarında 30 yıl performans garantisi sunmaktadır.

## Adım 7: Kırpma, Çerçeveleme ve Bağlantı Kutusu

Laminasyon ve soğumanın ardından modül, sert ve yalıtılmış bir panel olarak ortaya çıkar. Ama henüz bitmedi. Kenarların kesilmesi gerekiyor; laminasyon sırasında dışarı sızan fazla kapsülleyici ve arka tabaka malzemesi aynı hizada kesiliyor. Daha sonra üç son bileşen gelir:

**Alüminyum çerçeve.** Çoğu modülde, çevresine yapışan veya yapıştırılarak yapıştırılan ekstrüzyonlu alüminyum alaşım (tipik olarak 6063-T5) çerçeve bulunur. Çerçeve, montaj için mekanik sağlamlık sağlar, cam kenarlarını taşıma sırasında kırılmaya karşı korur ve modüle tanımlı bir montaj arayüzü sağlar. Silikon dolgu macunu veya bütil bant, cam kenarı ile çerçeve arasındaki boşluğu doldurarak nem girişini önler. Çerçevesiz cam-cam modüller bu adımı tamamen atlıyor ve kelepçelerle monte ediliyor, böylece modül başına yaklaşık 3-5 dolar ve 1-2 kg alüminyum tasarrufu sağlanıyor.

**Bağlantı kutusu.** Bu küçük plastik muhafaza (tipik olarak IP67 veya IP68 olarak derecelendirilmiştir), doğrudan veri yolu şeritlerinin laminattan çıktığı noktaların üzerinden modülün arkasına yapıştırılmıştır. Bağlantı kutusunun içinde **baypas diyotları** bulunur - genellikle 72 hücreli bir modül için alt dizi başına bir tane olmak üzere üç Schottky diyot. Bir alt dizi gölgelendiğinde veya arızalı bir hücre içerdiğinde, bypass diyotu alternatif bir akım yolu sağlayarak gölgeli hücrelerin ters taraflı sıcak noktalar olarak aşırı ısınmasını önler.

Bypass diyotunun seçimi beklediğinizden daha önemlidir. Standart silikon p-n diyotlar yaklaşık 0,6-0,7 V'luk bir ileri voltaj düşüşüne sahiptir; bu, aktif olduklarında, bu voltajın bağlantı kutusu içinde dağılan ısıdaki dizi akımıyla çarpımını kaybedersiniz. 0,7 V'luk bir diyottan geçen 10 amperlik bir akım, küçük bir plastik muhafazada 7 watt'lık ısı üretir. **Schottky diyotları** daha düşük ileri gerilime (0,3-0,4 V) sahiptir ve bu atık ısıyı neredeyse yarı yarıya azaltır. Bazı modern modüller, STMicroelectronics ve Maxim Integrated gibi şirketlerin voltaj düşüşünü neredeyse sıfıra indiren ve hatta hücre başına optimizasyon gerçekleştirebilen entegre devreleri olan **akıllı bypass cihazlarını** kullanır.

Bağlantı kutusu aynı zamanda çıkış kablolarını (tipik olarak 4 mm² veya 6 mm² kesitli bakır iletkenlere sahip MC4-uyumlu konektörler) ve dahili bağlantıları neme karşı yalıtan dolgu bileşiğini (silikon veya poliüretan) içerir.

## Adım 8: Son Test ve Sıralama

Bitmiş modül, dün ele aldığımız hücre testinin kendi versiyonundan geçer, ancak modül düzeyinde. Bir **modül flaş test cihazı** - esas olarak 2+ metrekarelik eşit şekilde aydınlatılmış bir alana sahip büyük bir güneş simülatörü - modülün IV eğrisi taranırken bir ksenon flaşı ateşler. Ortaya çıkan güç değeri isim plakası etiketinde yer alır ve modülün satış değerini belirler.

Modül flaş test cihazlarının kendi doğruluk zorlukları vardır. 2 m²'lik bir alan boyunca tekdüzelik gereksinimi zorludur — Modül düzeyindeki AAA Sınıfı simülatörlerin maliyeti 150.000–400.000 ABD Dolarıdır. Ve flaş süresinin, yüksek kapasiteli bir modülün IV eğrisini tarayacak kadar uzun olması gerektiğinden (paralel bağlı hücrelerin tümü büyük bir kapasitör görevi görür), modül simülatörleri, tek tek hücreler için kullanılan milisaniyelik ksenon flaşlar yerine **uzun darbeli** veya **sürekli** simülatörleri kullanır.

Modüller, genellikle 5 watt'lık artışlarla (örn. 545 W, 550 W, 555 W) güç çıkışına göre gruplandırılır ve bu gruplama, müşterilerin en çok önemsediği şeylerden biridir. 550 W'lık bir modülde %1'lik güç sıralama toleransı, modül başına ±5,5 W anlamına gelir; bu, 100 MW güneş enerjisi çiftliğinde (kabaca 180.000 modül) toplam tesis çıktısında MW-ölçekli bir fark anlamına gelebilir.

## Meclis Ekonomisi

İşte sizi şaşırtacak bir sayı: hücre-modül (CTM) güç **oranı aslında %100'ü** aşabilir. Durun, bir modül nasıl olur da tek tek hücrelerinin toplamından daha fazla güç üretebilir?

Optik konusuna geliyor. Hücreler kapsüllendiğinde birçok şey değişir. Cam ve kapsülleyici havadan (~1.0) daha yüksek bir kırılma indeksine (~1.5) sahiptir, bu da hücre yüzeyindeki yansıma kayıplarını azaltır. Hücreler arasındaki boşluklara çarpan ışık, beyaz arka tabaka tarafından cam yüzeye kadar yansıtılabilir ve burada toplam iç yansıma, onu bir hücreye doğru yönlendirebilir. Ve cam üzerindeki yansıma önleyici kaplamalar da yüzde onda birkaçı daha ekliyor. Bu optik kazançlar %2-4'e kadar çıkabilirken, hücreler arası aralıktan, şerit gölgelemesinden, ara bağlantılardaki dirençli kayıplardan ve dizi uyumsuzluğundan kaynaklanan kayıplar genellikle %1-3'tür. İyi tasarlanmış bir modülün net sonucu %100-102'lik bir CTM oranıdır; modül kelimenin tam anlamıyla hücrelerin tek tek üretebileceğinden biraz daha fazla güç üretir.

Bu her zaman böyle değildi. On yıl önce, CTM oranları tipik olarak %97-98'di ve modül montajı tamamen değere zarar veren bir adımdı. İyileşme, MBB ara bağlantı (daha az şerit gölgeleme), yarı kesilmiş hücreler (daha düşük dirençli kayıplar), daha yoğun hücre aralığı, daha yüksek yansıtıcı arka tabakalar ve daha iyi cam kaplamaların birleşiminden kaynaklandı. Bu, bir zamanlar gerekli olan kötülüğü net bir olumluya dönüştüren sistem düzeyinde mühendisliğin güzel bir örneğidir.

Standart bir 550 W modülün malzeme listesi kabaca şu şekilde ayrılır: hücreler (modül maliyetinin ~%55-60'ı), cam (~%8-10), kapsülleyici (~%5-7), arka tabaka (~%3-5), çerçeve (~%4-6), bağlantı kutusu ve kablolar (~%3-4) ve işçilik artı genel giderler (~%10-15). Mevcut piyasa fiyatlarında, toplam modül maliyeti watt başına yaklaşık 0,09-0,13 $'dır; bu da 550 W'lık bir modülün yaklaşık 50-72 $'a satıldığı anlamına gelir. Hücreden modüle dönüşüm kabaca 0,02–0,03 ABD Doları/W veya modül başına yaklaşık 11–17 ABD Doları ekler.

## Yarının Önizlemesi

Artık bir güneş hücresini çıplak test edilmiş plakadan bitmiş, hava şartlarına dayanıklı, test edilmiş ve nakliyeye hazır bir modüle kadar takip ettik. Ancak biz bu sürece, sanki bir mikroskoptan bakıyormuşçasına, adım adım bakıyoruz. Yarın, uzaklaşacağız ve kum teslimatından nakliye iskelesine kadar tüm fabrika katını yürüyeceğiz. 15. Gün, tüm fabrika düzeninin haritasını çıkaracak: tüm bu bireysel adımların nasıl birbirine bağlandığı, tampon stokların nerede olduğu, malzeme akışlarının nasıl göründüğü ve modern 10 GW hücre ve modül fabrikasının neden gezegendeki en hassas koreografiye sahip üretim operasyonlarından biri olduğu.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-14.toml}}
