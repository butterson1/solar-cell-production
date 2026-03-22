# 22. Gün: Tandem Hücreler - Silikon + Perovskit İstifleme

*4. Hafta, Ders 2 – Sınır ve Gelecek*

---

Dün, mürekkep gibi basılabilen, ışığı kara delik gibi soğuran ve silikon mühendislerinin yalnızca hayal edebileceği ayarlanabilir bant aralığına sahip yeni gelen perovskit ile tanıştık. Aynı zamanda onun şeytanlarıyla da karşılaştık: nem hassasiyeti, kurşun zehirliliği ve onlarca yıl yerine aylarla ölçülen çalışma ömrü. Yaklaşık 2018'den bu yana tüm fotovoltaik sektörünü yönlendiren soru şu: **ya seçim yapmak zorunda kalmazsanız?**

Perovskit'ten silikonu değiştirmesini istemek yerine onu *en üste* koysanız ne olur?

Bu tandem hücredir ve bu bir uzlaşma değildir. Shockley-Queisser sınırında aynı anda iki yönden bir pusu. LONGi, Nisan 2025'te perovskit-silikon tandemini %34,85 verimlilikle sertifikalandırarak tek bağlantılı silikonun asla dokunamayacağı bir engeli yıktı. Brandenburg an der Havel, Almanya'da dönüştürülmüş bir ince film fabrikasından faaliyet gösteren Oxford PV, kamu hizmeti ölçeğindeki müşterilere halihazırda ticari tandem modülleri sevk etti. Bu artık laboratuvar fantezisi değil. Bu bir üründür.

Her şeyi parçalara ayıralım ve neden iki kusurlu hücrenin istiflenmesinin, her ikisinin de tek başına olmasından daha iyi bir şey yarattığını anlayalım.

## Temel Sorun: Bir Bant Boşluğu Yeterli Değil

Shockley-Queisser limitinin acımasız matematiğini 12. Günden hatırlayın. 1,12 eV (silikon) bant aralığına sahip tek bağlantılı bir hücre teorik olarak gelen güneş ışığının yaklaşık %33'ünü elektriğe dönüştürebilir. Bant aralığı enerjisinin altındaki her şey doğrudan geçer; bu kızılötesi fotonlar silikon tarafından görülmez. Bant aralığının çok üzerindeki her şey emilir, ancak 1,12 eV'nin üzerindeki fazla enerji, termalizasyon adı verilen bir işlem yoluyla ısı olarak atılır. 3,0 eV'deki mavi bir foton bir elektronu uyarır, ancak bu elektron hemen iletim bandının kenarına doğru gevşer ve 1,88 eV'lik boşa harcanan ısıyı kristal kafese yayar.

Standart güneş ışığı altında bir silikon hücrenin acımasız açıklaması şu şekildedir: Güneş spektrumundaki enerjinin yaklaşık **%20'si** kaybolur çünkü fotonların emilemeyecek kadar az enerjisi vardır. **%30** daha termalizasyon nedeniyle kaybedilir; emilen ancak silikonun kullanabileceğinden daha fazla enerji taşıyan fotonlar. Geriye kalan kayıplar rekombinasyon, direnç ve yansımadan kaynaklanmaktadır. Teorik tavan ~%33'tür. En iyi laboratuvar silikon hücreleri %26,8'e ulaştı. Ticari paneller ise %22-24 civarında seyrediyor.

Tandem hücre aynı anda en büyük iki kayıp kanalına saldırır. Yüksek enerjili fotonları (mavi, mor, UV) termalleşmeden önce yakalamak için üstüne geniş bant aralıklı bir hücre yerleştirin. İletilen düşük enerjili fotonların (kırmızı, kızılötesi) alttaki, onları gerçekten kullanabilen dar bant aralıklı bir hücreye geçmesine izin verin. İki hücre, iki bant aralığı, güneş spektrumunda iki ısırık. Konsantre olmayan güneş ışığı altında optimize edilmiş iki kavşaklı tandem için teorik sınır yaklaşık **%46**'ya sıçramaktadır; bu da tek kavşaktan neredeyse yarı yarıya daha yüksektir.

