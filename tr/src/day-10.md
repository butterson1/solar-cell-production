# 10. Gün: İnce Film Alternatifleri — CdTe, CIGS, Amorf Si

*Dokuz gün boyunca kristalin silikon dünyasının derinliklerindeydik — külçeler, levhalar, eklemler, kontaklar. Ama çerçeveyi genişletin: Bugün üretilen güneş panellerinin ~%95'i kristalin silikon. Kalan %5? Güneş hücresi tasarımında kökten farklı bir felsefe — levhayı çöpe atan, yarı iletkenleri yüzlerce mikrometre yerine birkaç mikrometre kalınlığında biriktiren, ve en az bir durumda Amerikan tarihinin en kârlı güneş şirketini kuran bir felsefe.*

---

## Temel Soru: Neden İnce?

İnce filmi takdir etmek için kristalin silikondaki gizli bir verimsizliği anlamamız gerekiyor.

Silikon **dolaylı bant aralıklı** bir yarı iletken. Bu ne anlama geliyor?

> 💡 **Doğrudan vs dolaylı bant aralığı — basit anlatım:**
> **Doğrudan bant aralığında** foton tek adımda emilir — fotonun enerjisi ve momentumu geçiş için tam uyumlu.
> **Dolaylı bant aralığında** (silikon) foton tek başına yetmez — eksik momentumu sağlamak için aynı anda bir **fonon** (kafes titreşimi) gerekir. Bu üçlü etkileşim daha az olası → silikon ışığı **zayıf** emer.

Sonuç: Silikonun ışığın çoğunu yakalayabilmesi için **150–180 μm** kalınlığında olması gerekir.

**Kadmiyum tellür (CdTe)** ise doğrudan bant aralıklı — emilim katsayısı silikondan ~100 kat daha yüksek. Yalnızca **2 μm** CdTe, fotonların %99'undan fazlasını emer. **170 μm yerine 2 μm — malzemenin %2'sinden azı.**

> ⚡ **İnce filmin vaadi:**
> - 100 kat daha az yarı iletken malzeme kullan
> - Doğrudan cam veya esnek folyo üzerine biraktır
> - Polisilikon saflaştırma, kristal büyütme, levha dilimleme zincirinin tamamını atla
> - Bu zincir bir güneş modülü maliyetinin ~%40'ı

Peki neden kristal silikon hâlâ %95 pazar payında? Çünkü şeytan ayrıntıda gizli.

---

## CdTe: First Solar Mucizesi

Kadmiyum tellürün hikâyesi tek bir şirketten ayrılamaz: **First Solar** (Tempe, Arizona). Dünyanın en büyük ince film üreticisi, en büyük on panel üreticisi arasında Çinli olmayan tek şirket. 2024 geliri: 3,5+ milyar $. Tamamen Çin kristalin silikonunun hâkim olduğu bir pazarda hayatta kalmak ve büyümek — temiz enerji alanındaki en ilginç hikâyelerden biri.

### CdTe Nasıl Üretilir?

Kristalin silikondan şaşırtıcı derecede farklı. Bir silikon hücrenin hammaddeden bitmiş hücreye 3–4 gün sürdüğü yerde, First Solar bir CdTe modülünü **~4,5 saatte** bitirir.

1. **Cam girer:** Düşük demirli soda-kireç cam (~5–8 $/m²)
2. **TCO kaplanır:** Şeffaf iletken oksit (SnO₂:F) — ön elektrot
3. **CdS tampon katman:** 80–150 nm n-tipi kadmiyum sülfür — p-n eklemini oluşturur
4. **CdTe biriktirme (VTD):** CdTe tozu ~500–600°C'de süblimleştirilir, buhar cam üzerine yoğunlaşır. Dakikada 1–5 μm — **birkaç dakikada** 2–4 μm emici katman (CZ'nin 4–5 *saatine* kıyasla)
5. **CdCl₂ aktivasyonu:** 380–420°C'de tanecikleri büyütür, tane sınırlarını pasifleştirir. Bu adım olmadan verim sadece ~%10; bu adımla **%18'in** üzerine çıkar
6. **Arka kontak + cam laminasyonu:** Cam-cam modül

> 💡 **Modern gelişme:** First Solar, CdS tamponunu **MgZnO** (magnezyum çinko oksit) ile değiştirmeye başladı — daha geniş bant aralığı (%3,3 eV) daha fazla mavi/UV fotonun geçmesine izin veriyor.

