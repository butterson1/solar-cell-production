# 9. Gün: Hücre Mimarileri — PERC, TOPCon, HJT

*Geçtiğimiz sekiz gün boyunca silikonu kuvarsit madeninden serigrafi baskılı, metalize güneş hücresine kadar takip ettiniz. Ancak olay şu: "standart" bir alüminyum arka yüzey alanı (Al-BSF) hücresini tanımlıyoruz; bu tasarım, yaklaşık %20 verimliliğe ulaşmış ve 2025'te artık esasen bir müze parçası haline gelmiş bir tasarım. Gerçek güneş enerjisi endüstrisi yoluna devam etti ve birbirleriyle savaşan üç gruba ayrıldı: PERC, TOPCon ve HJT — her biri aynı sorunun farklı cevabı üzerine milyarlarca dolar bahis oynadı: Elektronların yüzeylerde ölmesini nasıl durdurursunuz?*

---

## Düşman: Yüzey Rekombinasyonu

Alfabe çorbasına dalmadan önce, her üç mimarinin de çözmeye çalıştığı sorunu anlamalısınız çünkü bu aynı sorundur ve sinir bozucudur.

Bir fotonu emerek bir elektron-delik çifti oluşturduğunuzda (1. Gün), bu çiftin p-n bağlantısına ulaşacak, ayrılacak ve metal temas noktalarından dışarı akacak kadar uzun süre hayatta kalması gerekir (8. Gün). Yüksek saflıkta monokristalin silikon levhanın büyük bir kısmında, bir azınlık taşıyıcısı birkaç milisaniye boyunca yaşayabilir; yarı iletken açısından sonsuzluk, birkaç yüz mikrometreyi yaymaya yetecek kadar süre. Büyüklük sorun değil.

Sorun yüzeylerde. Silikonun kristal kafesi her yüzeyde aniden sona eriyor ve geride "sallantılı bağlar" (tuzak gibi davranan eşleşmemiş elektronlara sahip tatminsiz silikon atomları) bırakıyor. Bir yüzeyin yakınında dolaşan herhangi bir elektron veya deliğin orada yeniden birleşmesi olasılığı çok yüksektir, enerjisi ısı olarak boşa harcanır. İşlenmemiş bir silikon yüzeyindeki rekombinasyon hızı 10⁶ cm/s'yi aşabilir. Karşılaştırma için, iyi pasifleştirilmiş bir yüzey, 2 cm/s'nin altındaki rekombinasyon hızlarına ulaşabilir. Bu 500.000'lik bir faktör.

Bir hücrenin ön yüzeyi büyük ölçüde 6. ve 7. Günlerde çözüldü: fosfor katkılı yayıcı, silikon nitrür ARC ve yüzey dokusu birlikte ön taraftaki rekombinasyon hızını yönetilebilir tutuyor. *Arka* yüzey, üç mimarinin birbirinden ayrıldığı ve geçtiğimiz on yıldaki verimlilik kazanımlarının çoğunun geldiği yerdir.

Eski Al-BSF hücresinde, arka kısım basitçe alüminyum macunla kaplandı ve ateşlendi; bu, mütevazı bir pasivasyon sağlayan (rekombinasyon hızı ~200–500 cm/s) ve arkaya ulaşan fotonların belki de %60–70'ini yansıtan bir p⁺ arka yüzey alanı oluşturdu. İşe yaradı ama masada en az yüzde 2-4 oranında mutlak verimlilik kalıyordu. PERC, TOPCon ve HJT'nin her birinin kapatmaya çalıştığı boşluk budur - ve hizmet ölçeğinde, mutlak verimliliğin her %0,1'i kabaca watt başına 0,002-0,003 ABD Doları değerindedir; bu da 50 GW üretim hattında modül değeri açısından yılda 100-150 milyon ABD Doları anlamına gelir.

---

## PERC: Her Şeyi Değiştiren Görevli

