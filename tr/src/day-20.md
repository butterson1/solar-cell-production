# 20. Gün: Modül Güvenilirliği — IEC Testleri ve Yaşlanma

*Güneş panelinizin 25 yıl boyunca UV bombardımanına, dolu fırtınasına, neme ve voltaj stresine dayanması gerekir. İşte sektörün bunu nasıl sağladığı ve bazen nasıl başarısız olduğu.*

---

İşte sizi tedirgin edecek bir rakam: Hizmet ölçeğindeki tipik bir güneş enerjisi çiftliği 500.000 ila 2 milyon modül dağıtır. Watt başına 0,20-0,30 dolarlık bir maliyetle, bu cam ve silikonlu sandviçlerin her birinin çeyrek yüzyıl boyunca elektrik üretmeye devam edeceğine dair 50-150 milyon dolarlık bir bahis var. Modüllerin %2'si bile vaktinden önce arızalanırsa, milyonlarca dolarlık değiştirme maliyetiyle, gelir kaybıyla ve çok mutsuz yatırımcılarla karşı karşıya kalırsınız.

Peki bir modülü Arizona çölündeki bir raf sistemine veya Hamburg'daki bir çatıya vidalamadan *önce* onun katmanlarına ayrılmayacağını, paslanmayacağını, çatlamayacağını veya üçüncü yıl içinde çalışmayı bırakmayacağını nasıl bilebilirsiniz? Ona işkence ediyorsun. Sistematik, metodik ve kırk yılı aşkın zorlu saha deneyimiyle gelişen bir dizi uluslararası standartlara göre. IEC test ve bozulma bilimi dünyasına hoş geldiniz; bu, 25 yıllık bir varlığı 25 yıllık bir yükümlülükten ayıran gösterişsiz disiplindir.

## IEC Çerçevesi: Garanti Değil, Minimum Gereksinimler

Güneş modülü güvenilirliğine ilişkin temel standartlar **IEC 61215** (tasarım yeterliliği ve tip onayı) ve **IEC 61730** (güvenlik yeterliliği)'dir. Bir modül veri sayfasına bakıp "IEC 61215 sertifikalı" ifadesini gördüyseniz, bunun modülün uzun süre dayanacak şekilde üretildiği anlamına geldiğini varsayabilirsiniz. Gerçek daha nüanslıdır ve bu nüansın anlaşılması kritik öneme sahiptir.

IEC 61215 ilk olarak 1993'te yayınlandı, 2005 ve 2016'daki büyük revizyonlarla geliştirildi ve yeni hücre teknolojilerine (TOPCon, HJT, tandem hücreler) yönelik değişikliklerle sürekli olarak güncellendi. Standart, tasarım zayıflıklarını ortaya çıkarmak için tasarlanmış bir dizi hızlandırılmış stres testini tanımlar. Bu açıkça ömür boyu sürecek bir tahmin *değildir*. IEC Teknik Komite'nin kendi belgeleri, IEC 61215'i geçmenin bir modülün minimum düzeyde strese dayanabileceğini gösterdiğini ancak 25 yıllık saha performansı hakkında herhangi bir iddiada bulunmadığını belirtir.

Bunu bir sürüş testi gibi düşünün: geçmek, temel konuları halledebileceğinizi kanıtlar, ancak yedinci yılda kaza yapıp yapmayacağınızı öngörmez. Yine de, *başarısız* olan bir modül IEC 61215 neredeyse kesinlikle saha arızalarına neden olacak tasarım sorunlarına sahiptir. Standart tavanı değil tabanı belirler.

Bu arada IEC 61730 güvenliğe (elektrik yalıtımı, yangına dayanıklılık ve mekanik bütünlük) odaklanıyor. 61215 "bu modül hala güç üretecek mi?" diye sorarken, 61730 "bu modül birini öldürecek mi?" Büyük pazarlarda (AB, ABD, Avustralya, Japonya) satılan tüm modüller için her iki sertifika da gereklidir.

## İşkence Odası: Her Test Aslında Ne Yapar?

IEC 61215'teki başlıca testleri gözden geçirelim. Her biri, gerçek dünyadaki kurulumlarda gözlemlenen belirli bir hata mekanizmasını hedefler. Başarılı/başarısız kriteri neredeyse her zaman aynıdır: güç kaybı ilk ölçüme göre %5'i geçmemelidir ve önemli görsel kusurlar (çatlak cam, katmanlara ayrılma, açıkta kalan canlı parçalar) olmamalıdır.

