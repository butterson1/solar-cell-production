# Day 10: Thin-Film Alternatives — CdTe, CIGS, Amorphous Si

*For nine days, we've been deep in the world of crystalline silicon — growing ingots, slicing wafers, doping junctions, printing contacts. If you stepped back and surveyed the solar industry from orbit, you'd see that about 95% of every solar panel made today is some variant of the crystalline silicon technology we've been studying. But that remaining 5%? It represents a radically different philosophy of solar cell design — one that throws out the wafer entirely, deposits semiconductors as thin films measured in micrometers rather than hundreds of micrometers, and in at least one case has built the most profitable solar company in American history. Welcome to thin film.*

---

## The Core Idea: Why Go Thin?

To appreciate thin-film solar cells, you need to understand a fundamental inefficiency in crystalline silicon that we've been politely ignoring. Silicon is an *indirect bandgap* semiconductor. This seemingly arcane distinction has enormous practical consequences.

In a direct bandgap material, an electron can absorb a photon and jump across the bandgap in a single, clean step — the photon's momentum and energy match what's needed for the transition. In silicon, the minimum of the conduction band and the maximum of the valence band sit at different points in momentum space. An electron can't just absorb a photon; it simultaneously needs a phonon (a lattice vibration) to supply the missing momentum. This three-body interaction is inherently less probable, which means silicon absorbs light *weakly* compared to direct bandgap semiconductors.

How weakly? A photon with energy near silicon's 1.12 eV bandgap (around 1100 nm wavelength) has an absorption length of over 100 micrometers in silicon. You need a wafer that's 150–180 μm thick just to capture most of the light — and even then, you rely on back-reflectors and light-trapping textures to get photons that pass through the first time.

Cadmium telluride (CdTe) is a direct bandgap semiconductor with a bandgap of 1.5 eV — almost perfectly centered in the sweet spot for single-junction solar cells. Its absorption coefficient is roughly 100× higher than silicon's at visible wavelengths. A CdTe layer just 2 micrometers thick absorbs over 99% of photons above the bandgap. That's 2 μm versus 170 μm — less than 2% of the material. CIGS (copper indium gallium selenide) is similarly aggressive: it's a direct bandgap material with a tunable bandgap of 1.0–1.7 eV and an absorption coefficient that lets 1–2 μm of material do the work of a hundred times its thickness in silicon.

This is the thin-film value proposition in a nutshell: use 100× less semiconductor material, deposit it directly onto cheap substrates like glass or flexible metal foils, and skip the entire energy-intensive chain of polysilicon purification, crystal growth, and wafer slicing that accounts for roughly 40% of a crystalline silicon module's manufacturing cost.

So why does crystalline silicon still own 95% of the market? Because the devil is in the details, and thin film's details are treacherous.

---

## CdTe: The American Underdog

Cadmium telluride's story is inseparable from one company: **First Solar**, headquartered in Tempe, Arizona. Founded in 1999, First Solar is the largest thin-film solar manufacturer on Earth and the only non-Chinese company among the world's top ten solar panel producers. In 2024, it reported revenues exceeding $3.5 billion, and its stock has outperformed every major Chinese silicon-based competitor over the past decade. In a market that has been utterly dominated by Chinese crystalline silicon, First Solar's survival — and thriving — is one of the most interesting stories in clean energy.

### How CdTe Cells Are Made

The manufacturing process for CdTe is startlingly different from crystalline silicon. Where a silicon cell takes 3–4 days to go from polysilicon to finished cell across dozens of process steps, First Solar produces a complete CdTe module in about **4.5 hours** on a continuous production line. Here's how.

A sheet of low-iron soda-lime float glass enters the line — this is the same kind of glass used in buildings, costing about $5–8 per square meter. The glass is washed and coated with a transparent conducting oxide (TCO), typically a fluorine-doped tin oxide (SnO₂:F), which serves as the front electrode. Its sheet resistance needs to be below about 10 Ω/□ while transmitting over 80% of visible light — a demanding balancing act.

