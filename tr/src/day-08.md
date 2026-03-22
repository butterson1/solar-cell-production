# 8. Gün: Serigrafi ve Metalizasyon — Güneşi Kablolamak

*Güneş piliniz neredeyse hazır. Yedi günlük saflaştırma, kristal büyütme, dilimleme, katkılama ve kaplamanın ardından, gelen güneş ışığının %97'sini emebilen ve elektronları deliklerden acımasız bir verimlilikle ayırabilen bir levhaya sahip olursunuz. Tek bir sorun var: Serbest kalan elektronların gidecek hiçbir yeri yok. Akımı toplayacak ve dış dünyaya yönlendirecek metal temas noktaları olmadığında, güzel bir şekilde tasarlanmış fotovoltaik cihazınız, sıcak, koyu mavi bir silikon levhadan başka bir şey değildir. Bugün bunu kablolarla bağlıyoruz ve endüstrinin seçtiği yöntem büyük ihtimalle tişört baskısından ödünç alınan bir teknik.*

---

## 5 Milyar Dolarlık Darboğaz

Metalleşme, fiziğin ekonomiyle mümkün olan en rahatsız edici şekilde buluştuğu yerdir. Bir güneş hücresinin ön tarafındaki temas noktalarının birbiriyle çelişen iki talebi karşılaması gerekir: elektriksel olarak mükemmel olmalı (düşük direnç, silikonla yakın temas) ve fiziksel olarak görünmez olmalı (gelen ışığı engellemeyen ince, dar çizgiler). Ön yüzeydeki her milimetrekare metal, elektrik üretemeyen bir milimetre karedir. Endüstri buna "gölgeleme kaybı" diyor ve bu genellikle hücre alanının %2-4'ü kadardır.

Bu iğneye iplik geçiren malzeme gümüştür; özellikle kilogram başına maliyeti yaklaşık 800 ila 1.200 ABD Doları olan ve toplam hücre üretim maliyetinin kabaca %10 ila 15'ini temsil eden özel bir gümüş macunudur. 2024 yılında fotovoltaik endüstrisi 7.000 metrik tonun üzerinde gümüş tüketerek elektronik, fotoğrafçılık ve mücevherat sektörlerinin toplamından önde, dünyadaki en büyük metal endüstriyel tüketicisi haline geldi. Yaklaşık ons ​​başına 1.000 dolar (2025 sonları itibarıyla), bu, yıllık gümüş macunu maliyetinin 5 milyar doların kuzeyinde olduğu anlamına geliyor. *Neden* gümüş ve *neden* serigrafi baskıyı ve endüstrinin nasıl umutsuzca her ikisinden de daha azını kullanmaya çalıştığını anlamak, bugünün dersinin hikayesidir.

---

## Gümüş Macunun Anatomisi

Gümüş macunu sadece tutkalla karıştırılmış gümüş tozu değildir. Hassas bir şekilde tasarlanmış üç bileşenli bir sistemdir ve her bileşen, baskıyı takip eden pişirme işlemi sırasında belirli bir şey yapar.

**Gümüş parçacıklar (ağırlıkça %65–85):** Mikron ölçekli gümüş tozu, genellikle 1–5 μm çapında, bazen gümüş nanopartiküllerle (20–100 nm) harmanlanır. Parçacık boyutu dağılımı son derece önemlidir; çok tekdüze olduğundan macun yoğun bir şekilde toplanmayacaktır; çok çeşitlidir ve yazdırılan çizgiler kabalaşır. Gümüş, bitmiş kontağın elektriksel iletkenliğini sağlar. Gümüşün 1,59 × 10⁻⁸ Ω·m'lik toplu direnci tüm elementler arasında en düşük olanıdır, tam da bu yüzden endüstri onu kolayca ikame edemez. Bakır (1,68 × 10⁻⁸ Ω·m) buna yaklaşıyor ancak kendi sorunları var; buna da değineceğiz.