### Rakamlar

| Metrik | CdTe (First Solar S7) | Kristalin Si (TOPCon) |
|--------|----------------------|----------------------|
| Modül verimi | %19,2–19,8 | %22–24 |
| Hücre rekoru | %22,3 | %26,89 |
| Sıcaklık katsayısı | **−0,28–0,32%/°C** | −0,32–0,45%/°C |
| Üretim maliyeti | ~0,26–0,28 $/W | ~0,22–0,26 $/W |

> ⚡ **Mantığa aykırı gerçek:** Birçok gerçek dünya koşulunda CdTe daha yüksek verimli c-Si'den **daha iyi performans** gösterir. Çöl kurulumlarında modül sıcaklıkları 65–70°C'ye ulaştığında CdTe nominal gücünün **%2–3 daha fazlasını** korur. Tüm yıl boyunca enerji verimini (kWh/kWp) hesapladığınızda, CdTe kağıt üzerinde %3–4 daha verimli c-Si modüllerle eşleşebilir veya geçebilir.

### Kadmiyum Sorusu

Her CdTe tartışmasında odadaki fil: kadmiyum bilinen bir kanserojen.

**Ama gerçeklik daha nüanslı:**

- CdTe bileşiğinde kadmiyum tellüre bağlı — erime noktası 1.041°C, ortam koşullarında buharlaşma yok
- İki temperli cam arasında kapsüllenmiş — çevreye sızma neredeyse imkansız
- Yangın testlerinde bir CdTe modülü, aynı elektriği üretmek için yakılacak kömürden **daha az** kadmiyum salıyor
- First Solar, %90 yarı iletken + %90 cam geri kazanan sektörün **tek kapsamlı geri dönüşüm programını** yürütüyor

> 🎯 **Şaşırtıcı detay:** CdTe'de kullanılan kadmiyumun çoğu **çinko madenciliğinin atık yan ürünü.** Güneş paneli almayanlar bile bu kadmiyum çıkartılmak zorunda — aksi halde tehlikeli atık olarak depolanır. Güneş paneli aslında onu sabit, geri dönüştürülebilir formda *ayırıyor.*

---

## CIGS: Parlak Ama Zor Deha

**Bakır İndiyum Galyum Diselenid — Cu(In,Ga)Se₂**

Herhangi bir ince film teknolojisi arasında en yüksek laboratuvar verimliliğine sahip: **%23,64** (Uppsala Üniversitesi, 2024). 1,0–1,7 eV ayarlanabilir doğrudan bant aralığı. Esnek yüzeylere biriktirilme yeteneği.

### Üretim Zorluğu

CIGS dörtlü bir bileşik — dört elementin hassas stokiyometride biriktirilmesi gerekiyor.

**Birlikte buharlaştırma** (en iyi sonuçlar): Cu, In, Ga, Se aynı anda 400–600°C'de vakumda buharlaştırılır. "Üç aşamalı" işlem, bant aralığının film kalınlığı boyunca değiştiği sofistike bir yapı oluşturur — zarif fizik ama dört buharlaşma kaynağını ±%2 kontrol etmek kabus.

**Püskürtme + selenizasyon** (üretim dostu): Metal katmanlar oda sıcaklığında püskürtülür, sonra selenyum atmosferinde 450–550°C'de tavlanır. Daha ölçeklenebilir ama tipik olarak daha düşük verim.

### Neden Ticari Başarısızlık?

Kayıp listesi uzun: Solyndra (535 milyon $ DoE kredisi, 2011 iflas), Nanosolar, MiaSolé, HelioVolt…

**Temel sorunlar:**
- Sermaye harcaması: 0,70–1,00 $/W (c-Si: 0,30–0,40 $/W)
- Üretim modül verimi: %15–17 (c-Si: %21–24)
- Dört elementli vakum bazlı işlem doğası gereği karmaşık

**CIGS'in parladığı yerler:**
- Esnek modüller (kavisli çatılar, araçlar)
- Hafif paneller (havacılık)
- Estetik cephe uygulamaları (tek tip siyah, şebeke çizgisi yok)
- Ve belki gelecekte: **perovskit-CIGS tandem** alt hücresi

---

## Amorf Silikon: İlk İnce Film

Hesap makinesini güneşle çalıştıran teknolojiyi hatırlıyor musunuz? İşte o.

