# 5. Gün: Külçe Dilimleme — Kristalleri Gofretlere Dönüştürme

*Dün, bir Czochralski çektirme makinesinden 300 kilogramlık bir monokristalin silikon külçesinin ortaya çıkmasını izledik; üç gün boyunca büyüyen kusursuz bir kristal, her atom, yarım metre uzunluğunda uzanan elmas kübik bir kafesin içine kilitlenmişti. Muhteşem. Aynı zamanda tamamen işe yaramaz. Bir güneş hücresi yaklaşık 170 mikrometre kalınlığındadır. Bu külçenin çapı 210 milimetre. Bir şekilde, bu muhteşem cam benzeri silindiri parçalamadan, silikonun yarısını toz olarak israf etmeden ve güneş enerjisinin tüm ekonomisini çökertecek kadar para harcamadan 5.000'den fazla jilet inceliğinde dilime dönüştürmemiz gerekiyor. Elmasları diş ipiyle kesme sanatı olan wafering'e hoş geldiniz.*

---

## Üretimde En Pahalı Saç Kesimi

İşte sizi ürkütecek bir rakam: 2015 yılında, gofret dilimleme makinesine giren saflaştırılmış silikonun kabaca %40-50'si toz haline geldi. Gofret değil. Toz. "Çentik" olarak adlandırılan (kesiğin genişliği nedeniyle tahrip olan malzeme) bu, tartışmasız güneş enerjisi endüstrisindeki en pahalı atık üründü. Silikonu altı dokuzluk saflığa çıkarmak için kg başına 20 dolar, onu monokristal haline getirmek için kg başına 10-15 dolar harcadınız ve sonra neredeyse yarısı bulamaç haline geldi ve kanalizasyona aktı.

Matematik yaptığınızda ekonomi acımasızdır. Tipik bir 182 mm × 182 mm M10 levhanın ağırlığı yaklaşık 5,7 gramdır. Polisilikon fiyatı 7-8 ABD doları/kg (tarihsel olarak düşük olan 2024 fiyatları) seviyesinde, her levhadaki silikonun maliyeti kabaca 0,04-0,05 ABD dolarıdır. Ancak çentik nedeniyle %30 kaybediyorsanız, levha başına efektif silikon maliyetiniz daha çok 0,06-0,07 $ civarında olur. Bunu, endüstrinin 2024'te ürettiği 400 milyardan fazla levhayla çarptığınızda, kerf kayıpları yıllık olarak israf edilen ultra saf silikonda 3-4 milyar dolar gibi bir rakama denk geliyor. Bu tek sorun (nasıl daha ince, daha verimli ve daha az atıkla dilimleneceği), güneş enerjisi üretiminde neredeyse tüm diğer adımlardan daha fazla mühendislik yeniliğine yol açmıştır.

Ve endüstrinin üzerinde birleştiği çözüm, ilk bakışta neredeyse saçma görünüyor: ince bir metal tel ve biraz kum kullanarak dünyadaki en sert malzemelerden birini kesmek.

---

## Gofret Kesiminin Kısa Tarihi

Solar'ın dilimleme teknolojisi, diğer pek çok şey gibi, yarı iletken endüstrisinden ödünç alınmıştır. Silikon cihaz imalatının ilk günlerinde (1960'lar-70'ler), levhalar iç çaplı (ID) testereler kullanılarak birer birer kesildi. Elmas kaplı iç kenarı olan bir çörek gibi, deliğin iç tarafında kesici kenarı olan dairesel bir bıçak hayal edin. Silikon külçe merkezden beslenir ve bıçak her geçişte tek bir levhayı keser.

ID testereler hassastı ancak buz gibi yavaştı. Her kesim birkaç dakika sürdü ve bir seferde yalnızca bir gofreti kesebiliyordunuz. Yüksek fiyatlarla (50-200$/wafer) günde birkaç bin levhaya ihtiyaç duyan yarı iletken endüstrisi için bu kabul edilebilir bir durumdu. Günde milyonlarca levhaya ihtiyaç duyan ve levha başına 0,30 ABD Doları'nın altındaki fiyatlarla güneş enerjisi için bu bir başlangıç ​​değildi.

