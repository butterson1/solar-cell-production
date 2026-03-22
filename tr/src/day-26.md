# 26. Gün: Uzay Güneş Enerjisi ve Yoğunlaştırıcılı PV — Yıldız Işığını Toplamak

## Güneş Uzayda Daha İyi

İşte Dünya'daki her güneş enerjisi mühendisinin aklına takılan bir sayı: Güneş, atmosferimizin üst kısmına **metrekare başına 1.361 watt** veriyor; buna güneş sabiti deniyor. Işık 100 kilometrelik havayı delip geçtiğinde, bulutlardan sektiğinde, tozlar tarafından dağıldığında ve çatınızın açısına göre karardığında, tipik bir yer tabanlı panel günde ortalama 200-300 W/m² görebilir. Arizona'da iyi bir günde öğle saatlerinde 1000 W/m²'ye ulaşabilirsiniz. Geceleri sıfır alırsın.

Ekvatorun 35.786 km yukarısında sabit bir yörüngede bulunan bir güneş paneli, kabaca **yılın %99,5'i** boyunca tam 1.361 W/m²'ye bakar; ekinoksların etrafında yalnızca birkaç hafta boyunca ve o zaman bile en fazla yalnızca 72 dakika boyunca Dünya'nın gölgesi tarafından gölgede kalır. Bulut yok. Atmosfer yok. Gece yok (neredeyse). GEO'daki bir güneş paneli, Almanya'daki bir çatıdaki aynı panele kıyasla yılda 5 ila 10 kat daha fazla enerji topluyor.

Bu şaşırtıcı avantaj, Isaac Asimov'un "Akıl" adlı kısa öyküsünde gezegenlere enerji ışınlayan bir uzay istasyonu hakkında yazdığı **1941**'den beri fizikçilerin ilgisini çekiyor. Konsept ilk ciddi mühendislik uygulamasını 1968'de yer antenine mikrodalga ışınlayan 5 km genişliğinde güneş kolektörüne sahip bir uydu öneren **Peter Glaser**'dan aldı. NASA 1970'lerin sonlarında bu konuyu kapsamlı bir şekilde inceledi, rakamları hesapladı ve şu sonuca vardı: teknik olarak mümkün, ekonomik açıdan çılgın. Uzay Mekiği'nde herhangi bir şeyin yörüngeye fırlatılmasının maliyeti **kilogram başına 54.000$** civarındadır. Matematik henüz kapanmadı.

Ancak fırlatma maliyetleri çöktü. SpaceX'in Falcon 9'u şu anda alçak Dünya yörüngesine **3.000$/kg** altında ücret alıyor. Starship, sözlerini yerine getirirse **100-200$/kg**'ı hedefliyor ve Elon Musk 10$/kg'lık hayali bir hedef belirledi. Aniden, uzay güneş enerjisinin aritmetiği dünya çapındaki mühendisler tarafından yeniden çalışılıyor.

## Boşlukta Hayatta Kalabilen Güneş Pilleri

Şehirlere yörüngeden enerji sağlamayı hayal etmeden önce, orada gerçekte hangi güneş pillerinin çalıştığından bahsedelim; çünkü standart konut silikon paneliniz berbat bir seçim olacaktır.

Uzay vahşidir. Atmosferin ötesinde, güneş pilleri **kozmik ışınlar, güneş proton olayları ve Van Allen kuşaklarında hapsolmuş radyasyon** ile karşı karşıyadır; bu da atomları kristal kafesten dışarı fırlatan ve performansı düşüren kusurlar yaratan yüksek enerjili parçacıkların sürekli bombardımanıdır. Korumasız bir silikon hücre birkaç gün içinde önemli miktarda çıktı kaybedecektir. Korunan hücreler bile bozulur: tipik bir görev bütçesi, radyasyon hasarından dolayı **yılda %2-3 verim kaybına** karşılık gelir.

Çözüm: Galyum arsenit (GaAs) ve indiyum galyum fosfit (InGaP) ve indiyum galyum arsenit (InGaAs) gibi ilgili bileşiklerden oluşturulan **III-V çok bağlantılı hücreler**. 11. Günde çok bağlantılı hücreleri ele aldık, ancak asıl geçimini sağladıkları yer uzaydır. Modern bir **üç bağlantılı InGaP/GaAs/InGaAs hücresi**, uzaydaki yaşamın başlangıcında yaklaşık **%30-32 verimlilik** elde eder (atmosferin üzerindeki filtrelenmemiş güneş spektrumu olan AM0 spektrumu altında). GEO'de 15 yıl geçtikten sonra radyasyon bunu kabaca **%26-28**'e düşürür; yine de silikonun başarabileceğinden çok daha iyidir.

