# Day 6: Doping — Creating the P-N Junction

*You're holding a silicon wafer. It's 170 micrometers thin, polished on both sides, etched clean of saw damage — a perfect slice of crystalline silicon containing roughly 5 × 10²² atoms arranged in flawless diamond cubic symmetry. And it is, electrically speaking, almost completely useless. Pure silicon at room temperature has an intrinsic carrier concentration of about 1.5 × 10¹⁰ free electrons per cubic centimeter. That sounds like a lot until you realize there are 5 × 10²² atoms in that same volume. Fewer than one atom in a trillion is contributing a mobile charge carrier. The resistivity is around 230,000 ohm-centimeters — not quite an insulator, but nowhere near useful as a conductor or a solar cell. Today we fix that, by introducing precisely controlled impurities that transform inert silicon into something that can actually harvest sunlight.*

---

## The Paradox of Deliberate Contamination

Everything we've done so far in this course has been about *removing* impurities. The Siemens process purified silicon to 99.9999% (six-nines). Czochralski crystal growth preserved that purity in a perfect lattice. We obsessed over parts-per-billion contamination levels. And now — after all that heroic purification — we're going to deliberately contaminate it.

This isn't a contradiction. It's the entire point. We purified silicon so that *we* get to choose exactly which impurities go where, in exactly what concentrations. The difference between a worthless chunk of dirty silicon and a functioning solar cell isn't cleanliness — it's *controlled* dirtiness. Semiconductor physics is, at its heart, the science of making impurities do what you want.

The process of deliberately introducing impurities into silicon is called **doping**, and it's the single most important step in turning a wafer into a solar cell. Without doping, there's no p-n junction. Without a p-n junction, there's no built-in electric field. Without that field, photogenerated electrons and holes just wander around randomly until they recombine, producing nothing but a tiny amount of heat. Doping is what gives a solar cell its directionality — the asymmetry that turns random charge generation into useful current.

---

## How Doping Works: The Atomic Picture

Silicon sits in Group 14 of the periodic table: four valence electrons, four covalent bonds per atom, everyone satisfied. Every electron is accounted for. There's nothing left over and nothing missing. This is why pure silicon is such a poor conductor — every electron is locked into a bond.

Now imagine replacing one silicon atom with a **phosphorus** atom. Phosphorus is in Group 15: five valence electrons. It slots into the silicon lattice just fine, forming four covalent bonds with its neighbors — but it has one electron left over. This extra electron isn't bound into any covalent bond. It sits in a shallow energy state just 0.045 eV below the conduction band (compare this to the full 1.12 eV band gap). At room temperature, thermal energy (kT ≈ 0.026 eV) is more than enough to kick it loose. That electron is effectively free from birth.

We call phosphorus a **donor** impurity because it donates a free electron. Silicon doped with phosphorus is **n-type** (negative, because the majority carriers are electrons). The phosphorus atom, having lost its extra electron, becomes a fixed positive ion in the lattice — but it can't move. Only the electron is mobile.

The mirror image: replace a silicon atom with **boron**, from Group 13. Boron has only three valence electrons. It forms three covalent bonds easily, but the fourth bond is incomplete — there's a missing electron, a **hole**. This hole has an ionization energy of just 0.045 eV above the valence band, meaning it's thermally activated at room temperature. A neighboring electron can hop into that empty bond, leaving its own bond incomplete — and so the hole *moves*. It behaves exactly like a positive charge carrier flowing through the lattice.

Boron is an **acceptor** impurity (it accepts an electron, creating a hole). Silicon doped with boron is **p-type** (positive majority carriers). The boron atom, having gained an electron, becomes a fixed negative ion.

Here's the part that surprises people: the concentrations involved are *tiny*. A typical solar cell base is doped with boron at about 1 × 10¹⁶ atoms per cubic centimeter. That's one boron atom for every 5 million silicon atoms — roughly 0.00002% boron. Yet this minuscule contamination increases silicon's conductivity by a factor of about 15,000. From 230,000 Ω·cm to approximately 1-10 Ω·cm. That's the power of doping: you don't need many impurities when each one contributes a free charge carrier with 100% efficiency.