Bu atılım 1990'larda HCT Shaping Systems adlı bir İsviçre şirketinin (daha sonra Applied Materials ve daha sonra Meyer Burger tarafından satın alındı) **çok telli testereyi** ticarileştirmesiyle gerçekleşti. Bu makine, tek bir bıçağın bir levhayı kesmesi yerine, yüzlerce yivli kılavuz silindir boyunca ileri geri sarılarak hepsi aynı anda kesen 5.000'den fazla paralel tel parçasından oluşan bir "ağ" oluşturan tek bir ince tel makarası kullanır. Bu ağa bir külçe beslerseniz tek geçişte 5.000 gofret elde edersiniz.

Geriye dönüp bakıldığında bariz görünen ama uygulanması muazzam mühendislik gerektiren fikirlerden biriydi. Ve bu telin silikonu nasıl kestiğine dair ayrıntılar son on yılda çarpıcı biçimde değişti.

---

## Bulamaçlı Tel Testere: Eski Muhafız

Orijinal çok telli testerelerde düz çelik tel (yüksek karbonlu çelik, yaklaşık 120-160 mikrometre çapında) ve gevşek bir aşındırıcı bulamaç kullanılıyordu. Kesme maddesi telin kendisi değil, bir taşıyıcı sıvı (tipik olarak polietilen glikol veya PEG) içindeki silikon karbür (SiC) parçacıklarının bir süspansiyonuydu. Tel bu bulamacı kesim boyunca sürükledi ve SiC parçacıkları asıl öğütmeyi gerçekleştirdi.

Mekanik olarak hayal edin: Saniyede 10-15 metre hızla hareket eden, her biri yaklaşık 10-15 mikrometre çapında seramik parçacıklarından oluşan bir macun taşıyan bir teliniz var. Bu parçacıklar tel ile silikon arasında yuvarlanıp takla atarak, üç gövdeli aşınma adı verilen bir işlemle kristal yüzeyinden ufalanıyor. Kesmeye daha az, daha çok zımparalamaya benziyor; saniyede milyonlarca küçük darbe, her biri birkaç mikrometre küp silikonu ortadan kaldırıyor.

Bulamaçlı testereyle kesme işe yaradı ancak ciddi dezavantajları vardı:

- **Kalın çentik.** Telin kendisi 120-160 μm idi ve bulamaç parçacıkları her iki tarafta da 20-40 μm'lik etkili kesme genişliği ekledi. Toplam çentik kaybı tipik olarak 170-200 μm idi; bu da neredeyse her levhada tuttuğunuz kadar silikonu yok ettiğiniz anlamına geliyor.
- **Düşük kesme hızı.** İlerleme hızları yaklaşık 0,3-0,6 mm/dak idi. Dolu bir külçeyi dilimlemek 6-8 saat sürdü.
- **Dağınık geri dönüşüm.** Kullanılan bulamaç, PEG, SiC parçacıkları, silikon tozu ve teldeki metal parçacıklarından oluşan zehirli bir karışımdı. Bunları geri dönüşüm veya imha için ayırmak pahalıydı ve çevreye zarar veriyordu.
- **Yüzey hasarı.** Gevşek aşındırıcı parçacıkların rastgele yuvarlanma hareketi, levhanın her iki tarafında yaklaşık 10-15 μm derinliğinde kaba, hasarlı bir yüzey katmanı ("testere hasar bölgesi") oluşturdu. Bunun daha sonra kazınması gerekiyordu, bu da daha fazla silikon israfına neden oluyordu.

Bu sorunlara rağmen, sulu tel testereyle kesme 1990'ların sonlarından 2015'e kadar hakim oldu. Daha sonra sektör bir sıçrama yaptı.

---

## Elmas Tel: Devrim

Fikir baştan çıkarıcı derecede basit: gevşek aşındırıcıyı kesim boyunca sürüklemek yerine neden aşındırıcıyı doğrudan tele bağlamayasınız? Küçük elmas parçacıklarını, nikel elektrokaplama veya reçine bağlama kullanarak çelik çekirdekli tel üzerine sabitleyin; kendi dişlerini taşıyan bir kesme aletiniz var.

Elmas tel testere (DWS) yıllardır safir ve silisyum karbür gibi sert malzemeleri kesmek için kullanılıyordu, ancak bunu kitlesel pazardaki güneş enerjisi levhalarına uyarlamak, birçok sorunun aynı anda çözülmesini gerektiriyordu. Telin ince (kertiği en aza indirmek için), dayanıklı (binlerce levhayı kesmeye dayanacak kadar) ve ucuz (çünkü güneş marjları çok ince) olması gerekiyordu. Güneş enerjisi ölçeğindeki buluş öncelikle 2000'li yıllarda elektrolizle kaplanmış elmas teller geliştiren Japonya'nın **Asahi Diamond Industrial**'ına ve daha sonra maliyetleri büyük ölçekte düşüren **Yangtze Optical Fiber and Cable (YOFC)** ve **Qingdao Gaoce Technology** gibi Çinli üreticilere verildi.

