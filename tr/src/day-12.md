# 12. Gün: Verimlilik Sınırları ve Bunları Nasıl Aşabilirsiniz — Çiğneyemeyeceğiniz Kanunlar (ve Yararlanabileceğiniz Boşluklar)

*Dün yarı iletkenleri, güneş spektrumunu özel katmanlara bölerek verimliliği %47'ye çıkaran çok bağlantılı kulelere yığdık. Ancak sanki kutsal bir emirmiş gibi bir rakama -%33,7, Shockley-Queisser sınırına- başvurmaya devam ettik. Bugün bu sınırı kaldırıyoruz. Aslında nereden geliyor? Mükemmel bir tek bağlantı hücresini gelen güneş ışığının kabaca üçte biri ile sınırlamak için hangi fiziksel süreçler bir araya geliyor? Ve en önemlisi, hangi zekice numaralar - biraz termodinamik, biraz optik, biraz tuhaf - bu tavanı delebilir? Bu, tüm kurstaki en önemli teori günüdür çünkü güneş hücresi tasarımındaki her mühendislik seçimi, sonuçta bu sınırlarla yapılan bir müzakeredir.*

## Oyunu Tanımlayan 1961 Makalesi

1961'de William Shockley (evet, transistörün ortak mucidi) ve Hans-Joachim Queisser, fotovoltaik tarihinde en çok alıntı yapılan çalışma haline gelecek bir makale yayınladılar. "P-n Bağlantılı Güneş Pillerinin Verimliliğinin Ayrıntılı Denge Limiti" başlıklı belge, aldatıcı derecede basit bir soru sordu: *Mükemmel bir güneş hücresi inşa ettiyseniz - üretim hatası, direnç kaybı, optik kusur yoksa - elde edebileceğiniz mutlak maksimum verimlilik nedir?*

Yaklaşımları zarifti. Güneş pilini, iki ısı rezervuarı arasında çalışan termodinamik bir motor gibi ele aldılar: 5,778 K sıcaklıktaki güneş ve 300 K sıcaklıktaki (oda sıcaklığı) hücrenin kendisi. Daha sonra ayrıntılı denge ilkesini uyguladılar; termal dengede her mikroskobik sürecin tersiyle dengelenmesi gerektiği fikri. Bir güneş hücresi fotonları emer, ancak aynı zamanda onları *yayması* da gerekir. Mükemmel bir hücre bile ışık yayar. Bu kaçınılmaz ışınımsal rekombinasyon, fiziğin fotovoltaik dönüşüme yüklediği temel vergidir.

Sonuçları: Konsantre olmayan güneş ışığı (AM1.5G spektrumu) altındaki tek bağlantılı bir hücre için maksimum verimlilik **%33,7** olup, yaklaşık **1,34 eV** bant aralığında elde edilmiştir. 1,12 eV'deki silikonun ayrıntılı denge sınırı yaklaşık %29,4'tür. 1,42 eV'deki galyum arsenit, %33,2 ile biraz daha iyi bir anlaşma elde ediyor; bu da küresel optimuma umut verici derecede yakın.

Bu bir tahmin ya da kaba bir tahmin değildi. Bu termodinamik bir kanıttı. Ve tek bağlantılı cihazlarda %50 verimlilik peşinde koşan tüm bir araştırmacı kuşağının moralini bozdu.

## Beş Hırsız: Enerji Aslında Nereye Gidiyor?

Shockley-Queisser (SQ) sınırını anlamak için, gelen güneş enerjisinin yaklaşık üçte ikisini çalmak için komplo kuran beş kayıp mekanizmasını karşılamanız gerekir. Onları aynı kalabalıkta çalışan beş yankesici olarak düşünün.

### 1. Alt Bant Aralığı İletimi (gelen enerjinin ~%19'u)