---

## The P-N Junction: Where the Magic Happens

Take a wafer of p-type silicon (boron-doped base, the starting material for most solar cells) and introduce a thin layer of n-type silicon at the surface (by diffusing phosphorus into it). You've just created a **p-n junction** — the structure that makes photovoltaics possible.

What happens at the boundary is beautiful. Free electrons on the n-side and holes on the p-side are in close proximity. Electrons diffuse across the boundary into the p-side; holes diffuse into the n-side. But here's the crucial twist: when an electron leaves the n-side, it leaves behind a fixed phosphorus ion (positive charge). When a hole leaves the p-side, it leaves behind a fixed boron ion (negative charge). These immobile ions create an electric field pointing from the n-side to the p-side.

This region of exposed ions is called the **depletion zone** (or space charge region) — it's been swept clean of mobile carriers by diffusion. In a typical solar cell, it's about 0.1 to 1 micrometer wide. The electric field inside it is substantial: roughly 10,000 to 100,000 V/cm, even though the total voltage across it — the **built-in potential** — is only about 0.6-0.7 volts for a silicon p-n junction.

The depletion zone is self-regulating. If more carriers try to diffuse across, they expose more ions, which strengthens the field, which pushes them back. It reaches equilibrium in nanoseconds. The resulting system is a one-way valve for charge carriers: the electric field sweeps electrons toward the n-side and holes toward the p-side. Any electron-hole pair generated by a photon near the junction will be separated by this field before it can recombine. The electron gets pushed to the n-side contact, flows through the external circuit (doing work), and recombines with a hole on the p-side. That's a solar cell.

Let that sink in for a moment: the entire photovoltaic effect relies on a 0.7-volt electric field in a region thinner than a red blood cell. Everything else — the anti-reflective coatings, the metallization, the encapsulation — exists to support this one whisper-thin interface.

---

## Diffusion Doping: Baking Phosphorus into Silicon

So how do we actually get phosphorus into the surface of a p-type wafer? In modern solar cell manufacturing, the dominant method is **phosphorus oxychloride (POCl₃) diffusion**.

The process happens in a quartz tube furnace — a horizontal cylinder about 2-3 meters long, heated to 800-900°C. Wafers are loaded vertically in quartz boats, about 1,200 wafers per batch in a modern production furnace. The key steps:

1. **POCl₃ delivery.** Liquid POCl₃ (a clear, fuming liquid stored at room temperature) is bubbled with nitrogen carrier gas and introduced into the hot furnace tube along with oxygen. At furnace temperature, it reacts:

   4 POCl₃ + 3 O₂ → 2 P₂O₅ + 6 Cl₂

2. **Phosphosilicate glass (PSG) formation.** The P₂O₅ deposits on the wafer surface and reacts with silicon to form a thin phosphosilicate glass layer, typically 20-40 nanometers thick. This glass acts as a constant source of phosphorus atoms.

3. **Drive-in diffusion.** At 850-900°C, phosphorus atoms from the PSG layer diffuse into the silicon bulk. Diffusion in solids is governed by Fick's laws — the same mathematics that describes a drop of ink spreading in water, just far slower. At 880°C, phosphorus has a diffusivity of roughly 3 × 10⁻¹⁴ cm²/s in silicon. After a 20-30 minute drive-in, you get a phosphorus-doped layer (the **emitter**) about 0.3-0.5 micrometers deep.

4. **PSG removal.** The phosphosilicate glass layer is stripped off in dilute hydrofluoric acid (HF).

The resulting phosphorus profile isn't flat — it's a steep gradient, with surface concentrations of about 10²⁰-10²¹ atoms/cm³ (nearly 1% phosphorus!) dropping exponentially to background levels over half a micrometer. This high surface concentration is actually a problem, which we'll discuss in a moment.