İşte elmas teli dönüştürücü kılan şey:

**Daha ince tel, daha ince çentik.** Modern elmas teller, yüzeye bağlı 6-12 μm'lik elmas parçacıklarıyla birlikte 38-46 μm'lik (2018'de 60-70 μm'den 2024 itibarıyla) çelik çekirdek kullanır. Toplam tel çapı kabaca 52-65 μm'dir; bu da insan saçından daha azdır. Kerf kaybı 170-200 μm'den (bulamaç dönemi) 55-70 μm'ye düştü. Bu, kesim başına silikon israfında %65'lik bir azalma anlamına gelir.

**Daha hızlı kesim.** Elmas parçacıkları sabit olduğundan iki gövdeli aşınma yoluyla kesilir; yuvarlanma yerine doğrudan çizilme. Tel hızları 20-30 m/s'ye çıktı ve ilerleme hızları 1,5-3,0 mm/dak'ya yükseldi; bu da çamurdan yaklaşık 5 kat daha hızlıydı. Dolu bir külçe artık 6-8 saat yerine 1,5-2,5 saat sürüyor.

**Temizleyici işlem.** DWS için kesme sıvısı, az miktarda yüzey aktif madde içeren sadece sudur (yüzey gerilimini azaltmak ve silikon kalıntılarını temizlemek için). PEG yok, SiC yok, kabus gibi geri dönüşüm yok. Çevre ve maliyet açısından faydaları çok büyüktür.

**Daha iyi yüzey kalitesi.** Sabit aşındırıcılar, daha sığ hasarla (5-8 μm ve 10-15 μm) daha düzgün bir yüzey oluşturur. Bu, levha işleme sırasında daha az malzemenin kazınması gerektiği anlamına gelir.

Bulamaçtan elmas tele geçiş şaşırtıcı derecede hızlıydı. 2015 yılında monokristalin levhaların %10'undan azı elmas telle kesildi. 2018 yılında bu oran yüzde 90'ın üzerindeydi. 2020 yılına gelindiğinde, monokristalin için bulamaçla kesme esasen sona ermişti.

Mantık dışı ayrıntı şu şekildedir: **elmas tel başlangıçta çok kristalli silikonu iyi kesemiyordu.** Çok kristalli külçelerdeki rastgele tanecik yönelimleri, elmas parçacıkları üzerinde eşit olmayan bir aşınma yaratarak telin kırılmasına ve pürüzlü yüzeylere neden oldu. Bu aslında endüstrinin monokristal levhalara geçişini hızlandıran faktörlerden biriydi; yalnızca mono hücreler daha verimli olmakla kalmadı, aynı zamanda yeni elmas tel teknolojisiyle mono külçelerin *dilimlenmesi* daha kolay oldu. Bir yeniliğin diğerine kademeli bir avantaj yaratmasının klasik bir örneği.

---

## Modern Tel Testerenin İçinde