Bu hücreler alan bazında şaşırtıcı derecede pahalıdır: Ticari silikon hücreler için m² başına yaklaşık 30 ABD dolarına kıyasla kabaca **metrekare başına 80.000 ila 130.000 ABD doları**. Ancak uzayda metrekare başına dolar için optimizasyon yapmıyorsunuz; **kilogram başına watt** için optimizasyon yapıyorsunuz. Fırlattığınız her gramın maliyeti vardır. Bir III-V hücresi, ultra hafif alt tabakalarda yaklaşık **350–450 W/kg** sağlar (bazı deneysel hücreler esnek filmlerde 3.000 W/kg'a ulaşır), ön kısmı cam kaplı bir silikon modül ise belki 15–20 W/kg'ı yönetir. Lansman maliyetleri bütçenize hakim olduğunda, pahalı ama tüy kadar hafif olan hücre kesin bir şekilde kazanır.

**Uluslararası Uzay İstasyonu** toplamda 2.500 m² alana yayılan sekiz büyük güneş paneli kanadı üzerinde çalışıyor ve başlangıçta silikon hücreleri kullanarak yaklaşık **120 kW** üretiyor (bunlar 1990'larda, III-V hücreleri standart hale gelmeden önce tasarlanmıştı). Onlarca yıl süren radyasyona maruz kalma ve mikrometeorit çarpmalarından sonra, kötü bir şekilde bozunmuşlardı; bu nedenle NASA, gücü yeniden sağlamak için 2021'den bu yana modern III-V hücreleri kullanan yeni **ROSA (Roll-Out Solar Array)** panellerini kaplıyor.

## Yoğunlaştırıcı PV: Daha Az Hücre, Daha Fazla Işık

Şimdi zarif bir soru: Çok bağlantılı hücreler, konsantre güneş ışığının %46'sını elektriğe dönüştürebiliyorsa (mevcut laboratuvar kaydı, dört bağlantı hücreli **Fraunhofer ISE** ve **NREL** tarafından tutuluyor), ancak metrekare başına maliyeti 50.000 dolardan fazlaysa, ya... çok daha az hücre kullansaydınız?

**Yoğunlaştırıcı fotovoltaiklerin (CPV)** arkasındaki temel fikir budur. Pahalı yarı iletkenle devasa bir alanı kaplamak yerine, *ucuz optiklerle* (mercekler veya aynalar) devasa bir alanı kaplarsınız ve tüm bu ışığı küçük, ultra verimli bir hücreye odaklarsınız. **500 kat konsantrasyondaki** bir sistem 500 kat daha az hücre alanına ihtiyaç duyar. Eğer konsantre optiklerinizin maliyeti 50 $/m² ve ​​hücrenizin maliyeti 50.000 $/m² ise, 50.000 $'lık yarı iletkeni 50 $'lık plastik ve başparmağınızın başparmağı büyüklüğünde bir hücre ile değiştirmişsiniz demektir.

### Nasıl Çalışır: Bir CPV Modülünün Anatomisi

Yüksek konsantrasyonlu bir PV (HCPV) modülü, geleneksel bir düz panele hiç benzemez. Bir dizi **Fresnel lensi** tutan metal bir çerçeve düşünün; tepegözlerde ve deniz feneri ışıklarında gördüğünüz düz, çıkıntılı lensler. Genellikle 10-20 cm çapında ve yalnızca birkaç milimetre kalınlığındaki her mercek, güneş ışığını yaklaşık **1 cm²** bir noktaya odaklar. Bu odak noktasında bir ısı dağıtıcıya monte edilmiş çok bağlantılı bir hücre (genellikle üçlü veya dörtlü bağlantı III-V) bulunur, çünkü 500 güneşi bir santimetrekare üzerinde yoğunlaştırmak yoğun termal yük oluşturur.

Konsantrasyon oranı çok önemlidir. **500×**'de izlemenizin yaklaşık ±0,5° dahilinde doğru olması gerekir. **1.000×**'de tolerans ±0,3°'ye daralır. Bu nedenle her HCPV sistemi, gökyüzünde güneşi yay dakikası hassasiyetiyle takip eden motorlu bir montaj parçası olan **çift eksenli güneş takip cihazı** üzerinde bulunur. Takipçi maliyete ve mekanik karmaşıklığa katkıda bulunur, ancak bu aynı zamanda sistemin tüm gün boyunca doğrudan normal ışınımı (DNI) yakaladığı ve her güneşli saatten daha fazla enerji çektiği anlamına da gelir.

İşte mantığa aykırı kısım: **CPV sistemler bulutlu iklimlerde iyi çalışmaz**. Geleneksel silikon paneller, dağınık ışığı (bulutlu gökyüzünden yayılan fotonlar) oldukça iyi bir şekilde kullanabilir. Ancak Fresnel lens yalnızca *direkt ışın* güneş ışığına odaklanabilir. Dağınık ışık her yönden gelir ve konsantre edilemez. Bu, CPV'yi **"güneş kuşağı"** için bir teknoloji haline getiriyor; yani çöller, kurak yaylalar, DNI değeri 2.000 kWh/m²/yıl'ın üzerinde olan yerler. Sahra'yı, Arap Yarımadası'nı, Avustralya taşrasını, Güneybatı Amerika'yı ve Batı Çin'in bazı kısımlarını düşünün.

### Verimlilik Tacı

Başka hiçbir ticari PV teknolojisi CPV'nin ham verimlilik rakamlarına yaklaşamaz. **Soitec** (piyasadan çıkmadan önce) ve **Suncore Fotovoltaiks** gibi şirketlerin üretim modülleri, yoğunlaştırıcı standart test koşullarında **%38,9 modül verimliliği** göstermiştir; bu, üst düzey silikon modüllerin %22-24'ünün çok üzerindedir. İzleme kayıplarını, optik kayıpları ve termal azalmayı hesaba katan **sistem** verimliliği **%28-32** civarındadır.

Ancak - ve bu ölümcül "ama"dır - CPV'nin **seviyeleştirilmiş elektrik maliyeti (LCOE)**, geleneksel silikonu yenmek için mücadele etti. Silikon modülü fiyatları o kadar acımasızca düştü ki (2008'de ~4 $/W'tan, bugün kamu hizmeti ölçekli modüller için 0,10 $/W'ın altına düştü), CPV'nin verimlilik avantajı silikonun katıksız üretim ölçeğinin üstesinden gelemez. 2012 yılında dünya çapında yaklaşık 350 MW CPV kuruluydu. 2020 yılına gelindiğinde yeni kurulumlar yavaşladı. **Amonix**, **SolFocus** ve **Soitec'in CPV bölümü** gibi şirketler kapandı ya da geri adım attı.

CPV ölmedi; bu bir niş. Arazinin son derece pahalı olduğu (verimlilik daha az dönüm anlamına gelir), sıcaklıkların aşırı olduğu (çok bağlantılı hücreler ısıyı silikondan daha iyi idare eder) veya endüstriyel işlemler veya tuzdan arındırma için atık ısıyı yakalayan **hibrit CPV-termal sistemlerde** zorlayıcı olmaya devam ediyor. Ve teknoloji çok önemli bir nesilde varlığını sürdürüyor: **micro-CPV**, küçük yoğunlaştırıcı optikler doğrudan çiplere entegre ediliyor ve potansiyel olarak geleneksel panellerden daha kalın olmayan yüksek verimli modüllere olanak sağlıyor.

## Büyük Rüya: Uzay Tabanlı Güneş Enerjisi

Yörüngeye dönelim. **Uzay tabanlı güneş enerjisi (SBSP)** vizyonu şu şekildedir: Devasa bir güneş dizisini sabit yörüngeye park edin, güneş ışığını elektriğe dönüştürün, elektriği mikrodalgalara (veya lazerlere) dönüştürün, bunları Dünya yüzeyindeki **doğrultucu bir antene ("doğrultucu")** ışınlayın ve tekrar elektriğe dönüştürün. Şebekeyi besleyen, 7/24, hava koşullarından bağımsız, temiz bir güç kaynağı.

Açıkçası, mühendislik zorluklarının ölçeği Kutsal Kitap'a uygundur.

### Zorluk 1: Boyut

Şebekeye **1 GW** güç sağlamak için (bir nükleer reaktörün çıkışına yakın), yörüngede yaklaşık 3-4 GW güneş ışığı toplamanız gerekir (dönüşüm ve iletim kayıplarını hesaba katarak). %30 hücre verimliliğinde bu, yaklaşık **10 milyon metrekare** güneş paneli anlamına gelir; yani bir kenarı 3,2 km karedir. İnsanoğlunun uzayda şimdiye kadar inşa ettiği en büyük yapı olan Uluslararası Uzay İstasyonu yaklaşık 2.500 m²'dir. Bir SBSP uydusu **4.000 kat daha büyük** olacaktır.

### 2. Zorluk: Kablosuz Güç İletimi

Atmosferin 36.000 km uzağına güç ışınlamak bilim kurgu değil, fiziktir. 2,45 GHz veya 5,8 GHz'deki **mikrodalga güç iletimi**, atmosferik geçişin kendisi için yaklaşık **%80-85 verimlilik** ile bulutlardan, yağmurdan ve atmosferden geçebilir. Ancak toplam zincir (DC'den mikrodalgaya, yayılımdan rectenna'ya geri DC'ye) şu anda laboratuvar gösterimlerinde yaklaşık **%40-50 uçtan uca verimliliği** yönetiyor.