**Pasifleştirilmiş Verici ve Arka Hücre** (PERC), 1983 yılında Martin Green'in New South Wales Üniversitesi'ndeki grubu tarafından icat edildi; bu laboratuvar, silikon hücre verimliliği rekorunu diğerlerinden daha fazla elinde tutan laboratuvardır. Ancak PERC'nin laboratuvar merakından üretim gerçekliğine geçmesi neredeyse 30 yıl sürdü. Konsept aldatıcı derecede basittir: arka kısmın tamamını alüminyumla kaplamak yerine, ince bir dielektrik pasivasyon katmanı (tipik olarak alüminyum oksit, Al₂O₃, 5-20 nm kalınlığında, ardından silikon nitrür) biriktirin ve ardından lazer ablasyon kullanarak dielektrik boyunca yerel temas noktalarını açın.

İşte bu yüzden bu kadar iyi çalışıyor. Alüminyum oksit, p-tipi silikon ile arayüzde cm² başına kabaca 10¹² ila 10¹³ yük arasında sabit bir negatif yük yoğunluğu taşır. Bu negatif yük, azınlık taşıyıcı elektronları arka yüzeyden uzaklaştırır; bu olaya "alan etkili pasifleşme" adı verilir. Al₂O₃'nun sağladığı kimyasal pasifleştirme (doymuş sarkan bağlar) ile birleştiğinde, arka yüzey rekombinasyon hızı Al-BSF'da ~300 cm/s'den PERC'de 10 cm/s'nin altına düşer. Tek başına bu bile yaklaşık %0,8-1,0 mutlak verimlilik değerindedir.

Ancak aynı derecede önemli olan ikinci bir fayda daha var: dielektrik yığın bir iç ayna görevi görüyor. Yakın kızılötesindeki (900–1200 nm) soğurulmadan tüm levhadan geçen fotonlar (silisyumun zayıf bir şekilde emdiği uzun dalga boylu fotonlar) artık çıplak alüminyumun ~%65'i yerine %90–96 verimlilikle dielektrik/alüminyum reflektörden yansıyor BSF. Yansıyan bu fotonlar levhadan ikinci bir geçiş yaparak uzun dalga boyu yanıtını önemli ölçüde artırır. Bu "optik kazanç", %0,3-0,5 oranında mutlak verimlilik daha ekler.

Temel üretim ilavesi yalnızca iki adımdan oluşur: Al₂O₃/SiNₓ arka pasivasyon yığınının yerleştirilmesi (atom katmanı biriktirme veya PECVD kullanılarak, ~0,005–0,008/W eklenerek) ve kontak deliklerinin lazerle açılması (darbeli bir lazer kullanılarak, tipik olarak 532 nm Nd:YAG, nokta boyutları ~50 μm). İşte bu. Hattın geri kalanı — dokulandırma, difüzyon, ön ARC, serigrafi baskı — temelde Al-BSF ile aynı kalır. Bu geriye dönük uyumluluk, PERC'ün sektörü bu kadar hızlı fethetmesinin nedenidir: Sıfırdan bir TOPCon veya HJT hattı için 100+ milyon $'a kıyasla, mevcut üretim hatlarını 10–20 milyon $'a yenileyebilirsiniz.

2020 yılına gelindiğinde PERC sıfıra yakın bir seviyeden küresel hücre üretiminin %80'inin üzerine çıktı. Dünyanın en büyük güneş enerjisi üreticisi LONGi Green Energy, şirkete PERC üzerine bahse girdi ve muhteşem bir şekilde kazandı ve orta kademe bir oyuncudan 60 milyar dolarlık bir piyasa değeri devine dönüştü. Üretim PERC hücreleri rutin olarak %23,0-23,5 verimliliğe ulaşırken, LONGi'nin rekoru %24,06'ydı. Ancak bu rakam önemli: %24, rahatsız edici derecede PERC'nin pratik tavanına yakın.

Sorun temeldir. PERC hala ön yayıcı için homojen bir fosfor difüzyonu kullanıyor ve yüzeyde nispeten ağır bir katkı (~10²⁰ atom/cm³) oluşturarak önemli Auger rekombinasyonuna neden oluyor; bu, bir elektronun enerjisini üçüncü bir taşıyıcıya aktararak bir delikle yeniden birleştiği üç gövdeli bir süreç. Bu ön yüzey rekombinasyonu ve yerel arka temas noktalarında kalan kayıplar, PERC'nin teorik maksimumunu %24,5 civarına getiriyor. Sektör halihazırda üretimde %23,5 seviyesindedir; bu, PERC'nin kapasitesinin yaklaşık %95'ini kullandığı anlamına gelir. Kuyu kurumaya devam ediyor.