### Termal Döngü (TC200 ve TC600)

Modüller bir çevre odasına yerleştirilir ve **−40°C ile +85°C** arasında, saatte yaklaşık 100°C'lik bir artış hızıyla ve her uç noktada en az 10 dakikalık bekleme süresiyle döngüye alınır. Standart test 200 döngüdür (TC200), ancak 600 döngüde (TC600) genişletilmiş testler, farklılaşma arayışında olan 1. kademe üreticiler arasında yaygın hale geldi.

Neden bu sıcaklıklar? Çünkü bir modülün sahada karşılaşabileceği aşırılıkları parantez içine alıyorlar. Phoenix'te bir çatı katı yaz öğleden sonra 75-80°C'ye ulaşabilir. Minnesota'daki bir zemin montajı Ocak ayında -35°C'yi görüyor. Termal döngü yalnızca silikonu test etmez; her arayüzü test eder. Silikon °C başına yaklaşık 2,6 × 10⁻⁶, cam yaklaşık 9 × 10⁻⁶, alüminyum çerçeveler 23 × 10⁻⁶ ve bakır şerit 17 × 10⁻⁶ genişler. 125°C'lik bir salınım üzerinde bu uyumsuz genleşme oranları, her bağlantı noktasında, lehim bağlantısında ve yapışkan katmanda kayma gerilimi oluşturur.

Tek bir termal döngü hiçbir şeyi bozmaz. Ancak 200 döngü (yaklaşık iki yıllık agresif dış mekan termal stresine eşdeğer) hücrelerde mikro çatlakların oluşmasına, hücre ara bağlantıları arasındaki lehim bağlantılarının yorulmasına ve EVA veya POE kapsülleyicinin camdan ayrılmasına neden olacaktır. Modül iyi tasarlanmışsa TC200 sonrasındaki güç kaybı %2–3'ün altında kalır. Kötü tasarlanmış modüller, özellikle kalaylı veya kurşunsuz lehimin yorulduğu ve çatladığı lehim bağlantılarında %5-8 oranında kayıp yaşayabilir.

### Nemli Isı (DH1000 ve DH2000)

