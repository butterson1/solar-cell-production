# 9. Gün: Hücre Mimarileri — PERC, TOPCon, HJT

*Sekiz gündür silikonu kuvarsit madeninden serigrafi baskılı güneş hücresine kadar takip ediyorsunuz. Ama bu anlatımda tarif ettiğimiz "standart" hücre — alüminyum arka yüzey alanlı (Al-BSF) tasarım — ~%20 verimliliğe ulaşmış ve 2025'te artık esasen müze parçası. Gerçek sektör üç gruba ayrıldı: PERC, TOPCon ve HJT — her biri aynı sorunun farklı yanıtı üzerine milyarlarca dolar yatırıyor: Elektronların yüzeylerde ölmesini nasıl durdurursunuz?*

---

## Ortak Düşman: Yüzey Rekombinasyonu

Üç mimariyi anlamadan önce hepsinin çözmeye çalıştığı sorunu kavrayalım — çünkü aynı sorun, ve sinir bozucu kadar inatçı.

Bir foton elektron-delik çifti oluşturduğunda (1. Gün), bu çift p-n eklemine ulaşacak, ayrılacak ve dışarı akacak kadar uzun yaşamalı. Saf monokristalin silikonun iç kısmında elektron milisaniyeler boyunca yaşayabilir — yüzlerce mikrometre yayılmaya yetecek kadar.

**Sorun yüzeylerde.** Kristal kafes yüzeyde aniden biter ve geride "sarkan bağlar" kalır — elektron tuzakları. İşlenmemiş bir yüzeyde rekombinasyon hızı 10⁶ cm/s'yi aşar. İyi pasifleştirilmiş yüzey? 2 cm/s'nin altı. **500.000 kat fark.**

> 💡 **Ön yüzey** büyük ölçüde 6–7. Gün'lerde çözüldü (fosfor difüzyonu + SiNₓ ARC). Üç mimarinin gerçekten ayrıştığı ve son on yılın verimlilik kazanımlarının geldiği yer **arka yüzey.**

Eski Al-BSF hücresinde arka tarafa basitçe alüminyum macun basılıp ateşleniyordu — mütevazı pasivasyon (~200–500 cm/s rekombinasyon hızı) ve orta seviye yansıma (~%60–70). İşe yarıyordu ama masada en az **%2–4 mutlak verimlilik** bırakıyordu.

> ⚡ **%0,1'in değeri:** Mutlak verimliliğin her %0,1'i, 50 GW üretim hattında modül değeri olarak yılda **100–150 milyon $** demek.

---

## PERC: Her Şeyi Değiştiren Görevli

**Pasifleştirilmiş Yayıcı ve Arka Hücre** (Passivated Emitter and Rear Cell)

1983'te Martin Green'in ekibi tarafından icat edildi, ama üretim gerçekliğine geçmesi **30 yıl** sürdü. Konsept aldatıcı derecede basit:

Arka yüzeyin tamamını alüminyumla kaplamak yerine:
1. İnce bir dielektrik pasivasyon katmanı biraktır (Al₂O₃ + SiNₓ)
2. Lazerle küçük kontak delikleri aç

**Neden işe yarıyor:**

- **Pasivasyon:** Al₂O₃ yüzeyde negatif yük taşır → elektronları arka yüzeyden uzaklaştırır. Rekombinasyon hızı ~300 cm/s'den **<10 cm/s'ye** düşer → **~%1 verimlilik** kazancı.
- **Ayna etkisi:** Dielektrik yığın, uzun dalga boylu fotonları **%90–96** verimlilikle geri yansıtır (Al-BSF'nin %65'ine karşı) → **~%0,3–0,5** ek verimlilik.

> 🎯 **PERC'ün süper gücü: Geriye dönük uyumluluk.**
> Mevcut Al-BSF hatlarına yalnızca iki adım eklemek yeterli (Al₂O₃ biriktirme + lazer delme). Yenilenme maliyeti: 10–20 milyon $. Sıfırdan TOPCon veya HJT hattı: 100+ milyon $. PERC'ün sektörü bu kadar hızlı fethetmesinin sebebi buydu.

2020'de PERC, neredeyse sıfırdan küresel üretimin **%80'inin** üzerine çıktı. LONGi Green Energy, PERC'e bahse girdi ve muazzam kazandı — orta kademe bir oyuncudan 60 milyar dolarlık bir deve dönüştü.

**Ama sınır yaklaşıyor:** Üretim PERC hücreleri %23,0–23,5'e ulaşırken, pratik tavan ~%24,5. Sektör tavanın %95'inde — kuyu kuruyor.