## Neden Perovskit + Silikon Rüya Eşleşmesidir

11. Günde, konsantre ışık altında %47'nin üzerinde verimliliğe ulaşan III-V yarı iletken tandemleri (galyum arsenit, indiyum fosfit ve bunların alaşımları) ele aldık. Muhteşemler. Ayrıca metrekare başına 50.000 ila 100.000 dolar arasında bir maliyete sahipler, bu yüzden yalnızca uzay aracı ve niş yoğunlaştırıcı sistemlerde yaşıyorlar. Modül metrekare başına 20 ila 50 ABD Doları tutarındaki karasal güneş enerjisi için, III-V tandemler başlangıç ​​dışıdır.

Perovskit denklemi tamamen değiştiriyor. İşte silikon-perovskit'in bu kadar doğal bir evlilik olmasının nedeni:

**Bant aralığı tamamlayıcılığı.** Silikon'un bant aralığı 1,12 eV'dir. Ayrıntılı denge hesaplamalarına göre silikon üzerinde bir tandem için en uygun üst hücre bant aralığı 1,65 ile 1,75 eV arasında bir yerdedir. Perovskitler (özellikle FA₀.₇₅Cs₀.₂₅Pb(I₀.₈Br₀.₂)₃ gibi formamidinyum-sezyum kurşun halojenür bileşimleri) yalnızca iyodür-bromür oranı ayarlanarak tam olarak bu aralığa ayarlanabilir. Başka hiçbir malzeme sistemi bu tür bant aralığı kadranını sunmuyor.

**Maliyet yapısı.** Perovskit üst hücre, mevcut bir silikon hücrenin üretim maliyetine nispeten az katkı sağlar. Aktif katman yaklaşık 400-600 nm kalınlığındadır ve çözeltiden veya birlikte buharlaştırma yoluyla biriktirilir. Tahminler, perovskit katmanları, taşıma katmanları ve rekombinasyon bağlantısı için ek maliyetin kabaca watt başına 0,02 ila 0,05 ABD Doları olduğunu ileri sürüyor; bu, halihazırda 0,10 ila 0,15 ABD Doları/W civarında bir maliyete sahip olan bir silikon hücre için mütevazı bir artış. Tandem modül verimliliğini %22'den %30'a çıkarırsa, *watt başına* maliyet gerçekten düşer çünkü tüm sabit maliyetlerinizi (cam, çerçeve, bağlantı kutusu, işçilik, nakliye) aynı alandan daha fazla watt'a yayarsınız.

**Altyapı gücü.** Dünya halihazırda yaklaşık 700 GW yıllık silikon hücre üretim kapasitesine sahiptir. Tandem stratejisi bunun yıkılmasını gerektirmez. Mevcut silikon hücre fabrikalarına bir perovskit biriktirme hattı (esasen bir kaplama adımı) eklersiniz. Bu bir yenilemedir, devrim değil. Bu nedenle her büyük silikon üreticisi (LONGi, Trina, JA Solar, Hanwha Q Cells) tandem yeteneğini geliştirmek için yarışıyor: bu, mevcut varlıkların üzerine inşa edilmiş rekabetçi bir hendek.

## İki Terminal mi, Dört mü? Mimarlık Kararı

Bir tandem hücreyi bağlamanın temelde iki farklı yolu vardır ve bu seçimin hem fizik hem de üretim açısından derin etkileri vardır.

### 2 Terminalli (Monolitik) Tandem

Monolitik bir 2T tandemde, perovskit üst hücre, aralarında ince bir rekombinasyon tabakası olacak şekilde doğrudan silikon alt hücrenin üzerine biriktirilir. Tüm yığın, tıpkı tek bağlantılı bir hücre gibi, biri üstte, biri altta olmak üzere iki elektrik kontağını paylaşıyor. Elektriksel olarak seri bağlı iki diyottur.

