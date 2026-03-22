# 7. Gün: Yansıma Önleyici Kaplamalar ve Yüzey Dokulandırma

*Dünün yeni katkılı levhası, çalışan bir elektronik cihazdır; fotojenlenmiş yük taşıyıcılarını ayırabilen bir p-n bağlantısıdır. Ancak ışığa tuttuğunuzda sorunu hemen göreceksiniz. Bu bir ayna. Cilalı silikon, gelen güneş ışığının yaklaşık %35'ini yansıtır; fotonların üçte birinden fazlası doğrudan gökyüzüne geri döner ve asla elektrik üretme şansı bulamaz. Bu küçük bir verimsizlik değil. Hücrenizin teorik maksimum verimliliği %29'sa, gelen fotonların %35'ini ön kapıdan kaybetmek, rekombinasyonu, direnci veya başka herhangi bir kayıp mekanizmasını düşünmeden önce sizi yaklaşık %19'a düşürür. Güneş enerjisi sektörünün ilk yirmi yılı boyunca bu, en büyük performans darboğazıydı. Bugün, 1800'lerden bu yana anlaşılan ancak nanometre hassasiyetinde tasarlanan fiziği kullanarak bunu ortadan kaldırıyoruz.*

---

## Silikon Neden Bu Kadar Yansıtıcıdır

Silikonun yansıtıcılığı tesadüfi değildir; onu iyi bir güneş hücresi malzemesi yapan aynı elektronik özelliklerin doğrudan bir sonucudur. Işık iki malzeme arasındaki bir arayüze çarptığında, yansıyan kısım **kırılma indekslerindeki** farka bağlıdır. Havanın kırılma indisi 1,0'dır. Görünür spektrumda silikonun kırılma indisi 3,5 ila 6,0 arasındadır (mavi ışık için daha yüksek, kırmızı için daha düşüktür). Bu çok büyük bir uyumsuzluk.

Düz bir arayüzden normal geliş açısındaki yansıma Fresnel denklemi ile verilir:

**R = ((n₁ - n₂) / (n₁ + n₂))²**