Haziran 2023'te **Caltech'in SSPD-1 (Uzay Güneş Enerjisi Göstericisi)**, **MAPLE** dizisini (özel CMOS entegre devrelere sahip esnek alt tabakalar üzerine inşa edilmiş hafif mikrodalga vericileri) kullanarak uzayda gücü kablosuz olarak ileterek tarih yazdı. Ekip, uydu yukarıdan geçerken Pasadena'daki kampüsteki binalarının çatısında bir sinyal bile tespit etti. Bu bir tespitti, kullanışlı bir güç değildi; ancak konseptin, gerçekten fırlatmaya yetecek kadar donanım ışığıyla çalıştığını kanıtladı.

### 3. Zorluk: Maliyet

Starship ekonomisinde bile rakamlar göz korkutucu. 2024'te yapılan bir NASA araştırması, birinci nesil SBSP sisteminin **400 milyar dolar veya daha fazla**, kabaca Danimarka ve Finlandiya'nın toplam GDP maliyetine mal olacağını tahmin etti. *Joule* dergisindeki 2025 tarihli bir makale daha iyimserdi; 10 GHz mikrodalga iletimi kullanan tamamen olgun bir sistemin, on yıllık bir teknoloji geliştirme sürecinden sonra elektriği **9,4 ¢/kWh** ile sağlayabileceğini hesaplıyordu; bu da diğer temiz enerji kaynaklarıyla rekabet edebilir, ancak yine de 2–3 ¢/kWh ile en ucuz karasal güneş enerjisinin üzerindedir.

