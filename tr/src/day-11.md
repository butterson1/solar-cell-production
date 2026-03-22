# 11. Gün: Çok Bağlantılı ve Tandem Hücreler — Güvertenin Termodinamiğe Karşı İstiflenmesi

*Dün, ince filmlerin dünyasını keşfettik; ince tabakayı tamamen atlayan ve yarı iletkenleri mikrometre cinsinden ölçülen katmanlar halinde biriktiren güneş pilleri. Bugün kavramsal olarak ters yöne gidiyoruz: basitleştirmek yerine istifliyoruz. Her biri güneş spektrumunun farklı bir dilimini absorbe edecek şekilde ayarlanmış birden fazla güneş hücresini üst üste yerleştiriyoruz ve bunu yaparak 1960'lardan bu yana tek bağlantılı cihazları kısıtlayan verimlilik tavanlarını yıkıyoruz. Bu, çok bağlantılı ve tandem hücrelerin hikayesidir; tüm fotovoltaikler arasında tartışmasız en şık hack ve güneş enerjisinin önümüzdeki on yılını tanımlayabilecek teknoloji.*

## Seçici Olmanın Sorunu

İstiflemenin neden önemli olduğunu anlamak için, 1. Günden beri tartıştığımız hayal kırıklığını tekrar gözden geçirmeniz gerekiyor. Tek eklemli bir silikon güneş hücresi (ne kadar mükemmel yapılmış olursa olsun) güneş ışığının yalnızca %29,4'ünü elektriğe dönüştürebilir. Bu, silikonun 1,12 eV bant aralığı için Shockley-Queisser sınırıdır ve bu bir mühendislik hatası değildir. Bu fizik.