Amorf silikon (a-Si) kristalin silikonun tam tersi: uzun menzilli düzen yok, atomlar "kabaca doğru" geometriyle bağlı ama öngörülebilir bir desen yok.

> 💡 **Paradoks:** Bu düzensizlik silikonu dolaylı bant aralığından etkili olarak **doğrudan bant aralığına** dönüştürür. Amorf silikon, görünür ışığı kristalin silikondan **~40 kat daha güçlü** emer — 0,3–0,5 μm kalınlık yeterli.

### Avantajlar
- PECVD ile düşük sıcaklıkta biriktirilir (150–300°C)
- Esnek plastik üzerine **rulodan ruloya** üretim mümkün
- Teorik olarak çok düşük maliyet

### Ölümcül Kusur: Staebler-Wronski Etkisi

Işığa maruz kalınca a-Si'deki zayıf bağlar kırılır, yeni rekombinasyon kusurları oluşur. İlk yüzlerce saatte verim **göreceli %10–30** düşer. %10'da başlayan bir hücre %7–8'de stabilize olabilir.

Üretim modüllerinde stabil verimlilik: **%6–8** — c-Si'nin üçte biri. Alan maliyetlerinin baskın olduğu yere monteli güneş enerjisinde bu verimlilik cezası yıkıcı.

### a-Si Nerede Hayatta?
- Hesap makineleri ve iç mekân cihazları (geniş bant aralığı iç mekân ışığıyla iyi eşleşir)
- **HJT hücrelerindeki pasivasyon katmanı** (9. Gün!) — amorf silikonun modern güneş enerjisindeki en önemli rolü kendi başına emici olmak değil, kristalin silikonda *pasivasyon katmanı* olmak olabilir

---

## 2025'te İnce Film: Dürüst Puan Kartı

İnce film, 2009'daki ~%17 zirvesinden küresel kapasitenin **~%5'ine** geriledi.

| Teknoloji | İnce film içindeki pay | Lider |
|-----------|----------------------|-------|
| CdTe | ~%45 | First Solar |
| CIGS | ~%25–30 | Avancis, çeşitli |
| a-Si | Geri kalan (küçülen) | Niş |

**İnce film neden silikonun yerini alamadı?**

1. **Çin c-Si çok ucuzladı:** 2010'da ~1,50 $/W → 2024'te <0,10 $/W. Bu seviyede rakip etmek neredeyse imkansız.
2. **c-Si verimliliği artmaya devam etti:** %14–16 (2010) → %22–24 (2025). Fark daralmadı, *açıldı.*
3. **İnce filmin avantajları koşullu:** CdTe'nin sıcaklık avantajı en çok çöl iklimlerinde önemli, CIGS esnekliği niş, a-Si verimi düşük.

**Ama ince film ölmüyor.** First Solar'ın sipariş defteri yıllarca ileriye uzanıyor — ABD yerli üretim bonusları (IRA), Çin dışı tedarik zinciri tercihi ve ticaret savaşı güvencesi sayesinde. Alabama'da 3,5 GW kapasiteli yeni fabrikaya 1,1 milyar $ yatırım.

Ve CdTe'nin teorik verimlilik tavanı **~%32** (c-Si'nin %29,4'üne karşı) — modül verimlilik açığını kapatacak önemli alan mevcut.

---

## Büyük Ders

İnce film teknoloji rekabetiyle ilgili önemli bir şey öğretiyor: **En iyi fizik her zaman kazanmıyor.**

CdTe ve CIGS birçok açıdan silikondan *daha iyi* güneş enerjisi malzemeleri — ışığı daha verimli emer, çok daha az malzeme gerektirir, daha düşük sıcaklıklarda üretilir, neredeyse ideal bant aralıklarına sahip.

Ama silikon, yarı iletken endüstrisinden 30 yıllık bir avantaja, milyonlarca ton malzemeyi işleyen köklü bir tedarik zincirine ve muazzam ölçek ekonomilerine sahipti. Teknoloji yarışmaları sadece fizikle değil — ekonomi, altyapı ve yol bağımlılığıyla da ilgili.

Yarın **çok bağlantılı ve tandem hücreler** — tek bağlantılı verimlilik sınırını kabul etmeyi reddeden, güneş spektrumunun daha fazlasını yakalamak için farklı bant aralıklarına sahip malzemeleri üst üste istifleyen tasarımlar. İnce film malzemeleri nihayet silikonun yerini almak yerine onu *tamamlayan* mükemmel rolü bulabilir.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-10.toml}}