En önemli değişken lansman maliyetidir. 1 GW uydusu için 10.000 tondan fazla donanımın fırlatılması, 3.000 ABD Doları/kg (şu anki Falcon 9 fiyatı) seviyesinde, tek bir güneş hücresi bile inşa edilmeden önce **yalnızca fırlatma ücreti olarak 30 milyar ABD dolarına** mal olacaktır. 100 $/kg'da (Starship hedefi), bu 1 milyar dolara düşüyor. 10$/kg mı? Şimdi bir gigawatt'ın yörüngeye fırlatılması için 100 milyon dolardan bahsediyorsunuz. Rüyanın ekonomik sürdürülebilirliği aslında lansman maliyet eğrileri üzerine oynanan bir bahistir.

### Bunu Aslında Kim Yapıyor?

Japonya en uzaktadır. **JAXA'nin OHISAMA projesinin** alçak Dünya yörüngesindeki 180 kg'lık bir uydudan kablosuz güneş enerjisi iletimini göstermesi planlanıyor — uydunun **2026**'da fırlatılması planlanıyor. Avrupa Uzay Ajansı'nın **SOLARIS** programı fizibilite çalışmaları yürütüyor. Çin, **2030'a kadar** megawatt sınıfı bir yörünge testi planlarını duyurdu ve mikrodalga güç aktarımı deneyleri için **Bishan, Chongqing**'de yer tabanlı bir test tesisi inşa etti.

