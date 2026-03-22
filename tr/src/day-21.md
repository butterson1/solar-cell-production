# 21. Gün: Perovskit Güneş Hücreleri — Sıradaki Devrim mi?

*4. Hafta, 1. Ders — Sınır ve Gelecek*

---

Yirmi gün boyunca silikonun kuvarsit madeninden bitmiş modüle kadar olan yolculuğunu izledik; bu süreç 1.400°C'nin üzerinde sıcaklıklar, ultra saf temiz odalar, elmas telli testereler ve milyarlarca dolarlık sermaye ekipmanı gerektirir. Silikon güneş pilleri harika çalışıyor. Peki ya gazete bastığınız gibi bir güneş hücresi yapabilseydiniz?

Perovskit güneş pillerinin baştan çıkarıcı vaadi budur: Üretimi o kadar kolay olan bir malzeme sınıfı ki araştırmacılar kelimenin tam anlamıyla mutfakta, oda sıcaklığında, kilogram başına birkaç yüz dolara çevrimiçi satın alabileceğiniz çözümlerden çalışan cihazlar yaptılar. On yıldan biraz daha uzun bir süre içinde perovskitler laboratuvar merakı olan %3,8 verimlilikten %26,7'yi aşan sertifikalı hücrelere fırladı; bu, silikonun yarım yüzyıllık yürüyüşünü buzul gibi gösteren bir gelişme hızı. Ve silikonun üstüne yerleştirilen tandem konfigürasyonlarda zaten %35'i aştılar.

Ama bir sorun var. Her zaman bir yakalama vardır.

## Perovskit Nedir?

"Perovskit" kelimesi tek bir malzemeyi isimlendirmez. ABX₃ olarak adlandırılan atomların belirli bir geometrik düzeni olan *kristal yapıyı* adlandırır. Orijinal perovskit minerali, kalsiyum titanat (CaTiO₃), 1839'da Ural Dağları'nda keşfedildi ve adını Rus mineralog Lev Perovski'den aldı. Güneş enerjisiyle alakası yoktu.

ABX₃ formülünde, **A** bir küpün köşelerinde bulunan büyük bir katyondur, **B** merkezde daha küçük bir metal katyondur ve **X**, B çevresinde bir oktahedron oluşturan bir anyondur (tipik olarak bir halojenür). Bunu bir kutu gibi düşünün: B atomu, altı X atomundan oluşan bir kafesin içinde oturur ve A atomları, bu kafeslerin arasındaki boşlukları doldurarak yapısal destek sağlar.

Güneş pilleri için sihirli tarif şudur:

- **A bölgesi**: Metilamonyum (MA⁺, CH₃NH₃⁺), formamidinyum (FA⁺, HC(NH₂)₂⁺), sezyum (Cs⁺) veya bunların karışımları
- **B-site**: Kurşun (Pb²⁺) — iş gücü ve tartışma
- **X-bölgesi**: İyodür (I⁻), bromür (Br⁻), klorür (Cl⁻) veya karışık halojenürler

Prototip bileşik, metilamonyum kurşun iyodür (MAPbI₃), yaklaşık 1,55 eV'lik bir bant aralığına sahiptir - tek bağlantılı güneş pilleri için Shockley-Queisser limiti tarafından tahmin edilen 1,34 eV tatlı noktaya heyecan verici derecede yakındır. A-bölgesinin veya X-bölgesinin parçalarını değiştirerek (örneğin, iyodürün bir kısmını bromürle değiştirerek) bant aralığını yaklaşık 1,2 eV'den 3,0 eV'ye kadar sürekli olarak ayarlayabilirsiniz. Elektromanyetik spektrum için bir radyo kadranına sahip olmak gibidir.

Bu ayarlanabilirlik çılgınca. Silikon size bir bant aralığı verir: 1,12 eV. Al ya da bırak. Perovskitler, ilk ilkelerden yola çıkarak emilim profilini *tasarlamanıza* izin verir; tandem konfigürasyonlarda bu kadar güçlü olmalarının nedeni tam olarak budur (bununla ilgili daha fazlası yarın).

## Perovskitler Işığı Emme Konusunda Neden Saçma Bir Şekilde İyidir?