**Gaoce Technology** (2024 itibarıyla küresel tel testere pazarının ~%70'ine sahip olacak lider Çinli ekipman üreticisi), **Meyer Burger** (İsviçre hassas mühendisliği) veya **Komatsu NTC** (Japon mirası) tarafından üretilen son teknoloji ürünü elmas tel testere makinesini inceleyelim.

### Tel Ağ

Tipik olarak 150-300 km uzunluğundaki tek bir elmas tel makarası, iki büyük makara arasına sarılır ve iki veya dört yivli kılavuz silindirin ("tel kılavuzları" veya "tel makaraları" olarak adlandırılır) üzerinden geçer. Bu poliüretan kaplı çelik silindirlerdeki oluklar, levha kalınlığı artı çentiği belirleyen 200-300 μm'lik bir aralıkta hassas bir şekilde işlenmiştir. 60 μm çentikli standart 150 μm levha için oluk aralığı yaklaşık 210 μm olacaktır.

Tel, makara makaraları arasında ileri geri hareket ederken ("hac modu" adı verilen ileri geri hareketle), paralel tel parçalarından oluşan yatay bir düzlem - "tel ağı" oluşturur. Modern bir makine, bu ağda hepsi aynı anda kesen 5.000-8.000 tel parçasına sahip olabilir.

### Kesim

Silikon külçe - genellikle "tuğla" adı verilen kare şeklinde bir blok (birazdan kare alma adımına geçeceğiz) - kendisi de tel örgünün üzerindeki motorlu bir besleme masasına kelepçelenen bir cam veya reçine kiriş üzerine yapıştırıcıyla monte edilir. Besleme tablası, tel 20-30 m/s hızla ileri geri hareket ederken tuğlayı yavaşça ağ içine indirir.

Soğutma sıvısı — %1-3 yüzey aktif madde içeren deiyonize su — silikon kalıntılarını uzaklaştırmak, teli soğutmak ve kesiği yağlamak için kesme bölgesini yüksek akış hızlarında (dakikada 50-100 litre) doldurur. Su, filtrelenen, temizlenen ve yeniden sirküle edilen silikon mikro parçacıklarının süt grisi süspansiyonu olarak çıkar.

Kesme basıncı, tel gerilimi, tel hızı ve ilerleme hızı bilgisayar kontrollüdür ve kesim sırasında sürekli olarak ayarlanır. Çok fazla besleme basıncı ve tel eğrileri kalınlık değişimi yaratıyor (TTV — Toplam Kalınlık Değişimi olarak adlandırılıyor). Çok az ve zaman harcıyorsun. Optimum denge, 182 mm'lik genişliğin tamamında 15 μm'nin altında TTV olan levhalar üretir; bu, %0,008'den daha iyi bir düzlük toleransıdır.

### Sayılar

Modern, yüksek verimli bir tel testere yaklaşık olarak şunları kesebilir:
- **kesim başına 5.000-8.000 gofret** (tuğla uzunluğuna ve gofret kalınlığına bağlı olarak)
- **Günde 6-8 kesim** (yükleme, kesme ve boşaltma dahil)
- **makine başına günde 30.000-60.000 gofret**

**LONGi Green Energy**, **TCL Zhonghuan (TZS)** veya **GCL Technology** tarafından işletilen büyük bir levha fabrikası, aynı anda çalışan 500-1.000 tel testereye sahip olacak ve günde 20-50 milyon levha üretecektir. LONGi tek başına 2024 sonu itibarıyla 130 GW'ün üzerinde levha levha kapasitesine sahipti; bu da günde yaklaşık 15-20 milyon levhaya karşılık geliyor.

---

## Testereden Önce: Külçeyi Kare Alma

Bir Czochralski külçesi silindiriktir. Güneş pilleri karedir (veya daha kesin olarak sözde kare - köşeleri yuvarlatılmış kare). Bu uyumsuzluk, yuvarlak külçeyi levha haline getirmeden önce kare bir kesite kesmemiz gerektiği anlamına gelir.

**Kareleme** veya **tuğlalama** olarak adlandırılan bu işlem, elmas şerit testereler veya elmas tel kesme makineleriyle yapılır. Tipik olarak 210 mm veya 300 mm çapındaki silindirik külçe ilk önce uzunluğa kesilir (konik kuyruk ve Dash boynu kırpılır). Daha sonra uzunlamasına bir kare veya sözde kare kesit halinde kesilir.

Baskın M10 plaka formatı (182 mm × 182 mm) için külçenin karesi 182 mm'ye alınır, bu da 210 mm çaplı bir silindirden dört kavisli parçanın çıkarılması anlamına gelir. Kareleme sırasında çıkarılan silikon (külçe kütlesinin yaklaşık %15-18'i) hammadde olarak CZ fırınına geri dönüştürülür. Zaten yüksek saflıkta monokristalin silikon olduğundan hemen geri erir. Burada hiçbir şey gerçekten israf edilmez (tel parçaları ve soğutucuyla kolayca geri dönüştürülemeyecek kadar kirlenmiş olan çentikten farklı olarak elektronik sınıf malzemeye geri dönüştürülür).

Daha büyük levha formatlarına doğru aktif bir eğilim var. Sektör yalnızca beş yıl içinde (2019-2024) M2'den (156,75 mm) G1'e (158,75 mm), M6'ya (166 mm), M10'a (182 mm) ve G12'ye (210 mm) geçti. Daha büyük plakalar, hücre başına daha fazla güç, modül başına daha az hücre ve watt başına daha düşük üretim maliyeti anlamına gelir. Ancak daha büyük levhalar aynı zamanda daha büyük külçeler gerektirir (G12 için 300+ mm çap), bu da CZ kristal büyütme ekipmanını zorlar. G12 formatı, yarı iletken endüstrisinin standart 300 mm levhasıyla eşleşen ilk güneş levhası boyutudur; bu, ekipman teknolojisinde bazı ilginç çapraz tozlaşmaya yol açan bir tesadüftür.