Major furnace manufacturers include **Tempress** (Netherlands), **centrotherm** (Germany), and **Laplace Solar** (China). A modern diffusion furnace can process around 5,000 wafers per hour and costs $500,000-$1,000,000. A typical cell factory running 10 GW/year capacity might have 20-30 such furnaces running simultaneously.

---

## The Dead Layer Problem

Here's the counterintuitive fact of the day: **making the surface more conductive actually makes the solar cell worse.**

That ultra-high phosphorus concentration at the surface (>5 × 10²⁰/cm³) creates a region called the **dead layer** or "over-doped emitter." In this zone, phosphorus concentration exceeds the solid solubility limit — there are more phosphorus atoms than the silicon lattice can electrically activate. The excess phosphorus atoms sit at interstitial sites or form precipitates, and instead of donating electrons, they act as **recombination centers**. They're traps where photogenerated electron-hole pairs go to die.

This is devastating for cell performance because it's right at the surface — exactly where short-wavelength (blue and UV) photons are absorbed. Blue light (400-500 nm) generates electron-hole pairs within the first 0.1-1 μm of silicon. If that region is a recombination graveyard, you lose the blue response entirely. Early solar cells with heavily doped emitters would show terrible quantum efficiency below 500 nm, wasting 15-20% of available solar energy.

The solution is the **selective emitter**: heavy doping only under the metal contacts (where you need low contact resistance) and lighter doping between the contacts (where you need good passivation and low recombination). In practice, this means the phosphorus concentration under the silver gridlines is ~10²¹/cm³ for good ohmic contact, while the field regions are doped at ~10¹⁹/cm³ for good carrier collection.

Selective emitters used to require complex patterning steps — laser doping, etch-back processes, or multiple diffusion masks. This added cost and complexity. Modern PERC cells largely addressed the problem through a different route: instead of spatially varying the doping, they use **passivation layers** (SiNₓ, AlOₓ) to neutralize surface recombination regardless of doping level. And in the newest TOPCon cells, the heavy doping is moved to the rear side entirely, avoiding the surface problem at the front.

---

## Boron: The Trickier Dopant

While phosphorus diffusion is relatively straightforward (POCl₃ has been the industry workhorse for decades), **boron doping** is harder — and it's becoming more important as cell architectures evolve.

In a traditional solar cell, the boron doping of the base wafer is done during crystal growth. You simply add a controlled amount of boron to the silicon melt in the Czochralski puller, and the growing crystal incorporates it uniformly. The typical base resistivity is 1-3 Ω·cm, corresponding to a boron concentration of about 5 × 10¹⁵ to 1.5 × 10¹⁶/cm³.

But modern high-efficiency cell designs like **TOPCon** (Tunnel Oxide Passivated Contact) have flipped the structure. Instead of a p-type base with an n-type emitter on top, TOPCon uses an **n-type base** (phosphorus-doped during crystal growth) with a **boron-doped emitter** on the front. This design has important advantages — n-type silicon doesn't suffer from boron-oxygen light-induced degradation (LID), a notorious defect complex that can reduce p-type cell output by 2-3% in the first hours of sun exposure.

Creating a boron emitter on an n-type wafer requires boron diffusion, typically using **BBr₃** (boron tribromide) as a source gas, at temperatures of 900-1,050°C. Boron diffusion is harder to control than phosphorus for several reasons:

- **Higher temperatures required.** Boron diffuses more slowly in silicon, so you need 50-100°C higher temperatures and longer drive-in times (30-60 minutes vs. 20-30 for phosphorus).
- **Boron-rich layer (BRL) formation.** Analogous to the PSG, a borosilicate glass forms on the surface, but it's more complex and harder to etch cleanly.
- **Sensitivity to oxygen.** Even traces of oxygen during BBr₃ diffusion can form problematic SiO₂ layers that disrupt the doping profile.

Despite these challenges, BBr₃ boron diffusion is now standard in TOPCon lines. Companies like **S.C New Energy Technology** (Wuxi, China) and **centrotherm** supply dedicated BBr₃ diffusion furnaces that have largely solved the uniformity and reproducibility issues. As of 2025, TOPCon has overtaken PERC as the dominant new production technology, meaning boron diffusion capacity is scaling massively — estimated at over 300 GW of annual furnace capacity installed globally.