---

## TOPCon: Görünen Varis

**Tünel Oksit Pasifleştirilmiş Temas** (TOPCon) (bazen "pasifleştirilmiş temas" veya "oksit üzerinde poli-Si" olarak da adlandırılır) PERC'nin en olası halefidir ve 2026'nın başlarında yeni üretim kapasitesi eklemelerinde PERC'yi çoktan geride bırakmıştır.

Ana fikir fiziği açısından güzeldir. TOPCon, arka dielektrikte delikler açmak ve yerel metal-silikon temas noktaları (rekombinasyon sıcak noktaları olan) oluşturmak yerine, "pasifleştirilmiş bir temas" oluşturur; bu, metal silikon levhanın yüzeyine hiç temas etmeden * akımı çeken bir temastır. İşte nasıl:

1. **Tünel oksit:** Arka yüzeyde yalnızca 1,0–1,5 nm kalınlığında, yaklaşık 5–7 atomik katmandan oluşan ultra ince bir silikon dioksit tabakası oluşturun. Bu oksit, elektronların kuantum-mekanik olarak içinden tünel açabileceği kadar incedir, ancak yüzeyi kimyasal olarak pasifleştirecek (sarkan bağları doyurarak) ve delik taşınmasına bir engel oluşturacak kadar kalındır.

2. **Katkılı poli-Si:** Tünel oksidin üzerine ağır n katkılı polikristalin silikondan (50–200 nm kalınlığında, ~10²⁰ cm⁻³'ye kadar fosfor katkılı) bir katman yerleştirin. Bu poly-Si katmanı iki şey yapar: güçlü bir alan etkili pasifleştirme (delikleri arka yüzeyden uzaklaştıran) oluşturan bir serbest elektron deposu sağlar ve akımı metal temas noktalarına taşımak için yanal bir taşıma katmanı olarak hizmet eder.

3. **Poly-Si üzerinde metalize edin:** Ekran baskılı metal temas noktaları yalnızca poly-Si katmanına temas eder, kristalin tabakaya asla temas etmez. Rekombinasyona yatkın metal-yarı iletken arayüzü artık emiciden tünel oksit ile ayrılarak "temas rekombinasyonunu" sıfıra yakın bir seviyeye düşürür.

Sonuç, PERC'nin yerel kontakları için 20-50 fA/cm² ve Al-BSF için ~200 fA/cm² ile karşılaştırıldığında yalnızca 2–5 fA/cm²'lik bir arka yüzey rekombinasyon akım yoğunluğudur (J₀). Bu, üretimde 710–720 mV açık devre gerilimlerine (Voc) olanak sağlarken, PERC için 680–690 mV'ye ulaşır. Verimlilik Voc × Jsc × FF ile orantılı olduğundan, bu voltaj kazancı tek başına %1,0–1,5 mutlak verimlilik değerindedir.

Üretim TOPCon hücreleri artık rutin olarak %25,0-25,5'e ulaşırken, JinkoSolar %26,89 ile rekoru elinde tutuyor (bağımsız olarak ISFH tarafından onaylandı, Kasım 2024'te duyuruldu). Tek bağlantılı TOPCon için teorik limit %28,7 civarındadır, dolayısıyla hala anlamlı bir boşluk payı vardır.