Silikona çarpan hava (n = 1,0) için (600 nm'de n ≈ 3,9): R = ((1,0 - 3,9)/(1,0 + 3,9))² = (2,9/4,9)² ≈ 0,35 — veya %35. Bu kaba bir tahmin değil; tam fizik budur. Her cilalı silikon yüzey, ne kadar temiz, saf veya mükemmel katkılı olursa olsun görünür ışığın yaklaşık %35'ini yansıtır.

Karşılaştırma için, cam (n ≈ 1,5) yüzey başına yalnızca yaklaşık %4'ü yansıtır. Su (n ≈ 1,33) yaklaşık %2'yi yansıtır. Elmas (n ≈ 2,42) yaklaşık %17'yi yansıtır. Silisyumun kırılma indisi, dielektrik fonksiyonunun yüksek bir gerçek kısmına bağlanan güçlü bantlar arası soğurma özelliğine sahip yarı iletkenler olan germanyum ve galyum arsenit ile paylaşılan bir sınıftadır. Silikona yararlı bant aralığını veren aynı sıkı elektron enerji aralığı, aynı zamanda ona bu şiddetli yansıtıcı yüzeyi de verir.

Bu sorunu çözmenin tam olarak iki yolu vardır: optik olarak yansımayı azaltmak için yüzeye bir şey koymak (yansımayı önleyici kaplamalar) veya fotonların birden fazla giriş şansı elde etmesi için yüzeyi yeniden şekillendirmek (doku oluşturma). Modern güneş pilleri her ikisini de yapar.

---

## Yansıma Önleyici Kaplamalar: İnce Film Hilesi

Yansıma önleyici kaplamaların (ARC'ler) arkasındaki prensip aldatıcı derecede basittir ve Lord Rayleigh'in 1886'daki keşfine kadar uzanır: kararmış cam, temiz camdan *daha fazla* ışık iletir. İnce kararmış film, üst ve alt yüzeylerinden yansıyan ışık arasında yıkıcı bir girişim yaratarak yansımayı ortadan kaldırıyordu.

İşte nasıl çalışıyor? Plakanın yüzeyine hava ve silikon *arasında* kırılma indisine sahip ince bir malzeme filmi yerleştirirsiniz. Işık iki arayüzden yansır: havadan kaplamaya ve kaplamadan silikona. Kaplama kalınlığı, yansıyan bu iki ışının tam olarak yarım dalga boyunda faz dışı olmasını sağlayacak şekilde seçilirse, yıkıcı bir şekilde girişimde bulunurlar ve iptal ederler. Yansıyan ışık kendi kendini yok eder ve enerjinin neredeyse tamamı silikona geçer.

Tek bir dalga boyunda mükemmel yansıma önleme koşulları şunlardır:

1. **Optimal kalınlık:** d = λ / (4n_coating), burada λ, vakumdaki hedef dalga boyudur. Buna "çeyrek dalga" kaplama denir.
2. **Optimal kırılma indisi:** n_kaplama = √(n_hava × n_silikon) = √(1,0 × 3,9) ≈ 1,97

Yani silikon için ideal ARC, 2,0'a yakın bir kırılma indisine ve hedef rengin çeyrek dalga boyuna ayarlanmış bir kalınlığa sahiptir. Güneş spektrumunun zirvesi için (~600 nm): d = 600 / (4 × 2,0) = 75 nm. Yalnızca 75 nanometre kalınlığındaki (insan saçının genişliğinin yaklaşık 1/700'ü kadar) bir katman, 600 nm'deki yansımayı neredeyse tamamen ortadan kaldırabilir.

Güneş pillerinin mavi görünmesinin nedeni de budur.

---

## Güneş Pillerinin Rengi

Eğer bir güneş paneline bakmışsanız hücrelerin koyu, tekdüze mavi rengini fark etmişsinizdir. Bu renk, işini yapan ve aynı zamanda sınırlarını da ortaya çıkaran ARC rengidir.

Tek katmanlı bir çeyrek dalga ARC yalnızca bir dalga boyunda sıfır yansıma elde edebilir. Endüstri bunu yaklaşık 600 nm'ye (turuncu ışık) ayarlıyor; bu, silikonun soğurulmasıyla ağırlıklandırılan güneş spektrumunun zirvesine yakın. 600 nm'de yansıma neredeyse sıfıra düşer. Ancak daha kısa dalga boylarında (mavi, 450 nm) ve daha uzun dalga boylarında (kırmızı, 750 nm), film kalınlığı artık tam olarak çeyrek dalga değildir ve yansıma %5-10'a kadar geriler.

Gördüğünüz mavi renk, kelimenin tam anlamıyla kaplamanın *bastıramadığı* ışıktır. Mavi fotonlar (400-500 nm) kısmen yansıtılarak hücreye karakteristik rengini verir. Mükemmel şekilde yansıma önleyici bir hücre siyah görünür - ve gerçekten de optimize edilmiş ARC değerine sahip en iyi dokulu hücreler neredeyse siyah görünür ve görünür spektrumun tamamında %2'den daha azını yansıtır.

Bazı üreticiler özellikle estetik uygulamalar için siyah paneller sunmaya başladı (ev sahiplerinin evlerinde cafcaflı mavi bir dikdörtgen istemediği çatı üstü konut kurulumları). Bunlar renklerini daha kalın ARC, agresif doku ve bazen çok katmanlı kaplamaların birleşimiyle elde ederler.

---

## Silikon Nitrür: Endüstrinin Mucize Kaplaması

Güneş enerjisi endüstrisi her zaman aynı ARC malzemeyi kullanmıyordu. 1970'li ve 80'li yıllardaki ilk hücreler, atmosferik basınçlı kimyasal buhar biriktirme yoluyla biriktirilen titanyum dioksit (TiO₂, n ≈ 2,2-2,6) kullanıyordu. Optik olarak iyi çalışıyordu ama sadece bir kaplamaydı; tek bir işi vardı.

Devrim, araştırmacıların plazmayla geliştirilmiş kimyasal buhar biriktirme (PECVD) tarafından biriktirilen **silikon nitrürün (SiNₓ:H)** aynı anda üç işi yapabildiğini keşfetmesiyle gerçekleşti:

1. **Yansıma önleme.** SiNₓ'nin ayarlanabilir kırılma indeksi 1,9-2,1'dir (silikon/nitrojen oranı değiştirilerek ayarlanır), silikon ARC'ler için neredeyse mükemmeldir.

2. **Yüzey pasivasyonu.** Bu, oyunun kurallarını değiştiren bir şeydir. SiNₓ:H atomik yüzde 10-15'e kadar hidrojen içerir. ~800°C'de sonraki bir ateşleme adımı sırasında, bu hidrojen silikon yüzeyine yayılır ve **sarkan bağları pasifleştirir** - kristal kafesin aniden sona erdiği silikon yüzeyindeki doymamış bağlar. Her sarkan bağ bir rekombinasyon merkezidir; Hidrojen atomları onları kapatarak tuzağı etkisiz hale getirir. Bu, yüzey rekombinasyon hızını >100.000 cm/s'den (çıplak silikon) <10 cm/s'ye (pasifleştirilmiş yüzey) düşürebilir - 10.000 kat iyileşme.

3. **Toplu pasifleştirme.** Hidrojen yüzeyde durmaz. Ateşleme, kusurları bulma ve nötrleştirme sırasında silikon yığını boyunca yayılır (çok kristalli hücrelerdeki tane sınırları, metalik safsızlık kompleksleri, bor-oksijen çiftleri). Çok kristalli silikonda, hidrojenasyondan sonra yığın ömrü 10 μs'den 100 μs'nin üzerine çıkabilir. Bu tek işlem adımı, çok kristalli silikonun onlarca yıldır monokristalin ile rekabet edebilmesinin önemli bir nedeniydi.

PECVD işlemi şu şekilde çalışır: levhalar bir vakum odasına girer (basınç ~0,1-1 Torr) ve **silan (SiH₄)** ve **amonyak (NH₃)** gaz karışımı eklenir. 13,56 MHz'lik bir radyo frekansı plazması (iletişime müdahaleyi önlemek için özel olarak endüstriyel kullanıma tahsis edilen standart endüstriyel RF frekansı) gazları ayrıştırır ve reaktif parçalar, levha yüzeyinde 350-450°C'de biriktirilir. 75 nm'lik bir filmin yerleştirilmesi yaklaşık 3-5 dakika sürer.

Önde gelen PECVD ekipman üreticisi **Meyer Burger**'dir (İsviçre, Roth & Rau'yu satın alarak). Çinli rakipleri arasında **S.C New Energy** (eski adıyla S.C Solar) ve **Shenzhen SC** yer alıyor. Modern bir hat içi PECVD sistemi saatte yaklaşık 4.000-6.000 levhayı işler ve maliyeti 1-2 milyon dolar olur. Tüm hücre hattındaki en yüksek verimli araçlardan biridir.

