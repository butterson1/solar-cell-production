# Day 2: Silicon — From Sand to Semiconductor

*The second most abundant element in Earth's crust built the modern world twice: first with glass, then with microchips. Now it's doing it a third time with solar panels. But transforming a grain of beach sand into a material that converts sunlight into electricity requires one of the most extraordinary purification journeys in all of industrial chemistry.*

---

## The Embarrassment of Riches

Look at any beach, any desert, any granite mountainside, and you're staring at silicon. It makes up 27.7% of Earth's crust by mass — second only to oxygen, and ahead of aluminum, iron, and everything else. The mineral quartz, which is silicon dioxide (SiO₂), is so common that it's essentially geological background noise. Every continent has mountains of it. Global reserves of quartzite — the metamorphic rock made almost entirely of quartz — are effectively unlimited.

And yet silicon for solar cells costs money. Real money. In early 2025, polysilicon — the ultra-purified form used in photovoltaics — traded at around $7–10 per kilogram, down from historic spikes above $400/kg during the 2008 shortage. That price isn't for the silicon atoms themselves. It's for removing everything that *isn't* silicon.

Here's the counterintuitive truth that defines this entire industry: **the raw material is essentially free, but making it pure enough to be useful is one of the most energy-intensive industrial processes humans have ever devised.** A kilogram of solar-grade polysilicon requires roughly 60–80 kilowatt-hours of electricity to produce. That means every solar panel carries an energy debt from its own birth — a debt that, thankfully, it repays within 1–2 years of operation and then generates clean power for another 25+ years.

## What Sand Actually Is

Before we can understand purification, we need to understand what we're purifying. Beach sand is mostly quartz grains — SiO₂ — but "mostly" isn't going to cut it. A typical handful of sand might be 95% SiO₂ along with iron oxides (the stuff that makes sand reddish), aluminum silicates, calcium carbonate from shells, traces of titanium, zirconium, and dozens of other elements. Even the quartz grains themselves aren't pure SiO₂ — they contain parts-per-million impurities of aluminum, iron, titanium, and alkali metals trapped within the crystal lattice.

For context, here's the purity ladder we need to climb:

| Grade | Purity | Typical Use |
|-------|--------|-------------|
| Beach sand | ~95–99% Si (as SiO₂) | Construction, glass |
| Metallurgical-grade silicon (MG-Si) | 98–99% Si | Aluminum alloys, silicones |
| Solar-grade silicon (SoG-Si) | 99.9999% Si (6N) | Photovoltaic cells |
| Electronic-grade silicon (EG-Si) | 99.999999999% Si (11N) | Computer chips |

That jump from 99% to 99.9999% is six orders of magnitude of improvement. And electronic-grade goes five orders further. To put "six nines" purity in perspective: if solar-grade silicon were a sports stadium holding 1 million fans, only *one* of them would be an impurity atom. For electronic-grade, you'd need a billion fans, and only one could be an outsider.

## Step One: Smelting the Oxygen Away

Silicon doesn't exist as a free element in nature. It's always bonded to oxygen — that's how stable the Si–O bond is (bond energy of ~452 kJ/mol, among the strongest in chemistry). Breaking that bond is the first and most violent step in silicon production.

This happens in a **submerged arc furnace** — a monstrous industrial vessel typically 10–15 meters in diameter. Workers load quartzite rock (high-purity SiO₂ ore, not random beach sand) along with carbon sources: coal, charcoal, and wood chips. Three enormous graphite electrodes, each potentially 2 meters in diameter, plunge into the mix and deliver currents of 100,000+ amperes.

The temperature at the electrode tips reaches approximately 2,000°C. At these temperatures, carbon strips oxygen from silicon in a reduction reaction:

**SiO₂ + 2C → Si + 2CO**

