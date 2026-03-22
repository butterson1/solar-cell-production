# Day 3: The Siemens Process & Polysilicon Purification

*Yesterday we watched sand become metallurgical-grade silicon — 99% pure, smelted in arc furnaces at 2,000°C. Impressive, until you realize that the remaining 1% of impurities would completely destroy a solar cell's ability to function. Today, we follow the most important — and most energy-hungry — step in the entire solar supply chain: turning that dirty metal into polysilicon so pure that only one atom in a million is out of place.*

---

## Why 99% Pure Isn't Even Close

Let's start with a thought experiment. You've got a chunk of metallurgical-grade silicon (MG-Si) sitting on your desk. It's 99% silicon by mass. Sounds clean, right? It's not. That 1% impurity load contains iron, aluminum, calcium, titanium, boron, phosphorus, and a rogues' gallery of other elements. In absolute terms, a kilogram of MG-Si carries about 10 grams of foreign atoms.

Now here's why that matters. In a silicon solar cell, the critical property is how freely electrons can move through the crystal lattice. Iron atoms are recombination centers — they act like sticky traps that capture excited electrons before they can reach the cell's contacts and become useful current. A single iron atom per billion silicon atoms can cut a solar cell's efficiency in half. Boron and phosphorus, which we'll intentionally add during doping (Day 6), need to be controlled at the parts-per-billion level. If they're already there at parts-per-million concentrations, you've lost control of the device physics before you even start.

So the purification challenge is staggering: we need to take silicon from 99% purity (two nines) to 99.9999% purity (six nines) — an improvement of four orders of magnitude. For some applications, we need nine or eleven nines. And we need to do it cheaply enough that the resulting solar panels can compete with fossil fuels on price.

The solution the industry landed on, more than seven decades ago, is elegant in concept and brutal in execution: convert the silicon into a gas, purify the gas, then convert it back into a solid. This is the Siemens process, and it produces roughly 95% of all polysilicon used in solar cells worldwide.

## A Brief History of an Accidental Monopoly

The Siemens process was developed in the 1950s by the German conglomerate Siemens AG at their semiconductor research labs. The original goal had nothing to do with solar energy — they wanted ultra-pure silicon for transistors, at a time when germanium was still the dominant semiconductor material. Engineers at Siemens discovered that if you reacted silicon with hydrogen chloride gas to make trichlorosilane (HSiCl₃), you could distill that liquid just like petroleum, achieving extraordinary purity. Then you could decompose the trichlorosilane back into solid silicon by heating it in a hydrogen atmosphere.

For decades, this process was a niche operation serving the semiconductor industry. Global polysilicon production in 1990 was only about 20,000 metric tons per year, virtually all of it going to computer chips. Then the solar industry exploded. By 2023, global polysilicon production exceeded 1.5 million metric tons, with over 95% destined for photovoltaics. The chip industry's boutique chemistry had become one of the largest chemical engineering operations on Earth, and the Siemens process — originally designed for batches of a few hundred kilograms — had been scaled to factories producing 100,000+ tons per year.

The companies that dominate this market read like a geography lesson in energy economics: Tongwei, Daqo New Energy, Xinte Energy, and GCL-Poly in China; Wacker Chemie in Germany; OCI in South Korea; Hemlock Semiconductor in Michigan. China now controls roughly 90% of global polysilicon production, largely concentrated in Xinjiang and Inner Mongolia, where cheap coal-fired electricity (around $0.03–0.04/kWh) made the energy-intensive process economical. Wacker's plant in Burghausen, Bavaria, is the largest non-Chinese producer, running on hydroelectric power — which is why German polysilicon commands a premium as "low-carbon silicon."

## Step by Step: From Metal to Gas and Back

### Step 1: Making Trichlorosilane

The Siemens process begins by reacting crushed metallurgical-grade silicon with anhydrous hydrogen chloride (HCl) gas in a fluidized bed reactor at 300–350°C:

**Si + 3HCl → HSiCl₃ + H₂**

This produces trichlorosilane (TCS) — a colorless liquid that boils at just 31.8°C, barely above room temperature. The reaction also produces silicon tetrachloride (SiCl₄) as a byproduct, along with smaller amounts of dichlorosilane (H₂SiCl₂) and various metal chlorides from the impurities in the MG-Si.

Here's the key insight: by converting silicon into a volatile liquid, we've moved the purification problem into the domain of chemical engineering's most powerful separation tool — distillation. And distillation is something humans have been perfecting since the invention of whiskey.

### Step 2: Fractional Distillation

Trichlorosilane is fed into distillation columns — tall towers packed with structured packing material that maximizes surface area for vapor-liquid contact. Industrial TCS distillation columns can be 30–50 meters tall and operate continuously, processing hundreds of tons per day.

The beauty of this step is that different chlorosilane species and impurity chlorides have different boiling points. Boron trichloride (BCl₃) boils at 12.6°C, while phosphorus trichloride (PCl₃) boils at 76°C. Trichlorosilane sits right in between at 31.8°C. By running the distillation at carefully controlled temperatures and pressures, you can separate TCS from virtually all metal chloride impurities.

