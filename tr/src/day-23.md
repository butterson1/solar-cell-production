# 23. Gün: İki Yüzlü Modüller ve Takip Sistemleri — Her Açıdan Işık Toplamak

*Güneş enerjisi endüstrisi, bir güneş panelinin ön yüzünü mükemmelleştirmek için onlarca yıl harcadı. Sonra biri sordu: Peki ya arkası?*

Devrim niteliğinde olamayacak kadar basit görünüyor. Halihazırda güneş ışığını elektriğe dönüştüren bir güneş hücresi alın, arka tarafını opak yerine şeffaf yapın ve birdenbire panelin altındaki yerden yansıyan ışıktan güç üretmeye başlayın. Ekstra silikon yok. Ek yarı iletken sihirbazlığı yok. Sadece... her iki tarafı da kullan.

Ancak bu aldatıcı derecede basit fikir - **çift yüzeyli modül** - şebeke ölçeğinde güneş enerjisi ekonomisini tamamen yeniden şekillendirdi. Panelleri gökyüzünde güneşi takip edecek şekilde eğen **tek eksenli izleme sistemleri** ile bir araya getirilen çift yüzeyli teknoloji, sabit tek yüzeyli kurulumlara göre %20-30'luk enerji kazanımlarının kilidini açtı. İki yüzeyli modüller, 2018'de yalnızca %10 iken, 2025 itibarıyla küresel hizmet ölçeğindeki sevkiyatların kabaca %70'ini oluşturdu. Bu kademeli bir geçiş değil, bir izdiham.

Bunun nedenini anlamak için, bir güneş panelinin alt tarafında gerçekte neler olup bittiğine, altındaki zeminin nasıl optik bir alete dönüştüğüne ve nispeten basit bir mekanik sistemin (günde bir kez dönen bir çelik kiriş) neden tüm güneş enerjisi alanındaki en uygun maliyetli enerji yükseltmesi olabileceğine bakmamız gerekiyor.

---

## İki Yüzlü Bir Panelin Anatomisi

Geleneksel bir monofasiyal güneş modülü basit bir sandviç yapıya sahiptir: ön tarafta temperli cam, EVA kapsülleyici, güneş pilleri, daha fazla EVA ve opak beyaz bir arka tabaka (tipik olarak Tedlar gibi bir floropolimer). Bu beyaz arka tabaka bir nem bariyeri ve elektrik yalıtkanı görevi görüyor, ancak aynı zamanda bir ayna görevi de görüyor ve iç ışığın bir kısmını ikinci bir geçiş için hücrelere geri yansıtıyor. Yeterince iyi çalışıyor ama bu bir çıkmaz sokak. Modülün arkasına çarpan ışık tamamen boşa gidiyor.

Çift yüzlü bir modül, o opak arka tabakayı şeffaf bir şeyle değiştirir. Piyasaya iki ana yaklaşım hakimdir:

**Cam (çift cam):** Her iki tarafta da temperli cam kullanılır, genellikle her biri 2,0–2,1 mm (tek yüzlü panellerdeki standart 3,2 mm ön camdan daha ince). Bu, son derece dayanıklı, simetrik, sağlam bir yapı oluşturur. Cam, arka tarafta yaklaşık %94 ışık geçirgenliği sunmakta ve mükemmel nem direnci sağlamaktadır, bu nedenle çoğu üretici artık çift yüzeyli ürünlerde bunu tercih etmektedir. Takas mı? Daha ağırdır; cam-cam iki yüzeyli modül genellikle 30-32 kg ağırlığındayken, aynı boyuttaki cam arka tabaka tek yüzeyli panel için bu ağırlık 22-24 kg'dır.

