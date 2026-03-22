# 19. Gün: Kusur Analizi — EL Görüntüleme, IV Eğriler ve Sıcak Noktalar

*0,10 ABD Doları/W modülünü 0,10 ABD Doları/W kağıt ağırlığından ayıran dedektif çalışma.*

---

Modern bir güneş hücresi fabrikası, üretim hattı başına saatte 5.000 ila 10.000 arasında plaka üretmektedir. Bu hızda, eğer dikkatli izlemiyorsanız, her birkaç saniyede bir tek bir kusurlu hücre gözden kaçar. Ancak rahatsız edici gerçek şu: Güneş pillerindeki kusurların çoğu görünmez. 20 mikrometre genişliğinde bir mikro çatlağı göremezsiniz; bu, insan saçının çapının beşte biri kadardır. 1000 voltta sodyum iyonlarının camdan geçişini göremezsiniz. Akımın bakteriden daha küçük bir kristal kusurundan sızdığı bir şönt yolu göremezsiniz.

Yapabileceğiniz şey, hücrenin kendi sırlarına ihanet etmesini sağlamaktır. Ve güneş kusuru analizinin üç temel direğinin (elektrolüminesans görüntüleme, IV eğri izleme ve termal sıcak nokta tespiti) amacı da tam olarak budur. Her teknik farklı bir teşhis dilini konuşur. Birlikte fabrikadan çıkan her hücre ve modül için eksiksiz bir tıbbi muayene oluştururlar.

## Elektrolüminesans: Güneş Hücresini Geriye Doğru Çalıştırma

İşte çoğu insanı şaşırtan bir gerçek: Bir güneş hücresi ve bir LED temelde aynı cihazdır, sadece zıt yönlerde çalıştırılırlar. Bir güneş hücresi, akım üretmek için fotonları emer. Ancak akımı bir güneş hücresine *içeriye* iterseniz (elektronik tabiriyle onu ileri yönde yönlendirirseniz) elektronlar ve delikler p-n bağlantısı boyunca yeniden birleşir ve fotonları hemen geri yayar. Bu elektrolüminesanstır (EL) ve fotovoltaik kalite kontrolündeki en güçlü görüntüleme tekniğidir.