Next comes the magic: **vapor transport deposition (VTD)**. CdTe powder is sublimated at around 500–600°C in an upstream chamber, and the resulting cadmium and tellurium vapor is carried by an inert gas (nitrogen or helium) to a cooler downstream region where the glass substrate passes beneath. The vapors condense on the glass, building up a polycrystalline CdTe film at rates of 1–5 μm per minute. In just a few minutes, you have a 2–4 μm absorber layer — compared to the 4–5 *hours* needed to grow a Czochralski silicon ingot.

Before the CdTe layer, a thin (80–150 nm) buffer layer of cadmium sulfide (CdS) is deposited to form the p-n junction. CdS is an n-type semiconductor with a wider bandgap (2.4 eV), so it's transparent to most of the solar spectrum while creating the built-in electric field needed for charge separation. More recently, First Solar has moved to using magnesium zinc oxide (MgZnO) as the buffer layer, which has a wider bandgap (~3.3 eV) and allows more blue and ultraviolet photons to reach the CdTe absorber — one of the innovations behind their push toward 22%+ cell efficiencies.

After deposition, the CdTe film undergoes a critical **cadmium chloride (CdCl₂) activation treatment**: a thin layer of CdCl₂ is applied and the film is heated to 380–420°C for 15–30 minutes. This seemingly simple step is actually crucial. It promotes recrystallization of the CdTe grains, increases grain size from ~0.5 μm to 2–5 μm, passivates grain boundaries, and enables chlorine atoms to diffuse into the grain boundaries where they reduce recombination. Without this treatment, CdTe cells barely reach 10% efficiency; with it, they jump to 18%+.

The back contact is then applied — historically a copper-doped graphite paste or a thin layer of copper and gold, though modern designs use zinc telluride (ZnTe) or other engineered back contacts. Finally, a second glass sheet is laminated onto the back, creating a glass-glass module that needs no aluminum frame and has the lowest embodied water of any PV technology.

### The Numbers

First Solar's current flagship is the **Series 7** module, a behemoth measuring 2.0 × 1.2 meters that produces up to 550 Wp. Module-level efficiency runs around 19.2–19.8% — notably below the 22–24% of premium crystalline silicon modules. The current CdTe *cell* efficiency record, set by First Solar in collaboration with NREL, stands at **22.3%**, with a roadmap to 25% by 2025 and 28% by 2030.

But here's the counterintuitive part: in many real-world conditions, CdTe *outperforms* higher-efficiency crystalline silicon. CdTe has a lower temperature coefficient — it loses about 0.28–0.32% of its power per degree Celsius above 25°C, versus 0.35–0.45% for crystalline silicon. In a desert installation where module temperatures routinely hit 65–70°C, this means CdTe retains 2–3% more of its rated power. CdTe also performs better in diffuse light conditions and has less spectral sensitivity in the morning and evening hours. When you calculate the *energy yield* per installed watt over a full year (measured in kWh/kWp), CdTe modules can match or beat crystalline silicon modules that are 3–4% more efficient on paper.

First Solar's manufacturing cost in 2024 was approximately **$0.26–0.28 per watt** — competitive with the top-tier Chinese crystalline silicon producers at $0.22–0.26/W, and dramatically lower than non-Chinese crystalline silicon manufacturing.

### The Cadmium Question

Every article about CdTe solar cells addresses the elephant in the room: cadmium is toxic. It's a known carcinogen, and its dust can cause kidney damage, bone softening, and lung disease at concentrations as low as 5 μg/m³ in air.

But the reality is more nuanced than the headlines suggest. In a CdTe compound, cadmium is chemically bound to tellurium and has an extremely high melting point (1,041°C) and negligible vapor pressure at ambient conditions. In fire tests, CdTe modules release less cadmium than a coal-fired power plant produces to generate the same amount of electricity. The CdTe is encapsulated between two sheets of tempered glass, making it virtually impossible to leach into the environment during normal operation. First Solar runs the industry's only comprehensive recycling program, recovering 90% of the semiconductor material and 90% of the glass from end-of-life modules.

Here's the truly surprising fact: **most of the cadmium used for CdTe solar cells is a waste byproduct of zinc mining.** Cadmium naturally occurs in zinc ores at concentrations of 0.01–0.05%, and zinc smelters must remove it regardless of whether anyone buys it. Without a market for it, this cadmium would be stored in hazardous waste facilities at considerable expense. Solar panels actually *sequester* cadmium in a stable, recyclable form — arguably the most environmentally responsible use of a substance that would otherwise be hazardous waste.