Enerjisi bant aralığının altında olan fotonlar, sanki orada değilmiş gibi yarı iletkenden doğrudan geçerler. 1,12 eV'deki silikon için bu, dalga boyu yaklaşık 1.100 nm'den uzun olan her fotonun (güneş spektrumunun tüm orta ve uzak kızılötesi kısmı) görünmez olduğu anlamına gelir. Dünyadaki güneş enerjisinin yaklaşık %19'u silikonun bant aralığının altına düşüyor. Daha dar bir bant aralığı seçerek bu kaybı azaltabilirsiniz ancak bu, bir sonraki hırsızı daha da kötüleştirir.

### 2. Termalleştirme (gelen enerjinin ~%33'ü)

Bu büyük olan. Bant aralığının *üzerinde* enerjiye sahip bir foton emildiğinde, bir elektron-delik çifti oluşturur. Ancak elektron tüm bu foton enerjisini tutamaz; femtosaniyeler (10⁻¹⁵ saniye) içinde hızla iletim bandı kenarına doğru termalleşir. Silikona çarpan 3,0 eV'lik bir foton, 1,12 eV değerinde bir elektron deliği çifti üretirken, 1,88 eV'yi kafes titreşimlerine (ısı) boşaltır. Bu süreç olağanüstü derecede hızlıdır: "Sıcak" elektron ilk pikosaniyede kristal kafesle binlerce kez çarpışır ve çarpışma başına yaklaşık 50 meV'lik adımlarla enerji kaybeder. Bunu ölçebildiğiniz zaman bile fazla enerji gitmiş olur. Tam güneş spektrumu boyunca termalizasyon, gelen enerjinin yaklaşık %33'ünü oluşturur. Bu, herhangi bir güneş hücresindeki en büyük kayıptır.

### 3. Işınımsal Rekombinasyon (açık devrede ~%2-3)

İşte Shockley ve Queisser'in temel görüşü: Termal dengedeki bir güneş hücresi, tam olarak emdiği kadar foton yaymalıdır. Onu aydınlattığınızda, onu dengeden *çıkarırsınız* ve bir voltaj üretir. Ama asla yaymayı bırakmaz. Maksimum güç noktasında, 300 K sıcaklıktaki bir silikon hücre, emdiği enerjinin yaklaşık %2-3'ünü kızılötesi fotonlar olarak gökyüzüne geri yayar. Bu çok küçük gibi görünse de bu *kaçınılmaz* bir kayıptır; daha iyi malzemeler veya daha akıllı tasarımlarla ortadan kaldıramayacağınız bir kayıptır. Isıyı işe dönüştürmek için ödediğiniz termodinamik kiradır.

Güneş pillerinin her zaman bant aralığından daha düşük bir maksimum gerilime sahip olmasının nedeni de budur. Silikonun 1,12 eV bant aralığı, en iyi hücrelerde yaklaşık 0,74 V'luk bir açık devre voltajı üretir; bu, 0,38 V'luk bir açıktır. Bu fark büyük ölçüde, yönlendirilmiş güneş ışığı ışınını (düşük entropi) hücre içindeki izotropik foton gazına (daha yüksek entropi) dönüştürmenin entropi maliyeti artı ışınımsal emisyon vergisidir.

### 4. Carnot Faktörü