İşte nedeni. Güneş ışığı tek renkli değildir. Bu, ultraviyoleden (yaklaşık 3,5 eV), görünür ışığa ve kızılötesine (0,5 eV'nin altında) kadar uzanan kaotik bir foton spreyidir. 1,12 eV bant aralığına sahip bir silikon hücre, bu spektrumu yalnızca 1 dolarlık banknotları kabul eden bir gişenin tüm zarafetiyle yönetir. 1,12 eV'den daha az enerjiye sahip fotonlar mı? Silikonun içinden geçip gidiyorlar; işe yaramaz, emilmemiş. Bu, güneş enerjisinin yaklaşık %19'unun tükendiği anlamına geliyor. 1,12 eV'den *daha fazla* olan fotonlar mı? Emilirler, ancak bant aralığının üzerindeki fazla enerjileri, termalizasyon adı verilen bir süreç yoluyla anında ısıya dönüşür. 3,0 eV'lik bir ultraviyole foton silikona çarparak 1,12 eV değerinde bir elektron deliği çifti üretirken, 1,88 eV (bu fotonun enerjisinin neredeyse üçte ikisi) atık ısıya dönüşür.

Bir araya getirildiğinde, alt bant aralığı iletimi ve bant aralığı üstü termalizasyon, gelen güneş enerjisinin yaklaşık %55'ini oluşturur. Bu özellikle silikonda bir kusur değil; *herhangi bir* tek bant aralıklı malzeme bu ödünleşimle karşı karşıyadır. Geniş bir bant aralığı seçtiğinizde daha az foton emersiniz. Dar bir bant aralığı seçtiğinizde emdiğiniz her fotonun daha fazlasını termalleştirirsiniz. Tek bağlantı sınırı, 1,34 eV civarında "ideal" bir bant aralığı için yaklaşık %33,7'ye ulaşır.

Çoklu bağlantı fikri etkisiz hale getirecek kadar basittir: Mükemmel bir bant aralığı bulmayı bırakıp bunun yerine birkaç tane kullansanız ne olur?

## Katmanlı Kek: Çok Bağlantılı Hücreler Nasıl Çalışır?

Her biri farklı bir yarı iletken malzemeden yapılmış, azalan bant aralığına göre yukarıdan aşağıya doğru düzenlenmiş bir güneş hücresi yığınını hayal edin. Üst hücre 1,9 eV'lik bir bant aralığına sahip olabilir. Yüksek enerjili mavi ve ultraviyole fotonları hevesle emer ve onları minimum termalizasyonla elektriğe dönüştürür çünkü 1,9 eV gerçek enerjiye yakındır. Absorbe edemediği kırmızı ve kızılötesi fotonlar doğrudan geçiyor; ancak kaybolmak yerine, örneğin 1,4 eV bant aralığına sahip olan alttaki ikinci hücreye düşüyorlar. Bu orta hücre, menzilindeki fotonları yakalar ve diğer her şey, yakın kızılötesini temizleyen, yaklaşık 1,0 eV bant aralığına sahip bir alt hücreye geçer.

Her katman, altındaki katman için bir spektral filtre görevi görür. Sonuç, güneş spektrumunu bir yerine birden fazla noktada örnekleyen, hem iletim hem de termalizasyon kayıplarını önemli ölçüde azaltan bir cihazdır. Teorik olarak üç bağlantılı bir hücre yaklaşık %49 verime ulaşabilir. Dört kavşağa gittiğinizde sınır %53'ü geçiyor. Sonsuz kavşaklarda (matematiksel bir düşünce deneyi), konsantre olmayan güneş ışığı altında %68'e veya maksimum konsantrasyon altında %86'ya yaklaşırsınız.

Yakalama mı? Bu katmanlı kekleri oluşturmak olağanüstü derecede zordur.

## III-V Yarı İletkenler: Fotovoltaik Aristokratları

Çoklu bağlantı hücrelerini mümkün kılan malzemeler periyodik tablonun III ve V Gruplarından gelir: galyum, indiyum, alüminyum (Grup III) ile arsenik, fosfor, nitrojen, antimon (Grup V) birleşir. Bu III-V bileşik yarı iletkenler silikonun sunamadığı bir şeyi sunuyor: ayarlanabilir bant aralıkları. Bir alaşımdaki elementlerin oranını (örneğin galyum indiyum fosfit (GaInP)) ayarlayarak bant aralığını 0,7 eV ile 2,3 eV arasındaki hemen hemen her değere çevirebilirsiniz. Tek bir akort çatalı yerine tüm notalardan oluşan bir klavyeye sahip olmak gibi.

Ticari çok bağlantılı hücrenin üç katmanı vardır: üstte 1,8-1,9 eV'de galyum indiyum fosfit (GaInP), ortada 1,4 eV'de galyum indiyum arsenit (GaInAs) ve altta 0,67 eV'de germanyum (Ge). Bu üçlü bağlantı tasarımı, 2000'li yılların başından bu yana fırlatılan neredeyse tüm yüksek değerli uydulara güç sağladı. Spectrolab (bir Boeing yan kuruluşu) ve SolAero Technologies (şu anda Rocket Lab'in bir parçası) gibi şirketler bu hücrelerden milyonlarcasını yörüngeye gönderdi; burada uzay koşullarında (AM0 spektrumu, atmosfer yok) kabaca %30'luk verimlilikleri göz yaşartan maliyetlerini haklı çıkarıyor.

Ve bu maliyete gelince: III-V üçlü bağlantılı bir hücre, watt başına yaklaşık 50-100 ABD doları çalıştırır. Bunu, kabaca watt başına 0,15-0,25 ABD doları olan standart bir silikon hücreyle karşılaştırın. III-V hücresi 200-400 kat daha pahalıdır. Neden? Üretim süreci - metalorganik kimyasal buhar biriktirme veya MOCVD - trimetilgalyum ve arsin gazı gibi toksik organometalik öncüleri kullanarak, 600-700°C'de bir reaktör odası içinde kristali her seferinde bir atomik katman halinde büyütür. Büyüme oranları saatte yaklaşık 1-2 mikrometre hızla ilerler. Yalnızca germanyum substratların maliyeti 100 mm'lik levha için 100 dolar civarındadır. Bu seri üretim değil butik imalattır.

## Altı Bağlantılı Rekor Tutucu

2020 yılında, Golden, Colorado'daki Ulusal Yenilenebilir Enerji Laboratuvarı'ndaki (NREL) araştırmacılar şimdiye kadar ölçülen en verimli güneş hücresini gösterdi: 143 güneş konsantrasyonu altında %47,1 verimliliğe ulaşan altı bağlantı noktalı bir cihaz. Her bir kavşak, güneş spektrumu boyunca inen bir merdiven gibi, bant aralıkları üstte 2,15 eV'den altta 0,69 eV'ye inen, hassas şekilde ayarlanmış bir III-V alaşımından oluşuyordu.

Bu cihazı dikkat çekici kılan sadece bağlantı noktalarının sayısı değil, aynı zamanda onu inşa etmek için kullanılan mühendislik hilesiydi. Katmanlardan üçü, germanyum substratıyla kafes uyumluydu; bu, kristal kafeslerinin neredeyse aynı atomik aralıklara sahip olduğu, dolayısıyla kusursuz bir şekilde büyütülebilecekleri anlamına geliyordu. Diğer üçü, ters çevrilmiş metamorfik çoklu bağlantı (IMM) adı verilen bir teknik kullanılarak kasıtlı olarak kafes-*yanlış*eşleştirildi. Hücre baş aşağı büyütüldü, ardından substratı soyuldu, ters çevrildi ve bir sapa bağlandı. Uyumsuz katmanlar, kafes sabitleri arasında yavaşça geçiş yapmak için kademeli tampon katmanları kullanır ve kusur yoğunluklarını santimetre kare başına 10⁶'nin altında tutar; bu da performansı olumsuz etkilemeyecek kadar düşük olur.

%47,1 oranıyla bu hücre, gelen tüm konsantre ışığın neredeyse yarısını elektriğe dönüştürür. Bağlamda, arabanızdaki benzinli motor, yakıt enerjisinin yaklaşık %25-35'ini harekete dönüştürür. En iyi doğal gaz santralleri yaklaşık %60'a ulaştı. Konsantrasyon altındaki altı eklemli bir güneş hücresi, insanlığın şimdiye kadar ürettiği en verimli termal makinelerle rekabet edebilir; ayrıca hareketli parçaları, yanmaları, emisyonları ve gürültüleri yoktur.

## Tandem'e girin: Silikonda Perovskite

İşte bu hikayedeki şaşırtıcı gelişme. Ticari açıdan en önemli çok bağlantılı hücre, 100$/W değerinde egzotik bir III-V yığını olmayacak. Bu, geleneksel bir silikon hücrenin üzerine perovskit katmanını koyan iki bağlantılı bir tandem olacak ve tek başına silikon hücreden çok az daha pahalıya mal olabilir.

21. Günde derinlemesine inceleyeceğimiz kristal malzemeler olan Perovskitlerin dikkate değer bir özelliği var: bant aralıkları, yalnızca öncü çözeltinin kimyasal bileşimini değiştirerek geniş bir aralıkta (1,2 ila 2,3 eV) ayarlanabilir. Yaklaşık 1,68 eV bant aralığına sahip bir perovskitin, iki eklemli bir tandemde silikon (1,12 eV) için bir üst hücre olarak neredeyse mükemmel olduğu ortaya çıkıyor. Perovskit mavi ve yeşil fotonları yakalıyor, düşük termalizasyonla akım üretiyor ve kırmızı ve kızılötesi ışığı silikon alt hücreye iletiyor. Birlikte, spektrumu her ikisinin de tek başına yapabileceğinden çok daha verimli bir şekilde kapsıyorlar.

Perovskit-silikon ikilisinin teorik verimlilik sınırı %43 civarındadır; bu da tek başına silikon için geçerli olan %29,4 sınırının oldukça üzerindedir. Uygulamada rekorlar nefes kesici bir hızla tırmanıyor. Nisan 2025'te, dünyanın en büyük güneş enerjisi üreticisi LONGi, perovskit-silikon tandem hücresini %34,85 verimlilikle sertifikalandırarak mevcut dünya rekorunu kırdı. Bunu 2025 sonlarında %34,76 ile JinkoSolar takip etti. Bu rakamlar şimdiden şimdiye kadar yapılmış en iyi tek bağlantılı silikon hücreyi (2024'te LONGi tarafından %26,81) yerle bir ediyor.

Bunu gerçekten devrim niteliğinde yapan şey potansiyel maliyettir. Germanyum substratları üzerinde pahalı MOCVD büyümesi gerektiren III-V hücrelerin aksine, perovskit katmanları çözeltiden (spin-kaplama, yarık-kalıpla kaplama) ve hatta silikon hücrenin yüzeyine mürekkep püskürtmeli baskıyla biriktirilebilir. Hammaddelerin (kurşun, iyot, metilamonyum, formamidinyum) neredeyse hiçbir maliyeti yoktur. İşleme sıcaklıkları, alttaki silikon hücrenin 1.400°C'sine kıyasla 100-150°C civarında düşük. Prensip olarak, mevcut bir silikon hücre üretim hattını perovskit biriktirme adımıyla yenileyebilir ve tek başına silikon hücrenin maliyetinden belki %10-20 daha fazla bir maliyetle tandem hücreler üretebilirsiniz.

## Akım Eşleştirme Sorunu

Tüm monolitik (iki terminalli) tandem hücrelerini yöneten temel bir mühendislik kısıtlaması vardır ve bu, bu alandaki tasarım kararlarının çoğunu açıkladığı için anlaşılmaya değerdir.

Monolitik bir tandemde, iki alt hücre, uç uca istiflenmiş piller gibi seri olarak bağlanır. Gerilim artar (iyi), ancak akımın her iki hücrede de aynı olması gerekir (zor). Üst hücre 20 mA/cm² ve ​​alt hücre 18 mA/cm² üretiyorsa cihazın tamamı 18 mA/cm² ile sınırlıdır. Üst hücrenin üretebileceği ekstra 2 mA/cm² boşa harcanır. Bu akım eşleştirme gereksinimi, üst hücrenin kalınlığını ve bant aralığını dikkatli bir şekilde tasarlamanız gerektiği anlamına gelir; böylece alt hücreyle aynı akımı üretmek için fotonların tam olarak doğru kısmını emer.

Bu, gerçek dünyada bir güvenlik açığı yaratır. Güneş spektrumu gün boyunca değişir; öğle vakti daha mavi, gün doğumu ve gün batımında daha kırmızıdır. Bulutlar mavi ışığı kırmızıdan daha fazla dağıtır. Tek eklemli bir hücrede bu spektral kaymaların pek önemi yoktur. Tandem hücresinde mevcut eşleşmeyi hizadan çıkarabilir ve anlık verimliliği yüzde birkaç oranında azaltabilirler. Araştırmacılar yıllık enerji verimini modellediler ve iyi tasarlanmış tandemlerin hala her iklimde tek bağlantı hücrelerini rahatlıkla geride bıraktığını, ancak standart test koşulları altında ölçülen "başlangıç ​​verimliliği"nin saha avantajını biraz abarttığını buldular.

Bir çözüm, iki terminal yerine dört terminale gitmektir: üst ve alt hücreleri bağımsız olarak bağlayın, her birinin kendi maksimum güç noktası izleyicisi vardır. Bu, mevcut eşleşmeyi tamamen ortadan kaldırır ancak kablolama karmaşıklığını ve maliyetini artırır. Endüstri, dört terminalli mimariyi öncelikle araştırma ortamlarında kullanırken, basitlik için iki terminalli monolitik yaklaşıma büyük ölçüde güveniyor.

## Ticarileştirme Yarışı

2026'nın başlarından itibaren tam olarak tek bir şirket ticari perovskit-silikon tandem modülleri sevk etti: Oxford PV, Brandenburg an der Havel, Almanya'da UK-kurulmuş bir başlangıç ​​üretim şirketi. Eylül 2024'te, yaklaşık 100 kW'lık ilk partiyi Amerika Birleşik Devletleri'ndeki kamu hizmeti ölçeğindeki bir müşteriye teslim ettiler. Ticari modülleri %24,5 modül verimliliğine ulaşır (hatırlayın, modül verimliliği aralık, kablolama ve kapsülleme kayıpları nedeniyle hücre verimliliğinden her zaman daha düşüktür), sertifikalı kayıt modülü ise %26,9'dur.

Oxford PV, 2027 yılına kadar üretimi GW-seviyesine yükseltmeyi planlıyor, ancak yalnız değiller. LONGi, JinkoSolar ve Canadian Solar, tandem üretim hatları geliştiriyor. Çinli üreticilerin çok büyük bir avantajı var: Zaten yüzlerce gigawatt'lık silikon hücre kapasitesi işletiyorlar. Perovskit üst hücre eklemek, sıfırdan bir fabrika yapısı değil, mevcut hatlarına *artımlı* bir yükseltmedir.

Çözülemeyen en önemli zorluk dayanıklılıktır. Silikon modüller 25-30 yıl garantilidir ve sahada yılda %0,3-0,5 oranında bozulma göstermiştir. Perovskitler tarihsel olarak çok daha hızlı bozunur; neme, oksijene, UV ışığa ve ısıya duyarlıdırlar. Oxford PV, kamuya açık olarak 2028 yılına kadar 20 yıllık modül ömrünü hedefledi, ancak pazarın şebeke ölçekli güneş enerjisi için beklediği 25 yıllık garantilerin elde edilmesi açık bir soru olmaya devam ediyor. Hızlandırılmış yaşlandırma testleri, modern kapsülleme tekniklerinin (kenar contaları, bariyer filmleri, bütil kauçuk) perovskitin ömrünü önemli ölçüde uzatabileceğini gösteriyor, ancak onlarca yıllık gerçek dünya saha verileri henüz mevcut değil.

## İkinin Ötesinde: Üçlü Kavşak Geleceği

Eğer iki kavşak bir kavşaktan daha iyiyse, peki ya üç kavşak? Perovskit-perovskit-silikon üçlü bağlantı hücreleri halihazırda laboratuvarlarda geliştirilmektedir. Konsept, silikonun (~1,12 eV) üzerine orta bant aralıklı bir perovskit (~1,5 eV) üzerine geniş bant aralıklı bir perovskit (~2,0 eV) ekler. Teorik sınır yaklaşık %51'e kadar çıkıyor; yani her fotonun mükemmel şekilde dönüştürülmesinin yarısına geliniyor.

Uygulamada, üçlü bağlantı tandem hücreleri hala düşük 20'li verimlilik aralığındadır, bunun nedeni geniş bant aralıklı perovskit formülasyonlarının aşırı kusur yoğunluklarından ve voltaj kayıplarından muzdarip olmasıdır. Ancak perovskit araştırmalarının hızı çok yüksek; perovskit güneş pilleri üzerine diğer fotovoltaik teknolojilere göre daha fazla makale yayınlanıyor ve laboratuvar kayıtları ile teorik sınırlar arasındaki fark herkesin tahmin ettiğinden daha hızlı kapanıyor.

## Mantıksız Gerçek

Çoğu insanı şaşırtan gerçek şu: Tarihteki en verimli güneş pilleri (bu %47,1'lik altı eklemli III-V canavarları) aslında güneş enerjisinin geleceğiyle alakasız. Bunlar muhteşem bilimsel başarılar, ancak 50-100 $/W seviyesinde bunlar uzay araçları ve askeri dronlarla sınırlı kalacak. Dünyayı gerçekten değiştirecek teknoloji, %30-35 verimlilikle çalışan ancak silikona yakın maliyetlerle üretilen, nispeten mütevazı perovskit-silikon ikilisidir.

Güneş enerjisi ekonomisinin temel dersi budur: verimlilik her şey değildir. Önemli olan *25+ yıl boyunca sağlanan elektriğin kilovatsaat başına maliyetidir*. Maliyeti 0,30 ABD Doları/W olan %35'lik bir tandem hücre, 80 ABD Doları/W maliyeti olan %47'lik bir hücreden çok daha değerlidir. Perovskit-silikon ikilisi, standart bir çatı üstü kurulumun enerji çıkışını minimum ek maliyetle %20-30 oranında artıracak şekilde ayarlandı ve bu, enerji piyasalarını yeniden şekillendiren türden bir gelişme.

## Yarın Neler Geliyor?

Artık güneş hücresi türlerinin tamamını (silikon, ince film, çoklu bağlantı ve tandem) ele aldık. Peki gerçekte ne kadar iyi olabilirler? Nihai bir tavan var mı? Yarın, fotovoltaikteki en önemli denklem olan Shockley-Queisser sınırına ve araştırmacıların bu sınırı aşmak için kullandıkları ustaca hilelere dalıyoruz: sıcak taşıyıcılar, çoklu eksiton üretimi, foton üst dönüşümü ve daha fazlası. Bir güneş hücresinin teorik maksimum verimliliğinin, kaç kurala boyun eğmek istediğinize bağlı olarak neden %33, %46, %68 veya %86 olduğunu öğreneceğiz.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-11.toml}}