---

## CIGS: The Beautiful Loser

If CdTe is the scrappy underdog that made it big, CIGS — copper indium gallium diselenide, or Cu(In,Ga)Se₂ — is the brilliant prodigy that never quite fulfilled its potential. CIGS has the highest lab efficiency of any thin-film technology (**23.64%**, set by Uppsala University in 2024), a gorgeous direct bandgap tunable from 1.0 eV (pure CIS, copper indium selenide) to 1.7 eV (pure CGS, copper gallium selenide) by adjusting the indium-to-gallium ratio, and it can be deposited on flexible substrates for applications silicon can't touch.

### How CIGS Cells Are Made

CIGS manufacturing is where the technology's promise meets its pain. The absorber layer is a quaternary compound — four elements that must be deposited in precisely controlled stoichiometry. There are two main deposition methods:

**Co-evaporation** is the lab champion's technique. Four elemental sources (Cu, In, Ga, Se) are evaporated simultaneously in a vacuum chamber at temperatures of 400–600°C. The substrate — typically soda-lime glass coated with a molybdenum back contact — passes through multiple zones where the evaporation rates are precisely controlled to produce a graded composition. The best cells use a "three-stage" process where a gallium-rich layer is deposited first (for rear-surface passivation), followed by an indium-rich layer (to optimize the absorber bandgap at ~1.15 eV for maximum current), and finished with another gallium-rich cap (to widen the front bandgap and reduce front-surface recombination). This gradient means the bandgap actually varies through the thickness of the film — wider at the front and back, narrower in the middle — creating built-in electric fields that drive carriers toward the junction. It's elegant physics, but requires maintaining four evaporation sources at different temperatures with ±2% rate control simultaneously.

**Sputtering and selenization** is the manufacturing-friendly alternative. Metallic precursor layers (Cu, In, Ga) are sputtered onto the substrate at room temperature — a fast, well-controlled industrial process. Then the precursor stack is annealed in a selenium-containing atmosphere (H₂Se gas or selenium vapor) at 450–550°C, where the metals react with selenium to form the CIGS compound. This "two-step" process is easier to scale but typically produces slightly lower efficiencies due to less control over composition grading.