Üretimdeki zorluk tünel oksittir. 182 mm × 182 mm (veya 210 mm × 210 mm) levha üzerinde tekdüze bir 1,2 nm oksitin büyütülmesi olağanüstü derecede zordur. Oksit iğne deliği içermemelidir; tek bir iğne deliği, akımı kesen ve voltajı öldüren bir "şant" yaratır. Endüstri iki yaklaşım üzerinde birleşti: bir tüp fırında termal oksidasyon (oksidin kontrollü bir O₂/N₂ atmosferinde 600°C'de büyütülmesi) ve poli-Si biriktirme için LPCVD. Bu araçlar büyük ve pahalıdır (tek bir LPCVD tüpün maliyeti 2–5 milyon dolar) ve titizdir; 1.200 levhalık bir partideki sıcaklık eşitliğinin ±2°C'de tutulması gerekir.

Bir PERC hattından TOPCon'a dönüşüm maliyeti, 5 GW tesisi için kabaca 30-50 milyon $ iken, sıfırdan bir TOPCon hattı için 150-250 milyon $'dır. Çinli üreticiler (Jolywood, Jinko, Trina, Tongwei, JA Solar) PERC hatlarını büyük bir hızla TOPCon'a dönüştürüyor. 2025'in sonunda küresel TOPCon kapasitesi 500 GW'ü aştı ve yeni kurulumlarda ilk kez PERC'yi aştı. Geçiş, sanayi tarihindeki en hızlı teknoloji değişimlerinden biri olarak yaklaşık üç yıl içinde gerçekleşti.

Kayda değer bir incelik var: Çoğu üretim TOPCon hücresi, p-n bağlantısının arkada olduğu (n-tipi plaka ile ön tarafta bor difüzyonu ile oluşturulan p-tipi yayıcı arasında) "arka bağlantı" tasarımlarıdır. Bu, ön tarafında n-tipi yayıcıya sahip p-tipi bir levha kullanan PERC'ın tam tersidir. P-tipinden n-tipi levhalara geçiş iki nedenden dolayı önemlidir. Birincisi, n-tipi silikon, p-tipi plakaları rahatsız eden ve ilk yılda %1-3 güç kaybına neden olan bor-oksijen kompleksi olan ışık kaynaklı bozulmadan (LID) etkilenmez. İkincisi, n-tipi silikon daha yüksek azınlık taşıyıcı ömürlerine sahiptir (p-tipi Cz için >1 ms'ye karşı ~0,1 ms), bu da pasifleştirilmiş kontaktan tam olarak yararlanmak için gereklidir. Dezavantajı: n-tipi plakaların maliyeti %5-10 daha fazladır çünkü külçenin fosfor katkısını kontrol etmek bor katkısını kontrol etmekten daha zordur.

---

## HJT: Zarif Yabancı

**Heteroeklem Teknolojisi** (HJT, bazen silikon heteroeklem için SHJ olarak da adlandırılır) üç mimari arasında en zarif olanıdır ve aynı zamanda geleneksel hücre üretiminden en farklı olanıdır. PERC ve TOPCon'un evrimsel olduğu (temel olarak benzer bir süreç akımına pasifleştirme katmanları eklendiği) durumda HJT tamamen farklı bir hayvandır.

Fikir 1990'ların başında Sanyo'dan (şu anda Panasonic) geldi ve "HIT" hücreleri olarak ticarileştirildi. Konsept, ince film teknolojisinden ilham alıyor: 800–900°C'de katkılı bölgeler oluşturmak için difüzyon fırınları kullanmak yerine, HJT, dokulandırmadan sonraki tüm süreç boyunca düşük sıcaklıklarda (200°C'nin altında) kristalin silikon levha üzerine ultra ince hidrojenlenmiş amorf silikon katmanları (a-Si:H) biriktirir.

HJT yığını, arkadan öne doğru:

1. **Metal kontaklar** (ekran baskılı veya kaplamalı, TCO üzerine)
2. **Şeffaf iletken oksit** (TCO, tipik olarak indiyum kalay oksit, ITO, ~75 nm)
3. **p katkılı a-Si:H** (~5–10 nm)
4. **İçsel a-Si:H** (i-katmanı, ~5–8 nm) — pasifleştirme büyüsü
5. **n-tipi kristal silikon levha** (130–150 μm)
6. **İçsel a-Si:H** (i-katman, ~5–8 nm)
7. **n-katkılı a-Si:H** (~5–10 nm)
8. **TCO** (~75 nm)
9. **Metal kontaklar**

Kritik katman, içsel (katkısız) amorf silikondur; PECVD tarafından biriktirilen yalnızca 5-8 nm a-Si:H'dir. Bu katman, kristalin silikon için bilim tarafından bilinen en iyi yüzey pasivasyonunu sağlar: en iyi TOPCon için 720 mV ile karşılaştırıldığında 750 mV'nin üzerinde ima edilen Voc değerleri. a-Si:H'deki hidrojen, c-Si yüzeyindeki hemen hemen her sarkan bağı doyurur ve 2 cm/s'nin altında yüzey rekombinasyon hızlarına ulaşır.

