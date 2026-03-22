# 7. Gün: Yansıma Önleyici Kaplamalar ve Yüzey Dokulandırma

*Dünün katkılanmış levhası çalışan bir elektronik cihazdır — fotonlardan oluşan yük taşıyıcılarını ayırabilen p-n eklemi. Ama ışığa tuttuğunuzda sorunu hemen görürsünüz: Bu bir ayna. Cilalı silikon gelen ışığın yaklaşık %35'ini yansıtır. Fotonların üçte biri doğrudan gökyüzüne geri sekerken, hiçbiri elektrik üretme şansı bulamaz. Hücrenin teorik maksimumu %29 ise, girişteki %35'lik kayıp sizi daha baştan ~%19'a düşürür. Bugün, 1800'lerden bu yana bilinen fiziği nanometre hassasiyetinde uygulayarak bu sorunu çözüyoruz.*

---

## Silikon Neden Ayna Gibi Parlak?

Bu bir tesadüf değil — silikonun iyi bir güneş hücresi malzemesi yapan aynı elektronik yapısının doğrudan sonucu. Işık, iki malzeme arasındaki sınırda kırılma indekslerinin farkına oranla yansır.

- Hava: n = 1,0
- Silikon: n = 3,5–6,0 (görünür spektrumda)

Bu devasa fark, Fresnel denklemiyle **%35** yansımaya karşılık gelir. Ne kadar saf, ne kadar mükemmel katkılanmış olursa olsun — her düz silikon yüzey görünür ışığın üçte birinden fazlasını geri yansıtır.

> 💡 **Karşılaştırma:**
> - Cam (n ≈ 1,5): ~%4 yansıma
> - Su (n ≈ 1,33): ~%2 yansıma
> - Elmas (n ≈ 2,42): ~%17 yansıma
> - Silikon (n ≈ 3,9): **~%35 yansıma**

Bu sorunu çözmenin tam olarak iki yolu var: **(1)** Yüzeye optik bir kaplama eklemek (yansıma önleyici kaplama) ve **(2)** yüzeyin geometrisini değiştirmek (dokulandırma). Modern güneş hücreleri **ikisini birden** yapar.

---

## Yansıma Önleyici Kaplamalar: İnce Film Hilesi

Prensip 1886'dan beri biliniyor (Lord Rayleigh): Hava ve silikon arasında, uygun kalınlık ve kırılma indeksinde ince bir film yerleştirirseniz, üst ve alt yüzeylerden yansıyan ışık birbirini **yok eder** (yıkıcı girişim).

**Mükemmel yansıma önleme koşulları:**

1. **Kaplama kırılma indeksi:** n = √(n_hava × n_silikon) = √(1,0 × 3,9) ≈ **2,0**
2. **Kalınlık:** Hedef dalga boyunun çeyreği. 600 nm için: d = 600/(4 × 2,0) = **75 nm**

Yalnızca 75 nanometre kalınlığındaki bir katman — insan saçının genişliğinin 1/700'ü — 600 nm'deki yansımayı neredeyse tamamen yok edebilir.

> 🎨 **Güneş hücreleri neden mavi?**
> Kaplama ~600 nm'de (turuncu) optimize edilir — o dalga boyunda yansıma neredeyse sıfır. Ama daha kısa dalga boylarında (mavi, 400–500 nm) kalınlık artık tam "çeyrek dalga" değildir ve yansıma %5–10'a çıkar. Gördüğünüz mavi renk, kaplamanın **bastıramadığı** ışıktır. En iyi optimize edilmiş hücreler neredeyse siyah görünür.

---

## Silikon Nitrür: Üç İşi Tek Kaplamayla

1970–80'lerde titanyum dioksit (TiO₂) kullanılıyordu — iyi çalışıyordu ama sadece yansıma önlemekti. Devrim, **silikon nitrürün (SiNₓ:H)** aynı anda **üç** işi yapabildiğinin keşfiyle geldi:

### 1. Yansıma Önleme
SiNₓ'nin kırılma indeksi 1,9–2,1 aralığında ayarlanabilir — silikon için neredeyse ideal.

### 2. Yüzey Pasivasyonu (Oyun Değiştirici!)
SiNₓ:H filmi %10–15 oranında hidrojen içerir. Sonraki ateşleme adımında (~800°C) bu hidrojen silikon yüzeyine yayılarak **sarkan bağları** doyurur.