---

## Kerf Kaybı Sorunu: Her Mikrometre İçin Mücadele

Gofretin kutsal kasesi, daha ince gofretleri daha ince çentikle kesmek ve her kilogram silikondan daha fazla gofret çıkarmaktır. Son on yılda kaydedilen ilerleme dikkat çekicidir:

| Yıl | Tel çapı (çekirdek) | Kerf kaybı | Gofret kalınlığı | kg başına gofret Si |
|----------|----------|-----------|----------------||-----------------|
| 2010 | 120 μm (bulamaç) | 180 mikron | 200 mikron | ~55 |
| 2015 | 70 μm (elmas) | 100 mikron | 180 mikron | ~62 |
| 2020 | 50 μm (elmas) | 75 mikron | 165 mikron | ~72 |
| 2024 | 38-42 μm (elmas) | 55-65 mikron | 130-150 mikron | ~80-95 |

Şu son sıra dikkat çekici. Her iki tarafında 7 μm elmas bulunan 38 μm'lik bir çekirdek tel, yaklaşık 52 μm'lik bir toplam tel çapı verir ve kabaca 55 μm'lik bir çentik üretir. 130 μm levhalarla (bazı önde gelen üreticilerin halihazırda kullandığı) birleştirildiğinde, kilogram silikon başına yaklaşık 95 levha elde edersiniz; bu sayı yalnızca on dört yıl önce 55'ti. Bu, silikon kullanımında %73'lük bir iyileşme anlamına geliyor.

Ancak yaklaşan fiziksel bir sınır var. Telin, düz kesimler için gereken gerilimi (tipik olarak 15-25 N) sürdürecek kadar güçlü olması gerekir ve çelik telin mukavemeti, yaklaşık 35 μm çapın altında olumlu bir şekilde ölçeklenmez. Bu eşiğin altında tel kopma oranları katlanarak artıyor. 2 saatlik bir kesim sırasında meydana gelen tek bir tel kopması binlerce levhayı aynı anda mahvedebilir; tel kopabilir, gevşeyebilir ve levha ağı çökerek kırık silikon ve çelikten oluşan karışık bir karmaşaya dönüşebilir. Tel kırılması, levha mühendisinin kabusudur. 2023 yılında Çin'in büyük bir levha fabrikasında, yalnızca tel kopmalarından kaynaklanan verim kaybının toplam üretimin %2-3'ü kadar olduğu tahmin ediliyordu; bu da yılda on milyonlarca dolar demekti.

Bazı üreticiler, aynı çapta karbon çeliğinin yaklaşık 2 katı çekme mukavemetine sahip olan **tungsten teli** çekirdek malzemesi olarak araştırıyor. Japonya'nın **Panasonic** ve **Sumitomo**, 45 μm'nin altında çentiği mümkün kılan, 30 μm kadar ince tungsten özlü elmas teller geliştirdi. Ancak tungsten telin maliyeti çelik telden kabaca 3-5 kat daha fazladır, dolayısıyla ekonomi yalnızca silikon tasarrufları tel priminden daha ağır basarsa işe yarar.

---

## Gofret Kalınlığı: Ne Kadar İnceye Gidebiliriz?

İşte güneş enerjisi mühendislerini geceleri uykusuz bırakan bir soru: Bir silikon levha ne kadar ince olabilir ve hala iyi bir güneş hücresi olarak işlev görebilir?

Fizik cevabı şaşırtıcı derecede zayıf. Silikon, gelen güneş ışığının çoğunu ilk 10-20 μm içinde (görünür dalga boyları için) emer. İyi ışık yakalama özelliğine sahip 50 μm kalınlığındaki bir hücre, teorik olarak faydalı fotonların %95'inden fazlasını yakalayabilir. Ve daha ince hücrelerin aslında bazı avantajları var: Taşıyıcı toplama için daha kısa mesafeler (düşük kaliteli silikon için önemli) ve daha az toplu rekombinasyon.

Mühendisliğin cevabı çok daha az cömerttir. Yalnızca 100 μm kalınlığındaki 182 mm × 182 mm'lik bir silikon levha, camdan yapılmış bir patates cipsi gibi olağanüstü derecede kırılgandır. Esniyor, eğiliyor, sertçe baktığınızda çatlıyor. Geri kalan 20'den fazla işlem adımını (temizleme, dokulandırma, difüzyon, metalleştirme, lehimleme) kırılmadan tamamlamak bir üretim kabusudur.