Rakamlar kendileri için konuşuyor. LONGi, 2024 sonlarında HJT hücresinde %27,30 verimliliğe ulaştı ve birçok üretici üretimde %26'yı aştı. Tek eklemli HJT için teorik sınır herhangi bir kristalin silikon hücreyle aynıdır (~%29,4), ancak HJT üstün pasifleştirmesi nedeniyle ona yaklaşmaktadır.

Mantık dışı sürpriz şu: **HJT hücreleri, PERC veya TOPCon'dan daha az işlem adımına sahiptir.** Tipik bir HJT satırında yalnızca 4-5 ana adım bulunur:

1. Dokulandırma ve temizleme
2. a-Si:H biriktirme (bir PECVD aletinde 4 katman: bir tarafta i/n, diğer tarafta i/p)
3. TCO püskürtme (her iki tarafta)
4. Metalleştirme (serigrafi veya kaplama, her iki taraf)
5. (İsteğe bağlı) hafif tavlama

Bunu PERC'nin ~10 adımıyla veya TOPCon'un ~12 adımıyla karşılaştırın. Sadelik baş döndürücü. Ancak bir sorun var; aslında birkaç sorun var.

**Sıcaklık kısıtlaması:** Amorf silikon ~200°C'nin üzerinde kristalleştiğinden (ve pasifleştirme özelliklerini kaybettiğinden), a-Si:H biriktirmeden sonraki tüm sürecin soğuk kalması gerekir. Bu, 750–850°C'de geleneksel gümüş hamurunun pişirilmesini dışlar. HJT hücreleri, 150–200°C'de sertleşen, düşük sıcaklıkta özel gümüş macunlara ihtiyaç duyar. Bu macunlar, pişirilmiş macunlardan daha yüksek dirence sahiptir (hücre başına daha fazla gümüş gerektirir - TOPCon için yaklaşık 15–20 mg/W'a karşı 10–13 mg/W) ve kilogram başına maliyeti daha yüksektir. Gümüş tüketimi HJT'nin Aşil topuğu kadardır.

**Ekipman maliyeti:** a-Si:H biriktirme için PECVD araçları, katkı gazlarının (silan, trimetilbor, fosfin) ppm'nin altında kontrolüyle, büyük plakalar boyunca angstrom seviyesinde kalınlık tekdüzeliğine ulaşmalıdır. Önde gelen ekipman tedarikçileri - Meyer Burger (İsviçre), Maxwell (Çin) ve Sumitomo (Japon) - bu aletlerin her biri 15-25 milyon dolara satılıyor. ITO püskürtme hedefleri pahalı indiyum kullanır (300–600$/kg). Tam bir HJT hattının maliyeti GW başına kabaca 80-120 milyon dolar iken, TOPCon'un GW başına 50-70 milyon doları var.

**İndiyum sorusu:** Her HJT hücresi yaklaşık 200–300 mg indiyum gerektirir (ITO yoluyla). Küresel indiyum üretimi yılda yaklaşık 900 tondur. HJT yıllık 500 GW üretime ulaşacak olsaydı, yaklaşık 1.500 ton indiyuma ihtiyaç duyacaktı; bu, mevcut arzın tamamından çok daha fazla. Bu, endüstrinin alternatif TCO'larla (alüminyum katkılı çinko oksit, AZO veya hidrojen katkılı indiyum oksit, IOH) ve daha ince ITO katmanlarla saldırdığı gerçek bir ölçeklendirme darboğazıdır.

---

## Puan Kartı: Karşılıklı

Buna gerçek sayılar koyalım:

| Metrik | PERC | TOPCon | HJT |
|----------|------|----------|-----|
| Üretim verimliliği (2025) | %23,0–23,5 | %25,0–25,5 | %25,0–26,0 |
| Hücre verimliliğini kaydedin | %24,06 | %26,89 | %27,30 |
| Tipik Vok | 680–690mV | 710–720mV | 740–750 mV |
| İşlem adımları | ~10 | ~12 | ~5 |
| Maksimum proses sıcaklığı | 850°C | 850°C | 200°C |
| Gümüş tüketimi (mg/W) | 12–15 | 10–13 | 15–20 |
| GW başına sermaye harcamaları | 40–60 Milyon Dolar | 50–70 Milyon Dolar | 80–120 milyon $ |
| Gofret tipi | p-tipi | n-tipi | n-tipi |
| Sıcaklık katsayısı | −0,38%/°C | −0,32%/°C | −0,26%/°C |
| İki yüzeylilik faktörü | %70 | %80–85 | %90–95 |