İşte bu adımın ne kadar kritik olduğunu gösteren bir rakam: Çıplak silikon hücreye SiNₓ:H PECVD eklenmesinden elde edilen verimlilik kazancı genellikle **3-5 mutlak yüzde puanıdır**. Bu çok büyük. Verimliliğin %15'ten %20'ye çıkması, aynı alandan %33 daha fazla güç elde edilmesi anlamına gelir. Güneş pili üretiminde başka hiçbir tek süreç adımı bu kadar performans artışı sağlayamaz.

---

## Yüzey Dokulandırma: Fotonlara İkinci Bir Şans Vermek

Yansıma önleyici kaplamalar güçlüdür ancak temel bir sınırlamaları vardır: yalnızca tek bir dalga boyunda ve tek bir geliş açısında mükemmel çalışırlar. Rengi değiştirdiğinizde veya ışığı eğdiğinizde yansıma artar. Soruna optikten ziyade geometrik olarak saldıran tamamlayıcı bir yaklaşım var: yüzeyi pürüzlü hale getirmek.

Fikir son derece basittir. Silikon yüzeyi küçük piramitlerle kaplıysa, piramidin bir yüzünden yansıyan bir foton, bitişik yüze sıçrayarak silikonun içine girmek için ikinci bir şans elde eder. Tekrar yansırsa üçüncü bir şans yakalayabilir. Her sıçrama hayatta kalan yansıyan fraksiyonu çarpımsal olarak azaltır. Düz bir yüzey %35'i yansıtıyorsa, ışığın iki kez çarptığı dokulu bir yüzey 0,35 × 0,35 = %12,25'i yansıtır. Üç isabet: 0,35³ = %4,3. Dokunun üstündeki ARC ile her iki etkiyi birleştiriyorsunuz: her sıçrama yalnızca ~%1-3 yansıma görüyor, dolayısıyla iki sıçrama <%0,1 toplam yansıma sağlıyor.