The carbon monoxide gas bubbles away (and is often captured or flared), while molten silicon — now metallurgical-grade, around 98–99% pure — pools at the bottom of the furnace and is tapped off like beer from a keg. Except this "beer" is a glowing orange-white liquid at 1,414°C (silicon's melting point), and the "keg" weighs several tons.

Each batch consumes staggering amounts of electricity — roughly 11–13 MWh per metric ton of MG-Si. This is why silicon smelters cluster near cheap hydropower. Norway's Elkem (now owned by China National Bluestar) operates smelters powered by Nordic hydro. Brazil uses its abundant hydroelectric capacity. And China — which now produces over 80% of the world's metallurgical-grade silicon — runs smelters in Xinjiang, Yunnan, and Sichuan, regions chosen specifically for cheap electricity from hydro and coal.

Global production of MG-Si is around 3.5–4 million metric tons per year. Most of it never sees a solar panel — it goes into aluminum alloys (for cars and aircraft), silicone polymers (for sealants and medical devices), and chemical applications. Only about 15–20% gets further purified for semiconductors and photovoltaics.

## Why Purity Matters: The Physics

Why can't we just use 99% pure silicon in a solar cell? Because solar cells are semiconductor devices, and semiconductors are exquisitely sensitive to impurities.

Recall from Day 1 that a solar cell works by creating an electric field at the junction between two types of silicon — one doped with a few atoms of phosphorus (n-type), the other with boron (p-type). The doping concentrations are themselves tiny: typically around 1 boron atom per million silicon atoms for p-type material. That's roughly 10¹⁶ dopant atoms per cubic centimeter, against 5 × 10²² silicon atoms per cm³.

Now imagine you have "only" 1% impurities — that's 10²⁰ foreign atoms per cm³. These uncontrolled impurities would **completely overwhelm** the deliberate doping. Worse, many common contaminants are electrically active in devastating ways:

- **Iron** creates deep energy levels in silicon's bandgap that act as recombination centers — places where electrons and holes meet and annihilate, releasing their energy as useless heat instead of electricity. Just 1 part per billion of iron can cut a solar cell's efficiency in half.
- **Copper** does the same thing, and diffuses through silicon extremely fast, even at moderate temperatures.
- **Carbon** above about 5 × 10¹⁷ atoms/cm³ forms silicon carbide precipitates that create mechanical stress and electrical dead zones.
- **Oxygen** is less harmful in small amounts and actually strengthens the crystal, but above ~10¹⁸ atoms/cm³ it forms troublesome thermal donors that shift the material's electrical properties unpredictably.

This is why the purification step exists. We're not removing impurities because of some abstract standard — we're removing them because physics demands it. Every stray iron atom is a tiny assassin for photogenerated electrons.

## Step Two: Enter the Gas Phase

Going from 99% to 99.9999% purity using solid-state or liquid-metal techniques is essentially impossible. You can't pick individual atoms out of a molten pool. Instead, the silicon industry pulls off one of the cleverest tricks in industrial chemistry: **it converts the silicon into a gas, purifies the gas, and then converts it back to solid silicon.**

The dominant process — which we'll explore in full detail on Day 3 — involves reacting MG-Si with hydrogen chloride (HCl) at around 300–350°C:

**Si + 3HCl → SiHCl₃ + H₂**

The product, trichlorosilane (SiHCl₃, or TCS), is a liquid at room temperature that boils at just 31.8°C. And here's the magic: because it's a liquid, you can **distill** it. Fractional distillation — the same basic technique used to separate crude oil into gasoline, diesel, and kerosene — works brilliantly for purifying TCS because the chlorosilane impurities of iron, aluminum, boron, and phosphorus have significantly different boiling points.

After multiple rounds of distillation in columns that can be 30+ meters tall, the TCS emerges with impurity levels in the parts-per-trillion range. It's one of the purest bulk chemicals produced anywhere on Earth.

The purified TCS is then decomposed back into solid silicon via the Siemens process (Day 3's topic), where it's passed over hot silicon rods at about 1,100°C. The TCS breaks down, depositing ultra-pure silicon onto the rods:

**2SiHCl₃ + 2H₂ → 2Si + 6HCl**

The result is polysilicon — chunky, silvery-gray rods of 6N to 9N purity, ready to be melted and grown into crystals.

## The Alternative Path: Fluidized Bed Reactors

The Siemens process works beautifully, but it's slow and electricity-hungry. Each batch takes 5–7 days, and the heated rods radiate enormous amounts of energy into the reactor walls. Energy consumption runs 60–80 kWh per kilogram of polysilicon.

Starting in the 2000s, companies began commercializing **fluidized bed reactor (FBR)** technology as an alternative. Instead of depositing silicon on stationary rods, FBR systems flow silane gas (SiH₄) upward through a bed of tiny silicon seed particles. The gas decomposes on the particle surfaces, growing them like snowballs rolling downhill. The resulting granular polysilicon — small beads rather than chunky rods — uses only about 15–25 kWh/kg, a 60–75% energy reduction.

China's GCL-Poly (now GCL Technology) bet big on FBR granular polysilicon and has ramped capacity aggressively. By 2024, GCL operated granular polysilicon plants in Xuzhou, Leshan, and Baotou with combined capacity exceeding 300,000 metric tons per year. REC Silicon in Moses Lake, Washington, also operates FBR technology.

The tradeoff? Granular polysilicon can have slightly higher hydrogen content, which causes bubbling during crystal growth. It also picks up more surface contamination due to its high surface-area-to-volume ratio. But these issues are increasingly well-managed, and the economics are compelling enough that FBR's market share continues to grow.

## Silicon's Unique Position: Why Not Something Else?

Given all this effort, it's fair to ask: why silicon? There are hundreds of semiconductors. Gallium arsenide is more efficient at converting sunlight. Cadmium telluride is cheaper to deposit as thin films. Perovskites can be printed from solution like ink. Why does silicon command over 95% of the solar market?

The answer is a convergence of about six factors, none sufficient alone, but devastating in combination:

1. **Abundance.** Silicon is inexhaustible. Tellurium (used in CdTe cells) is rarer than gold. Indium (used in CIGS cells) is a byproduct of zinc mining. You can't build a terawatt-scale industry on scarce materials.

2. **Bandgap.** Silicon's bandgap is 1.12 electron volts — remarkably close to the theoretical optimum of ~1.34 eV for a single-junction cell under the solar spectrum. This wasn't designed; it's a cosmic coincidence.

3. **Stability.** A silicon solar cell installed in 1985 is still producing power today, degraded by perhaps 15–20% over 40 years. Silicon doesn't corrode in air, doesn't decompose in sunlight, and withstands temperature cycling from -40°C to +85°C. Perovskites, by comparison, can degrade in *hours* if exposed to moisture.

4. **Infrastructure.** Sixty years of semiconductor manufacturing built an entire ecosystem — equipment makers, chemical suppliers, process engineers, metrology tools — all optimized for silicon. Switching to a new material means rebuilding all of that.

5. **Learning curve.** The price of silicon solar modules has fallen 99.6% since 1976, from about $106/watt to under $0.20/watt. That's not because silicon got fundamentally cheaper — it's because humanity got extraordinarily good at processing it. Every doubling of cumulative production has dropped prices by roughly 24% (Swanson's Law). Competing technologies are trying to beat a target that keeps falling.

6. **Toxicity.** Silicon is biologically inert. You can eat it (you already do — it's in oats, rice, and beer). Compare this with cadmium, a known carcinogen, or the lead in many perovskite formulations. Regulatory and public acceptance matter.

## The Scale of the Machine

To appreciate where we are: in 2024, global polysilicon production capacity exceeded 2.5 million metric tons per year, with Chinese producers — Tongwei, GCL Technology, Daqo New Energy, Xinte Energy, and East Hope — controlling roughly 95% of it. The largest single polysilicon plant in the world, operated by Tongwei in Leshan, Sichuan, has an annual capacity of over 200,000 metric tons.

These factories run 24/7, 365 days a year. A single large Siemens reactor might contain 36 pairs of silicon rods, each growing to about 15 cm in diameter over a week-long run, producing roughly 8–10 metric tons per batch. A factory might operate 48 or more such reactors simultaneously.

All of this infrastructure exists to answer one question: *How do you take one of the dirtiest, most common substances on Earth and make it clean enough to feel individual photons?*

The answer, as we've seen, is heat, chemistry, and an obsessive attention to purity that borders on the spiritual. Tomorrow, we'll go deep into the Siemens process itself — the century-old chemical trick that makes modern solar energy possible, and the upstart FBR technology trying to replace it.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-02.toml}}