Fizik zariftir. Kristalin bir silikon hücreye akım enjekte ettiğinizde (tipik olarak kısa devre akımında veya yakınında, standart 182 mm'lik bir hücre için yaklaşık 8-10 amper), rekombinasyon radyasyonu kabaca 1.150 nm'de zirveye çıkar - yakın kızılötesinin derinliğinde, insan gözünün görebileceğinin çok ötesinde. Bu zayıf parıltıyı yakalamak için o dalga boyu aralığına duyarlı bir kameraya ihtiyacınız var. Endüstri iki ana seçenek kullanıyor: değiştirilmiş silikon CCD/CMOS sensörler (ucuz, ~5.000–15.000 ABD doları, ancak kuantum verimlilikleri 1.000 nm'nin üzerine keskin bir şekilde düştüğü için 5–30 saniyelik uzun pozlamalar gerektirir) veya InGaAs (indiyum galyum arsenit) kameralar (30.000–80.000 ABD doları, ancak en yüksek hassasiyet tam ortada) 950–1.300 nm tatlı nokta, saniyenin altında pozlamalara olanak tanır).

Temel fikir şudur: **bir EL görüntüdeki her pikselin parlaklığı, hücrenin o kısmındaki yerel voltaj ve rekombinasyon oranıyla doğrudan orantılıdır.** Sağlıklı bir bölge parlak ve eşit bir şekilde parlar. Akımın düzgün bir şekilde akamadığı veya taşıyıcıların ışınımsız yollardan yeniden birleştiği kusurlu bir bölge karanlık görünür. Bu, kabaca 50 mikrometreye kadar uzaysal çözünürlüğe sahip bir elektrik sağlığı haritası oluşturarak, üretim hızında başka hiçbir tekniğin yakalayamayacağı kusurları ortaya çıkarır.

### EL'nin Ortaya Çıkardığı Şeyler

EL görüntüde görünen kusurların kataloğu bir patoloji ders kitabı gibi okunur:

**Mikro çatlaklar** genellikle silikondaki kristalografik düzlemleri takip eden koyu çizgiler veya koyu lekeler halinde görünür. Bu çatlaklar, levha kesme (5. Gün), hücre işleme, lehimleme ve hatta taşıma sırasındaki kaba taşıma sırasında oluşmuş olabilir. İnce bir çatlak performansı hemen etkilemeyebilir; ancak termal döngü altında (modül gündüzleri 65°C'ye ısınır ve geceleri -10°C'ye soğur) bu çatlak yayılır. Bir veya iki yıl içinde, bir mikro çatlak tüm hücre parçasını elektriksel olarak izole edebilir ve yalnızca ışığı israf etmekle kalmayıp aynı zamanda tehlikeli sıcak noktaları tetikleyebilen ölü bir bölge yaratabilir.

**Kırık parmaklar ve kesintili kılavuz çizgileri** serigrafi baskılı gümüş metalizasyonun (8. Gün) temas edemediği yerlerde koyu şeritler halinde görünüyor. Bara çatlağı hücrenin bir bölümünü izole ederse, o bölümden gelen akımın gidecek hiçbir yeri kalmaz ve EL görüntüsünde keskin biçimde tanımlanmış koyu bir dikdörtgen görürsünüz.

**Şantlar** (p-n bağlantısı boyunca akım sızıntılarının olduğu yerel bölgeler) karanlık halelerle çevrelenmiş parlak noktalar olarak görünür. Bu mantığa aykırıdır: Şantın kendisi parlak bir şekilde parlayabilir çünkü akım içinden akarken çevredeki alan taşıyıcılardan yoksun kalır ve karanlığa bürünür. Katkılama sırasında (6. Gün) hücre kenarının etrafına sarılan fosfor difüzyonunun neden olduğu, levha çevresi boyunca kenar şantları özellikle yaygındır.

Çok kristalli silikondaki tanecik sınırları, kristal dislokasyonları ve metal yabancı maddelerin kalıntıları gibi **maddi kusurların tümü, dağınık karanlık alanlar olarak görülebilen, azınlık taşıyıcı ömrünün azaldığı bölgeler oluşturur. Silikonda çözünmüş tek bir demir atomu, yerel taşıyıcı ömrünü yüzlerce mikrosaniyeden birin altına düşürebilir; bu, EL görüntülemenin acımasızca istismar ettiği baş döndürücü bir hassasiyettir.

### Fotolüminesans: EL'ın Temassız Kuzeni

Fotolüminesans (PL) görüntüleme adı verilen yakından ilişkili bir teknik var. Akımı elektriksel olarak enjekte etmek yerine, levhayı bir lazerle veya yüksek yoğunlukta LED (tipik olarak 808 nm'de) ile aydınlatırsınız ve ortaya çıkan parlaklığı yakalarsınız. Fizik aynıdır - ışınımsal olarak yeniden birleşen elektron-delik çiftleri üretiyorsunuz - ancak PL'nin çok büyük bir avantajı var: **elektrik temasları gerektirmez.** Bu, herhangi bir işlem gerçekleşmeden önce ham levhaları inceleyebileceğiniz ve doping, metalizasyon ve yansıma önleyici kaplamalara para harcamadan önce üretim hattının en başında malzeme kusurlarını yakalayabileceğiniz anlamına gelir.

BT Imaging (şu anda Freiberg Instruments'ın bir parçası) gibi şirketler, bir saniyenin altında maruz kalma süreleriyle saatte 2.400'e kadar levhayı denetleyen hat içi PL sistemleri kurdu. Bir fabrika PL'yi üç noktada kullanabilir: gelen levha muayenesi, difüzyon sonrası ve metalizasyon sonrası; her aşamada farklı kusur türleri ortaya çıkar. Toplam inceleme maliyeti, modül fiyatına watt başına belki 0,001-0,002 dolar ekler; kusurlu hücrelerin nakliyesinin garanti yükümlülüğüyle karşılaştırıldığında önemsiz bir yatırımdır.

## IV Eğriler: Bir Güneş Hücresinin Yaşamsal Belirtileri

EL görüntüleme bir röntgen ise, akım-voltaj (IV) eğrisi bir kan basıncı ölçümüdür. Bu, bir fotovoltaik cihazda gerçekleştirebileceğiniz en temel elektriksel ölçümdür ve size, tek bir zarif taramada, bir hücrenin güneş ışığını elektriğe tam olarak ne kadar iyi dönüştürdüğünü söyler.

Ölçüm kavramsal olarak basittir. Hücreyi Standart Test Koşulları (STC: 1.000 W/m² ışınım, AM1.5 spektrum, 25°C hücre sıcaklığı) altında aydınlatırsınız ve her noktadaki akımı kaydederken voltajı sıfırdan (kısa devre) açık devre voltajına kadar tararsınız. Ortaya çıkan eğri karakteristik bir şekildir: solda düz ve yüksek (yüksek akım, düşük voltaj), ardından açık devreye yaklaştığınızda keskin bir şekilde düşer. Bu eğrinin altındaki alan, daha doğrusu içine yazabileceğiniz maksimum güç dikdörtgeni, hücrenin çıkışını belirler.

IV eğrisinden çıkarılan dört parametre hikayenin tamamını anlatıyor:

**Kısa devre akımı (Isc):** Gerilim sıfır olduğunda akım. Modern bir 182 mm M10 PERC hücre için bu genellikle 10,5–11,5 A'dir. Isc öncelikle optik özelliklerle, yani ne kadar ışığın emildiği ve taşıyıcılar oluşturduğuyla belirlenir. Düşük bir Isc, yansıma önleyici kaplama, yüzey dokusu veya metalizasyondan kaynaklanan aşırı gölgeleme ile ilgili sorunlara işaret eder.

**Açık devre voltajı (Voc):** Akım sıfır olduğunda voltaj, PERC hücreleri için genellikle 0,68–0,72 V'dir. Voc, malzeme kalitesine ve bağlantı özelliklerine son derece duyarlıdır. Spesifikasyonun 10 mV altındaki bir düşüş bile aşırı rekombinasyon, şönt veya doping sorunlarına işaret edebilir. TOPCon hücreleri, pasifleştirilmiş kontakları sayesinde Voc'yi 0,72–0,74 V'ye iterken, HJT hücreleri 0,74–0,76 V'a ulaşır.

**Doldurma faktörü (FF):** Gerçek teşhis gücünün yaşadığı yer burasıdır. Doldurma faktörü, gerçek maksimum gücün teorik maksimuma (Isc × Voc) oranıdır. Mükemmel bir hücre FF = %100'e sahip olacaktır; yani mükemmel bir dikdörtgen IV eğrisi olacaktır. Gerçek hücreler PERC için %78-84'e ve TOPCon için %85-86'ya kadar ulaşır. Doldurma faktörü iki parazit direncine karşı yıkıcı derecede hassastır:

- **Seri direnç (Rs):** Akım yolundaki toplam direnç — silikon yığını, metal ve silikon arasındaki temas, parmaklar boyunca, baralar ve lehimli bağlantılar boyunca. Sağlıklı bir hücrenin Rs değeri 0,3–0,8 Ω·cm²'dir. Her ilave 0,1 Ω·cm², doldurma faktörünü kabaca yüzde 1-2 puan düşürür. Yüksek Rs, IV eğrisinde eğimli bir üst kenar olarak kendini gösterir; düz kalmak yerine voltaj arttıkça akım düşer.

- **Şönt direnci (Rsh):** Bağlantı noktası boyunca kaçak akıma karşı direnç. İdeal olarak sonsuz; üretim hücreleri için genellikle 100–10.000 Ω·cm². Düşük bir Rsh (örneğin 50 Ω·cm²'nin altında), akımın harici devreye akmak yerine kusurlu yollardan sızdığı anlamına gelir. IV eğrisinde bu, eğimli bir sol kenar olarak görünür: tamamen dikey olmak yerine eğri eğimlidir, kısa devre yakınında bile akım akar.

### IV Eğrisini Bir Kardiyolog Gibi Okumak

Deneyimli kalite mühendisleri, kusurları bir kardiyoloğun ECG okuması gibi teşhis edebilir. Eğrinin ortasında içbükey bir "göbek" mi var? Muhtemelen ılımlı seri ve şönt direnç sorunlarının bir kombinasyonu. Eğride keskin bir adım mı yoksa bükülme mi var? Bu, cihazın bir kısmının diğerlerinden farklı bir voltajda çalıştığı çatlamış bir hücrenin klasik bir işaretidir. Düşük ışıkta normal görünen ancak yüksek parlaklıkta çöken bir eğri mi? Metalizasyon kusurlarından dolayı mevcut kalabalıklaşma; parmaklar yükü taşıyamaz.

Modern fabrikalarda her hücre, 10-50 milisaniye boyunca yanan, kalibre edilmiş bir ksenon flaş lambası olan bir flaş test cihazından geçer; bu sırada bir kaynak ölçer, IV eğrisini 20 ms'den daha kısa bir sürede tarar. Verim, üretim hattına uygundur: saatte 5.000'den fazla hücre. Hücreler verimliliğe göre otomatik olarak kategorilere ayrılır (tipik olarak %0,1 verimlilik artışları) ve minimum eşiğin altına düşen hücreler reddedilir. Tek başına IV testinden kaynaklanan verim kaybı, iyi yönetilen bir fabrikada genellikle %1-3'tür; bu, gigawatt ölçeğinde günlük 50.000-150.000 ABD Doları tutarında bir maliyettir ve saha arızalarını önleyerek kendi maliyetini defalarca amorti eder.

## Sıcak Noktalar: Kusurlar Tehlikeli Hale Geldiğinde

Şu ana kadar tartıştığımız her şey, kusurları gönderilmeden önce yakalamakla ilgili. Sıcak noktalar, kusurların sahaya kaçması veya zamanla gelişmesi durumunda meydana gelen olaylardır ve fotovoltaik sistemlerdeki en tehlikeli arıza modudur.

Mekanizma şaşırtıcı derecede basit ve şaşırtıcı derecede yıkıcıdır. Tipik bir modülde 60 veya 72 hücre seri olarak bağlanır. Her hücreden geçen akım aynı olmalıdır (seri devre kuralı) ve bu akım *en zayıf* hücre tarafından belirlenir. Şimdi bir hücrenin düşen bir yaprak tarafından kısmen gölgelendiğini veya alanının %30'unu izole eden bir çatlak geliştirdiğini hayal edin. Bu hücre artık dizi akımını üretemez. Güç üretmek yerine, diğer tüm hücrelerin ürettiği gücü *emmesi* gerekir. Arızalı hücre ters kutuplu hale gelir (kaynak yerine yük olarak çalışır) ve emilen gücün tamamı küçük bir alanda ısı olarak dağılır.

Sıcaklıklar şok edici. Tek bir sıcak nokta hücresi 150–200°C'ye ulaşabilir; ekstrem durumlarda 300°C'nin üzerinde olduğu belgelenmiştir. 150°C'de EVA kapsülleyici sararmaya ve bozulmaya başlar. 200°C'de kömürleşebilir. 250°C'de arka tabaka polimeri ayrışmaya başlar ve potansiyel olarak yanıcı gazlar açığa çıkar. Sıcak nokta kaynaklı yangınların belgelenmiş vakaları var - Güneş Enerjisi Malzemeleri ve Güneş Pilleri'nde 2019 yılında yapılan bir çalışmada, modül yüzey sıcaklıklarının çatı kaplama malzemelerini tutuşturmaya yetecek kadar sıcak olan 350°C'yi aştığı örnekler kataloglandı.

### Baypas Diyotları: Güvenlik Ağı

Bu nedenle her modül baypas diyotları içerir - genellikle bir "alt dizide" 20-24 hücre başına bir diyot. Bir hücre kabaca -0,7 V'den (silikon diyot için) -0,4 V'ye (Schottky diyot için) kadar ters kutuplandığında, bypass diyotu etkinleştirilir ve akımı etkilenen alt dizi etrafında yönlendirir. Bu, herhangi bir hücredeki maksimum ters voltajı sınırlar ve güç kaybını sınırlar.

Ancak bypass diyotları mükemmel değildir. Yalnızca yıkıcı aşırı ısınmaya karşı koruma sağlayabilirler, güç kaybını ortadan kaldıramazlar. Bir bypass diyotu etkinleştirildiğinde, 20 hücreli alt dizinin tamamının çıktısını kaybedersiniz; bu, modülün gücünün kabaca üçte biri kadardır. Ve diyotların kendisi de arızalanabilir: kısa devre yapan diyotlar alt diziyi kalıcı olarak atlanmış halde bırakırken, açık devre diyot arızaları korumayı tamamen ortadan kaldırarak tehlikeli sıcak noktalara zemin hazırlar.

### Termal Görüntüleme: Isıyı Görmek

Kızılötesi (IR) termografi, sahadaki sıcak noktaları tespit etmek için birincil araçtır. Teknisyenler, 8-14 μm termal kızılötesi banda (tipik modül sıcaklıklarındaki nesnelerin en güçlü yayılımı yaptığı yer) duyarlı kameralar kullanarak, tüm güneş enerjisi çiftliklerini yerden veya giderek artan oranda drone'lardan tarayabiliyor. En yüksek güçte çalışan sağlıklı bir modül, güneşli bir günde 45–55°C'lik tekdüze bir yüzey sıcaklığı gösterebilir. Bir sıcak nokta hücresi, komşularından 10 ila 40°C daha sıcak bir parlak nokta olarak göze çarpacaktır.

Drone tabanlı IR denetimi, saha teşhislerinde devrim yarattı. Tek bir drone operatörü, 10 MW güneş enerjisi çiftliğini (yaklaşık 30.000 modül) 2-3 saat içinde inceleyebilir ve yerleşik veya bulut tabanlı görüntü analizi kullanarak sıcak noktaları otomatik olarak işaretleyebilir. Maliyet, modül başına 0,01 ila 0,03 ABD dolarına ulaşıyor; bu, her birini manuel olarak incelemesi için bir teknisyen gönderme maliyetinin çok küçük bir kısmı. DJI, Raptor Maps ve Above Surveying gibi şirketler tüm işlerini bu yetenek etrafında kurdular.

Ancak mantığa aykırı olan ayrıntı şu: **termal görüntülerdeki tüm sıcak noktalar kusur değildir ve tüm kusurlar sıcak noktalar oluşturmaz.** Daha yüksek bir yerel ışınım oranına (örneğin bitişik bir binadan yansıyan ışık) sahip olduğu için biraz daha sıcak çalışan bir hücre IR'da görünecektir ancak tamamen sağlıklıdır. Tersine, büyüyen bir mikro çatlağa sahip bir hücre, çatlak önemli bir hücre parçasını izole edecek kadar yayılana kadar hiçbir termal imza göstermeyebilir; bu noktada kusur ciddi olabilir. Bu nedenle deneyimli denetçiler IR termografisini EL görüntüleme ve IV ölçümleriyle birleştirir ve kesin bir tanıya ulaşmak için her üç tekniği de üçgenleştirir.

## Kusur Tespitinde AI Devrimi

Modern bir güneş enerjisi fabrikasında üretilen görüntüleme verilerinin büyük hacmi (saatte binlerce EL görüntü, her biri potansiyel olarak ince kusur modelleri içeriyor) bunu derin öğrenme için doğal bir uygulama haline getirdi. 2020'den beri evrişimli sinir ağları (CNN'ler) araştırma merakından üretim gerekliliğine dönüştü.

Tipik yaklaşım, ResNet, YOLOv8 gibi mimarileri veya kusurlu ve kusurlu olmayan EL görüntülerin etiketli veri kümeleri üzerinde eğitilmiş özel U-Net modellerini kullanır. ELPV veri seti (Erlangen-Nürnberg Üniversitesi'nden ~2.600 hücre görüntüsü içeren, halka açık bir kıyaslama) araştırmacılar için Rosetta Stone oldu, ancak üretim sistemleri çok daha büyük özel veri setleri üzerinde eğitim alıyor. En son teknolojiye sahip modeller, mikro çatlaklar, parmak kesintileri, şöntler ve malzeme kusurları gibi kategorilerde kusur sınıflandırmasında %95-98 doğruluk elde ederek, üretim hattı hızlarında çalışırken eğitimli insan denetçilere eşdeğer veya onları aşar.

En iddialı sistemler, üç teşhis akımının tümünü birleştirir: EL görüntüler, IV eğri parametreleri ve termal veriler, kapsamlı bir hücre sağlığı puanı üreten tek bir ML modeline beslenir. Bu sistemler yalnızca kusurları tespit etmekle kalmaz, aynı zamanda hangi kusurların saha arızalarına neden olabileceğini tahmin ederek üreticilerin ikili başarılı/başarısız kararları yerine gruplama konusunda incelikli kararlar almasına olanak tanır.

## Yanlış Anlamanın Maliyeti

Bütün bunlar neden önemli? Çünkü garanti talepleri güneş enerjisi endüstrisinin mali saatli bombasıdır. Modül üreticileri genellikle 25-30 yıl sonra nominal güç çıkışının %80-87,5'ini garanti eder. Garanti edilenden daha hızlı bozulan bir modül bir iddiayı tetikler ve fayda ölçeğinde bu iddialar çok büyük olabilir. 100 MW güneş enerjisi çiftliği yaklaşık 300.000 modül içerir; %5'i bile zamanından önce başarısız olursa, değiştirme ve işçilik maliyetleri 5 milyon doları aşabilir.

Fabrikada arıza tespitine harcanan her dolar, garanti maliyetlerinden, saha denetimlerinden ve zamanından önce değiştirmelerden yaklaşık 10-30 dolar tasarruf edilmesini sağlar. En iyi fabrikalar %0,1'in altında arıza oranlarına ulaşıyor; bu, 1.000 modülde 1'den daha azının, garanti süresi içinde sahada arızaya neden olacak kadar ciddi bir gizli kusurla gönderildiği anlamına geliyor.

Modern güneş enerjisi üretiminin sessiz mucizesi budur: Hücreler ucuz *ve* güvenilirdir; kusur oluşmadığı için değil, bir dizi tespit tekniği onları çatınıza ulaşmadan yakaladığı için.

---

*Yarın, 20. Günde, modül gönderildikten sonra ne olacağını keşfedeceğiz - birkaç ay içinde 25 yıllık hava durumunu simüle eden meşakkatli IEC sertifika testleri ve bir modülün onlarca yıllık ömrü boyunca çıktısını yavaş yavaş tüketen bozulma mekanizmaları. Bugün bir polisiye hikayeyse yarın stres testidir.*

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-19.toml}}