---

## TOPCon: Görünen Varis

**Tünel Oksit Pasifleştirilmiş Temas** (Tunnel Oxide Passivated Contact)

PERC'ün en olası halefi — ve 2026 başında yeni kapasite eklemelerinde PERC'yi çoktan geride bıraktı.

**Ana fikir (fiziği güzel):**

PERC'te lazerle açılan deliklerdeki metal-silikon temasları rekombinasyon sıcak noktaları oluşturuyordu. TOPCon bunu "metal silikon levhaya hiç temas etmeden akım çeken" bir yapıyla çözer:

1. **Ultra ince tünel oksit** (~1,2 nm SiO₂, 5–7 atom katmanı) — elektronların kuantum tünelleme ile geçeceği, ama yüzeyi kimyasal olarak pasifleştirecek kadar ince.
2. **Katkılı poli-Si katman** (50–200 nm, ağır n-katkılı) — alan etkili pasivasyon + yanal akım taşıma.
3. **Metal kontaklar yalnızca poli-Si'ye temas eder** — kristalin tabakaya asla dokunmaz.

> 💡 **Tünel oksit — 1,2 nanometre:**
> Bu, 5–7 atom sırasından oluşan bir tabaka. 182 mm levha üzerinde tekdüze büyütmek olağanüstü zordur. Tek bir iğne deliği akımı kesen bir "şant" yaratır ve voltajı öldürür.

**Sonuçlar:**

| Metrik | PERC | TOPCon |
|--------|------|--------|
| Arka yüzey J₀ | 20–50 fA/cm² | **2–5 fA/cm²** |
| Voc | 680–690 mV | **710–720 mV** |
| Üretim verimi | %23,0–23,5 | **%25,0–25,5** |
| Rekor | %24,06 | **%26,89** (JinkoSolar) |

Teorik limit ~%28,7 — hâlâ anlamlı ilerleme alanı var.

**Geçiş hızı:** PERC → TOPCon dönüşüm maliyeti 5 GW tesis için ~30–50 milyon $. Çinli üreticiler (Tongwei, Jinko, Trina, JA Solar) PERC filosunu büyük hızla TOPCon'a dönüştürüyor. 2025 sonunda küresel TOPCon kapasitesi **500+ GW** — sanayi tarihinin en hızlı teknoloji geçişlerinden biri, ~3 yılda.