### Monokristal Silisyumun Alkali Tekstürü

Monokristalin silikon, dokulamayı zarif bir şekilde basitleştiren kristalografik bir sırra sahiptir. (100) kristal düzlemi (ticari levhaların standart yüzey yönelimi) sıcak potasyum hidroksit (KOH) çözeltisini kristal yönüne önemli ölçüde bağlı olan bir hızda aşındırır. (111) düzlemleri, (100) düzlemlerinden yaklaşık **30-50 kat daha yavaş** aşınır. Bu anizotropi, bir (100) levhayı sıcak KOH (%1-5 konsantrasyon, 70-80°C, 15-30 dakika boyunca) içine daldırdığınızda, yavaş aşındıran (111) düzlemler hayatta kalırken hızlı aşındıran yüzeylerin aşındığı anlamına gelir. Elmas kübik kafesin geometrisi, hayatta kalan (111) yüzlerin karakteristik 54,7° taban açısına ((100) ve (111) düzlemleri arasındaki açı) sahip **rastgele dik piramitler** oluşturmasını garanti eder.

Piramitler tipik olarak 1-10 mikrometre uzunluğundadır; görünür ışığı (dalga boyları 0,4-1,1 μm) etkili bir şekilde yakalayacak kadar büyüktür, ancak sonraki işlemlere müdahale etmeyecek kadar da küçüktür. Boyut dağılımı rastgeledir ve bu aslında faydalıdır: Piramit boyutlarının dağılımı, tekdüze yapılardan daha geniş bir dalga boyu aralığında yansımayı bastırır.

Bu süreci üretime hazır hale getiren katkı maddesi **izopropil alkol (IPA)** veya daha yakın zamanda **GP Solar** (Almanya) gibi şirketlerin tescilli yüzey aktif maddeleridir. IPA yüzeydeki kabarcık yapışmasını kontrol eder — aşındırma reaksiyonu sırasında hidrojen gazı üretilir ve yüzey aktif madde olmadığında kabarcıklar yüzeye yapışır ve dağlanmamış düz noktalar oluşturur. %3-5'lik bir IPA ilavesi, kabarcıkların anında serbest kalmasını sağlayarak, tek biçimli piramit kapsamı sağlar.

Tamamen dokulu ve ARC-kaplamalı monokristal plaka, gelen ışığı yalnızca **%1,5-3** yansıtır; bu oran cilalı silikonda %35'tir. Bu, yansıma kayıplarında %90-95'lik bir azalma anlamına gelir.

### Çok Kristalli Silikonun Asit Dokusu