> 💡 **Sarkan bağ nedir?**
> Kristal kafesin sona erdiği yüzeyde, bağlanacak komşu bulamayan atomların eşleşmemiş elektronları. Her biri bir rekombinasyon tuzağı — fotojenere elektronları yakalayıp yok eden. Hidrojen bu tuzakları "kapatır."

Sonuç: Yüzey rekombinasyon hızı >100.000 cm/s'den (çıplak silikon) **<10 cm/s'ye** düşer — **10.000 kat** iyileşme!

### 3. Yığın Pasivasyonu
Hidrojen yüzeyde durmaz — ateşleme sırasında silikonun derinliklerine de yayılarak kristal kusurlarını, tane sınırlarını ve metalik safsızlık komplekslerini nötralize eder.

**PECVD işlemi:** Levhalar vakum odasına girer, silan (SiH₄) + amonyak (NH₃) gaz karışımı 13,56 MHz RF plazma ile ayrıştırılır, 350–450°C'de 75 nm film biriktirilir. Süre: ~3–5 dakika.

> ⚡ **Tek sayıyla özetlemek gerekirse:**
> SiNₓ:H PECVD eklenmesinden gelen verimlilik kazancı genellikle **3–5 mutlak yüzde puanı**. Güneş pili üretiminde başka hiçbir tek adım bu kadar büyük performans artışı sağlamaz.

---

## Yüzey Dokulandırma: Fotonlara İkinci Şans

Kaplamalar güçlüdür ama yalnızca tek dalga boyunda ve tek açıda mükemmel çalışır. Tamamlayıcı yaklaşım: **yüzeyi pürüzlü yapmak.**

Fikir basit: Silikon yüzeyi küçük **piramitlerle** kaplıysa, bir piramit yüzeyinden yansıyan foton bitişik yüzeye sekererk ikinci bir giriş şansı yakalar. Her sıçrama yansıyan oranı çarpımsal olarak azaltır:

- Düz yüzey: %35 yansıma
- İki sıçrama: 0,35 × 0,35 = **%12,3**
- Üç sıçrama: 0,35³ = **%4,3**
- ARC ile birleşince: **<%0,1** toplam yansıma mümkün

<!-- 📊 [DİYAGRAM ÖNERİSİ: Düz silikon yüzeyde tek yansıma vs piramitli yüzeyde çoklu sıçrama — ışık ışınlarının yolunu gösteren basit geometrik çizim.] -->

### Monokristalin İçin: Alkali Dokulandırma

Monokristalin silikon güzel bir kristalografik sır barındırır: Sıcak KOH (potasyum hidroksit) çözeltisi, farklı kristal düzlemlerini çok farklı hızlarda aşındırır. (111) düzlemleri, (100) düzlemlerinden **30–50 kat** daha yavaş aşınır. Sonuç: (100) yönlendirilmiş bir levhayı KOH'a daldırdığınızda, 54,7° taban açılı **rastgele dik piramitler** oluşur — tipik olarak 1–10 μm boyunda.

İşlem: %1–5 KOH, 70–80°C, 15–30 dakika, izopropil alkol (IPA) veya yüzey aktif madde katkılı.

Sonuç: ARC ile birlikte **%1,5–3** ağırlıklı ortalama yansıma — düz yüzeydeki %35'ten **%90–95 azalma**.

### Çok Kristalli İçin: Asit Dokulandırma

Çok kristalde rastgele tane yönlenmeleri alkali dokulamayı bozar. Bunun yerine HF/HNO₃ asit karışımı kullanılır — kristal yönünden bağımsız, yuvarlak çukurlar ve tepecikler oluşturur. Optik sonuç daha kötü: ARC ile ~%5–8 yansıma.

> 🎯 **Bu fark, çok kristalin pazar payını kaybetmesinin nedenlerinden biri.** 2015'te çok kristal küresel üretimin ~%55'iydi. 2024'te %10'un altına düştü.

---

## Siyah Silikon: Doğanın İlham Verdiği Yüzey

En iyi yüzey dokusu piramitler değil — **nano ölçekli iğne ormanları.** Plazma veya kimyasal aşındırma ile oluşturulan 100–500 nm yüksekliğinde sivri uçlar, o kadar çok ışık emer ki yüzey tamamen siyah görünür: Tüm spektrumda **%0,3'ten az** yansıma.