İşte sizi durduracak bir sayı: Yalnızca **500 nanometre kalınlığında** (yarım mikrometre, kabaca insan saçı çapının 1/200'ü kadar) bir perovskit film, 200 mikrometre kalınlığındaki bir silikon levhayla aynı miktarda güneş ışığını emer. Bu 400x'lik bir faktör.

Bunun nedeni, bu malzemelerin fotonlarla nasıl etkileşime girdiğine iniyor. Perovskitler *doğrudan bant aralıklı* yarı iletkenlerdir; yani bir elektron değerlik bandından iletim bandına geçtiğinde momentumu korumak için eş zamanlı olarak bir fonon (kafes titreşimi) soğurması veya yayması gerekmez. Geçiş düz bir şekilde gerçekleşir; foton içeri girer, elektron desteklenir. Buna karşılık silikon, fonon yardımını gerektiren *dolaylı* bir bant aralığına sahiptir, bu da doğası gereği birim kalınlık başına emilimi daha az olası hale getirir.

MAPbI₃'nın absorpsiyon katsayısı 550 nm dalga boyunda yaklaşık 1,5 × 10⁵ cm⁻¹'dir; bu, aynı dalga boyundaki silikondan kabaca 10 kat daha yüksektir. Pratik sonuç: şaşırtıcı derecede az malzemeye ihtiyacınız var. Bir perovskit güneş hücresi, standart bir silikon hücre için metrekare başına kabaca 800 grama kıyasla, metrekare başına belki de 1 gram aktif madde kullanır. Daha az malzeme, daha az maliyet, üretim için daha az enerji ve daha hafif paneller anlamına gelir.

Ancak avantajlar emilimle bitmiyor. Perovskitler ayrıca oldukça uzun taşıyıcı difüzyon uzunlukları da sergiliyor; bu uzunluk, uyarılmış elektronların ve deliklerin yeniden birleşmeden önce kat edebileceği mesafedir. Yüksek kaliteli tek kristallerde 175 mikrometreyi aşan difüzyon uzunlukları ölçülmüştür. Çok kristalli ince filmlerde bile (gerçekte bir cihazda kullanacağınız türden), 1-10 mikrometrelik değerler yaygındır. Filmin kalınlığı yalnızca 500 nm olduğundan, bu, taşıyıcıların yeniden birleşmeden önce elektrotlara kolayca ulaşabilecekleri anlamına gelir. Bu, çoğu arabanın dolu depoyla kat ettiği mesafeden daha kısa bir otoyol inşa etmeye benziyor.

## Beherden Güneş Hücresine: Perovskitler Nasıl Yapılır?

Perovskitlerin silikondan en dramatik biçimde ayrıldığı nokta burasıdır. 4. Gündeki Czochralski sürecini hatırlıyor musunuz - 1.425°C'lik bir eriyikten dakikada 1-2 mm hızla bir kristal çekmek? Perovskit birikimi bir duvarı boyamaya daha yakındır.

En yaygın laboratuvar tekniği **döndürerek kaplama**dır: öncü tuzları (örneğin kurşun iyodür ve metilamonyum iyodür) dimetilformamid (DMF) gibi bir çözücü içinde çözersiniz, çözeltiyi bir alt tabakaya bırakırsınız ve 2.000–6.000 RPM sıcaklıkta döndürürsünüz. Çözücü uçup gidiyor ve yaklaşık 30 saniye içinde ince bir film kristalleşiyor. Toplam enerji girişi: önemsiz. Sıcaklık: Kısa bir tavlama adımı için genellikle 100–150°C. Bunu silikonun birçok gün süren, binlerce derecelik destanıyla karşılaştırın.

Endüstriyel ölçek büyütmede önde gelen rakip, öncü mürekkebin dar bir yarıktan hareketli bir alt tabaka üzerine pompalandığı sürekli bir rulodan ruloya işlem olan **slot-die kaplama**'dır. Dakikada metre hızla hareket eden çok hassas bir sileceği düşünün. Slot-die kaplamalı perovskit modüller 10×10 cm² ölçeğinde halihazırda %17,6 verimliliğe ulaştı ve şirketler bunu tam boyutlu panellere taşıyor.

Ayrıca **buhar biriktirme** de var; öncülleri bir vakum odasında buharlaştırıyor ve alt tabaka üzerinde yoğunlaşmalarını sağlıyor. UK-merkezli şirket olan Oxford PV (fabrikası Brandenburg, Almanya'dadır), tandem ürünleri için perovskit katmanlarını dokulu silikon hücrelerin üzerine biriktirmek için ortak buharlaştırma yaklaşımını kullanır. Buhar biriktirme, mükemmel film bütünlüğü sağlar ve çözelti işlemenin solvent toksisitesi sorunlarını ortadan kaldırır, ancak vakum ekipmanı gerektirir ve sermaye maliyetini artırır.

İlgi çeken alternatiflerden biri de, perovskit öncü mürekkebini hassas desenlerde biriktiren **mürekkep püskürtmeli baskı**'dır; tam anlamıyla bir fotoğraf bastığınız gibi güneş pilleri basar. Bu, karmaşık modül tasarımlarına olanak tanır ve malzeme israfını en aza indirir, ancak üretim bir zorluk olmaya devam etmektedir.

## Verimlilik Roketi

Perovskit verimlilik kazanımlarının hızı, fotovoltaikte gerçekten benzeri görülmemiş bir düzeydedir. İşte zaman çizelgesi:

- **2009**: Tsutomu Miyasaka'nın Japonya'daki grubu, boyaya duyarlı bir mimaride perovskiti duyarlılaştırıcı olarak kullanan, %3,8 verimliliğe sahip ilk perovskit güneş hücresini bildirdi. Hücre, sıvı elektrolit içinde dakikalar içinde bozundu.
- **2012**: Oxford'dan Henry Snaith ve Kore'deki Nam-Gyu Park bağımsız olarak katı hal perovskit hücrelerinin %10'u aştığını göstererek malzemenin sıvı elektrolitler olmadan çalışabileceğini kanıtladı. Bu dönüm noktasıdır.
- **2015**: Verimlilik %20'yi aştı.
- **2020**: Verimlilik %25,2'ye ulaştı.
- **2024**: Tek eklemli perovskit hücreleri %26,7'ye ulaştı (NREL tarafından onaylanmıştır).
- **2025**: LONGi'nin perovskit-silikon ikilisi %34,85'e ulaştı ve NREL tarafından onaylandı.

Bağlam açısından, kristal silikonun perovskitlerin on beş yılda eşleştiği kabaca aynı tek bağlantı verimliliğine ulaşması 1954'ten (Bell Laboratuvarlarında %6) 2024'e (LONGi'ye göre %26,81) - yetmiş yıl - ulaştı. Ve silikon, malzeme biliminde onlarca yıldır öndeydi, Ar-Ge fonunda milyarlarca dolarlık bir avantaja sahipti ve temel bilgi sağlayan yarı iletken endüstrisinin tamamı vardı.

MAPbI₃ için teorik tek bağlantı sınırı (bant aralığı ~1,55 eV), Shockley-Queisser çerçevesi altında %31 civarındadır. Bant aralıkları 1,34 eV'ye yakın olan optimize edilmiş perovskit bileşimleri için sınır %33,7'ye tırmanıyor. Hala önemli bir boşluk payı var.

## Odadaki Fil: Kararlılık

Güneş enerjisi sektörü yöneticilerini geceleri uykusuz bırakan mantığa aykırı gerçek şu: **Perovskitlerin üretimini kolaylaştıran aynı özellikler aynı zamanda onların yok edilmesini de kolaylaştırıyor.**

Silikon güneş hücresi, dünyadaki en kararlı malzemelerden birinden yapılmıştır. Silikon dioksit (cam) silikonun oksidasyonunun ürünüdür ve koruyucu bir bariyer oluşturur. Silikon paneller rutin olarak yıllık %0,5'ten daha az bozulmayla 25-30 yıl dayanır. Dolu fırtınalarından, çöl sıcağından, kutup soğuğundan ve kıyı neminden kurtulurlar.

Perovskitler mi? Yumuşak iyonik kafesleri Aşil topuğudur. Bozunma yolları çok sayıdadır ve birbiriyle bağlantılıdır:

**Nem:** Su molekülleri kristal yapıya sızar ve metilamonyum kurşun iyodürü kurşun iyodür, metilamin gazı ve hidroiyodik asite ayrıştırır. Oda sıcaklığında yalnızca %55'lik bir bağıl nem, kapsüllenmemiş bir film için saatler içinde bozulmaya başlayabilir. Bir zamanlar koyu kahverengi olan bir filmde görünen PbI₂'nin sarı rengi, ölmekte olan bir perovskit hücresinin görsel imzasıdır.

**Isı:** Çatı panellerinin yaz aylarında rutin olarak ulaştığı sıcaklık olan yaklaşık 85°C'nin üzerinde, metilamonyum katyonu buharlaşmaya başlar. Kelimenin tam anlamıyla kristalden buharlaşır. Formamidinyum bazlı bileşimler termal olarak daha kararlıdır, bu nedenle alan büyük ölçüde saf MA'den FA-zengin ve FA/Cs karışık bileşimlere geçiş yapmıştır.

**Işık:** Uzun süreli aydınlatma, perovskit kafes içinde iyon göçüne neden olur. Bu yumuşak yapılarda nispeten hareketli olan iyodür iyonları, yerleşik elektrik alanı altında sürüklenerek arayüzlerde birikir. Bu, yerel bileşim değişiklikleri yaratır, kümeleri kusurlu hale getirir ve karışık halojenür bileşimlerinde faz ayrımını tetikleyebilir; iyodür açısından zengin ve bromür açısından zengin alanlar ayrılır, her biri farklı bir bant aralığına sahiptir ve dikkatle tasarlanmış absorpsiyon profilini bozar.

**Oksijen + Işık:** Belki de en sinsi yol. Aydınlatma altında perovskit yüzeyinde süperoksit radikalleri (O₂⁻) oluşur ve bunlar daha sonra organik katyona saldırır. Bu foto-oksidasyon yolu, iyi kapsüllenmiş bir hücrenin bile eser miktarda oksijen mevcut olması durumunda bozunabileceği anlamına gelir.

Sektörün operasyonel kararlılık açısından mevcut en iyi sonuçları: bileşime ve kapsülleme şemasına bağlı olarak sürekli aydınlatma altında maksimum güç noktasında yaklaşık 1.000-5.000 saat. Karşılaştırma için, silikon modüllere yönelik IEC 61215 sertifikası, yaklaşık 25 yıllık saha maruziyetine eşdeğer koşullar altında dayanıklılığın gösterilmesini gerektirir. Perovskit'ler henüz orada değil ama aradaki fark kapanıyor.

Oxford PV Ocak 2026'da perovskit-silikon tandem modülleri için 2028 yılına kadar 20 yıllık bir kullanım ömrü hedeflediğini duyurdu; bu, silikonun garanti alanına yaklaşan ilk perovskit ürünü olacak.

## Kurşun Sorunu

Gelelim diğer file: neredeyse tüm yüksek verimli perovskit güneş pilleri kurşun içeriyor. Standart bir MAPbI₃ hücresinde metrekare başına yaklaşık 0,4 gram kurşun bulunur. Şebeke ölçeğinde bir güneş enerjisi çiftliği genelinde bu bir araya geliyor.

Bu aslında bir sorun mu? Kime sorduğunuza bağlı. Taraftarlar, standart bir araba aküsünün 10 kg kurşun içerdiğini ve kurşun lehimin elektronikte her yerde bulunduğunu belirtiyor. 1 GW üreten bir perovskit güneş çiftliğindeki toplam kurşun yaklaşık 400 kg olacaktır; bu, halihazırda dolaşımda olan kurşunun çok küçük bir kısmıdır. Ve kurşun tamamen geri dönüştürülebilir.

Eleştirmenler, çözünebilir kurşun bileşiklerinin (PbI₂ gibi) metalik kurşundan daha biyolojik olarak kullanılabilir olduğunu ve yağmur fırtınasında çatlayan bir panelin kurşunun toprağa ve yeraltı suyuna sızmasına neden olabileceğine karşı çıkıyor. Araştırmalar, hasarlı perovskit modüllerinin, milyarda 15 parça olan EPA güvenli içme suyu limitlerini aşan konsantrasyonlarda kurşun salabildiğini göstermiştir.

İzlenen çözümler şunları içerir:

1. **Kapsülleme mühendisliği** — modül çatladığında bile kurşunun kaçmasını fiziksel olarak önleyen çok katmanlı bariyerler. Sülfonlanmış aerojel kapsülleme, kurşun sızıntısının 10 ppb'nin altına düştüğünü göstermiştir.
2. **Kurşun tutma katmanları** — modülün içine yerleştirilmiş, çözünmüş kurşunu kaçmadan önce yakalayan kimyasal süngerler. Araştırmacılar, hasarlı hücrelerdeki kurşunun %99'undan fazlasını emen fosfat bazlı ve amino aşılanmış karbon ağ katmanlarını gösterdi.
3. **Kalay bazlı perovskitler** — kurşunun kalay (Sn²⁺) ile değiştirilmesi. Sorun: kalay havada kolayca Sn²⁺'den Sn⁴⁺'ye oksitlenir, bu da performansı düşürür. En iyi salt kalaylı perovskit hücreler, kurşun bazlı cihazların çok gerisinde, yaklaşık %15 verime ulaşır.
4. **Kurşunsuz alternatifler** — bizmut, antimon ve germanyum bazlı bileşikler araştırılıyor, ancak hiçbiri kurşun halojenür perovskitlerin performansına yaklaşamıyor.

İleriye yönelik pragmatik yol, kurşunu tamamen ortadan kaldırmak yerine sağlam kapsülleme + kullanım ömrü sonu geri dönüşümü gibi görünüyor. Sonuçta, kadmiyum tellür (CdTe) ince film panelleri (First Solar'ın ekmeği ve tereyağı) muhtemelen kurşundan daha toksik olan kadmiyum içeriyor ve yirmi yıldır ticari olarak başarılılar.

## Bunları Aslında Kim Yapıyor?

Ticarileştirme yarışı kızışıyor:

**Oxford PV** (Brandenburg, Almanya) ilk ticari perovskit-silikon tandem modüllerini Eylül 2024'te piyasaya sürdü: %24,5 verimlilikle 72 hücreli paneller, geleneksel silikona göre %20 daha fazla enerji üretimi talep ediyor. 2027'de seri üretim için GW-ölçekte bir fabrika planlıyorlar. Şubat 2026'da First Solar, ABD pazarındaki perovskit teknoloji hakları için Oxford PV ile münhasır olmayan bir lisans anlaşması imzaladı.

**UtmoLight** (Wuxi, Çin), yılda 1,8 milyon paneli hedefleyerek dünyanın ilk GW-ölçekli perovskit üretim hattını 2025'in başlarında faaliyete geçirdi. Pilot üretimde, 2,8 m²'lik devasa bir modülden %16,1 verimlilikle 450 W çıkış elde ettiler. Hedefleri: %20 seri üretim verimliliği, %18,1'i zaten 0,72 m² modüllerde kanıtlanmıştır.

**Microquanta Semiconductor** (Hangzhou, Çin), 100'den fazla MW perovskit üretim hattı işletiyor ve gerçek dünyadaki pilot projelerde modüller kullanıyor ve uzun vadeli performansa ilişkin önemli saha verilerini topluyor.

**GCL Perovskite** (Çin), **Renshine Solar** ve **Wonder Solar**'ın her biri 100 MW ölçeğinde üretim hatları işletiyor ve ülkenin silikon PV alanındaki hakimiyetini yansıtmaya başlayan Çin perovskit üretim ekosistemine katkıda bulunuyor.

Şu anda en az beş Çinli şirketin 100 MW veya daha yüksek üretim hatları var ve önümüzdeki birkaç yıl içinde GW-ölçekte olma hedefi açıkça görülüyor.

## Üretim Maliyeti Denklemi

Perovskitlerin gerçekten yıkıcı olabileceği yer burasıdır. Perovskit modüllerin teorik maliyet tabanı silikondan çok daha düşüktür:

- **Yüksek sıcaklıkta kristal büyümesi olmaz** — çözelti bazlı yöntemler için tüm süreç 150°C'nin altında kalır
- **Elmas tel testereyle kesmeye gerek yok** — dilimlenecek külçe yoktur, bu da çentik kaybını tamamen ortadan kaldırır
- **Minimum malzeme tüketimi** — ~1 g/m² aktif maddeye karşılık ~800 g/m² silikon için
- **Esnek alt tabakalarla uyumludur** — cam isteğe bağlıdır, plastik veya metal folyo üzerinde rulodan ruloya üretim yapılabilir
- **Daha düşük sermaye harcaması** — perovskit kaplama hattının maliyeti silikon hücre fabrikasının çok altındadır

Sektör analistleri, GW ölçeğinde perovskit modül üretim maliyetlerinin 0,10-0,15 $/W'a ulaşabileceğini tahmin ediyor; bu da silikon modüllerin mevcut maliyetinin yaklaşık yarısı kadar. Ama "ulaşabilmek" bu cümlede ağır kaldırmak anlamına geliyor. Günümüzün perovskit modülleri aslında silikondan daha pahalıdır çünkü üretim hacimleri küçüktür, verimler hâlâ optimize edilmektedir ve kapsülleme gereklilikleri maliyeti artırmaktadır.

Dürüst resim: Perovskitler, kanıtlanmış üretim verimleriyle üretim 10+ GW ölçeğine ulaşana kadar maliyet açısından silikonla rekabet etmeyecektir. UtmoLight'ın kurucu ortağı Jesse Zheng, 2025'teki bir konferansta perovskitlerin "henüz silikonla rekabet edemediğini" kabul etti, ancak geçiş noktasının kümülatif üretim kapasitesinin 10 GW civarında olabileceğini öne sürdü.

## Perovskitleri *Farklı* Yapan Nedir? — Felsefi Bir Ayrım

Bu kurs boyunca silikon üretiminin temel olarak entropiyle mücadele etmek, yani muazzam enerji girdileri yoluyla düzensizlikten düzen yaratmakla ilgili olduğunu gördük. Kuvarsı 1.800°C'de eritiyor, karbonla indirgeyip, 1.100°C'de Siemens prosesiyle saflaştırıyor, 1.425°C'de kristalleri büyütüyor ve katkı maddelerini 800°C'de tavlıyorsunuz. Her adım, doğanın düzensizlik tercihine karşı enerji yoğun bir savaştır.

Perovskitler bu senaryoyu tersine çeviriyor. ABX₃ kristal yapısı *oluşmak istiyor*. Doğru tuzları bir solvent içinde karıştırın ve perovskit, mutfak fırınınızın ulaşabileceği sıcaklıklarda solvent buharlaştıkça kendiliğinden kristalleşir. Termodinamik sizin tarafınızda. Döndürmeli kaplayıcıya sahip bir yüksek lisans öğrencisinin öğleden sonra çalışan bir perovskit hücresi yapabilmesinin nedeni budur; silikon hücrenin inşası için ise 500 milyon dolara mal olan bir fabrika gerekir.

Ancak termodinamik verir ve alır. Kolayca oluşan bir yapı aynı zamanda kolayca *biçimsizleşebilir*. Perovskitlerin üretimini kolaylaştıran düşük oluşum enerjisi, onları neme, ısıya ve ışığa karşı savunmasız hale getiren düşük oluşum enerjisiyle aynıdır. Kararlılık sorunu, akıllı mühendisliğin basitçe ortadan kaldıracağı bir hata değildir; bu, bu malzemelerin temel fiziğidir. Her stabilite iyileştirmesi, aslında perovskitleri çekici kılan aynı termodinamik erişilebilirlikle mücadele ediyor.

Yapılması kolay, sürdürülmesi zor olan bu gerilim, perovskit fotovoltaiklerin merkezi dramasıdır ve alanın 21. yüzyılın en yaratıcı malzeme biliminden bazılarını çekmesinin nedeni budur.

## İleriye Bakmak

Yarın, pek çok araştırmacının perovskitlerin ticari pazara girmesi için yakın vadede en muhtemel yol olarak düşündüğü şeyi keşfedeceğiz: bağımsız paneller olarak değil, geleneksel silikon hücrelerin *üzerinde* ince bir tabaka olarak. Tandem hücreler (alttaki silikon kırmızı ve kızılötesi ışığı yakalıyor, üstteki perovskit ise mavi ve yeşili yakalıyor) laboratuvarda şimdiden %35 verimlilik oranına ulaşmış durumda. Birbirinden çok farklı olan bu iki malzemenin fiziksel olarak nasıl istiflendiğini, bunların güzel bir şekilde çalışabilmesi için hangi arayüz mühendisliğinin gerekli olduğunu ve bu "her iki dünyanın da en iyisi" yaklaşımının neden silikon üreticilerinin gerçekten satın almak isteyeceği ilk perovskit içeren ürünü sunabileceğini inceleyeceğiz.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-21.toml}}