Çok kristalli silikon, alkalin dokulamayı kullanamaz çünkü rastgele tane yönelimleri, anizotropik dağlamanın kaotik bir manzara ürettiği anlamına gelir: bazı taneler mükemmel piramitler oluşturur, bazıları ise düz raflara veya derin çukurlara kazınır. Sonuç berbat görünüyor ve daha kötü performans gösteriyor.

Bunun yerine, çok kristalli plakalar **asidik izotopik aşındırma** kullanır; hidroflorik asit (HF) ve nitrik asit (HNO₃) karışımı, bazen "HF/HNO₃ aşındırma" olarak da adlandırılır. Bu aşındırma, kristal yöneliminden bağımsız olarak silikona saldırır ve 1-5 μm ölçeğinde yuvarlak çukurlar ve tepeciklerden oluşan bir yüzey oluşturur. Doku geometrik olarak piramitler kadar zarif değildir ve biraz daha kötü optik performansa ulaşır: monokristalin için %1,5-3'e kıyasla ARC ile yaklaşık **%5-8 ağırlıklı ortalama yansıma**.

Bu yansıtma dezavantajı, çok kristalli silikonun pazar payını kaybetmesinin çeşitli nedenlerinden biridir. 2015 yılında çoklu kristal küresel üretimin yaklaşık %55'ini oluşturuyordu. 2024 yılına gelindiğinde bu oran %10'un altına düştü ve monokristalin neredeyse tamamen hakimiyeti ele geçirdi. Daha iyi dokulandırma hikayenin bir parçasıydı.

---

## Siyah Silikon: Üstün Yüzey

İşte günün mantığa aykırı sürprizi: **en iyi yüzey dokusu kesinlikle piramitler değildir; nano ölçekli çimlerdir.**

2010'ların başında araştırmacılar, belirli plazma aşındırma işlemlerinin silikon yüzeylerde iğne benzeri nanoyapılar oluşturabildiğini keşfettiler; bunlar yalnızca 100-500 nm yüksekliğinde ve 50-200 nm aralıklı sivri uç ormanlarıydı. Bu "siyah silikon" adını görünümünden alıyor: O kadar çok ışık emiyor ki tamamen siyah görünüyor ve tüm güneş spektrumunda **%0,3**'ten daha azını yansıtıyor. Karşılaştırma için, en iyi geleneksel dokulu ve kaplamalı yüzey yaklaşık %1,5'i yansıtır.

Fizik piramidal dokulandırmadan farklıdır. Nano ölçekte, sivri uçlar **kademeli bir kırılma indisi** oluşturur; yani ışığın dalga boyuyla karşılaştırılabilir bir mesafe boyunca havadan (n = 1) silikona (n = 3,9) yumuşak bir geçiş. Işık keskin bir arayüzü "görmez"; kademeli bir değişim görüyor. Güvelerin gözleri bu nedenle yansıma önleyicidir; güvelerin karanlıkta gözleri parıldamadan ve yırtıcı hayvanları çekmeden görebilmelerini sağlamak için milyonlarca yıl boyunca evrimleşen, aynı dereceli indeks etkisini yaratan nano ölçekli çıkıntılara sahiptirler.

Siyah silikonun üretim sürecinde kükürt heksaflorür (SF₆) ve oksijen plazmaları ile **reaktif iyon aşındırma (RIE)** veya alternatif olarak gümüş veya altın nanopartiküllerin bir HF/H₂O₂ çözeltisi içinde silikonun yerel aşındırılmasını katalize ettiği **metal destekli kimyasal aşındırma (MACE)** kullanılır. MACE daha ucuzdur ve ıslak tezgahlarda (vakum ekipmanı olmadan) yapılabilir, bu da onu imalat için çekici kılar.