Bu belki de standarttaki en cezalandırıcı testtir. Modüller **85°C ve %85 bağıl nemdeki bir odada 1.000 saat boyunca** kalır; bu da yaklaşık 42 günlük tropik cehennem anlamına gelir. PVEL (eski adıyla PV Evolution Labs, artık Kiwa'nın bir parçası), Ürün Yeterlilik Programında DH2000 (2.000 saat) ve hatta DH3000 modülleri çalıştırarak bunu daha da ileri götürdü.

85/85 koşulları acımasızdır çünkü nem girişini hızlandırırlar. Su buharı arka tabakadan, kenar contalarından ve bağlantı kutusu yapıştırıcısı boyunca nüfuz eder. İçeri girdikten sonra nem her şeye saldırır: hücre yüzeyindeki gümüş şebeke çizgilerini aşındırır, yansıma önleyici kaplamayı bozar, EVA kapsülleyiciyi hidrolize eder (korozyonu daha da hızlandıran asetik asit açığa çıkarır) ve metal iyonlarının yalıtım boşlukları boyunca elektrokimyasal göçüne neden olabilir.

Şaşırtıcı gerçek şu: **DH1000 değerini geçen ancak DH2000 değerinde başarısız olan bir modül, Madrid veya Denver gibi kuru ve ılıman bir iklimde hala 25 yıl dayanabilir — ancak Chennai veya Singapur gibi nemli tropik bir ortamda 10-15 yıl içinde neredeyse kesin olarak arızalanır.** IEC minimum 1.000 saat, orta düzeyde nemde kabaca 10 yıla karşılık gelir, ancak yıl boyunca yüksek neme sahip bir bölgede 5 yıldan daha az bir süreye karşılık gelir. ve sıcaklıklar. PVEL'nin genişletilmiş DH2000 testinin güvenilir modüller için fiili sektör standardı haline gelmesinin ve tropikal kurulumlara yönelik modüllerin giderek daha fazla DH3000 testine tabi tutulmasının nedeni budur.

### Nem Donması (HF10)

On döngü yüksek nem (85°C'de %85 RH) ve ardından -40°C'ye hızlı soğutma. Fikir şeytani derecede basit: Modül sıcakken nemi modülün derinliklerine sürün, sonra dondurun. Su donduğunda yaklaşık %9 oranında genleşir ve bir katman katmanları arasında veya bir mikro çatlak boyunca sıkışıp kalırsa, katmanları birbirinden ayıran küçük bir hidrolik kriko gibi davranır. On döngü minimumdur; zayıf kenar sızdırmazlığını ve yetersiz kapsülleyici yapışmayı ortaya çıkarmada şaşırtıcı derecede etkilidir.

### Mekanik Yük (ML)

Modüller eşit basınç yüklerine tabi tutulur — **ön tarafta 2.400 Pa** (kar yükünü simüle eder, yaklaşık 245 kg/m²'ye veya kabaca metrekare başına 50 pound'a eşdeğerdir) ve **arka tarafta 5.400 Pa** (rüzgar emişini simüle eder). Bağlam açısından, 5.400 Pa, modül yüzeyinin her 3 metrekaresine kompakt bir araba park etmek gibidir.

Bu test, çerçeve mukavemeti, camdan çerçeveye yapışma ve sapmadan kaynaklanan hücre çatlaması ile ilgili sorunları tespit eder. 182 mm veya 210 mm hücreli modern modüller burada özellikle savunmasızdır çünkü daha büyük hücreler eğilmenin neden olduğu mikro çatlaklara daha yatkındır. Bazı üreticiler artık yükleri taşımak için çelikle güçlendirilmiş çerçeveler veya daha kalın cam (2,0 mm yerine 3,2 mm) kullanıyor ve bu da modül başına 2-3 kg ekstra ağırlık maliyeti anlamına geliyor.

### Dolu Etkisi

Yaklaşık 7,5 gram ağırlığında, 25 mm çapında (kabaca büyük bir mermer büyüklüğünde) bir buz topu, modül üzerinde belirlenmiş 11 çarpma noktasında 23 m/s (yaklaşık 83 km/saat) hızla ateşlenir. Dolu direncini artırmak için, bazı laboratuvarlar 27,2 m/s hızında 35 mm buz toplarıyla test yapıyor ve ABD'de yakın zamanda tanıtılan UL 61730-2 eki, Teksas ve ABD Ortabatı'da artan dolu fırtınalarına yanıt olarak 30+ m/s hızında 50 mm doluya kadar testleri içeriyor.

Dolu hasarının fiziği öğreticidir. Temperli cam dolu nedeniyle nadiren kırılır; darbelere karşı dayanıklı olacak şekilde tasarlanmıştır. Ancak şok dalgası camdan, kapsülden geçerek hücrelere yayılır ve burada gözle görülmeyen ancak uzun vadeli performansı olumsuz yönde etkileyen yıldız şeklinde çatlak desenleri oluşturabilir. Dolu sonrası EL görüntüleme (19. Gün), bu hasarı tespit etmenin tek güvenilir yoludur.

### UV Ön koşullandırma

Modüller minimum **15 kWh/m² UV radyasyon** (dalga boyları 280–400 nm) alır; bu, birkaç ay boyunca açık havada kalmaya eşdeğerdir. Bu, hücrelerde ışık kaynaklı bozunmayı (LID) ve kapsülleyici ve arka tabaka polimerlerinin UV bozunmasını tetikler. Bu, kasıtlı olarak diğer testlerden *önce* yapılır, çünkü UV-bozunmuş malzemeler daha sonraki termal ve nem streslerine karşı daha savunmasızdır.

## IEC Ötesi: Mühendisleri Uyanık Tutan Bozunma Mekanizmaları

IEC 61215'i geçmek, modülünüzün temel seviyedeki hızlandırılmış strese dayanabileceğini kanıtlar. Ancak gerçek dünya, yıkım konusunda çok daha yaratıcıdır. Burada, çoğu saha arızasına neden olan bozulma mekanizmaları yer almaktadır; bunlardan birçoğuna IEC testi zar zor dokunmaktadır.

### Potansiyel Kaynaklı Bozulma (PID)

Seri olarak bağlanan bir dizi güneş modülünde sistem voltajı, toprağa göre 1.000V'a, hatta 1.500V'a ulaşabilir. Topraklanmış bir sistemde, dizinin negatif ucundaki modüller, hücreleri ile topraklanmış alüminyum çerçeve arasında büyük bir negatif gerilime maruz kalır. Bu voltaj, sodyum iyonlarını camdan kapsülleyici aracılığıyla hücrenin yansıma önleyici kaplamasına ve p-n bağlantısına yönlendirerek modül gücünü yalnızca birkaç yıl içinde **%30-80** oranında azaltabilecek şönt yollar oluşturur.

PID, IEC 62804 kapsamında test edilir (ve artık PVEL'nin puan kartına entegre edilmiştir), genellikle 96 saat boyunca 85°C'de ve %85 RH'de modüle −1.000V veya −1.500V uygulanarak test edilir. Düzeltme, PID-dirençli kapsüllerin (EVA yerine POE, çünkü POE çok daha düşük su buharı iletimine sahip olduğundan), azaltılmış sodyum içeriğine sahip PID-dirençli camın veya şantları "iyileştirmek" için geceleri voltajı tersine çeviren bir cihazın takılması gibi sistem düzeyinde çözümlerin kullanılmasını içerir.

Mantık dışı gelişme şu: **PID kısmen tersine çevrilebilir.** Etkilenen modüllerin bağlantısını keser ve onları güneşte bırakırsanız, sodyum iyonları yavaş yavaş hücrenin dışına geri döner ve güç, bazen %50-70 oranında geri kazanılır. Bazı büyük kamu tesisleri artık geceleri kabloya pozitif voltaj uygulayan ve hasarı aktif olarak tersine çeviren PID kurtarma kutuları kuruyor.

### Işık Kaynaklı Bozulma (LID) ve LeTID

LID konusuna 6. Günde değinmiştik: bor katkılı p-tipi silikon ilk kez ışığa maruz bırakıldığında, rekombinasyon merkezleri görevi gören bor-oksijen kompleksleri oluşur ve çalışmanın ilk birkaç saatinde verimliliği **%1-3** oranında azaltır. Bu başlangıç ​​LID iyi anlaşılmıştır ve büyük ölçüde "fiyatlandırılmıştır"; üreticiler modüllerini ışıkla ıslatıldıktan sonra ölçer ve stabilize gücü bildirirler.

Ancak 2012 civarında daha sinsi bir varyant ortaya çıktı: **Işık ve Yüksek Sıcaklık Kaynaklı Bozulma (LeTID)**. Bu mekanizma öncelikle PERC hücrelerini etkiler ve yalnızca ışığa maruz kalma ve 50°C'nin üzerindeki sıcaklıkların (herhangi bir güneşli iklimde doğal olarak oluşan koşullar) birleşimi altında etkinleşen hidrojenle ilgili kusurları içerir. LeTID, saha çalışmasının ilk 2-3 yılı boyunca ek **%2-6 güç kaybına** neden olabilir ve ciddi durumlarda bu oran %10'a kadar çıkabilir.

LeTID'i sinsi yapan şey zaman ölçeğidir. Klasik LID saatler içinde gerçekleşirken LeTID aylar ve yıllar içinde gelişerek 60°C'nin üzerindeki hücre sıcaklıklarında yaklaşık 1.000-3.000 saatlik çalışma süresine ulaşır. Daha sonra *yavaş yavaş iyileşir*, ancak tam iyileşme sahada 5-10 yıl sürebilir. Mekanizma, silikon kütlesindeki kusurlu kompleksleri oluşturan ve çözen hareketli hidrojen atomlarını içeriyor; bu, sıcaklığa bağlı ve altta yatan fiziği değiştirmeden laboratuvarda hızlandırılması çıldırtıcı derecede zor bir süreç.

PVEL artık LID+LeTID kombinasyonunu test ediyor ve puan kartı sonuçları üreticiler arasında önemli farklılıklar gösteriyor. Bazıları azaltma stratejileri uyguladı: üretim sırasında hücreleri yüksek sıcaklıkta yoğun ışıkla ön koşullandırma (temel olarak fabrikadaki LeTID aşamasını "yakma") veya bor-oksijen LID mekanizmasının uygulanmadığı galyum katkılı plakalara geçiş.

### Arka Sayfada Çatlama ve Sararma

Modülün arkasındaki beyaz veya siyah polimer tabaka olan arka tabaka, modülün nem girişine karşı ilk savunma hattıdır. Arka tabakaların çoğu çok katmanlı laminatlardır: bir dış floropolimer katman (Tedlar, Kynar veya PVDF), yapısal dayanıklılık için bir PET (polyester) çekirdek ve kapsülleyiciye bağlanan bir iç katman.

NREL ve IEA-PVPS Görev 13'ten alınan saha verileri, **arka sayfayla ilgili arızaların, saha kusurları arasında en hızlı büyüyen kategori olduğunu** göstermektedir. En yaygın arıza modu, belirli poliamid (PA) ve PET-bazlı arka tabakaların iç katman çatlamasıdır; bu, bazı üreticilerin pahalı üç katmanlı Tedlar/PET/Tedlar'dan (TPT) daha ucuz alternatiflere geçiş yaptığı yaklaşık 2010 ile 2016 yılları arasında üretilen modüllerde ortaya çıktı. Çatlak arka tabakalar nem girişine izin verir, korozyonu hızlandırır ve elektriksel güvenlik tehlikeleri (topraklama hatası riski) oluşturur.

EVA kapsülleyicinin sararması başka bir yavaş yanma sorunudur. UV radyasyonu EVA'deki polimer zincirlerini kırar, asetik asit açığa çıkarır (eski bir modülü açtığınızda oluşan sirke kokusu) ve mavi ışığı emen sararmaya neden olur. Aşırı derecede sararmış bir kapsülleyici, silikonun en verimli şekilde emdiği kısa dalga boyundaki fotonları filtreleyerek modüle **mevcut nesilde** %2-5** maliyet getirebilir.

### Salyangoz Yolları

Hücre yüzeyinde gizemli kahverengimsi dalgalı çizgilere (gerçek salyangozların bıraktığı izlere benzer) sahip bir güneş modülü gördüyseniz, fotovoltaiklerdeki görsel açıdan en belirgin kusurlardan birini görmüşsünüzdür. Salyangoz izlerine salyangozlar neden olmaz. Bunlara **hücredeki nem ve asetik asidin (EVA ayrışmasından) gümüş metalizasyonuna ulaşmasını sağlayan mikro çatlaklar neden olur ve gümüş macunla reaksiyona girerek gümüş asetat ve gümüş karbonat (her ikisi de kahverengi renkli bileşikler) oluşturur.

Salyangoz izleri aslında altta yatan mikro çatlaklar için görünür bir işarettir ve bunların varlığı, güç çıkışının azalmasıyla ilişkilidir. Çatlaklar üretim sırasında, taşıma sırasında (bir paletin üzerinden kayan bir modül) veya sahadaki termal döngüden kaynaklanmış olabilir. 5-7 yıl sonra kapsamlı salyangoz izlerine sahip bir modül, öncelikle aşınmış parmaklar nedeniyle artan seri dirençten dolayı tipik olarak %5-10 güç kaybı gösterir.

## Gerçek Dünyanın Bozulması: Sayılar

Peki tüm bu testlerden ve tüm bu arıza modlarından sonra gerçek güneş modülleri gerçekte ne kadar hızlı bozulur?

NREL'ın saha bozunma verilerine ilişkin dönüm noktası niteliğindeki meta-analizi (bilimsel literatürde rapor edilen 11.000'den fazla bozunma oranını kapsayan), kristalin silikon modüller için **yıllık ortalama %0,5 bozunma oranı** buldu. Ancak bu medyan muazzam çeşitliliği gizliyor. Ilıman iklimlerde en iyi performans gösteren modüller yılda %0,2-0,3 göstermektedir. Sıcak ve nemli iklimlerdeki modüller yılda %0,8-1,2 oranında bozunabilir. Ve belirli üretim dönemlerinde belirli üreticilerin modülleri (size bakınca, 2011–2014 çok kristalli PERC) tropik tesislerde yılda %2'yi aşan bozulma oranları göstermiştir.

2024 NREL PV Ömür Boyu Yıllık Raporu, Jinko, Trina, Q Cells, LONGi ve benzer üreticilerin modern 1. kademe modüllerinin **yılda %0,3-0,6** ortalama bozulma oranları gösterdiğini ve kaybın çoğunun önden yüklendiğini gösterdi ilk yılda (başlangıç LID/LeTID stabilizasyonu). Bu, başlangıç gücünün %80'inde 25 yıl garantili olan bir modülün yılda %0,5 oranında bozulması durumunda teknik özelliklere rahatlıkla uygun olduğu anlamına gelir; 25. yılda yaklaşık %87,5 güçte olacaktır.

Ancak işte kritik iş öngörüsü: 30 yıllık proje ömrü boyunca yılda %0,3 ile yıllık %0,7 bozulma arasındaki fark, **%12 kümülatif enerji üretimi** civarındadır. Yılda 15 milyon ABD Doları gelir üreten 100 MW güneş enerjisi santrali için bu, 30. yılda yaklaşık 1,8 milyon ABD Doları veya projenin ömrü boyunca yaklaşık 30 milyon ABD Doları kümülatif gelir kaybı demektir. PVEL (şimdi Kiwa PVEL) tarafından yapılan güvenilirlik testinin bu kadar önemli hale gelmesinin nedeni budur: Ürün Yeterlilik Programı, IEC minimumlarının çok ötesindeki modülleri, DH2000, TC600 çalıştıran ve birleşik stres dizilerini test eder ve "En İyi Performans Gösterenler" olarak yıllık Güvenilirlik Puan Kartı derecelendirme modülleri yayınlar.

2025 Puan Kartlarında, termal döngü, nemli ısı, mekanik stres, dolu stresi, PID ve LID+LeTID'de test edilen 300'den fazla benzersiz modül modelinden yalnızca küçük bir kısmı tüm kategorilerde En İyi Performansçı statüsüne ulaştı — ve **yalnızca üç modül ayrıca PAN dosya doğruluğunda da başarılı oldu** (yani gerçek dünyadaki enerji verimleri veri sayfası vaatleriyle eşleşti). Bu, her üreticinin "Tier 1" kalitesini iddia ettiği bir sektörde ciddi bir istatistik.

## Garanti Oyunu

Modül garantileri rekabetçi bir savaş alanı haline geldi. Standart yapı, bir **ürün garantisi** (malzeme kusurları ve işçilik için 10-15 yıl) ve bir **performans garantisi** (genellikle 25 veya 30 yıl, kullanım ömrü sonunda nominal gücün en az %80-84'ünü garanti eder ve yılda yaklaşık %0,4-0,55 doğrusal bozulma garantisi) içerir.

LONGi yakın zamanda Hi-MO X6 serisinde performans garantisini **nominal gücün %87,4'ünde** 30 yıla kadar uzattı. JinkoSolar, N tipi TOPCon modülleri için **30 yıl, %87,0** garanti vermektedir. Bu rakamlar gerçek güveni temsil eder, aynı zamanda hesaplanmış bir bahistir. Üreticiler aslında şunu söylüyor: "Modüllerimiz yılda en fazla %0,4 oranında bozulacaktır ve eğer bozulmazlarsa, onları değiştireceğiz veya size tazminat ödeyeceğiz."

Yakalama mı? Bir garanti yalnızca arkasındaki şirket kadar iyidir. Güneş enerjisi sektöründe son yirmi yılda düzinelerce üreticinin iflas ettiği, birleştiği veya piyasadan çıktığı görüldü. 10 yıl sonra var olmayacak bir firmanın 30 yıllık garantisi sadece bir kağıt parçası. Bu, kurumsal yatırımcıların en büyük, finansal açıdan en istikrarlı üreticilerin modüllerini tercih etmelerinin bir nedenidir; garantinin banka güvenilirliğine ilişkin durum tespitinin maliyeti, proje finansmanında önemli bir kalemdir.

## Yarın Neler Oluyor

Bununla fabrika yerleşim planlarından ekonomiye, tedarik zincirlerinden robotlara, kusur tespitinden uzun vadeli güvenilirliğe kadar imalat ve endüstriye derinlemesine dalışımızı tamamladık. Yarın sınıra dönüyoruz: **perovskit güneş pilleri**, 2009'da verimliliği %3,8'den bugün %26'nın üzerine çıkan ve silikonun yarım yüzyıllık hakimiyetini altüst etme tehdidi oluşturan kristalin yeni başlayan malzeme. Bu, fotovoltaik alanındaki en heyecan verici ve kelimenin her anlamıyla en istikrarsız hikayesidir. Orada görüşürüz.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-20.toml}}