Fizik piramitlerden farklıdır: Nano sivri uçlar, havadan (n=1) silikona (n=3,9) **kademeli** bir kırılma indeksi geçişi oluşturur. Işık keskin bir sınır görmez; yumuşak bir geçiş görür. Bu aynı prensip güvelerin gözlerinde var — güvelerin karanlıkta gözleri parlamadan görebilmesi için doğal olarak evrimleşmiş.

Sorun: Devasa yüzey alanı = daha fazla sarkan bağ = daha fazla rekombinasyon. Siyah silikon ancak Al₂O₃ atomik katman biriktirme gibi gelişmiş pasivasyonla birleşince pratik oldu.

---

## Arka Taraf Optikleri

Ön yüzeye odaklandık ama arka tarafta da foton yönetimi var. Uzun dalga boylu fotonların (900–1200 nm) %20–30'u, emilmeden 170 μm'lik levhadan geçer.

- **Eski Al-BSF hücre:** Alüminyum arka yüzey ~%60–70 yansıma
- **Modern PERC:** Dielektrik yığın (Al₂O₃ + SiNₓ) **>%95** dahili arka yansıma

Ayrıca **çift yüzlü (bifacial) hücreler** — her iki taraftan ışık toplayan — arka taraftaki doku ve ARC'yi ön yüzey kadar önemli kılıyor (4. Hafta'da detaylı).

---

## Optik Yığın: Hepsi Bir Arada

Modern monokristalin PERC hücresinin yukarıdan aşağıya optik yapısı:

| Katman | Kalınlık | İşlev |
|--------|---------|-------|
| Hava | — | — |
| SiNₓ:H ARC | 75 nm | Yansıma önleme + pasivasyonu |
| Dokulu Si yüzey | 3–8 μm piramitler | Çoklu sıçrama ile ışık yakalama |
| Si yığın (yayıcı + taban) | ~170 μm | Foton emilimi + taşıyıcı üretimi |
| Al₂O₃ arka pasivasyonu | 5–10 nm | Pasivasyon + arka yansıma |
| SiNₓ arka dielektrik | 100–120 nm | Arka yansıma + koruma |

**Kombinasyon etkisi:** Ön ARC + doku → ağırlıklı ortalama ön yansıma ~%1,5–2,5. Arka dielektrik → >%95 dahili yansıma. Toplam olarak cilalı, kaplanmamış bir hücreye kıyasla ~**5–7 mA/cm²** ek fotoakım — bu, SiNₓ pasivasyonuyla birleştirilince **6–8 yüzde puanlık** verimlilik artışı demek.

---

## Kimyasal Atık Gerçeği

Dokulandırmanın az konuşulan yanı: KOH dokulandırma levha başına 2–4 litre çözelti tüketir; asit dokulandırma daha da kötü (HF ve HNO₃ — HF cilde nüfuz edip kemik kalsiyumuna saldırır). Günde 500 milyon levha işleyen küresel endüstri, devasa bir kimya akışı üretir.

Modern çözümler: Kimya geri dönüşüm sistemleri (%60–80 azalma), kapalı devre su sistemleri (levha başına 15 L → 3 L'nin altı). Ama ıslak kimyaya bağımlılık, güneş üretiminin çevresel sıkıntı noktalarından biri olmaya devam ediyor.

---

## Yarına Hazırlık

Levha hazırlama üçlememiz tamamlandı: doplama (6. Gün) bize p-n eklemini, bugünkü doku + ARC bize optik ön ucu verdi. Levha artık güneş ışığından verimli bir şekilde yük taşıyıcıları üretebilir. Ama hâlâ akımı *dışarı* çıkarmanın yolu yok — elektrik bağlantıları henüz yapılmadı.

Yarın **serigrafi baskı ve metalizasyon** — ön tarafa gümüş şebeke çizgileri, arkaya alüminyum yerleştirme. Tişört baskısından ödünç alınan bu teknik, gram başına silikon levhadan daha değerli macunlar kullanıyor ve imkansız bir ödünleşmeyle karşı karşıya: eklediğiniz her metal çizgi akımı toplar ama gelen ışığı engeller. Bu iğneye nasıl iplik geçiriyorsun? 8. Gün.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-07.toml}}