Bu çok zarif. Bu, mevcut modül montaj hatlarının tandem hücreleri sıfır değişiklikle işleyebileceği anlamına gelir. Hücre dışarıdan bakıldığında tam olarak sıradan bir silikon hücreye benziyor. Aynı şekil, aynı temaslar, aynı çekim süreci. Bu, ticarileştirme açısından büyük bir avantajdır.

Ancak önemli ve önemli bir sorun var: **mevcut eşleşme**. Seri devrede akım en zayıf halka tarafından sınırlanır. Her iki alt hücrenin de aynı foto akımı üretmesi gerekir, aksi takdirde aşırı üreten hücreden gelen aşırı akımın gidecek hiçbir yeri kalmaz ve boşa gider. Üst hücre mavi ışığı emdiği ve alt hücre kırmızıyı emdiğinden ve güneş spektrumu gün boyunca değiştiğinden (öğle vakti daha mavi, şafak ve akşam karanlığında daha kırmızı) mevcut denge sürekli değişir.

2T tandemi optimize etmek, perovskit bant aralığını ve kalınlığını dikkatli bir şekilde seçmek anlamına gelir; böylece akımlar *temsili* bir spektrum (tipik olarak AM1.5G standardı) altında eşleşir. 1,68 eV bant aralığı ve ~500 nm kalınlıkta, araştırmacılar genellikle 19–20 mA/cm² civarında eşleşen akımlar elde ederler. Ancak bulutlu bir sabahta veya kışın yüksek enlemde spektrum kırmızıya kayar, perovskit üst hücreyi aç bırakır ve tandemin çıktısını sınırlar. Yıllık enerji verimi simülasyonları, mevcut uyumsuzluğun, iyi tasarlanmış bir 2T tandeminin, teorik optimumla karşılaştırıldığında gerçek dünyadaki enerji hasadında yaklaşık %1-2'ye mal olduğunu göstermektedir.

Rekombinasyon katmanının kendisi, takdir edilmeye değer bir nano ölçekli mühendislik parçasıdır. Görevi, üst hücredeki elektronların ve alt hücredeki deliklerin buluşup yok olmasına izin vererek iç devreyi tamamlamaktır. Çoğu tasarımda ince (10-20 nm) bir indiyum kalay oksit (ITO) veya indiyum çinko oksit (IZO) tabakası kullanılır; bunlar telefon ekranlarında kullanılan şeffaf iletkenlerin aynısıdır. Bu katman optik olarak şeffaf, elektriksel olarak iletken ve hem yukarıdaki perovskit hem de aşağıdaki silikon yüzey işlemleriyle kimyasal olarak uyumlu olmalıdır. Ayrıca perovskiti bozmadan sonraki işlem adımlarının termal bütçesine de dayanması gerekir.

### 4 Terminalli (Mekanik Olarak Yığılmış) Tandem

4T ikilisinde perovskit hücre ve silikon hücre tamamen bağımsız olarak üretilir, her birinin kendi iki kontağı vardır ve fiziksel olarak basitçe istiflenir. Dört kablo çıkıyor. Her hücre kendi optimum voltajında ​​ve akımında çalışır; akım eşleştirmeye gerek yoktur.

Fizik avantajı gerçektir. Her iki hücre de diğerini kısıtlamadığından, 4T ikilisi spektral değişimi çok daha iyi tolere eder. O bulutlu sabahta perovskit hücrenin akımı düşüyor ama silikon hücre kendi optimal noktasında daha da sertleşiyor. Yıllık enerji verimi, yüksek enlem veya değişken iklim konumlarındaki eşdeğer 2T tasarımından genellikle %2-4 daha yüksektir.

Üretim dezavantajı da aynı derecede gerçektir. Artık iki ayrı kapsülleme sistemine ihtiyacınız var. İki kablo setine, iki maksimum güç noktası izleyicisine (veya özel bir çift girişli invertöre) ihtiyacınız var ve hücreler arasındaki ekstra cam/kapsülant katmanlarından kaynaklanan optik kayıplar, verimlilik kazancını tüketiyor. Perovskit üst hücrenin şeffaf bir arka temasa ihtiyacı vardır; bu, ikinci bir ITO katmanı veya kaçınılmaz olarak ışığın bir kısmını gölgeleyen ince bir metal şebeke anlamına gelir.

