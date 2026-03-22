# 6. Gün: Doplama — P-N Ekleminin Oluşturulması

*Elinizde silikon bir levha var. 170 mikrometre ince, her iki tarafı temizlenmiş, testere hasarından arındırılmış — yaklaşık 5 × 10²² atom içeren kusursuz bir kristal dilim. Ve elektriksel açıdan neredeyse tamamen işe yaramaz. Saf silikon çok kötü bir iletkendir: Trilyonda birden az atomu serbest yük taşıyıcısına katkıda bulunur. Bugün, inert silikonu güneş ışığını toplayabilen bir cihaza dönüştüren hassas kontrollü safsızlıkları ekliyoruz.*

---

## Kasıtlı Kirlilik Paradoksu

Bu kursta bugüne kadar yaptığımız her şey safsızlıkları *çıkarmakla* ilgiliydi. Siemens işlemi silikonu altı dokuza saflaştırdı. CZ kristal büyütmesi bu saflığı mükemmel bir kafeste korudu. Milyar başına parça kontaminasyon seviyelerine takıntılıydık.

Ve şimdi kasıtlı olarak kirletiyoruz.

Çelişki mi? Hayır — bütün mesele bu. Silikonu saflaştırdık ki **hangi yabancı maddelerin nereye, hangi miktarda gideceğini biz seçebilelim.** İşe yaramaz bir kirli silikon yığını ile çalışan bir güneş hücresi arasındaki fark, temizlik değil — *kontrollü* kirlilik.

> 💡 **Doplama (Doping) nedir?**
> Saf silikona kasıtlı olarak belirli yabancı atomlar ekleme işlemidir. Doplama olmadan p-n eklemi olmaz, p-n eklemi olmadan elektrik alanı olmaz, alan olmadan fotonların oluşturduğu elektronlar rastgele dolaşarak ısıya dönüşür — güneş hücresi yerine süslü bir ısıtıcınız olur.

---

## Atomik Resim: Nasıl Çalışıyor?

Silikon periyodik tablonun 14. grubunda: dört dış elektronu, dört kovalent bağ, herkes memnun. Her elektron hesaplanmış. Hiçbir şey kalmamış, hiçbir şey eksik değil.

### Fosfor Eklersek (n-tipi)

Fosfor 15. grupta: **beş** dış elektron. Kafese girdiğinde dört komşuyla bağ yapıyor ama bir elektronu açıkta kalıyor. Bu fazla elektron çok gevşek bağlı — oda sıcaklığında fiilen serbest.

→ Fosfor bir **verici** safsızlık: serbest elektron bağışlar.
→ Sonuç: **n-tipi silikon** (negatif çoğunluk taşıyıcıları).

### Bor Eklersek (p-tipi)

Bor 13. grupta: **üç** dış elektron. Üç bağ yapıyor ama dördüncü bağ eksik — bir **delik** var. Komşu bir elektron bu boşluğa atlayabilir ve delik ters yönde "hareket eder."

→ Bor bir **alıcı** safsızlık: bir delik (pozitif yük taşıyıcısı) oluşturur.
→ Sonuç: **p-tipi silikon** (pozitif çoğunluk taşıyıcıları).

> ⚡ **İnanılmaz oranlar:** Tipik güneş hücresi tabanında her 5 milyon silikon atomuna karşılık *bir* bor atomu var — yaklaşık %0,00002. Ama bu küçücük kirlilik, silikonun iletkenliğini **~15.000 kat** artırıyor.

---

## P-N Eklemi: Sihrin Gerçekleştiği Yer

Bir p-tipi tabaka alın (bor katkılı taban) ve yüzeyine ince bir n-tipi katman ekleyin (fosfor yayarak). Az önce **p-n eklemi** oluşturdunuz.

Sınırda çok güzel bir şey olur:

1. N tarafının fazla elektronları p tarafına yayılır; p tarafının delikleri n tarafına yayılır.
2. Her yayılma arkasında **sabit iyon** bırakır — n tarafında pozitif fosfor iyonları, p tarafında negatif bor iyonları.
3. Bu sabit iyonlar n'den p'ye doğru bir **elektrik alanı** oluşturur.

Bu alan 0,1–1 μm genişliğinde bir bölgede (tükenme bölgesi) sıkışmıştır ama şiddeti devasa: 10.000–100.000 V/cm. Toplam yerleşik gerilim ise yalnızca 0,6–0,7 volt.

> 🎯 **Anlam:** Fotovoltaik etkinin tamamı, kırmızı kan hücresinden daha ince bir bölgedeki 0,7 voltluk elektrik alanına dayanır. Geri kalan her şey — kaplamalar, metalizasyon, kapsülleme — bu fısıltı kadar ince arayüzü desteklemek için var.

<!-- 📊 [DİYAGRAM ÖNERİSİ: P-N eklem yapısı — p-tipi taban, n-tipi yayıcı, tükenme bölgesi, elektrik alan yönü, elektron ve delik hareketi. Etiketli kesit.] -->

---

## Fosfor Difüzyonu: Pratikte Nasıl Yapılıyor?

Baskın yöntem: **POCl₃ difüzyonu.** 800–900°C'ye ısıtılmış kuvars tüplü fırında, parti başına yaklaşık 1.200 levha işlenir.

**Adımlar:**

1. **POCl₃ dağıtımı:** Sıvı POCl₃ nitrojen gazıyla taşınır, oksijenle birlikte fırına beslenir:
   *4 POCl₃ + 3 O₂ → 2 P₂O₅ + 6 Cl₂*