**Cam-şeffaf arka tabaka:** Arka cam, şeffaf bir polimer filmle değiştirilerek ağırlığın yaklaşık 25 kg'a düşürülmesi sağlanır. Şeffaf arka tabaka ışığın yaklaşık %89'unu (camdan daha az) iletir ve daha düşük UV geçirgenliği sunar (camın %40-50'sine karşılık <%1), bu da aslında kapsülleyiciyi UV-kaynaklı bozulmadan koruyabilir. Bununla birlikte, daha düşük arka geçirgenlik, biraz daha az iki yüzeyli kazanç anlamına gelir ve uzun vadeli güvenilirlik verileri, çift camlı tasarımlarla karşılaştırıldığında hala olgunlaşmaktadır.

Hücrelerin kendilerinin de değişikliğe ihtiyacı var. Standart bir PERC hücresinde (9. Gün malzemesi), arka alüminyum temas noktası tüm arka yüzeyi kaplayarak arka aydınlatmayı tamamen engeller. Çift yüzeyli PERC hücreler bunun yerine desenli bir arka kontak kullanır ve arka yüzeyin çoğunu ışık emilimi için açık bırakan bir alüminyum şebekeye sahiptir. Ancak gerçek iki yüzeyli şampiyonlar **n-tipi teknolojilerdir**: TOPCon ve HJT hücreleri, pasifleştirme katmanları şeffaf olduğundan ve açık arka kontakları iki taraflı ışık toplama için tasarlandığından doğası gereği güçlü arka taraf tepkisi üretir.

Bu bizi kritik bir parametreye getiriyor: **iki yüzeylilik faktörü**.

---

## İki Yüzlülük Faktörü: Tüm Sırtlar Eşit Değildir

İki yüzeylilik faktörü, yüzde olarak ifade edilen şekilde, ön tarafa kıyasla arka tarafın ışığı ne kadar verimli dönüştürdüğünü ölçer. Bir hücre önden %22, arkadan %17,6 verim üretiyorsa çift yüzeylilik faktörü %80 olur.

Bu sayı hücre teknolojisine göre önemli ölçüde değişiklik gösterir:

| Teknoloji | Tipik İki Yüzlülük Faktörü |
|---|---|
| Çift Yüzlü PERC (p-tipi) | %70–75 |
| TOPCon (n-tipi) | %80–85 |
| HJT (n-tipi) | %90–95 |
| IBC (n-tipi) | %85–90 |

Bu yayılma düşündüğünüzden daha önemli. %70 ile %90 çift yüzeylilik faktörü arasındaki fark kulağa dramatik gelmeyebilir, ancak arka ışınımın ön ışınımın %15-20'si olabileceği gerçek bir kurulumda, bu enerji veriminde anlamlı bir boşluğa dönüşür - kabaca toplam iki yüzeyli kazancın yüzde 1,5 ila 3 puanı. 200 MW güneş enerjisi çiftliğinde 30 yıllık proje ömrü boyunca, bu milyonlarca kilovat saat ve önemli bir gelir demektir.

NREL, p-tipi PERC'den n-tipi TOPCon ve HJT mimarilerine devam eden geçişin etkisiyle sektör ortalaması iki yüzeylilik faktörlerinin 2021'de yaklaşık 0,70'den 2035'e kadar 0,85'e çıkacağını öngörüyor. Panelin arka tarafının neredeyse ön kısmı kadar iyi hale geldiği ortaya çıktı.

---

## Optik Bir Araç Olarak Zemin

İşte mantığa aykırı kısım: iki yüzeyli bir güneş panelinin performansı büyük ölçüde *altında* ne olduğuna bağlıdır. Zemin yüzeyi dağınık bir reflektör görevi görerek güneş ışığını modülün arka tarafına doğru yansıtıyor. Bu yüzeyin yansıtıcılığı (0'dan (mükemmel soğurucu) 1'e (mükemmel yansıtıcı) kadar **albedo** olarak ölçülür) iki yüzeyli enerji verimi için tartışmasız en önemli çevresel değişkendir.

Bazı tipik albedo değerleri:

- **Taze kar:** 0,80–0,90
- **Beyaz beton/çakıl:** 0,55–0,70
- **Hafif kum/çöl:** 0,35–0,45
- **Kuru çim/çıplak toprak:** 0,20–0,30
- **Koyu toprak/ıslak toprak:** 0,10–0,15
- **Yeşil bitki örtüsü:** 0,15–0,25

Araştırmalar albedodaki her 0,1'lik artışın arka taraftaki güç üretimini yaklaşık %3-5 oranında artırdığını gösteriyor. Bu, büyüleyici bir tasarım düşüncesi yaratır: Güneş enerjisi çiftliğinizin altındaki *kir* artık bir performans değişkenidir.

Bazı geliştiriciler **albedo ile geliştirilmiş yüzeyler** kullanmaya başladı; esas olarak zemini beyaza boyadı veya dizilerinin altına beyaz çakıl veya yansıtıcı membranlar koydu. Beyaz boyalı bir yüzey albedo'yu 0,60-0,70'e itebilir ve koyu toprakta kabaca %5-8'e kıyasla %20'ye varan iki yüzeyli kazanımlar sağlayabilir. Ekonomi sahaya özeldir, ancak arazinin ucuz olduğu ve iki yönlü kazancın daha yüksek kapasite faktörleri yoluyla paraya çevrildiği büyük kamu hizmeti kurulumlarında, beyaz zemin örtüsüne metrekare başına 0,50-1,00 dolar harcamak iki ila üç yıl içinde kendini amorti edebilir.

Ve işte çoğu insanı hazırlıksız yakalayan şaşırtıcı gerçek: **çift yüzeyli modüller kışın yüksek enlemlerde orantısız bir şekilde daha iyi performans gösterir.** Yeri kar kapladığında albedo 0,80'in üzerine çıkar ve güneş gökyüzünde alçakta olduğundan dağınık ve yansıyan ışığın daha büyük bir kısmı arka tarafa çarpar. Kuzey Avrupa kurulumlarında, Ocak ayındaki iki yönlü kazanç %30'u aşabilir ve bu da kısa günlerin kısmen telafi edilmesini sağlar. Bu, ekvatordan *uzaklaşmanın* yalnızca performansı düşürmediği birkaç güneş enerjisi teknolojisinden biridir; panelin arkası buna karşı koyar.

---

## Montaj Yüksekliği ve Sıra Aralığı: Arka Işımanın Geometrisi

İki yüzeyli bir modülün arka tarafı düzgün bir aydınlatma görmüyor. Panelin hemen altındaki zemin alanı, panelin kendisi (ve bitişik sıralar) tarafından gölgelendirilerek, gün boyunca değişen karmaşık bir ışık ve gölge yaması yaratılıyor. Arka ışınım dağılımı üç geometrik parametreye bağlıdır:

**Modülün yerden yüksekliği:** Daha yüksek montaj, arka tarafın aydınlatılmış zemini daha geniş bir şekilde "görmesi" anlamına gelir. Çoğu yardımcı çift yüzeyli kurulum, geleneksel tek yüzeyli sabit eğimli sistemler için kabaca 0,5 ila 1,0 metreye kıyasla modülleri 1,5 ila 2,5 metreye (alt kenar yerden yukarıda) monte eder. Her ilave 0,5 metrelik açıklık, iki yüzeyli kazancın %1-2'sini sağlayabilir, ancak daha uzun rafların maliyeti de artar.

**Sıra aralığı (aralık):** Sıralar arasındaki daha geniş aralık, hem ön tarafta (komşu sıralardan) hem de her sıranın arkasındaki zeminde (ışığı arkaya yansıtan şey) kendi kendine gölgelemeyi azaltır. Modül genişliğinin sıra aralığına bölünmesiyle tanımlanan zemin kapsama oranı (GCR), tek yüzlü izleme cihazı kurulumları için genellikle 0,30-0,40 iken, tek yüzlü izleme sistemleri için 0,40-0,50'dir.

**Eğim açısı:** Sabit eğimde, daha dik açılar arka yüzeyin daha büyük bir kısmını yerden yansıyan ışığa maruz bırakır ancak aynı zamanda sıra gölgelemesini de artırır. İki yüzeyli bir sistem için optimum eğim, genellikle tek yüzeyli bir sistem için enlem için optimize edilmiş açıdan 5 ila 10° daha düşüktür, çünkü arka taraftaki kazanç, daha fazla zeminin görülebildiği daha sığ eğimlerde zirveye ulaşır.

Ancak modern güneş enerjisinin en dönüştürücü donanım yükseltmesini eklediğinizde tüm bu sabit geometri hususları ikincil hale gelir: izleyici.

---

## Tek Eksenli İzleyiciler: Her Şeyi Değiştiren 0,05 ABD Doları/W Yükseltmesi

Tek eksenli bir izleyici mekanik olarak basittir: yere çakılan kazıklar üzerinde desteklenen yatay bir çelik boru (tork tüpü), tüpe bağlı aşıklar üzerine monte edilmiş güneş modülleri. Tipik olarak sadece 5-15 watt çeken küçük bir elektrik motoru, tüm modül sırasını sabahları doğuya bakan taraftan (~55° eğim), öğlen yatay olarak öğleden sonra batıya bakan tarafa (~55° eğim) döndürür. Bir motor, 50-80 metre tork tüpüne yayılan 80-120 modülü çalıştırabilir.

Sabit eğime kıyasla tek eksenli takipten elde edilen enerji kazancı, enlem ve iklime bağlı olarak genellikle **%15-25**'tir. Güneybatı Amerika, Şili'nin Atacama'sı veya Arap Yarımadası gibi doğrudan normal ışınımın yüksek olduğu (DNI) konumlarda izleyici kazanımları %25'i aşıyor. Daha dağınık ışığın olduğu daha bulutlu iklimlerde, izleme esas olarak doğrudan ışın radyasyonundan yararlandığından kazanç %12-18'e düşer.

Pazar liderleri bu teknolojinin ne kadar baskın hale geldiğinin öyküsünü şöyle anlatıyor:

- **Nextracker** (Flex Ltd'den türetildi, 2023'te IPO' edildi): ~%30 küresel pazar payı, dünya çapında 90'ın üzerinde GW konuşlandırıldı
- **Array Technologies** (Albuquerque, NM): ~%15-18 pazar payı, pasif rüzgar depolama mekanizmasına sahip DuraTrack platformuyla biliniyor
- **Arctech Solar** (Kunshan, Çin): ~%12 pazar payı, Çin'in en büyük takip cihazı üreticisi
- **Trina Tracker** (Trina Solar'ın yan kuruluşu): hızla büyüyor ve Trina'nın modül üretimiyle dikey entegrasyondan yararlanıyor
- **Soltec** (Murcia, İspanya): Avrupa ve Latin Amerika'da güçlü

Tek eksenli izlemenin maliyet primi kabaca kurulu kapasitenin **watt başına 0,04-0,06 ABD dolarıdır**. 300 MW elektrik santrali için bu, 12–18 milyon dolarlık ek donanım demektir; bu, 30 yıllık kullanım ömrü boyunca %20–25 enerji kazancıyla birçok kez geri ödenir. İzleyiciler o kadar belirgin bir şekilde maliyet etkin hale geldi ki, 2025 yılına kadar ABD'deki yeni şebeke ölçekli güneş enerjisinin yaklaşık %70'i tek eksenli izleme ile konuşlandırıldı.

---

## Geriye Dönüş: Geometriyi Zekice Aşan Algoritma

İzleyicilerin gerçekten akıllılaştığı yer burasıdır. Sabahın erken saatlerinde ve öğleden sonra, güneşin ufukta alçakta olduğu zamanlarda, güneşe doğru agresif bir şekilde eğilmek, her sıranın komşusunun üzerine gölge düşürmesine neden olur. Basit bir izleme algoritması, her bir satırdaki geliş açısını maksimuma çıkaracak, ancak bitişik satırların çıktısını yok edecektir.

Çözüm **geri izleme**: yazılım, güneşin az olduğu dönemlerde eğim açısını kasıtlı olarak azaltır ve sıralar arası gölgelemeyi tamamen ortadan kaldırmak için doğrudan ışın yakalamanın bir kısmından fedakarlık eder. İzleyici, komşu sıralardaki çok daha büyük gölge kaybını önlemek için her sıradaki küçük bir kosinüs kaybını kabul ederek optimum güneşe bakma açısından "geri çekilir".

Matematik zariftir. Belirli bir güneş yükselme açısı ve sıra aralığı için, her sıranın gölgesinin tam olarak bir sonraki sıranın tabanına düştüğü benzersiz bir izleme açısı vardır; sıfır gölgeleme çakışması. Klasik geri izleme algoritmaları bu açıyı geometrik olarak hesaplar. Ancak Array Technologies'in **SmarTrack** gibi modern sistemleri daha da ileri gidiyor: her bir motor bloğu için geri izlemeyi optimize etmek amacıyla gerçek üretim verileri ve arazi analizi üzerine eğitilmiş makine öğrenimini kullanıyor ve optimum açıyı birkaç derece değiştirebilen yerel zemin eğimi değişikliklerini hesaba katıyor.

Nextracker'ın **TrueCapture** sistemi de benzer bir AI-odaklı yaklaşım benimsiyor; hava durumu istasyonu verilerini, ışınım sensörlerini ve hatta uydu görüntülerini kullanarak izleme algoritmalarını gerçek zamanlı olarak ayarlıyor. Standart izleme algoritmalarına göre %2-6 oranında ek enerji kazanımı talep ediyorlar; bu da şebeke ölçeğinde anlamlı LCOE azalma anlamına geliyor.

Özellikle iki yüzeyli modüller için geri izleme daha da ilginç hale geliyor. Geri izleme periyotları sırasında, modüller yataya daha yakındır, bu da aslında arka tarafı yerden yansıyan ışığa daha fazla maruz bırakarak arka taraftaki aydınlatmayı *artırır*. Bazı gelişmiş algoritmalar artık **iki yüze duyarlı geri izleme** gerçekleştiriyor; burada geri izleme açısı, yalnızca ön taraftaki doğrudan ışın değil, ön + arka enerji yakalamanın birleşimini en üst düzeye çıkarmak için daha da optimize ediliyor. Kazanımlar mütevazı (%0,5-1,5) ancak ücretsizdir; bu yalnızca bir yazılımdır.

---

## İki Yüzlü + Takipçi Sinerjisi

Tek eksenli izleyiciler üzerindeki iki yüzeyli modüllerin kombinasyonu, katkının ötesinde kazançlar üretir. İşte nedeni:

Paletli iki yüzeyli bir sistem, modülleri gün boyunca doğrudan ışına kabaca dik tutar. Bu, modülün hemen altındaki zemin gölgesinin güneşle birlikte hareket ettiği ve sürekli olarak taze zemini güneş ışığına maruz bıraktığı anlamına gelir. Yeni aydınlatılan zemin, ışığı arka tarafa yansıtıyor. Bunun aksine, sabit eğimli çift yüzeyli sistem statik bir gölge düzenine sahiptir ve modüllerin altındaki zemin, özellikle düşük GCR değerlerinde günün büyük bölümünde gölgeli kalabilir.

Monofasiyal sabit eğime göre iki yüzeyli + izlemenin birleşik enerji kazancı, uygun koşullarda (yüksek DNI, orta-yüksek albedo) **%27-35**'e ulaşabilir. Ilıman iklimlerde bile %20-25'lik birleşik kazanç tipiktir. PPA fiyatı 0,03 ABD Doları/kWh olan bir kamu hizmeti tesisi için, 30 yıl boyunca bu ekstra enerji üretimi, artan maliyeti kolayca haklı çıkarır.

Bu sinerji, eşleştirmeyi yeni kamu hizmeti inşaatı için esasen standart hale getirdi. 2026'da 100'den fazla MW güneş enerjisi çiftliği inşa ediyorsanız, neredeyse kesinlikle AI-optimize edilmiş geri izleme yazılımına sahip tek eksenli izleyiciler üzerinde n tipi iki yüzeyli modüller kullanıyorsunuzdur. Artık son teknoloji değil; temel çizgi.

---

## Çift Eksenli Takip: (Genellikle) Alınmayan Yol

Eğer izlemenin bir ekseni iyiyse neden iki olmasın? Çift eksenli izleyiciler, hem azimutu (doğu-batı) hem de yüksekliği (yukarı-aşağı) ayarlayarak modülleri gün boyunca *ve* mevsimler boyunca doğrudan güneşe dönük tutar. Sabit eğimden elde edilen enerji kazancı %30-45'tir; bu, tek eksene göre önemli ölçüde daha fazladır.

Peki neden her yerde değiller?

**Maliyet ve karmaşıklık.** Çift eksenli bir izleyici, rüzgar yüklerini keyfi yönlerde idare etmek için daha sağlam bir yapıya, daha güçlü motorlara ve daha karmaşık kontrol sistemlerine ihtiyaç duyar. Kurulu maliyet primi kabaca 0,12-0,18 ABD doları/W'dir; bu, tek eksenliye göre üç ila dört kat daha yüksektir. Tek eksene göre ilave %10-15'lik enerji kazancı, şebeke ölçeğinde bu maliyeti nadiren karşılar.

**Arazi kullanımı.** Çift eksenli izleyiciler, karşılıklı gölgelemeyi önlemek için birimler arasında daha fazla boşluğa ihtiyaç duyar ve tek eksenli sıralara kıyasla güç yoğunluğunu (hektar başına MW) azaltır. Arazinin pahalı olduğu yerde bu ekonomiyi öldürür.

**Bakım.** Daha fazla hareketli parça, daha fazla rulman, daha fazla potansiyel arıza modu. Tek eksenli izleyiciler son derece güvenilirdir; tek bir doğrusal aktüatör veya minimum hareketli parçaya sahip döner tahrik. Çift eksenli sistemler en az iki kat daha fazla mekanik karmaşıklığa sahiptir.

Çift eksenli izleme iki alanda varlığını sürdürüyor: Yüksek konsantrasyonlu optiklerin hassas yönlendirme (±0,1°) gerektirdiği **yoğunlaştırılmış fotovoltaikler (CPV)** ve sınırlı sayıda panelden üretimi en üst düzeye çıkarmanın birim başına maliyeti haklı çıkardığı küçük **şebekeden bağımsız konut kurulumları**. Faydalı güneş enerjisi alanında tek eksen kesin bir şekilde kazandı.

---

## Sınır: Sırada Ne Var?

Çift yüzeyli + takip cihazı hikayesi henüz bitmedi. Bazı gelişmeler sınırları zorluyor:

N-tipi geçişten kaynaklanan **daha yüksek iki yüzeylilik faktörleri**, arka taraf neslinin ön taraf eşitliğine yaklaştığı anlamına gelir. Beyaz çakıl üzerinde çalışan %95 çift yüzeyli bir HJT hücresi, toplam üretimin %15'ini aşan arka taraf katkısı görebilir.

Nextracer (NX Horizon) gibi şirketlerin **araziye uyum sağlayan izleyicileri**, zemin hatlarını takip eden bağımsız motor bloklarıyla engebeli veya engebeli araziler için tasarlanmıştır. Bu, daha önce güneş enerjisiyle takip edilen eğimli alanlar, ıslah edilen maden sahaları ve düzensiz parseller için uygun olmayan arazilerin açılmasını sağlıyor.

**Agrivoltaics** (yükseltilmiş iki yüzeyli izleyici dizileri altında çiftçilik), güneş enerjisi üretimi ve tarımın aynı araziyi paylaştığı ikili kullanımlı bir model yaratıyor. Çiftlik ekipmanlarının altından geçmesine izin vermek için modülün yüksekliği 4-5 metreye çıkarıldı ve paletli panellerden gelen hareketli gölgeler, su stresini azaltarak gölgeye dayanıklı bitkilere gerçekten fayda sağlayabilir.

Bu gelişmeler ortak bir temayı paylaşıyor: Çift yüzeyli modüller ve izleyiciler, güneş enerjisini "güneşi işaret et ve unut" teknolojisinden, geometri, optik, zemin koşulları ve yazılım algoritmalarının mevcut ışıktan mümkün olan her fotonu sıkıştırmak için etkileşime girdiği karmaşık bir sisteme dönüştürdü.

---

## Yarının Önizlemesi

Güneş panellerinden nasıl *daha fazla* enerji elde edebileceğimizden bahsediyoruz; daha verimli hücreler, iki yüzeyli kazanç, izleme. Peki ya güneş panellerinin yapılı çevrede *kaybolmasını* sağlamaya ne dersiniz? Yarın, cephelere, pencerelere, çatı kiremitlerine ve hatta yol yüzeylerine gömülü güneş pilleri olan **Binaya Entegre Fotovoltaikleri (BIPV)** keşfedeceğiz. Bu temelde farklı bir tasarım felsefesi: Binalara güneş panelleri eklemek yerine bina güneş paneli *oluyor*. Mühendislik zorlukları büyüleyici ve estetik olanaklar güneşi görünmez kılmak üzere.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-23.toml}}