SQ sınırının içinde Carnot benzeri bir termodinamik kısıtlama gömülüdür. Güneş 5,778 K'de, hücre ise 300 K'dadır. Bu sıcaklıklar arasındaki mükemmel bir Carnot motoru 1 - 300/5778 = %94,8 verim elde edecektir. Ancak güneş hücresi bir Carnot motoru değildir; radyasyonu yalnızca çok küçük bir katı açıdan emer (güneşin diski Dünya'dan görüldüğü gibi yalnızca 0,00068 steradiye karşılık gelir), üzerindeki gökyüzünün tam 2π steradyanına yeniden yayar. Katı açılardaki bu asimetri entropi cezası yaratır. Daha alakalı bir termodinamik sınır olan Landsberg limiti, spektral uyumsuzluğu hesaba katmadan önce bile tek bağlantı verimliliğini yaklaşık %93,3 ile sınırlandırır.

### 5. Spektrum Uyumsuzluğu Laneti

1 ve 2 numaralı kayıpların birleşiminin temel nedeni: Güneş spektrumu geniştir, ancak herhangi bir bant aralığı tek bir sayıdır. Bir kovayla gökkuşağını yakalamaya çalışıyorsun. AM1.5G spektrumu yaklaşık 280 nm'den (4,4 eV) 2.500 nm'ye (0,5 eV) kadar uzanır; bu, foton enerjisinde neredeyse on yıl kadardır. Hiçbir bant aralığı tek başına bu aralığın tamamını verimli bir şekilde dönüştüremez. 1,34 eV'deki optimal bant aralığı bir uzlaşmadır: tatlı noktayı bulmak için iletim kayıplarını (dar bant aralığını destekleyen) termalizasyon kayıplarına (geniş bant aralığını destekleyen) dengeler.

Beş hırsızın hepsini bir araya getirdiğinizde, 1,34 eV bant aralığına sahip mükemmel bir tek bağlantılı hücre, güneş ışığının yaklaşık %33,7'sini elektriğe dönüştürür. Geriye kalan %66,3 ise ısıya, yeniden yayılan fotonlara veya iletilen kızılötesine dönüşür. Bu çözülmesi gereken bir mühendislik problemi değil. Bu, saygı duyulması veya atlatılması gereken fiziksel bir yasadır.

## Sınırı Aşmak: Yasal Boşluklar

Shockley-Queisser limiti belirli varsayımlara dayanmaktadır. Bu varsayımlara meydan okuduğunuzda daha yüksek verimliliğin kapılarını açmış olursunuz. Burada en umut verici yaklaşımlar kabaca teknolojik olgunluğa göre sıralanmıştır.

### Boşluk 1: Birden Fazla Bant Boşluğu Kullanın (Çoklu Bağlantı)

Bunu dün ele aldık, ancak SQ terimlerle çerçevelemeye değer. %33,7 sınırı *bir* bant aralığını varsayar. İki kavşak teorik tavanı %42'ye yükseltir. Üçü sizi %49'a çıkarır. Herhangi bir güneş enerjisi cihazı için mevcut dünya rekoru (Fraunhofer Enstitüsü tarafından 2022'de dört bağlantılı bir III-V hücre kullanılarak belirlenen %47,6 konsantrasyon altında) bu boşluğun doğrudan bir ürünüdür. Her ilave bağlantı, spektrumu daha ince bir şekilde dilimleyerek hem iletimi hem de termalizasyonu azaltır. Yoğun güneş ışığı altında sonsuz kavşaklar için nihai sınır %86,8'dir.

22. Günde keşfedeceğimiz perovskit-silikon ikilisi bu fikrin ticari düzenlemesidir. Oxford PV ve LONGi, iki kavşaklı tandemlerle %33,9'u aştı; bu, ticari olarak ilgili materyallerin kullanıldığı tek kavşaklı SQ sınırının gerçek dünyadaki ilk ihlalidir.

### Boşluk 2: Güneş Işığını Yoğunlaştırın

%33,7'lik SQ sınırı tek güneş ışığının aydınlatıldığını varsayar. Ancak güneş ışığını mercekler veya aynalar kullanarak küçük bir hücreye odaklarsanız ilginç bir şey olur: Akım konsantrasyonla orantılı olarak artar, ancak voltaj *logaritmik olarak* artar. 1000 güneş konsantrasyonunda, tek bir kavşak için teorik sınır yaklaşık %40,7'ye yükselir. Neden? Işığın yoğunlaştırılması, fotonların geldiği katı açının arttırılmasına eşdeğerdir ve yukarıda tartıştığımız entropi cezasını azaltır. Gelen ışığı dağınık bir parıltıdan ziyade lazer ışınına daha "düzenli" hale getiriyorsunuz.

Güneş ışığını 500-1.000 kat küçük III-V çoklu bağlantı hücrelerine odaklamak için Fresnel mercekleri kullanan konsantre fotovoltaik (CPV) sistemler, uygulamada %46'nın üzerinde verimliliğe ulaştı. Ancak ticari olarak zorluk yaşıyorlar çünkü doğrudan normal ışınım (bulutların altında işe yaramaz), hassas iki eksenli izleme ve aktif soğutmaya ihtiyaç duyuyorlar. Düz plaka silikonun düşen maliyeti, CPV'yi çoğu karasal uygulama için ekonomik olmaktan çıkardı, ancak uzay ve bazı çöl kurulumları için geçerli olmaya devam ediyor.

### Kaçak Deliği 3: Sıcak Taşıyıcıları Soğumadan Hasat Edin

İşte radikal bir fikir: Ya elektronları termalleşmeden *önce* çıkarabilseydiniz? Unutmayın, 3,0 eV'lik bir foton tarafından üretilen bir sıcak taşıyıcı, silikon bant aralığının üzerinde 1,88 eV'lik fazla kinetik enerjiyle başlar. Eğer bu elektronu ilk 100 femtosaniye içinde (enerjisini kafese aktarmadan önce) hücrenin dışına fırlatabilseydiniz, normalde ısıya dönüşen enerjiyi yakalardınız.

Sıcak taşıyıcı güneş pilleri teorik olarak tek güneş aydınlatması altında %66 verime ulaşma kapasitesine sahiptir. Sorun çok acımasız: Taşıyıcının soğumasının yavaş olduğu (normal pikosaniye altı yerine yüzlerce pikosaniye) bir malzemeye ihtiyacınız var ve kuantum mekanik bir turnike gibi taşıyıcıları yalnızca belirli enerjilerde çıkaran enerji seçici temaslara ihtiyacınız var. UNSW Sidney ve Oklahoma Üniversitesi'ndeki araştırma grupları, indiyum nitrür ve hafniyum nitrür nanoyapılarında taşıyıcı soğutmanın yavaşladığını ve soğutma sürelerinin 5-10 pikosaniyeye kadar uzatıldığını gösterdi. Bu hala pratik çıkarım için çok hızlı, ancak toplu silikondan 10 kat daha yavaş, bu da fiziğin işe yaradığını kanıtlıyor.

### Boşluk 4: Taşıyıcıları Çarpın (MEG / Tekli Bölünme)

Çoklu Eksiton Üretiminde (MEG), tek bir yüksek enerjili foton, bir yerine *iki veya daha fazla* elektron deliği çifti üretir. Toplu silikonda bu aslında asla gerçekleşmez; küçük bir şansa sahip olmak için en az 3,4 eV'lik (bant aralığının üç katı) bir fotona ihtiyacınız vardır. Ancak kuantum noktalarında (sadece 2-10 nm çapında yarı iletken nanokristaller) kuantum sınırlaması kuralları değiştiriyor. 2004 yılında Los Alamos Ulusal Laboratuarı'ndaki araştırmacılar kurşun selenit (PbSe) kuantum noktalarında MEG olduğunu gösterdiler ve tek bir fotondan yediye kadar eksiton ürettiler.

MEG'ın organik kimya versiyonuna tekli fisyon denir: bir yüksek enerjili "tekli" uyarılmış durum, bitişik moleküller üzerinde iki düşük enerjili "üçlü" duruma bölünür. Pentasen ve tetrasen, fisyon verimlilikleri %200'e yaklaşan şampiyon tekli fisyon malzemeleridir (bu, soğurulan her fotonun iki üçlü eksiton ürettiği anlamına gelir). MIT adresindeki bir grup, belirli dalga boylarında %100'ün üzerinde harici kuantum verimliliği üreten bir silikon hücreye bağlı tekli bir fisyon katmanı gösterdi; dışarı çıkan elektron, içeri giren fotonlardan daha fazla. Tekli fisyonla güçlendirilmiş bir silikon hücrenin teorik verimlilik tavanı yaklaşık %45'tir.

### Boşluk 5: Foton Yukarı Dönüştürme ve Aşağı Dönüştürme

Hücreyi değiştiremiyorsanız ışığı değiştirin. Aşağı dönüşüm, bir yüksek enerjili fotonu alır ve onu, hücrenin daha verimli bir şekilde absorbe edebileceği iki düşük enerjili fotona böler (termalizasyonu azaltır). Yukarı dönüşüm, hücrenin normalde kaçıracağı iki alt bant aralığı fotonunu alır ve bunları bant aralığı üstü bir fotonda birleştirir (iletim kayıplarını azaltır).

Erbiyum katkılı malzemeler (NaYF₄:Er³⁺ gibi) kullanılarak yapılan üst dönüşümün, silikon tarafından tamamen görülmeyen 1.500 nm kızılötesi fotonları, silikonun kolayca emdiği 980 nm fotonlara dönüştürdüğü gösterilmiştir. Ancak mevcut yukarı dönüştürücüler son derece verimsiz: yoğunlaştırılmış aydınlatma altında yaklaşık %5-10 dönüşüm verimliliği, tek güneş koşullarında %1'in altına düşüyor. Süreç, iki fotonun aynı iyon tarafından sırayla emilmesini gerektiriyor ve normal güneş yoğunluklarında bunun gerçekleşme şansı çok düşük. Teorik modelleme, üst dönüşümle geliştirilmiş bir silikon hücrenin %40,2'ye ulaşabileceğini öne sürüyor, ancak pratik cihazlar şu ana kadar %1'den daha az mutlak verimlilik ekledi.

### Boşluk 6: Termofotovoltaikler — Işık Kaynağını Yeniden Tanımlayın

Güneş ışığını doğrudan kullanmak yerine, bir ara soğurucuyu 1.000-2.000°C'ye ısıtıp ardından bu parlayan gövdeden *termal radyasyonu* toplasaydınız ne olurdu? Bu termofotovoltaiktir (TPV). Avantajı: örneğin 1.900°C'de ısıtılmış bir yayıcı, güneşten daha dar, kırmızıya daha fazla kayan bir spektrum üretir ve bu, tek bir bant aralığıyla daha iyi eşleştirilebilir. Ayrıca, alt bant aralığı fotonlarını hücrenin arkasında bir ayna kullanarak yayıcıya geri yansıtarak geri dönüştürebilirsiniz.

2022'de MIT'daki bir ekip, %41,1 ısı-elektrik verimliliğine sahip bir TPV sistemini gösterdi; bu sistem, termal enerjiyi (2.400°C'de) herhangi bir tek bağlantılı güneş hücresinin güneş ışığını dönüştürmesinden daha verimli bir şekilde dönüştürüyor. Hücre, alt bant aralığı fotonlarını grafit yayıcıya geri gönderen altın renkli bir arka reflektöre sahip III-V yarı iletkenlerden yapılmıştır. Bu artık teknik olarak "güneş enerjisi" değil - fotovoltaik çalışma sıvısına sahip bir ısı motoru - ancak foton spektrumunun yeniden şekillendirilmesinin verimliliğin kilidini nasıl açtığını gösteriyor.

## Mantıksız Gerçek: Kayıt Hücreleri Zaten Yakın

İnsanları sıklıkla şaşırtan şey şu: En iyi laboratuvar güneş pilleri SQ sınırının çok altında kalmıyor. Buna *dikkat çekici derecede yakınlar*. Tek bağlantılı silikon hücre için mevcut dünya rekoru, heteroeklemli arka kontak mimarisi kullanılarak belirlenen %26,81'dir (LONGi, 2024). Silikon için SQ sınırı %29,4'tür. Bu, en iyi silikon hücrenin **teorik maksimum değerinin %91,2'sini** yakaladığı anlamına gelir. Geri kalan %8,8, Auger rekombinasyonu (Shockley ve Queisser'in hesaba katmadığı silikondaki içsel bir kayıp mekanizması), kontaklardaki dirençli kayıplar ve küçük optik kayıplar arasında bölünmüştür.

Galyum arsenit daha da iyisini yapar. Alta Devices (artık Hanwha'nın bir parçası) %29,1 ile tek bağlantı rekorunu elinde tutuyor; bu, GaAs'ın %33,2'lik SQ sınırının** %87,6'sına denk geliyor. Bu hücreler, araştırmacıların "derin verimlilik" rejimi olarak adlandırdığı, kalan her yüzde 0,1'lik iyileşmenin yeni bir doktora tezi gerektirdiği şekilde çalışıyor.

Temel sınıra olan bu yakınlık hem zafer hem de tuzaktır. Bu, geleneksel silikon hücre mühendisliğinin sonuna yaklaştığı anlamına geliyor. Silikonun verimliliğini ikiye katlayamazsınız. %5'lik mutlak değeri bile ekleyemezsiniz. %30'dan fazla güneş enerjisine giden yol ve önemli ölçüde daha ucuz elektriğe giden yol, SQ sınırından *geçmelidir*, onun kenarlarından değil. Tandem hücreler, perovskitler ve bugün tartıştığımız egzotik kavramların bu kadar önemli olmasının nedeni budur. Bunlar artımlı iyileştirmeler değil. Termodinamik bir hapishaneden kaçıyorlar.

## Pratik Verimlilik Hiyerarşisi

Gerçek cihazların bu sınırlara göre nerede bulunduğunu haritalandırmaya değer:

| Teknoloji | SQ / Teorik Sınır | Laboratuvar Kaydı | Ticari Modül |
|---|---|---|---|
| Silikon (tek bağlantı) | %29,4 | %26,81 | %23-24 |
| GaAs (tek bağlantı) | %33,2 | %29,1 | ~%28 (boşluk) |
| Perovskit (tek bağlantı) | ~%31 | %26,7 | ~%20 (erken) |
| CdTe (ince film) | ~%32 | %22,3 | %19-20 |
| Perovskit/Si tandem | ~%45 | %34,6 | ~%27 (pilot) |
| III-V üçlü bağlantı (kons.) | ~%49 | %47,6 | %38-40 (CPV) |

Laboratuvar kayıtları ile ticari modüller arasındaki boşluğa dikkat edin; genellikle %3-6 mutlak. Bu "üretim açığı" seri üretimin gerçeklerinden kaynaklanmaktadır: hafif saf olmayan malzemeler, ideal olmayan doku, temas direnci, kapsülleme ve kablolama nedeniyle hücreden modüle kayıplar. Bu açığı kapatmak, kalite kontrol ve hücre testlerini inceleyeceğimiz 13. Günün konusudur.

## Bu Sonraki Her Gün İçin Neden Önemli?

SQ sınırı yalnızca akademik bir merak değildir. Her güneş hücresi yeniliğinin değerlendirilmesi gereken mercek budur. Birisi yeni bir malzemenin %15 verimliliğe ulaştığını iddia ettiğinde ilk soru şudur: o malzemenin bant aralığı için SQ sınırı nedir? Limit %30 ise ve bunlar %15'teyse, iyileştirme için çok fazla alan vardır. Sınır %18 ise zaten derin verimlilik rejimindedirler ve kazanımlar artacaktır.

Yarın, üretim hattından çıkan bir hücrenin tasarımının vaat ettiği verimliliği gerçekten yakalayıp yakalayamayacağını belirleyen araçlar ve teknikler olan **kalite kontrol ve hücre testi** ile teoriden pratiğe geçeceğiz. Elektrolüminesans görüntülemenin görünmez kusurları nasıl tespit edebildiğini, IV eğrilerinin bir hücrenin elektriksel kişiliğini nasıl ortaya çıkardığını ve tek bir sıcak noktanın neden bütün bir modülü yangın tehlikesine dönüştürebildiğini göreceğiz. Teori tavanı belirliyor; kalite kontrol aslında ne kadar yaklaşacağınızı belirler.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-12.toml}}