Fin şirketi **Aalto Üniversitesi** yan ürünü **Elfys** ve Çinli hücre üreticileri, monokristal ile yansıtma aralığını kapatan, özellikle çok kristalli hücreler için siyah silikon dokulamayı ticarileştirdi. Ancak bir sorun var: tüm bu nano ölçekli sivri uçlar yüzey alanında *muazzam* bir artışı temsil ediyor; potansiyel olarak düz bir plakadan 10-50 kat daha fazla yüzey. Daha fazla yüzey, daha fazla sarkan bağ, daha fazla rekombinasyon anlamına gelir. Eğer bu yüzeyi yeterince pasifleştiremezseniz optik kazanç elektriksel kayıplar nedeniyle yok olur. Bu nedenle siyah silikon ancak nano ölçekli özellikleri uyumlu bir şekilde kaplayabilen alüminyum oksit (Al₂O₃) atomik katman biriktirme gibi gelişmiş pasifleştirme tekniklerinin geliştirilmesinden sonra pratik hale geldi.

---

## Arka Taraf Optikleri: İçeriden Geleni Yakalamak

Ön yüzeye odaklandık ama arka tarafta da foton yönetimi gerçekleşiyor. Gelen uzun dalga boyundaki fotonların yaklaşık %20-30'u (yakın kızılötesi, 900-1.200 nm), emilmeden 170 μm'lik tabakanın içinden geçer. Alüminyum arka teması olan geleneksel bir hücrede, bunların bir kısmı ikinci geçiş için geri yansıtılır; alüminyum, yaklaşık %60-70 yansıtma oranıyla bir arka ayna görevi görür.

Modern **PERC hücreler**, uzun dalga boylu fotonlar için >%95 dahili arka yansıtma sağlayan dielektrik arka pasifleştirme katmanı (Al₂O₃ + SiNₓ yığını) ile bunu önemli ölçüde geliştirdi. İyileşme, doğrudan silikon-alüminyum temasıyla karşılaştırıldığında dielektrikteki daha düşük optik absorpsiyondan kaynaklanmaktadır. Arka dielektrik, alanın yalnızca %1-3'ünü kaplayan küçük lazerle delinmiş açıklıklara (yerel arka yüzey alan temasları) sahiptir, dolayısıyla arka yüzeyin büyük çoğunluğu yüksek kaliteli bir aynadır.

Ve bir de **çift yüzlü hücreler** var; her iki taraftan da ışık toplayan hücreler. İki yüzeyli bir modülde, arka taraf yerden yansıyan albedo ışığa (beyaz çatılar, kum, kar) maruz kalır. Çift yüzeyli hücreler opak alüminyum arka tabakayı atlar ve şeffaf bir arka kısım kullanır ve zemin koşullarına bağlı olarak %5-20 ek enerji kazanır. Arka yüzeydeki doku ve ARC ön yüzey kadar önemli hale geliyor. 4. Haftada çift yüzeyli teknolojiye derinlemesine dalacağız.

---

## Yığın: Hepsini Bir Araya Getirmek

Uzaklaştıralım ve modern bir monokristalin PERC hücresinin optik yığınının tamamını yukarıdan aşağıya görelim:

| Katman | Kalınlık | Kırılma İndeksi | İşlev |
|----------|-----------|-----------|----------|
| Hava | — | 1.00 | — |
| SiNₓ:H ARC | 75nm | 1.95-2.05 | Yansıma önleme + pasifleştirme |
| Dokulu Si yüzeyi | 3-8 μm piramitler | 3.5-6.0 | Işık yakalama + çoklu sıçrama |
| Si toplu (yayıcı + taban) | ~170 mikron | 3.5-6.0 | Emilim + taşıyıcı oluşumu |
| Al₂O₃ arka pasivasyon | 5-10nm | 1.65 | Pasivasyon + arka yansıma |
| SiNₓ arka dielektrik | 100-120nm | 2.05 | Arka yansıma + koruma |
| Tüm yerel kişiler | — | — | Elektrik kontağı |