**2025 itibariyle sektördeki fikir birliği kararlı bir şekilde 2 terminale yönelmiştir.** Üretimin basitliği fazlasıyla ikna edicidir. LONGi'nin %34,85'lik rekoru, Oxford PV'un ticari modülleri ve hemen hemen her büyük üreticinin geliştirme yol haritası, 2T monolitik entegrasyonu hedefliyor. Mevcut eşleştirme cezası, trilyon dolarlık silikon tedarik zinciriyle kusursuz uyumluluk için ödenmeye değer bir vergidir.

## Yığın İçinde: Katman Katman

En son teknolojiye sahip 2T monolitik perovskit/silikon ikilisini yukarıdan aşağıya doğru inceleyelim. Her katman önemlidir. Silikon tabaka hariç toplam kalınlık: kabaca 1-2 mikrometre.

**Yansıma önleyici kaplama (MgF₂ veya LiF, ~110 nm).** Tıpkı tek bağlantılı silikon hücreler gibi yansımayı en aza indirmeniz gerekir. Magnezyum florür, düşük kırılma indeksi (~1,38) ve kolay termal buharlaşması nedeniyle popülerdir.

**Şeffaf üst elektrot (ITO veya IZO, ~70–100 nm).** Bu, perovskit hücrenin ön temasıdır. Görünür ışığın >%90'ını iletirken akımı hücre kenarındaki metal bir şebekeye yanal olarak iletmelidir.

**Elektron taşıma katmanı (SnO₂ veya C₆₀, ~20–30 nm).** Bu, delikleri bloke ederken perovskitten seçici olarak elektronları çıkarır. Atomik katman birikimi (ALD) yoluyla biriktirilen kalay dioksit şu andaki favoridir; uyumlu, iğne deliği olmayan ve silikonun tolere edebileceği sıcaklıklarda işlenebilir.

**Perovskit soğurucu (~400–600 nm).** Üst hücrenin kalbi. Tipik olarak ~1,68 eV bant aralığına sahip Cs₀.₀₅FA₀.₈₀MA₀.₁₅Pb(I₀.₈₃Br₀.₁₇)₃ gibi karışık katyon, karışık halojenür bileşimi. Döndürerek kaplama (laboratuvar ölçeği), slot-die kaplama (pilot ölçek) veya birlikte buharlaştırma (geniş alanlar üzerinde en düzgün filmleri ürettiği için ortaya çıkan endüstriyel favori) yoluyla biriktirilir.