Multiple distillation stages are used in series. The first column does a rough cut, removing heavy-boiling contaminants (metal chlorides of iron, aluminum, titanium). The second and third columns perform progressively finer separations, targeting boron and phosphorus — the two impurities that matter most for semiconductor performance because they're electrical dopants. A well-run distillation train can reduce boron and phosphorus to below 0.1 parts per billion in the final TCS product.

This is distillation on a level that would make a Scotch distiller weep. We're not separating water from ethanol — we're separating molecules that differ by a few degrees in boiling point, and we need to hit purities measured in atoms per billion. The energy cost is substantial: distillation accounts for roughly 15–20% of the Siemens process's total energy consumption.

### Step 3: Chemical Vapor Deposition (The Siemens Reactor)

This is the heart of the process and the step that gives it its name. The Siemens reactor is a bell-shaped chamber — typically 2–3 meters in diameter and 2–3 meters tall — made of high-purity quartz or stainless steel. Inside, thin rods of ultra-pure silicon (called "slim rods" or seed rods) are mounted in an inverted U-shape, with two vertical rods connected by a horizontal bridge at the top. These slim rods are typically 7–10 mm in diameter.

Electrical current is passed through the slim rods, heating them to 1,050–1,150°C by resistive heating — the same principle as a toaster, but at temperatures that would melt glass. The purified TCS vapor, mixed with excess hydrogen gas (typically at a 3:1 to 5:1 H₂:TCS molar ratio), is fed into the reactor.

At the hot surface of the slim rods, the TCS decomposes:

**HSiCl₃ + H₂ → Si + 3HCl**

Silicon atoms deposit on the surface of the rods, building up layer by layer like a pearl forming around a grain of sand. Over a period of 5–7 days, the slim rods grow from their initial 7–10 mm diameter to massive U-shaped rods 150–200 mm in diameter. Each rod can weigh 100–150 kg at the end of a production run. A single reactor typically holds 24–48 pairs of rods, yielding 5–10 metric tons of polysilicon per batch.

Here's the surprising part: the conversion efficiency is terrible. Only about 10–15% of the trichlorosilane fed into the reactor actually decomposes into silicon. The rest exits as a mixture of unreacted TCS, SiCl₄, HCl, and H₂. This exhaust gas is captured and recycled — the SiCl₄ is hydrogenated back to TCS, and the HCl is recycled to the first step. A modern Siemens plant operates as a nearly closed chemical loop, with only small amounts of makeup HCl needed.

### The Energy Problem

Now for the uncomfortable truth. Those slim rods glowing at 1,100°C inside each reactor? They're consuming enormous amounts of electricity. A single Siemens reactor draws 1–3 megawatts of electrical power. Continuously. For five to seven days. A large polysilicon plant with hundreds of reactors can consume 500 MW or more — comparable to a small city.

The total energy requirement for Siemens-process polysilicon is 60–80 kWh per kilogram. For a standard 72-cell solar panel containing about 1.5 kg of polysilicon, that means roughly 100–120 kWh of electrical energy was consumed just in the polysilicon step alone — before crystal growth, wafering, cell fabrication, or module assembly. This single step accounts for about 30–40% of the total energy embodied in a finished solar panel.

This is why polysilicon production gravitates toward cheap electricity. At $0.04/kWh (cheap coal in Xinjiang), the electricity cost for one kilogram of polysilicon is about $2.80. At $0.10/kWh (typical European industrial rate), it's $7.00. When polysilicon sells for $7–10/kg, electricity cost alone determines whether a plant is profitable. It's not a technology race — it's an energy race.

## The Challenger: Fluidized Bed Reactors

The Siemens process works, but its energy hunger has always been its Achilles' heel. Starting in the 2000s, a competing technology emerged: the fluidized bed reactor (FBR), championed most aggressively by GCL-Poly (now GCL Technology) in China and by REC Silicon in Moses Lake, Washington.

Instead of depositing silicon onto hot rods, FBR technology feeds silane gas (SiH₄) — a simpler molecule than trichlorosilane — into a reactor containing a bed of tiny silicon seed particles. The gas decomposes at a lower temperature (600–800°C versus 1,100°C for Siemens), depositing silicon onto the seed particles. Hot gas blown upward from the bottom keeps the particles suspended — "fluidized" — ensuring uniform deposition. The growing particles eventually become heavy enough to sink to the bottom and are extracted as finished granular polysilicon, each granule about 1–3 mm in diameter.

The advantages are significant:

- **Energy consumption: 25–35 kWh/kg** — roughly half that of the Siemens process
- **Continuous operation** instead of batch processing (no 5–7 day cycles)
- **Granular product** that's easier to handle and feeds directly into crystal growth furnaces without the chunking step that Siemens rods require