2. **Fosfosilikat cam (PSG) oluşumu:** P₂O₅ levha yüzeyinde birikir, silikonla tepkimeye girerek 20–40 nm kalınlığında cam tabaka oluşturur — sürekli fosfor kaynağı.

3. **Difüzyon:** 850–900°C'de fosfor atomları silikonun içine yayılır. 20–30 dakikada yaklaşık 0,3–0,5 μm derinliğinde **n-tipi yayıcı** katman oluşur.

4. **PSG çıkarma:** Cam tabaka seyreltik HF (hidroflorik asit) ile sıyrılır.

> 💡 **Difüzyon benzetmesi:** Mürekkebin suda yayılmasıyla aynı matematik (Fick yasaları) — sadece çok daha yavaş ve çok daha kontrollü. Silikonda fosfor difüzyonu 880°C'de yaklaşık 3 × 10⁻¹⁴ cm²/s.

Modern bir difüzyon fırını saatte ~5.000 levha işleyebilir. Önde gelen üreticiler: Tempress (Hollanda), centrotherm (Almanya), Laplace Solar (Çin).

---

## Ölü Katman Sorunu

İşte günün mantık dışı gerçeği: **Yüzeyi daha iletken yapmak hücreyi daha kötü yapabilir.**

Fosfor difüzyonunda yüzey konsantrasyonu çok yüksek olur (>5 × 10²⁰/cm³). Bu bölgede kafes alabileceğinden fazla fosfor atomu var — fazlalar **rekombinasyon merkezleri** gibi davranır. Tam da mavi ve UV fotonların emildiği yerde elektronların öldüğü bir "ölü katman" oluşur.

**Çözüm:** **Seçici yayıcı** — metal kontakların altında yoğun katkı (düşük dirençe ihtiyaç var), kontaklar arasında hafif katkı (düşük rekombinasyon isteniyor). Modern PERC ve TOPCon hücreleri bunu farklı stratejilerle çözer — 9. Gün'de detaylarını göreceğiz.

---

## Bor Difüzyonu: Daha Zor Ama Giderek Daha Önemli

Geleneksel güneş hücrelerinde bor katkısı kristal büyümesi sırasında yapılırdı (CZ eriyiğine bor ekleme). Ama modern **TOPCon** hücreleri yapıyı tersine çevirdi: n-tipi taban + ön tarafta bor katkılı yayıcı.

Bor difüzyonu fosfordan daha zor:
- **Daha yüksek sıcaklık** gerekiyor (900–1.050°C)
- **Daha uzun süre** (30–60 dk vs fosfor için 20–30 dk)
- Oksijene çok hassas

Kaynak gaz olarak **BBr₃** (bor tribromür) kullanılır. 2025 itibarıyla TOPCon, PERC'yi geride bırakarak baskın yeni üretim teknolojisi oldu — bu da bor difüzyon kapasitesinin küresel olarak 300+ GW'a ulaştığı anlamına geliyor.

---

## İyon İmplantasyonu: Hassas Alternatif

Difüzyona alternatif olarak, katkı atomlarını bir parçacık ışınında hızlandırıp doğrudan silikona **fırlatabilirsiniz.** Bu, İyon implantasyonu — aslında küçük bir parçacık hızlandırıcısı.

**Avantajları:**
- ±%1 doz doğruluğu (difüzyonda ±%5–10)
- Cam tabaka yok — PSG/BSG sıyırma adımı gereksiz
- Maske olmadan seçici katkılama mümkün

**Dezavantajı:** Maliyet. Bir iyon implanteri 3–5 milyon $ — difüzyon fırınından 5–10 kat daha pahalı. Bu nedenle yaygınlaşması yavaş; ağırlıklı olarak yüksek verimli premium hücrelerde (Maxeon IBC hücreleri gibi) kullanılıyor.

---

## Doplama Profili: Rakamlar

Tamamlanmış bir güneş hücresinin doplama profili:

| Katman | Kalınlık | Katkı konsantrasyonu | Katkı maddesi |
|--------|---------|---------------------|---------------|
| Ön yayıcı (PERC) | 0,3–0,5 μm | 10¹⁹–10²⁰/cm³ | Fosfor |
| Taban (p-tipi PERC) | ~170 μm | 10¹⁶/cm³ | Bor |
| Arka BSF (PERC) | 5–10 μm | 10¹⁸–10¹⁹/cm³ | Alüminyum |

Yayıcı, hücre kalınlığının yaklaşık **%0,2'si** kadar ama bazdan **1.000–10.000 kat** daha yoğun katkılı. Katkı konsantrasyonu 170 μm boyunca dört büyüklük sırası değişiyor. Bu profili milyarlarca levhada doğru tutmak, üretimdeki temel zorluk.

---

## Yarına Hazırlık

Doplama, pasif bir levhayı aktif bir elektronik cihaza dönüştürdü — ama yeni katkılanmış levhanın hâlâ korkunç optik özellikleri var. Silikon parlaktır ve gelen ışığın yaklaşık **%35'ini** geri yansıtır. Fotonların üçte biri doğrudan geri sekerse, hiçbir akıllıca katkılama sizi kurtaramaz.

Yarın bu soruna çift yönlü saldırıyı göreceğiz: Yansımayı bastıran **yansıma önleyici kaplamalar** ve silikon yüzeye kazınmış piramitlerle ışığı yakalayan **yüzey dokulandırma**. Birlikte, ön yüzey yansımasını %35'ten **%2'nin** altına indirecekler.

---

## 🧪 Anlayışınızı Test Edin

{{#quiz quizzes/day-06.toml}}