---

## Ion Implantation: The Precision Alternative

There's a second way to dope silicon that offers far more control: **ion implantation**. Instead of bathing the wafer in a hot gas and waiting for atoms to diffuse in, you accelerate dopant ions to high energy in a particle beam and shoot them directly into the silicon surface.

An ion implanter is essentially a small particle accelerator. It ionizes the dopant source (e.g., PH₃ for phosphorus, BF₃ for boron), magnetically separates the desired species, accelerates them to 5-200 keV, and scans the beam across the wafer. The ions slam into the silicon lattice and embed at a depth controlled by their energy — typically 0.1-0.5 μm for solar cell applications.

The advantages are compelling:

- **Precise dose control.** You measure beam current directly, so you know exactly how many atoms per cm² you've implanted. Accuracy of ±1% is routine, compared to ±5-10% for diffusion.
- **No surface glass layer.** No PSG or BSG to strip off.
- **Selective doping without masks.** You can pattern the beam to create selective emitters directly.
- **Low temperature process.** Implantation itself happens at room temperature (though you still need a 900-1,000°C anneal afterward to repair lattice damage and activate the dopants).

The company that pioneered ion implantation for solar is **Intevac** (Santa Clara, California), whose ENERGi system could process 2,400 wafers per hour. Chinese companies like **Kingstone Semiconductor** and **Wanye Semiconductor** have since entered the market with lower-cost tools.

So why doesn't the entire industry use ion implantation? **Cost.** An ion implanter for solar costs $3-5 million — 5-10× more than a diffusion furnace. The throughput is competitive (2,000-3,000 wafers/hour), but the capital expenditure and maintenance costs (high-vacuum systems, ion sources that need periodic replacement) make diffusion the economically preferred choice for standard cell architectures. Ion implantation finds its niche in high-efficiency cells where the precision justifies the cost — interdigitated back-contact (IBC) cells from companies like **Maxeon** (formerly SunPower) use implantation extensively.

---

## The Numbers That Matter

Let's put some real dimensions on a finished solar cell's doping profile, because the numbers are remarkable:

| Layer | Thickness | Doping concentration | Dopant |
|-------|-----------|---------------------|--------|
| Front emitter (PERC) | 0.3-0.5 μm | 10¹⁹-10²⁰/cm³ | Phosphorus |
| Base (p-type PERC) | ~170 μm | 10¹⁶/cm³ | Boron |
| Rear BSF (PERC) | 5-10 μm | 10¹⁸-10¹⁹/cm³ | Aluminum |

The emitter is about 0.2% of the cell thickness but contains 1,000-10,000× more dopant per volume than the base. The doping concentration spans four orders of magnitude across 170 micrometers. Getting this profile right — and keeping it right across a billion wafers per year — is the central manufacturing challenge.

And there's one more doping step we haven't mentioned: the **back surface field (BSF)**. In PERC cells, aluminum paste is printed on the rear and fired at ~800°C, causing aluminum atoms to diffuse into the silicon and create a p⁺ layer (heavily doped p-type). This high-low junction at the rear creates a field that repels minority carriers (electrons) back toward the front junction, reducing recombination at the back surface. It's doping, just done through metallization rather than a dedicated diffusion step.

---

## From Doping to the Finished Surface

Doping transforms a passive silicon wafer into an active electronic device — but a freshly doped wafer still has terrible optical properties. Silicon is shiny. It reflects about 35% of incoming light. If more than a third of photons bounce off the surface before they can make electron-hole pairs, no amount of clever doping will save you.

Tomorrow, we tackle the two-pronged attack on this reflection problem: **anti-reflective coatings** that use thin-film interference to suppress reflection, and **surface texturing** that traps light using microscopic pyramids etched into the silicon surface. Together, they'll cut front-surface reflection from 35% to under 2% — one of the biggest single improvements in solar cell history.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-06.toml}}