The disadvantages? Surface area. Those tiny granules have an enormous surface-to-volume ratio compared to a massive Siemens rod, which means more surface contamination. Hydrogen and carbon impurities tend to be higher in FBR material. For years, FBR polysilicon was considered "solar-grade only" — fine for photovoltaics but not pure enough for semiconductors.

GCL's massive FBR plants in Jiangsu and Inner Mongolia have steadily closed this quality gap. By 2024, GCL claimed its granular polysilicon met the purity requirements for monocrystalline ingot growth, the dominant technology in modern solar. Their market share has grown to roughly 25–30% of global production, with the rest still Siemens-process material. The industry may be witnessing a slow-motion technology transition, but the Siemens process's seven decades of proven reliability keep it firmly in the lead.

## What Comes Out: The Polysilicon Product

After 5–7 days in the Siemens reactor, the power is cut, the reactor is opened, and out come those massive U-shaped rods — silvery-gray, crystalline, and extraordinarily pure. Each rod is a polycrystalline mass of silicon: millions of tiny silicon crystals fused together in random orientations, like a mosaic made of mirror fragments. This is why it's called "poly-silicon" — many crystals.

The rods are broken into irregular chunks using specialized crushing equipment — jaw crushers lined with ultra-pure materials to avoid recontamination. Each chunk is etched with hydrofluoric acid and deionized water to remove surface contaminants from handling, then tested.

Testing happens at multiple levels. Resistivity measurements (using a four-point probe) can detect dopant impurities in the parts-per-billion range. Fourier-transform infrared spectroscopy (FTIR) measures oxygen and carbon content. Glow-discharge mass spectrometry (GDMS) provides a complete elemental analysis down to parts-per-trillion for some elements. The specs for solar-grade polysilicon are demanding:

- **Boron:** < 0.3 parts per billion atomic (ppba)
- **Phosphorus:** < 0.5 ppba
- **Iron:** < 0.1 ppba
- **Total metals:** < 1 ppba
- **Carbon:** < 0.5 parts per million atomic (ppma)
- **Oxygen:** < 10 ppma (interstitial)

These chunks are then packed into clean polyethylene bags, placed in protective drums, and shipped to the next stop in the supply chain: the crystal growth furnaces. There, this randomly-oriented polycrystalline material will be melted and recrystallized into a single, perfectly ordered crystal — but that's tomorrow's story.

## The Environmental Ledger

No honest account of polysilicon production can skip the environmental picture. The Siemens process is chemical-intensive: hydrochloric acid, hydrogen gas (explosive), trichlorosilane (toxic and flammable), and silicon tetrachloride (a problematic byproduct that reacts violently with water to produce hydrochloric acid fumes).

In the early days of China's polysilicon boom (roughly 2005–2012), silicon tetrachloride disposal was a genuine scandal. Some smaller producers dumped SiCl₄ illegally, creating toxic wastelands. A 2008 Washington Post investigation documented barren fields near Chinese polysilicon plants where nothing would grow. The industry has since cleaned up significantly — modern plants convert virtually all SiCl₄ back into TCS for reuse, achieving closed-loop operation with minimal waste. Wacker Chemie's Burghausen plant claims 99.9% chlorine recycling.

Then there's the carbon footprint. Polysilicon made with coal-fired electricity (as in Xinjiang) carries a carbon intensity of roughly 50–70 kg CO₂ per kilogram. Polysilicon made with hydroelectric power (Wacker, some Sichuan-based Chinese producers) drops to 15–25 kg CO₂/kg. For a 400W solar panel containing 1.5 kg of polysilicon, that's the difference between 75–105 kg CO₂ and 23–38 kg CO₂ embedded in just the polysilicon step. The panel will offset far more CO₂ over its lifetime — but the question of *whose* coal powered its birth has become a serious trade policy issue, driving tariffs and supply-chain traceability requirements in the US and EU.

## The Counterintuitive Truth

Here's the fact that surprises most people learning about polysilicon for the first time: **the most expensive and energy-intensive step in making a solar panel isn't the fancy semiconductor processing, the precision wafering, or the cleanroom cell fabrication — it's the purification of a raw material that literally comes from dirt.**

The Siemens process is, at its core, a brute-force solution. We heat things to extreme temperatures, convert between solid and gas phases twice, run enormous distillation columns, and consume city-scale amounts of electricity — all to remove a few parts per million of the wrong atoms. It's the chemical engineering equivalent of burning down a forest to find a specific tree.

And yet it works. It works at scale, it works reliably, and the relentless optimization of the past two decades has driven polysilicon costs from over $400/kg in 2008 to under $10/kg today. That 97% cost reduction is one of the great engineering achievements of the 21st century, and it's the reason solar electricity is now the cheapest form of new power generation in most of the world.

Tomorrow, we'll follow those chunks of ultra-pure polysilicon into the crystal growth furnace, where the Czochralski process will transform a chaotic polycrystalline mass into a single perfect crystal — one of the largest and most flawless crystals produced anywhere on Earth. It's where materials science starts to feel like alchemy.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-03.toml}}