Ön dokulandırma + ARC birlikte, ağırlıklı ortalama ön yansımayı ~%1,5-2,5'e düşürür. Arka dielektrik yansıma, dahili arka yansımayı %95'in üzerine çıkarır. Toplam optik yol iyileştirmesi (tek bir geçişle karşılaştırıldığında fotonların hücre içinde etkin olarak ne kadar süre harcadığı), silikon için ~60x olan teorik sınırda (Yablonovitch sınırı) yaklaşık **4n²**'dir. Pratik hücreler yaklaşık 10-20 kat yol iyileştirmesi sağlar.

Kombine optik mühendislik, cilalı, kaplanmamış bir hücreye kıyasla kabaca **5-7 mA/cm² fotoakım** ekler. Tipik çalışma voltajında ​​(~0,65 V), bu, hücre başına yaklaşık 3,5-4,5 watt veya 2-3 mutlak yüzdelik verimlilik puanı anlamına gelir. SiNₓ pasifleştirme etkileriyle birleştirildiğinde, ARC + dokulandırma adımlarının toplam faydası kolayca **6-8 yüzde puanlık** olur; bu, laboratuvar merakı ile ticari olarak uygun bir ürün arasındaki farktır.

---

## Kimsenin Bahsetmediği Kimyasal Atık Sorunu

Dokumanın bahsetmeyi hak eden daha az çekici bir yanı var. Alkali dokulandırma, levha başına yaklaşık 2-4 litre KOH çözeltisi tüketir ve çözünmüş silikatlar, potasyum tuzları ve IPA atık akışı üretir. Asit dokusu daha da kötüdür: HF ve HNO₃'nun her ikisi de tehlikelidir (HF herkesin bildiği gibi tehlikelidir; cilde nüfuz eder ve kemik kalsiyumuna saldırır) ve harcanan asit, çözünmüş silikon ve nitrojen oksitler içerir.

Saatte 10.000 gofret tekstüre eden bir fabrika, nötralizasyon, arıtma ve imha gerektiren saatte yüzlerce litre kimyasal atık üretiyor. Küresel güneş enerjisi endüstrisi *günde* yaklaşık 500 milyon levha işliyor. Bu bir kimya okyanusu.

Endüstri, harcanan dokulandırma çözümlerini yeniden üreten ve kimyasal tüketimini %60-80 oranında azaltan kimya geri dönüşüm sistemleriyle (**RENA Technologies**, Almanya gibi şirketler) yanıt verdi. Kapalı devre su sistemleri, su kullanımını gofret başına 15 litreden 3 litrenin altına düşürdü. Ancak agresif ıslak kimyaya olan temel bağımlılık, güneş enerjisi üretiminin çevresel sıkıntı noktalarından biri ve siyah silikon RIE gibi kuru plazma dokulandırma yöntemlerinin motivasyonlarından biri olmaya devam ediyor.

---

## İleriye Bakış: Serigrafi Metal Kontaklar

Artık levha hazırlama üçlemesini tamamladık: doping (6. Gün) bize p-n bağlantısını verdi ve bugünkü dokulandırma ve ARC bize optik ön ucu verdi. Gofret, güneş ışığından verimli bir şekilde yük taşıyıcıları üretebilir. Ama hâlâ akımı *dışarı* çıkarmanın bir yolu yok. Elektrik bağlantıları henüz yapılmadı.

Yarın, fotojenere akımı toplamak ve çıkarmak için ön tarafa gümüş şebeke çizgileri ve arkaya alüminyum yerleştirme işlemi olan **serigrafi baskı ve metalizasyon** ile uğraşacağız. Bu, asırlık tekstil baskı sanatından ödünç alınan, gram başına silikon tabakanın kendisinden daha değerli olan macunlar içeren ve imkansız bir mühendislik değiş tokuşu ile karşı karşıya olan bir süreçtir: eklediğiniz her metal çizgi mevcut koleksiyonu geliştirir ancak gelen ışığı engeller. O iğneye nasıl iplik geçiriyorsun? 8. Gün.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-07.toml}}