**Cam hamuru (ağırlıkça %2-10):** Bu gizli silahtır. Cam hamuru, dikkatlice ayarlanmış bir erime noktasına sahip, ince öğütülmüş bir kurşun-borosilikat camdır (tipik olarak PbO-B₂O₃-SiO₂, ancak kurşunsuz formülasyonlar ortaya çıkmaktadır). Pişirme sırasında, cam malzemesi dikkate değer bir şey yapar: Dün çok dikkatli bir şekilde yerleştirdiğiniz silikon nitrür yansıma önleyici kaplamayı *aşındırır*. Camdaki kurşun oksit (PbO), 500–650°C'de SiNₓ ile reaksiyona girer, onu çözer ve altındaki çıplak silikon yayıcıyı açığa çıkarır. Bu kimyasal saldırı olmasaydı gümüş, yarı iletkenle hiçbir elektrik bağlantısı olmadan ARC'nin üzerinde dururdu. Cam malzemeyi yalnızca yüksek sıcaklıkta, tam da ihtiyaç duyduğunuz anda etkinleşen bir asit olarak düşünün.

**Organik araç (ağırlıkça %15-30):** Çözücüler (terpineol, teksanol), polimerik bağlayıcılar (etil selüloz) ve reoloji değiştiricilerden (tiksotropik maddeler) oluşan bir karışım. Bu kokteyl, macuna basılabilirliğini kazandırır; baskıdan sonra şeklini koruyacak kadar kalın olması gerekir (istirahatte 200-400 Pa.s viskozite), ancak silecek basıncı altında elek açıklıklarından akacak kadar ince (kesme altında 20-50 Pa.s'ye düşer). Bu Newton olmayan davranış (kayma incelmesi) serigrafi baskının işe yaramasını sağlayan şeydir. Organik bileşenler pişirme sırasında tamamen yanar ve geride yalnızca gümüş ve cam kalır.

Büyük macun üreticileri - Heraeus, DuPont (şu anda Dupont de Nemours'un bir parçası), Samsung SDI, Giga Solar ve Suzhou Jingyin gibi birkaç Çinli firma - formülasyonlarını devlet sırrı gibi koruyor. Tam cam hamuru bileşimi, parçacık boyutu dağılımları ve organik kimyalar onlarca yıllık optimizasyonu temsil eder. Frit bileşimindeki %1'lik bir fark, hücre verimliliğinde %0,3'lük bir salınım anlamına gelebilir; bu da gigawatt'lık bir fabrikada milyonlarca dolara karşılık gelir.

---

## Baskı Süreci: Üç Geçiş, Üç Yapıştırma

Standart bir güneş hücresi, genellikle sırayla düzenlenmiş üç ayrı ekranlı yazıcıda üç kez yazdırılır. Metalizasyon hattının tamamı saatte 4.000-6.000 levha (saniyede kabaca bir levha) hızında çalışıyor.

### Geçiş 1: Arka Taraf Gümüş (Baralar/Pad'ler)

Gofret ters çevrilir ve arkasına ince gümüş şeritler veya pedler basılır. Bunlar doğrudan akımı toplamak için değil; bakır şeridin daha sonra bir modüldeki bir hücreyi diğerine bağlayacağı lehimleme noktalarıdır. 12–16 baralı modern çoklu bara (MBB) tasarımında bunlar yalnızca birkaç miligram gümüş kullanan, belki de 0,5 mm genişliğinde küçük pedlerdir.

### Geçiş 2: Arka Taraf Alüminyum (Tam Alan)

Alan açısından en büyüğü bu. Hücrenin arka yüzeyinin neredeyse tamamına alüminyum bir macun basılmıştır. Alüminyum ucuzdur (macun maliyeti yaklaşık 30-50 $/kg'a karşılık gümüş için 800 $'ın üzerindedir), bu nedenle sırtın tamamını kaplamak bir maliyet sorunu değildir. Pişirme sırasında, alüminyum alaşımları 577°C ötektik sıcaklıkta silikonla birleşerek yaklaşık 5–10 μm derinliğinde p⁺ katkılı bir "arka yüzey alanı" (BSF) oluşturur. Bu BSF bir elektron aynası görevi görür; arka yüzeye doğru dolaşan azınlık taşıyıcıları (p tipi hücredeki elektronlar), akıma katkıda bulunabilecekleri yığının içine geri itilir. BSF olmasaydı, arka yüzey rekombinasyonu mutlak verimliliğin kabaca %2-3'ünü tüketirdi.

### Geçiş 3: Ön Taraf Gümüş (Parmaklar ve Baralar)

Burası sanatın yaşadığı yer. Ön tarafta kritik ince çizgili bir şebeke bulunur: hücre boyunca uzanan, akımı toplayan ve onu kenarlara yönlendiren dikey "baralar" ile birbirine bağlanan ince paralel "parmaklar". Bu desen, bitmiş bir güneş hücresinin en görünür özelliğidir; güneş paneline yakından baktığınızda gördüğünüz paralel çizgiler.

---

## Ekran Yazıcısının İçinde

Makine kavramsal olarak basit, mekanik olarak hassas ve aldatıcı derecede hızlıdır. Her bir levhanın yazıcıda geçirdiği yaklaşık 1,5 saniye içinde şunlar gerçekleşir:

**Ekran (veya şablon)**, alüminyum bir çerçeve üzerine gergin bir şekilde gerilmiş, 16-20 μm tel çapına sahip, genellikle inç başına 360 satırdan oluşan ince bir paslanmaz çelik ağdır. Ağ, ışığa duyarlı bir emülsiyonla kaplandı, bir maske aracılığıyla UV ışığa maruz bırakıldı ve geliştirildi; tıpkı rock grubu tişörtlerini basmak için kullanılan işlem gibi, toleranslar milimetre yerine mikron cinsinden ölçüldü. Ortaya çıkan ekranda yalnızca gümüş olmasını istediğiniz yerde açıklıklar bulunur: parmaklar, baralar ve pedler. Modern parmak açıklıkları 20–30 μm genişliğindedir, ancak basılı çizgi, macun hafifçe aktıktan sonra 25–40 μm'ye yayılır.

En yüksek çözünürlüklü baskı için çoğu fabrika **şablonlara** geçiş yaptı: lazerle kesilmiş veya elektrikle şekillendirilmiş açıklıklara sahip sert metal folyolar (25–30 μm kalınlığında). Şablonlar örgü eleklerden daha keskin kenarlar üretir çünkü macun akımını bozacak ağ eklemleri olmadığından parmak genişliklerinin 20 μm'nin altında olmasını sağlar.

**Poliüretandan veya giderek paslanmaz çelikten yapılmış bir bıçak olan silecek**, elek boyunca 200-400 mm/sn hızla hareket ederek macunu açıklıklardan alttaki levhaya zorlar. Silecek basıncı, hızı ve açısı kritik öneme sahiptir. Çok fazla baskı uygulandığında macun bulaşır; çok az ve açıklıkları tam olarak doldurmuyor. Kopma mesafesi (ekran ile plaka arasındaki boşluk, genellikle 1-2 mm) ekranın baskılı hamurdan ne kadar temiz ayrıldığını belirler. Silecek geçerken, elek levhaya temas etmek için aşağı doğru eğilir, ardından geri yaylanarak ıslak macundan sıyrılır ve arkasında temiz çizgiler bırakır.

**Hizalama** kritik öneme sahiptir çünkü ön taraftaki parmakların emitöre tam olarak inmesi gerekir ve sonuçta, çok adımlı işlemlerde farklı yazdırma geçişlerinin ±10 μm doğrulukla üst üste binmesi gerekir. Modern yazıcılar bunu başarmak için levha üzerinde referans işaretleri bulunan makine görüşünü kullanır.

Yükleme, hizalama, yazdırma, boşaltma gibi tüm döngü, ekipmana bağlı olarak levha başına yaklaşık 1,2-1,8 saniye sürer. Önde gelen ekipman üreticileri arasında ASMPT (eski adıyla ASM Pacific Technology), Baccini (artık Applied Materials'ın bir parçası) ve Maxwell yer alıyor.

---

## Pişirim Fırını: Kimyanın Olduğu Yer

Yazdırma yalnızca yüzeyde macun biriktirir. Sihir, **ateşleme fırınında** gerçekleşir; 6-10 metre uzunluğunda, sürekli bir kızılötesi bant fırını olup, içinden levhalar bir örgü bant üzerinde kontrollü bir hızda toplamda yaklaşık 30-60 saniye boyunca hareket eder.

Sıcaklık profili dikkatlice koreografisi yapılmış bir danstır:

**Artış (200–400°C, ~15 saniye):** Organik solventler ve bağlayıcılar yanar. Atmosfer hava benzeri durumdan hafif oksitleyiciye doğru değişir. Eskiden kalın, ıslak bir film, gümüş parçacıkları ve cam hamurundan oluşan kuru, gözenekli bir iskelete dönüşür. Bu aşama çok hızlı ilerlerse, kaçan gazlar temasta kabarcıklar ve boşluklar oluşturur.

**Cam aktivasyonu (500–650°C, ~10 saniye):** Bu çok önemli bir penceredir. Kurşun-borosilikat cam malzemesi erir ve aşındırıcı bir sıvı haline gelir. Camdaki PbO, SiNₓ yansıma önleyici kaplamayla reaksiyona girer:

*PbO + SiNₓ → PbSiO₃ + ½N₂*

Cam, kelimenin tam anlamıyla ARC yoluyla kanalları çözerek silikon yayıcıyı açığa çıkarır. Aynı zamanda erimiş camın içinde bir miktar gümüş çözünür. Yerinde X-ışını kırınım çalışmaları (*Nature Communications* dergisinde yayınlanmıştır) bu çözünmenin yaklaşık 550°C'de başladığını göstermiştir; gümüş iyonları cam fazına girer, kazınmış kanallardan aşağıya doğru ilerler ve daha sonra doğrudan silikon yüzeyinde gümüş kristalitler halinde çöker.

**En yüksek ateşleme (750–850°C, 1–3 saniye):** Plaka inanılmaz derecede kısa bir süre için maksimum sıcaklığına ulaşır — "en yüksek ateşleme" genellikle maksimum 30°C içinde yalnızca 1-3 saniye sürer. Bu aşırı ısı parlaması sırasında, çözünmüş gümüş, camdan açıktaki silikonun üzerine küçük kristalitler (5-100 nm) halinde çökelerek yakın bir Ag-Si teması oluşturur. Arka tarafta, 577°C ötektik sıcaklıktaki silikonlu alüminyum alaşımları BSF oluşturuyor. Tepe sıcaklığı, tüm süreçteki en kritik parametredir — ±5°C, hücre verimliliğini mutlak olarak %0,1 ila %0,2 oranında değiştirebilir.

**Hızlı soğuma:** Gofret yaklaşık 10 saniyede 800°C'den 400°C'nin altına düşer. Bu söndürme, kontak yapısını yerinde dondurur ve bağlantı noktasına zarar verebilecek aşırı alaşımlamayı önler.

Fırından çıkan şey tamamlanmış bir güneş hücresidir. Yüksek sıcaklıkta bir dakikadan kısa bir sürede gümüş ARC'yi deldi, silikon emitörle ohmik temas kurdu, yoğun iletken bir hat halinde sinterlendi ve alüminyum arkada bir BSF oluşturdu. Tek termal çekimde üç sorun çözüldü; bu "ortak ateşleme" işlemi, güneş enerjisi üretimindeki en zarif adımlardan biridir.

---

## Mikroskop Altındaki Temas

Ateşlenmiş bir gümüş kontağın kesitini alıp taramalı elektron mikroskobu (SEM) altında incelerseniz, gördüğünüz şey şaşırtıcı derecede karmaşıktır. Temas basit bir metal-yarı iletken sandviçi değil. Aşağıdan yukarıya:

1. Silikon emitör yüzeyinde epitaksiyel olarak büyümüş **gümüş kristalitler** (5–100 nm)
2. **Gümüş nanopartiküller içeren ince bir cam katman** (~50–200 nm)
3. **Toplu gümüş** — iletken parmağı oluşturan sinterlenmiş parçacıklar

Akım silikondan gümüş kristalitler boyunca akar, gömülü nanopartiküller aracılığıyla ince cam katman boyunca tüneller açar ve toplu gümüş iletkene girer. Cam katman aslında parazitik bir bariyer değil, bir avantajdır; bağlantı noktasına zarar verecek olan silikonun içine aşırı gümüş difüzyonunu önler. İyi ateşlenen bir ön kontağın spesifik kontak direnci tipik olarak 1–5 mΩ·cm²'dir ve önemli bir direnç kaybı olmadan akımı çekmeye yetecek kadar düşüktür.

---

## Geometri Savaşı: Parmaklar, Baralar ve Gölgeleme Dengesi

Metalizasyon modeli klasik bir mühendislik optimizasyon problemidir. Her parmak, her iki tarafındaki silikondan akım topluyor ve elektronları yayıcıdan yanal olarak metal kontağa yönlendiriyor. Daha geniş parmaklar daha düşük dirence sahiptir ancak daha fazla alanı gölgeler. Daha dar parmaklar daha az ışık harcar ancak daha fazla direnç gösterir. Optimum tasarım üç kaybı dengeler:

- **Gölgeleme kaybı** (parmak genişliği × parmak sayısıyla orantılı)
- **Parmak direnci kaybı** (parmak genişliği ve yüksekliği ile ters orantılı)
- **Verici levha direnç kaybı** (parmak aralığının karesiyle orantılı)

2015 yılında tipik bir PERC hücresinde 5 bara ve 50 μm genişliğinde ~100 parmak vardı ve hücrenin yaklaşık %3,5'ini gölgeliyordu. 2025 yılına gelindiğinde endüstri, 12–16 yuvarlak telli baralara (veya barasız SmartWire teknolojisine), 25–30 μm genişliğinde 140'tan fazla parmak ve %2,5'in altında gölgelendirmeye sahip çoklu bara (MBB) tasarımlarına geçti. Tek başına bu evrim kabaca %0,5'lik mutlak verimlilik artışına katkıda bulunmuştur; bu, daha iyi baskı ve daha akıllı geometriden başka hiçbir şeyden elde edilmeyen yarım puanlık bir puandır.

Daha fazla baraya yönelik eğilim aynı zamanda bir elektronun baraya ulaşmadan önce parmak boyunca kat ettiği ortalama mesafeyi de azaltarak I²R kayıplarını azaltır. Mantıksal uç nokta (yüzlerce ince kablonun doğrudan parmaklara bağlandığı sıfır baralar) SmartWire Bağlantı Teknolojisini (SWCT) kullanan Meyer Burger gibi şirketlerde zaten üretimde.

---

## Gümüş Sorunu: Çok Pahalı, Çok Kıt

İşte, güneş enerjisi yöneticilerinin geceleri uyanık kalmasına neden olan mantığa aykırı gerçek: **gümüş, güneş enerjisinin küresel iklim hedeflerine ulaşacak şekilde ölçeklenmesini engelleyen bir darboğaz olabilir.**

2024 yılında bir TOPCon hücresi watt başına yaklaşık 90-95 mg gümüş tüketiyordu (ön ve arka kombine). Sektör o yıl yaklaşık 500 GW güneş enerjisi kurulumu yaptı. Bu yükleme sırasında PV yaklaşık 7.000 tondan fazla gümüş tüketiyordu; bu da toplam küresel gümüş madeni üretiminin yaklaşık %20'sine tekabül ediyordu (~26.000 ton/yıl). Dünyanın iklim hedeflerini tutturmak için 2030 yılına kadar yılda 1,5–2 TW kurması gerekiyorsa ve gümüş yüklemeleri önemli ölçüde düşmezse, tek başına PV talebi toplam gümüş madeni arzını aşabilir.

Sektör buna birçok açıdan saldırıyor:

**Daha ince, daha dar çizgiler:** Gümüş tüketimi 2010'da ~200 mg/W'tan TOPCon için 2025 ortası itibarıyla ~80–85 mg/W'a düştü; bu neredeyse tamamen daha ince baskıdan kaynaklanan %60'ın üzerinde bir azalma. TW-ölçek dağıtımı için 5 mg/W hedefine ulaşmak için 15 μm'nin altında parmak genişliği gerekecektir.

**Bakır değişimi:** Bakır, kilogram başına gümüşün yaklaşık 1/100'ü kadardır ve 100 kat daha fazladır. Ancak bakırın yıkıcı bir kusuru var: Oda sıcaklığında hızla silikonun içine yayılarak hücre verimliliğini azaltan rekombinasyon merkezleri yaratıyor. Herhangi bir bakır metalizasyon şeması, bakır ve silikon arasında bir difüzyon bariyerine (tipik olarak nikel veya tungsten) ihtiyaç duyar. Heteroeklem hücreleri (HJT) bakır metalizasyonu için en iyi adaylardır çünkü amorf silikon katmanları doğal difüzyon bariyerleri görevi görür. Fraunhofer ISE, 2025'te serigrafi baskılı bakır macunlu HJT hücrelerin gümüş bazlı referanslara göre yalnızca %0,13 daha düşük verimlilik elde ettiğini gösterdi.

**Gümüş-bakır alaşımları ve yalın-gümüş macunları:** Gümüş içeriğini %30-50 oranında azaltırken, ateşleme mekanizmasını koruyarak, macunun içindeki gümüşün bakırla kısmi ikamesi.

**Kaplama:** Serigrafi baskıyı tamamen atlayarak bakırın doğrudan hücre üzerine elektrokaplanması. Bu, daha iyi iletkenliğe sahip daha dar çizgiler (5-10 μm mümkün) üretir, ancak ek işlem adımları (tohum katmanı biriktirme, maskeleme, kaplama, kapatma) gerektirir ve kimyasal atık üretir.

---

## Bu Adım Neden Önemli?

Metalleşme, hücrenin bir cihaza dönüştüğü yerdir. Yazdırmadan önce ışığa duyarlı bir yarı iletkeniniz var. Yazdırdıktan ve ateşledikten sonra, bir kabloya bağlayıp güç alabileceğiniz bir şeye sahip olursunuz. Aynı zamanda hücreye en büyük malzeme maliyetinin girdiği yer burasıdır; gümüş macunu, TOPCon ve HJT hücreleri için malzeme listesine hakimdir.

Serigrafi baskı tekniğinin kendisi konsept olarak neredeyse saçma derecede basittir: macunu desenli bir elek boyunca lastik bir bıçakla itin. TW-ölçekli üretim için gereken hızlarda, toleranslarda ve hacimlerde (saniyede bir levha, 25 μm çizgi genişliği, yılda milyarlarca hücre) çalışması, onlarca yıllık artımlı mühendisliğin bir kanıtıdır. Pek çok kişi denemiş olsa da (mürekkep püskürtmeli, aerosol püskürtmeli, lazer transfer, fleksografik baskı) hiçbir rakip teknoloji onun yerini almayı başaramadı. Serigrafi baskı dayanıklıdır çünkü hızlıdır, güvenilirdir ve eş zamanlı olarak ön ve arka kontakları oluşturan ve hidrojen pasifleştirmesini tek bir fırın geçişinde tamamlayan ortak ateşleme süreciyle uyumludur.

Yarın, metalleştirme adımından uzaklaşıp büyük resme bakacağız: **hücre mimarileri**. Bu hafta inşa ettiğiniz klasik alüminyum-BSF hücrenin yerini şimdiden PERC, TOPCon ve HJT — arka yüzeyden temas yapısına kadar her şeyi yeniden düşünen tasarımlar alıyor. Her mimari farklı macunlar, farklı baskı desenleri ve farklı pişirme profilleri gerektirir. Özellikle gümüş sorunu aralarında büyük farklılıklar gösteriyor ve bu fark sektörü yeniden şekillendiriyor.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-08.toml}}