Mevcut üretim standart kalınlığı on yıl önce 200 μm iken 130-150 μm'dir. 2028 yılı için sektör hedefi 100-120 μm. 100 μm'nin altında, geleneksel taşıma ekipmanlarının plakaları çatlatmadan kavrayamadığı bir rejime girersiniz ve yeni yaklaşımlar (havayla yüzdürme işlemi, mekanik destek için daha kalın metalizasyon, yarı hücreli veya kiremitli modül mimarileri) gerekli hale gelir.

Şaşırtıcı gerçek şu: **silikon levha artık bir güneş modülünde baskın maliyet değil.** 2024'te, ~7$/kg polisilikon fiyatında, standart bir levhanın silikon içeriğinin maliyeti yaklaşık 0,04 ABD dolarıdır. Kesmek için kullanılan elmas telin maliyeti levha başına yaklaşık 0,02-0,03 dolar. Gofret satış fiyatı ise 0,15-0,20 dolar civarında. Buna karşılık, metalizasyon için kullanılan gümüş macunun (8. Gün) hücre başına maliyeti 0,10-0,15 ABD dolarıdır ve modülün camı, arka sayfası ve çerçevesi tüm hücrelerin toplamından daha pahalıdır. Plakanın inceltilmesi silikondan daha fazla tasarruf sağlar, evet - ancak silikon ucuz olduğunda getiriler azalıyor. İnce plakalara yönelik gerçek motivasyon, malzeme maliyet tasarrufundan **performansa** kaymıştır: daha ince hücreler, azaltılmış toplu rekombinasyondan yararlanan heteroeklem (HJT) gibi gelişmiş mimarilerle daha iyi çalışır.

---

## Gofretin Testereden Çıkışı

Taze kesilmiş bir gofret neye benziyor? Çatıda gördüğünüz parlak mavi karelere pek benzemiyor.

Tel testere kesmeyi tamamladığında ve tuğla tel ağdan kalktığında, tarak benzeri bir yapıya sahip olursunuz: saç inceliğinde boşluklarla ayrılmış, üst kenarlarından montaj kirişine hala yapıştırılmış binlerce levha. Robotik bir kol, bu tarağı bir **tutkal giderme istasyonuna** aktarır; burada sıcak su veya hafif bir solvent yapıştırıcıyı çözer ve tek tek levhalar suya batırılmış bir taşıyıcı kasete aktarılır (birbirlerine çarparak ufalanmalarını önlemek için).

Her levha, silikon tozu ve mikroskobik tel izleriyle kaplı, gri ve opak (mat gümüş rengi) ortaya çıkıyor. Yüzey, telin hareketinden kaynaklanan ve tel yönüne dik uzanan ince paralel oluklardan oluşan karakteristik bir desene sahiptir. Mikroskop altında testerenin hasar bölgesini görürsünüz: elmas parçacıklarının kristal kafesi parçaladığı 5-8 μm derinliğinde çatlak, amorfize silikon tabakası. Bu hasarlı katman elektriksel olarak ölüdür (rekombinasyon aktif kusurlarla doludur) ve levhanın bir güneş hücresi olabilmesi için tamamen ortadan kaldırılması gerekir.

Plakalar ultrasonik olarak temizlenir, deiyonize suyla durulanır, kalınlığa göre ayrılır (hat içi lazer ölçümü kullanılarak) ve çatlak, talaş ve kirlenme açısından incelenir. Bu aşamadaki reddetme oranları genellikle %1-3'tür; çoğunlukla kenar talaşlarından ve kalınlık aykırılıklarından kaynaklanmaktadır. Hayatta kalan ince tabakalar 100-200'lük kasetlere paketleniyor ve bazen bir fabrika katından, bazen de okyanustan geçerek hücre üretim hattına gönderiliyor.

Ve asıl sihir orada başlıyor. Çünkü yarın, bu tertemiz kristal levhaları alıp onlara mantık dışı bir şey yapacağız: onları kasten kirleteceğiz. **Doping** adı verilen bir süreç olan, hassas bir şekilde kontrol edilen safsızlıkları ekleyerek, bir güneş hücresinin gerçekten çalışmasını sağlayan elektrik alanını yaratacağız. Bu, düz bir silikon parçası ile ışığı elektriğe dönüştüren bir cihaz arasındaki farktır. Ve her şey birkaç fosfor atomuyla başlıyor.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-05.toml}}