**Delik taşıma katmanı (Me-4PACz veya PTAA, ~2–5 nm).** Me-4PACz gibi kendiliğinden birleşen tek katmanlar (SAM'ler), tandem tasarımında devrim yarattı. Bu molekül kelimenin tam anlamıyla bir molekül kalınlığındadır; alttaki yüzeye bağlanır ve perovskitten delik açmak için mükemmel bir enerji seviyesi sunar. Spiro-OMeTAD gibi kalın, pahalı ve kararsız olan eski polimerik katmanların yerini aldı.

**Rekombinasyon bağlantısı (ITO, ~10–20 nm).** Kritik köprü. Perovskitten gelen elektronlar ve silikondan gelen delikler burada buluşup yeniden birleşiyor. Bu katman ayrıca perovskit işlemi ile silikon yüzeyi arasında kimyasal bir bariyer sağlar.

**Silikon alt hücre (~150–180 μm).** Genellikle bir heteroeklem (HJT) veya TOPCon mimarisi — her ikisi de tandemin toplam voltajına katkıda bulunan yüksek voltajlar (>710 mV) sunar. Ön yüzey, 7. Günde ele aldığımız gibi, ışığı yakalamak için rastgele piramitlerle dokuludur. Bu ~3 μm piramitler üzerinde uyumlu perovskit birikimi elde etmek, tandem imalatın en büyük mühendislik zorluklarından biridir.

**Arka kontak ve pasifleştirme.** Standart silikon arka uç işleme — pasifleştirilmiş kontaklar üzerine alüminyum veya gümüş metal kaplama.

## Doku Sorunu: İnce Bir Battaniyenin Altındaki Dağlar

Kağıt üzerinde önemsiz gibi görünen ancak binlerce insan-saatlik araştırma gerektiren bir şey var: silikon levhaların dokulu yüzeyleri var ve perovskit bundan hoşlanmıyor.

Silikon levha üzerindeki rastgele piramit dokusu (tepeden vadiye yüksekliği 1-5 μm) ışığı yakalamak için gereklidir; silikon hücrelerin nispeten zayıf emme katsayılarına rağmen bu kadar iyi emmesinin nedeni budur. Ancak 500 nm'lik bir perovskit filmi 3 μm özelliklere sahip bir yüzey üzerine yerleştirmeye çalıştığınızda eşit olmayan bir kapsama alanı elde edersiniz. Piramit tepelerinde ince noktalar. Vadilerde havuzlanma. Hücreye kısa devre yapan iğne delikleri.

İlk tandem makaleleri bunu kabaca çözdü: Silikonun ön yüzeyini düz bir şekilde parlatın ve yansıma cezasını kabul edin. Bu işe yarar, ancak artan yansıma nedeniyle 1-2 mA/cm² fotoakım kaybedersiniz; bu, yüzde birin her kesri için mücadele ederken acı verici bir fedakarlıktır.

Atılım iki yönden geldi. İlk olarak, perovskitin **birlikte buharlaşması** (PbI₂ ve FAI/CsBr'nin vakumda çift kaynaklı buharlaştırılması), bir sprey boya tabakası gibi piramit dokusunu takip eden güzel uyumlu filmler üretir. İkincisi, araştırmacılar **mikron altı dokular** geliştirdiler; silikon piramitlerini 0,5-1 μm yüksekliğe kadar parlattılar; bu, çözeltiyle işlenmiş perovskitin eşit şekilde kaplanmasına yetecek kadar küçük olmasına rağmen yine de önemli bir yansıma önleyici fayda sağlıyor.

LONGi'nin rekor %34,85'lik hücresi, uyumlu perovskit üst hücreye sahip tamamen dokulu bir silikon alt hücre kullanıyor; bu, doku sorununun tamamen çözülmese bile en azından evcilleştirildiğinin kanıtı.

## Gerilim Bonusu: 1 + 1 > 2

Tandem fiziğinin en tatmin edici yönlerinden biri voltaj aritmetiğidir. 2T tandemde, iki alt hücrenin açık devre gerilimleri toplanır. İyi bir silikon HJT alt hücresi yaklaşık 720 mV sağlar. İyi bir geniş bant aralıklı perovskit üst hücre yaklaşık 1.200 mV sağlar. Tandem: ~1.920 mV — tek bir güneş altındaki tek bir hücreden yaklaşık 2 volt.

Ancak mantığa aykırı olan kısım şu: Tandemin birleşik voltajı aslında bağımsız çalışan iki hücreden alacağınız voltajdan *daha yüksek*. Neden? Çünkü tandem konfigürasyonda silikon hücre yalnızca perovskitin ilettiği kızılötesi fotonları emer. Bu fotonların enerjisi silikonun bant aralığına nispeten yakındır, bu da emilen foton başına daha az termalizasyon kaybı anlamına gelir. Silikon hücre spektral anlamda "daha soğuk" çalışır; spektrumun daha dar, daha uygun bir dilimini görür. Bu, tam spektrumlu ışık altında bağımsız bir silikon hücreye kıyasla voltajını biraz artırır.

Net etki: İyi optimize edilmiş bir tandem, gelen güneş enerjisinin yaklaşık %34-35'ini elektrik olarak sağlarken, en iyi tek eklemli silikon için bu oran %26-27'dir. Bu sadece artan bir gelişme değil; güneş enerjisi tesislerinin ekonomisini temelden değiştiren bir adım değişikliğidir, çünkü alana bağlı tüm maliyetler (arazi, raf, kablolama, kurulum işçiliği) %30-40 daha fazla enerji çıkışı üzerinden amortismana tabi tutulur.

## Yarış: Kim Kazanıyor?

Perovskit-silikon tandem yarışı, temiz enerjideki en yoğun yarışmalardan biridir. İşte 2026 başı itibarıyla liderlik tablosu:

**LONGi Green Energy** — %34,85 (NREL-sertifikalı, Nisan 2025). Çinli dev birçok kez kendi rekorunu kırdı. Hücreleri, dokulu silikon HJT alt hücre üzerinde monolitik bir 2T mimarisi kullanıyor. LONGi ilk önce bunu ölçeklendirecek üretim gücüne sahip.

**Oxford PV** — Eylül 2024'ten bu yana %26,9 modül verimliliği rekoru, %24,5 ticari modül sevkıyatı. Brandenburg fabrikalarının kapasitesi kabaca 50-100 MW ve ABD'deki kamu hizmeti ölçeğindeki bir müşteriye paneller teslim ettiler; bu, tandem teknolojisinin dünyanın herhangi bir yerindeki ilk ticari dağıtımıdır. 72 hücreli panelleri, aynı boyuttaki standart silikon panellerden yaklaşık %20 daha fazla enerji üretiyor.

**Hanwha Q Cells** — Helmholtz-Zentrum Berlin (HZB) ile ortaklık kurdu ve 2026 yılına kadar üretim hacmini hedefliyor. HZB bağımsız olarak küçük hücrelerde >%30'a ulaştı.

**Trina Solar** — ISFH tarafından onaylanmış perovskite-HJT tandemde %34,15. Sessizce pilot hatlar inşa ediyoruz.

**CSEM/EPFL (İsviçre)** — Geniş alanlı (>1 cm²) bir hücrede %33,2; bu da yüksek verimliliğin yalnızca posta pulu boyutundaki örneklerde elde edilemeyeceğini gösteriyor.

Model açık: Çinli üreticiler hücre düzeyindeki rekorları kazanırken, Oxford PV ticarileştirmede başı çekiyor. Asıl soru tandemlerin işe yarayıp yaramayacağı değil; bu çözüldü. Önemli olan bunların düz silikonla rekabet edebilecek maliyetlerde, uygun ölçekte ve kabul edilebilir ömürlerle üretilip üretilemeyeceğidir.

## Geriye Kalan Zorluklar

Tandem üretimi silikon hücrelerin üretiminden daha zordur ve zorluklar ciddidir:

**Kararlılık.** Perovskit üst hücresinin açık havada 25 yıldan fazla hayatta kalması gerekir. Dün tartıştığımız gibi perovskit nem, ısı ve UV ışıkta bozunur. Birlikte, silikon alt hücre biraz daha soğuk çalışır (perovskit, ısı üreten mavi ışığın bir kısmını emer), bu da yardımcı olur. Ancak güneşli iklimlerde modül sıcaklıkları rutin olarak 65-75°C'ye ulaşıyor ve perovskit, tek kalkanı kapsüllemeyle buna dayanmak zorunda. Oxford PV, modüllerinin 85°C'de ve %85 bağıl nemde 1.000 saat boyunca nem-ısı testleri de dahil olmak üzere IEC 61215 yeterlilik testini (aynı standart silikon modüllerinin karşılaması gereken) geçtiğini iddia ediyor. Bu cesaret verici, ancak birkaç yıldan sonraki saha verileri henüz mevcut değil.

**Ölçeklenebilirlik.** Laboratuvar kayıtları ~1 cm²'lik hücrelere ayarlanır. Ticari modüller ~2,5 m² tekdüze perovskit filme ihtiyaç duyar. Küçük hücreler ile büyük modüller arasındaki verimlilik farkı hâlâ yüzde 8-10 puandır. Bu boşluğun kapatılması, film tekdüzeliğinin çözülmesini, hücreler arasındaki ölü alanın en aza indirilmesini ve levhadan levhaya değişim boyunca pasivasyon kalitesinin korunmasını gerektirir.

**Kurşun.** Her perovskit güneş hücresi, metrekare başına yaklaşık 0,5-1 gram kurşun içerir. Şebeke ölçeğinde bir kurulum on binlerce metrekareyi kapsıyor. Avrupa düzenlemeleri (RoHS direktifi) şu anda fotovoltaik panelleri muaf tutmaktadır, ancak bu muafiyet periyodik olarak gözden geçirilmektedir. Kapsülleme başarısız olursa ve yağmur suyu sızarsa, kurşun kirliliği gerçek bir endişe kaynağı olur. Kalay bazlı perovskitlere (kurşunun yerini alan) yönelik araştırmalar aktiftir ancak rekabetçi verimliliğe yaklaşamaz.

**Süreç entegrasyonu.** Bir silikon hattına perovskit birikiminin eklenmesi, inorganik yarı iletken işleme için tasarlanmış fabrikalara yeni malzemelerin (organik katyonlar, halojenür tuzları, fullerenler) dahil edilmesi anlamına gelir. Kirlenme kontrolü, kimyasal uyumluluk ve termal bütçe yönetiminin tümü gerçek mühendislik sorunlarıdır. Silikon hücresinin pasifleşmesine zarar vermemek için perovskit katmanlarının ~150°C'nin altındaki sıcaklıklarda biriktirilmesi gerekir; bu, işlem seçeneklerini sınırlayan bir kısıtlamadır.

## Şaşırtıcı Ekonomi

Tandemleri neredeyse kaçınılmaz kılan mantığa aykırı gerçek şu: **üretimi %20 daha fazla maliyetli olan ancak %30 daha fazla güç üreten bir tandem modülü, yerine geçtiği silikon modülden watt başına daha ucuzdur.** Ve *sistem* seviyesinde watt başına önemli ölçüde daha ucuzdur, çünkü invertör, raf, kablolama, arazi, izinler ve kurulum işçiliğinin tamamı watt başına maliyet cinsindendir. 400 W tandem panel ile 300 W silikon panelin kurulum maliyeti neredeyse aynıdır; kurulumu yapan kişi camın içinde ne olduğunu umursamaz.

BloombergNEF ve diğer analistler, mevcut üretim ölçek büyütme yörüngelerinin geçerli olduğu varsayılarak, perovskit-silikon tandemlerinin 2028-2030 yılına kadar geleneksel silikonla modül düzeyinde maliyet eşitliğine ulaşabileceğini öngörüyor. Bundan sonra, her ilave watt verimlilik saf ekonomik kazançtır.

Yatırım çılgınlığının gerçek olmasının nedeni budur. Oxford PV 400 milyon doların üzerinde bağış topladı. LONGi'nin tandemlere yönelik Ar-Ge bütçesi açıklanmadı ancak yüz milyonlarca olduğu tahmin ediliyor. Hanwha Q Cells tandem programına 100 milyon dolar ayırdı. Tez basit: Güvenilir tandem modüllerin seri üretimini ilk başaran kişi, piyasadaki diğer her şeyi geçersiz kılan bir ürüne sahip olacak.

## Sonra Ne Gelir?

Silikon-perovskit ikilisi çoğu insanın karşılaşacağı *ilk* ikilidir. Ama bu son değil. Araştırmacılar halihazırda tek güneş altında %40'ın üzerinde verimliliği hedefleyen üç bağlantı noktasını (silikon üzerinde perovskit üzerinde perovskit) istifliyorlar. Ve yakın vadede tandem teknolojisi, her panelden daha fazla enerji tüketen diğer yeniliklerle birleşiyor.

Yarın bu yeniliklerden birini inceleyeceğiz: **çift yüzeyli modüller ve izleme sistemleri** — panelin her iki tarafından da ışık toplayan ve gökyüzünde güneşi takip eden teknolojiler. Çift yüzeyli tasarımı tandem hücrelerle birleştirdiğinizde, kurulu metrekare başına enerji verimi, on yıl önce bilim kurgu gibi görünen sınırlara yaklaşmaya başlar.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-22.toml}}