Son satır dikkati hak ediyor. HJT'nin simetrik yapısı (her iki tarafta pasifleştirilmiş temaslar) onu doğal olarak iki yüzeyli kılar; ışığı hem önden hem de arkadan yakalayabilir; bu, albedo'nun (yerden yansıyan ışık) enerji verimini %5-15 artırabildiği yere monteli tesisatlar için son derece önemlidir. HJT'nin sıcaklık katsayısı da en iyisidir: 25°C'nin üzerindeki her santigrat derece için, HJT gücünün yalnızca %0,26'sını kaybederken, PERC için bu oran %0,38'dir. Sıcak iklimlerde (Orta Doğu, Hindistan, Avustralya) bu, yıllık %3-5 daha fazla enerji üretimi anlamına gelir.

---

## Piyasa Gerçeği: TOPCon Neden Kazanıyor (Şimdilik)

HJT'in çeşitli ölçümlerdeki teknik üstünlüğüne rağmen, TOPCon kapasite geliştirmede hakim konumdadır. Bunun nedeni son derece pratiktir: dönüşüm ekonomisi. Çin'in güneş enerjisi üreticilerinin, kapasite watt başına 6-10 $ karşılığında TOPCon'a dönüştürülebilecek yüzlerce GW PERC üretim hattı vardı. Yeni HJT hatları inşa etmenin maliyeti watt başına kapasite başına 80-120 ABD dolarıdır ve PERC hatları HJT hattına dönüştürülemez; ekipman tamamen farklıdır.

Matematik basitti. 80'den fazla GW kapasitesiyle dünyanın en büyük hücre üreticisi Tongwei, 2023'te PERC filosunun tamamını TOPCon'a dönüştüreceğini duyurdu. JinkoSolar, JA Solar, Trina — hepsi aynı bahse girdi. Huasun, Risen ve Maxwell gibi HJT üreticiler ölçeklerini büyüttüğünde, TOPCon'un ezici gücü zaten 500'ün üzerinde GW seviyesindeydi.

Ama yarış bitmedi. HJT'nın gümüş tüketimi (en büyük maliyet dezavantajı) birçok açıdan saldırıya uğruyor. Bakır kaplama (ekran baskılı gümüşün tamamen değiştirilmesi), metalizasyon maliyetlerini %70-80 oranında azaltabilir. Meyer Burger'in öncülüğünü yaptığı SmartWire Bağlantı Teknolojisi (SWCT), baralar yerine ince bakır teller kullanarak gümüşü 5 mg/W'ın altına indiriyor. Ve 11. ve 22. Günlerde göreceğimiz gibi, HJT perovskit-silikon ikilileri için doğal alt hücredir; seri üretimde %30 verimliliği aşması en muhtemel teknolojidir.

Önümüzdeki beş yıl, TOPCon'un önde başlamasının hakimiyetini sağlamlaştırıp sağlamlaştırmayacağını veya HJT'nin tandem istiflemeyle üstünlük sağlayıp sağlamayacağını belirleyecek. Her iki durumda da Al-BSF öldü, PERC ölüyor ve gelecek pasifleştirilmiş bağlantılara ait.

---

## İleriye Bakmak

Yarın kristalin silikonu tamamen geride bırakacağız - en azından bir günlüğüne. **10. Gün: İnce Film Alternatifleri** kadmiyum tellür (CdTe), bakır indiyum galyum selenit (CIGS) ve amorf silikon teknolojilerini ele alıyor; bunlar maliyet verimliliği konusunda tamamen farklı bir yaklaşım benimsiyor. First Solar neden zehirli ağır metalden yapılmış bir teknolojiye 5 milyar dolar yatırdı? CdTe nasıl belirli iklimlerde watt başına en ucuz güneş enerjisi teknolojisi haline geldi? Ve neden ince film, kristal silikonun ezici maliyet düşüşlerine rağmen inatla ölmeyi reddediyor? Cevaplar beklediğinizden daha ilginç.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-09.toml}}