> 🎯 **Önemli detay:** Çoğu TOPCon hücresi **n-tipi levha** kullanır (PERC'ün p-tipi levhasının tersi). N-tipi silikon, p-tipi hücrelerde ilk yılda %1–3 güç kaybına neden olan bor-oksijen ışık bozunmasından (LID) etkilenmez. Dezavantaj: n-tipi levhalar %5–10 daha pahalı.

---

## HJT: Zarif Yabancı

**Heteroeklem Teknolojisi** (Heterojunction Technology)

Üç mimari arasında en zarif ve geleneksel üretimden en farklı olanı. PERC ve TOPCon'un evrimsel olduğu yerde HJT tamamen farklı bir hayvan.

1990'larda Sanyo'dan (şimdi Panasonic) gelen fikir: 800–900°C'de difüzyon fırınları yerine, kristalin levha üzerine ultra ince **amorf silikon (a-Si:H)** katmanları biriktirilir — tüm süreç **200°C'nin altında**.

**HJT yığını (arkadan öne):**

| Katman | Kalınlık | İşlev |
|--------|---------|-------|
| Metal kontaklar | — | Akım toplama |
| TCO (ITO) | ~75 nm | Şeffaf iletken |
| p-katkılı a-Si:H | ~5–10 nm | P-n eklemi |
| **İçsel a-Si:H** | **~5–8 nm** | **Pasivasyon büyüsü** |
| n-tipi c-Si levha | 130–150 μm | Ana emici |
| İçsel a-Si:H | ~5–8 nm | Pasivasyon |
| n-katkılı a-Si:H | ~5–10 nm | Arka alan |
| TCO (ITO) | ~75 nm | Şeffaf iletken |
| Metal kontaklar | — | Akım toplama |

Kritik katman: yalnızca 5–8 nm kalınlığındaki **içsel (katkısız) amorf silikon**. Kristalin silikon yüzeyindeki neredeyse her sarkan bağı doyurarak bilim dünyasının bildiği en iyi yüzey pasivasyonunu sağlar: **750+ mV** Voc.

> ⚡ **Şaşırtıcı gerçek:** HJT hücreleri PERC veya TOPCon'dan **daha az işlem adımına** sahip! Sadece 4–5 ana adım (doku + temizlik → a-Si biriktirme → TCO → metal). PERC'ün ~10, TOPCon'un ~12 adımına karşı.

**Ama sorunlar var:**

- **Sıcaklık kısıtı:** a-Si ~200°C üzerinde kristalleşir → geleneksel gümüş macunu ateşlemesi (750–850°C) kullanılamaz → düşük sıcaklıklı özel macunlar gerekir → **daha fazla gümüş** (15–20 mg/W vs TOPCon 10–13 mg/W)
- **Ekipman maliyeti:** Angstrom seviyeli kalınlık kontrolü gerektiren PECVD araçları, 15–25 milyon $/adet. Tam hat: GW başına **80–120 milyon $** (TOPCon: 50–70 milyon $)
- **İndiyum sorunu:** Her hücre ~200–300 mg indiyum (ITO). Küresel indiyum üretimi ~900 ton/yıl. 500 GW HJT, ~1.500 ton indiyum gerektirir — mevcut arzın çok üstünde.

---

## Karşılaştırma Tablosu

| Metrik | PERC | TOPCon | HJT |
|--------|------|--------|-----|
| Üretim verimi (2025) | %23,0–23,5 | %25,0–25,5 | %25,0–26,0 |
| Rekor | %24,06 | %26,89 | %27,30 |
| Tipik Voc | 680–690 mV | 710–720 mV | **740–750 mV** |
| İşlem adımı | ~10 | ~12 | **~5** |
| Maks. proses sıcaklığı | 850°C | 850°C | **200°C** |
| Gümüş (mg/W) | 12–15 | **10–13** | 15–20 |
| GW başına yatırım | 40–60 M$ | 50–70 M$ | 80–120 M$ |
| Sıcaklık katsayısı | −0,38%/°C | −0,32%/°C | **−0,26%/°C** |
| Çift yüzeyli faktör | %70 | %80–85 | **%90–95** |

> 🌡️ **Son iki satır neden önemli:**
> HJT'nin simetrik yapısı onu doğal olarak çift yüzlü kılar — yerden yansıyan ışıkla %5–15 ek enerji. Ve sıcaklık katsayısı en düşük: Sıcak iklimlerde (Orta Doğu, Hindistan) yıllık **%3–5 daha fazla** enerji üretimi.

---

## Piyasa Gerçeği: TOPCon Neden Kazanıyor (Şimdilik)

HJT'nin teknik üstünlüğüne rağmen TOPCon kapasite geliştirmede baskın. Neden? **Dönüşüm ekonomisi.**

Çin'in güneş üreticilerinin yüzlerce GW PERC hattı vardı. Bu hatlar watt başına kapasite başına 6–10 $ karşılığında TOPCon'a dönüştürülebildi. Yeni HJT hatları ise 80–120 $/W kapasite maliyeti — ve PERC hatları HJT'ye dönüştürülemez (ekipman tamamen farklı).

> 📈 **Durum özeti:**
> - Tongwei: 80+ GW PERC → TOPCon dönüşüm
> - JinkoSolar, JA Solar, Trina: Aynı strateji
> - TOPCon kapasitesi 2025 sonunda: **500+ GW**
> - HJT ölçekleniyor ama geride (Huasun, Risen, Maxwell)

**Ama yarış bitmedi.** HJT'nin gümüş sorunu (en büyük maliyet dezavantajı) çözülürse — bakır kaplama, SmartWire teknolojisi, düşük-gümüş macunlar — ve özellikle **perovskit-silikon tandem** hücreleri için HJT en uygun alt hücre olduğundan, 5 yıl içinde tablolar değişebilir.

**Net olan:** Al-BSF öldü. PERC ölüyor. Gelecek pasifleştirilmiş kontaklara ait.

---

## Yarına Hazırlık

Yarın kristalin silikonu tamamen bırakıyoruz — en azından bir günlüğüne. **10. Gün: İnce Film Alternatifleri** — kadmiyum tellür (CdTe), CIGS ve amorf silikon. First Solar neden zehirli ağır metalden yapılmış bir teknolojiye 5 milyar $ yatırdı? CdTe nasıl belirli iklimlerde en ucuz güneş teknolojisi oldu? Ve ince film, kristalin silikonun ezici maliyet düşüşüne rağmen neden inatla ölmeyi reddediyor?

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-09.toml}}