Özel sektörde **Virtus Solis**, Starship fırlatmalarına uygun boyutlarda modüler yörüngesel güneş enerjisi santralleri tasarlıyor. UK'nın **Uzay Enerjisi Girişimi**, 2 GW gönderen uydulardan oluşan bir takımyıldız önerdi. Caltech hafif, katlanabilir güneş paneli ve verici teknolojisini geliştirmeye devam ediyor.

## Şaşırtıcı Yakınsama

İşte bu hikayeyi ilginç kılan şey: görünüşte farklı teknolojiler olan uzay güneş enerjisi ve yoğunlaştırıcı PV, aynı fizik üzerinde birleşiyor. Her ikisi de **çok bağlantılı III-V hücreleri** kullanır. Her ikisi de **kilogram başına watt** (fırlatma için) veya **hücre doları başına watt** (CPV için) konularına kafayı takmış durumda. Her ikisinin de hassas **ışın yönlendirmesi** gerekir; CPV için güneşi takip etmek, SBSP için mikrodalgaları yönlendirmek. Ve her ikisi de geleneksel silikonun acımasız maliyet düşüşüne karşı rekabet ediyor.

Yakın vadedeki en olası kazanan ya/veya değil, bir melez. Perovskit-silikon tandem hücrelerinin (22. Gün), silikon benzeri maliyetlerle ancak %35'in üzerinde verimlilikle üretildiğini, CPV- tarzı mikro yoğunlaştırıcılara monte edildiğini ve Starship sınıfı roketlerle fırlatıldığını hayal edin. Her teknoloji diğerini besliyor.

Ve uzay güneş enerjisinin halihazırda burada ve son derece baskın olduğu bir uygulama daha var: **insanlığın şimdiye kadar Dünya'nın ötesine gönderdiği her uyduya, uzay istasyonuna, geziciye ve sondaya güç sağlıyor**. ISS'dan Mars gezicilerine, Jüpiter'in yörüngesindeki Juno sondasına kadar (dış güneş sistemine şimdiye kadar gönderilen en büyük güneş enerjisi dizileri, Jüpiter'in zayıf güneş ışığında 43 m²'den 500 W üretiyor - Dünya'dakinin yalnızca %4'ü kadar yoğun), uzay dereceli güneş pilleri uzay araştırmalarının tartışmasız güç kaynağıdır. 65 yıldır uzayda güneş enerjisi yapıyoruz. Henüz eve ışınlamadık.

## Temel Çıkarımlar

- **Uzay, atmosferin, hava koşullarının ve neredeyse sürekli güneş ışığının olmaması nedeniyle birim alan başına yerdeki güneş enerjisinden 5 ila 10 kat daha fazla enerji alır**
- **III-V çok bağlantılı hücreler** alan uygulamalarına hakimdir: %30–32 verimlilik, radyasyonla sertleştirilmiş, son derece hafif (350–450 W/kg)
- **Yoğunlaştırıcı PV**, 500–1000 kat güneş ışığını küçük, pahalı, ultra verimli hücrelere odaklamak için ucuz optikler kullanıyor; %39 modül verimliliğine ulaşıyor ancak maliyet ve ticari silikon konusunda zorlanıyor
- **Uzay tabanlı güneş enerjisi**, mikrodalga ışınımı yoluyla 7/24 temiz enerji sağlayabilir, ancak büyük ölçek, maliyet ve fırlatma zorluklarının çözülmesini gerektirir
- **Caltech'in SSPD-1** (2023) ve **Japonya'nın OHISAMA** (2026), uzaydan gelen kablosuz gücün ilk gerçek donanım gösterilerini temsil ediyor
- **Fırlatma maliyeti temel değişkendir**: Yörüngeye 10$/kg ile SBSP ekonomik olarak makul hale gelir

---

*Yarın: 27. Gün bizi, kuantum nokta hücrelerinden organik fotovoltaiklere ve öğrendiğimiz her şeyi geçersiz kılabilecek radikal fikirlere kadar geleceğin icat edildiği laboratuvarlara götürüyor. Bugün laboratuvarda neler var ve 2035'te çatınızda ne olabilir?*

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-26.toml}}