After the absorber, a thin buffer layer of cadmium sulfide (yes, CIGS uses cadmium too, though in much smaller amounts — typically 50 nm versus CdTe's 2–4 μm of cadmium compound) is deposited by chemical bath deposition. Then a transparent window layer of intrinsic zinc oxide (i-ZnO, ~50 nm) and aluminum-doped zinc oxide (ZnO:Al, ~400 nm) serves as the top electrode.

### Why CIGS Struggles Commercially

The lab results are spectacular. The commercial results have been a graveyard. Solyndra — the cylindrical CIGS startup that became a political scandal after receiving $535 million in US Department of Energy loan guarantees and then going bankrupt in 2011 — is the most infamous example, but the casualty list is long: Nanosolar, MiaSolé, HelioVolt, Global Solar, and a dozen others have failed, been acquired at fire-sale prices, or retreated to niche markets.

The fundamental problem is **manufacturing complexity and cost scaling**. A CIGS production line requires vacuum-based deposition at high temperatures with precise control of four-element stoichiometry and a wet-chemistry CdS buffer step that's inherently difficult to integrate into inline processing. Capital expenditure for a CIGS factory runs $0.70–1.00 per watt of annual capacity, roughly 2–3× higher than crystalline silicon at $0.30–0.40/W. Module efficiencies in production hover around 15–17% — well below crystalline silicon's 21–24%.

The few survivors include **Avancis** (a German company, now owned by China National Building Material), making CIGS glass-glass modules for building-integrated applications, and **Miasolé** (acquired by Hanergy), producing flexible CIGS on steel foil for portable and automotive applications. Japan's **Solar Frontier** (a subsidiary of oil giant Showa Shell) was the largest CIGS manufacturer, operating a 1 GW factory in Miyazaki Prefecture, but announced in 2021 that it would exit the solar module business to focus on lighter-weight perovskite-CIGS tandem development.

Where CIGS *does* shine is in niche applications that exploit its unique properties: flexible modules for curved rooftops and vehicles, lightweight panels for aerospace, and building-integrated facades where aesthetics matter (CIGS has a sleek, uniform black appearance without the grid lines of silicon). Its tunable bandgap also makes it an excellent candidate for tandem cell bottom absorbers — a role that might give CIGS a second act in the 2030s.

---

## Amorphous Silicon: The First Thin Film

Before CdTe and CIGS entered the scene, there was amorphous silicon (a-Si) — and if you've ever used a solar-powered calculator, you've already been a thin-film adopter.

Amorphous silicon is, structurally, the opposite of the crystalline silicon we've spent days studying. Where crystalline silicon has atoms arranged in a perfect, repeating diamond cubic lattice with bond angles of exactly 109.5°, amorphous silicon is a disordered jumble — atoms bonded to their neighbors in roughly the right geometry, but with no long-range periodicity. Imagine the difference between a perfectly laid brick wall and a pile of bricks roughly stacked in the same direction. The pile still has bricks, still has mortar, but has no repeating pattern you could predict.

This disorder has a critical consequence: it converts silicon from an indirect bandgap material to an effectively direct bandgap material. The random arrangement smears out the sharp features in the electronic band structure, relaxing the momentum conservation requirements that make crystalline silicon a weak absorber. Amorphous silicon absorbs visible light roughly **40× more strongly** than crystalline silicon, allowing films as thin as 300–500 nm (0.3–0.5 μm) to capture most incident photons. That's about 1/500th the thickness of a crystalline silicon wafer.

### How a-Si Cells Are Made

Amorphous silicon is deposited by **plasma-enhanced chemical vapor deposition (PECVD)**. Silane gas (SiH₄) is introduced into a vacuum chamber and decomposed by a radio-frequency (13.56 MHz) plasma at relatively low temperatures of 150–300°C — far below the 1,420°C of crystal growth or the 1,100°C of polysilicon production. The silicon atoms deposit onto the substrate (glass, steel, or plastic film) along with about 10% hydrogen atoms, which is why the material is more precisely called hydrogenated amorphous silicon (a-Si:H). Those hydrogen atoms are crucial: they passivate the dangling bonds in the disordered network, without which the material would have so many defect states that it would be useless as a semiconductor.

The low deposition temperature is a-Si's superpower. It means you can deposit solar cells on **flexible plastic substrates** using roll-to-roll processing — imagine a web of thin stainless steel or polyimide film unrolling through a series of vacuum chambers like newspaper through a printing press, emerging at the other end as a continuous strip of solar cell. This enables production at extremely low temperatures and, in theory, at very high speeds and low costs.

### The Staebler-Wronski Effect: a-Si's Fatal Flaw

But amorphous silicon has a debilitating weakness that has kept it from ever seriously challenging crystalline silicon for mainstream power generation: the **Staebler-Wronski effect**, discovered in 1977 by David Staebler and Christopher Wronski at RCA Laboratories.

When light hits a-Si:H, the energy from absorbed photons can break weak Si-Si bonds in the disordered network, creating metastable dangling bond defects. These new defects act as recombination centers, degrading cell performance. Over the first few hundred hours of light exposure, a-Si cell efficiency can drop by **10–30% relative** (meaning a cell that starts at 10% might stabilize at 7–8%). The degradation is partially reversible by annealing at ~150°C, but in practical outdoor use, the cells settle at a "stabilized" efficiency well below their initial rating.

Peak lab efficiency for a single-junction a-Si cell is about **14%**, but stabilized efficiencies in production modules are typically **6–8%**. That's about a third of what crystalline silicon delivers. For ground-mounted utility solar, where land and racking costs scale with area, this efficiency penalty is fatal — you'd need 3× the land and 3× the mounting hardware to produce the same energy.

### Where a-Si Survives

Despite its limitations, amorphous silicon hasn't disappeared. It still dominates several niches:

- **Calculators and consumer electronics**: The original thin-film market. A-Si works well under indoor fluorescent and LED lighting, where its wider bandgap (~1.7 eV vs. crystalline silicon's 1.12 eV) is actually better matched to the blue-shifted indoor light spectrum.
- **HJT cell architecture**: Remember Day 9? The intrinsic amorphous silicon layers in heterojunction cells — those 5–10 nm passivation films that give HJT its extraordinary surface passivation — are deposited using the same PECVD process as a-Si solar cells. Amorphous silicon's most important role in modern solar may be as a *passivation layer* in crystalline silicon cells, not as an absorber in its own right.
- **Multi-junction thin-film**: Companies like United Solar Ovonic (now bankrupt) stacked a-Si junctions with different bandgaps — amorphous silicon (1.7 eV), amorphous silicon-germanium (1.4 eV), and nanocrystalline silicon (1.1 eV) — to build triple-junction cells on flexible stainless steel that achieved ~13% stabilized efficiency. This approach is now mostly of historical interest, but the multi-junction concept lives on in III-V space cells and perovskite tandems.

---

## The Thin-Film Landscape in 2025

Here's the honest scoreboard. Thin film as a whole commands roughly **5% of global solar module production by capacity**, down from a peak of about 17% in 2009. Within that slice, CdTe dominates with approximately 45% of the thin-film market (essentially all First Solar), CIGS holds around 25–30%, and a-Si has dwindled to the remainder, mostly in consumer products and building-integrated applications.

The total PV market in 2024 was roughly 400+ GW of new installations. First Solar shipped approximately 15 GW of CdTe modules. The rest was almost entirely crystalline silicon, overwhelmingly manufactured in China.

**Why hasn't thin film displaced silicon?** Three reasons:

1. **Chinese crystalline silicon got too cheap.** Between 2010 and 2024, crystalline silicon module prices dropped from ~$1.50/W to under $0.10/W for the cheapest Chinese modules. This was driven by massive Chinese government subsidies, vertically integrated supply chains, relentless polysilicon cost reduction (from $400/kg to $6–8/kg), and economies of scale that thin-film factories couldn't match. When your competitor's module costs $0.10/W, your technology needs to offer extraordinary advantages to justify even $0.15/W.

2. **Crystalline silicon efficiency kept climbing.** In 2010, mainstream c-Si modules were 14–16% efficient. By 2025, TOPCon modules hit 22–24%, and the Shockley-Queisser limit for silicon (~29.4%) still offers headroom. The efficiency gap between silicon and thin film *widened*, not narrowed, over the past decade.

3. **Thin film's advantages are real but conditional.** CdTe's temperature coefficient advantage matters most in hot climates. CIGS's flexibility matters only for specific applications. a-Si's low cost matters only where efficiency doesn't. For the vast majority of utility-scale and rooftop solar — which together make up 90%+ of the market — crystalline silicon is simply the better product at the better price.

But thin film isn't dying. First Solar's order book extends years into the future, driven by customers who want non-Chinese supply chains, trade-war-proof sourcing, and the Inflation Reduction Act's domestic content bonuses (worth $0.02–0.04/W). The company is investing $1.1 billion in a new factory in Alabama, with 3.5 GW of annual capacity. And CdTe's theoretical efficiency ceiling is about 32% (versus silicon's 29.4%), meaning there's substantial room for cell-level improvements that could close the module efficiency gap.

CIGS may find its redemption not as a standalone technology, but as the bottom cell in a perovskite-CIGS tandem — a design that could potentially exceed 30% efficiency on a flexible substrate. Several groups, including Solar Frontier's research arm and HZB (Helmholtz-Zentrum Berlin), are pursuing this approach.

---

## The Big Picture

Thin film teaches us something important about technology competition: the best physics doesn't always win. CdTe and CIGS are, in many respects, *better semiconductors* for solar energy conversion than silicon — they absorb light more efficiently, need far less material, can be deposited at lower temperatures, and have nearly ideal bandgaps. If you were designing a solar cell from scratch with no legacy constraints, you'd almost certainly choose a direct bandgap material.

But silicon had a 30-year head start from the integrated circuit industry, an entrenched supply chain processing millions of tons of material, and the manufacturing cost advantages of truly enormous scale. Technology competitions aren't just about physics — they're about economics, infrastructure, and path dependence.

Tomorrow, we'll explore **multi-junction and tandem cells** — designs that refuse to accept the single-junction efficiency limit and instead stack multiple absorbers with different bandgaps to capture more of the solar spectrum. It's in tandems that thin-film materials may finally find their killer application, not replacing silicon but complementing it.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-10.toml}}
