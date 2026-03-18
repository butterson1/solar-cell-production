# Day 22: Tandem Cells — Silicon + Perovskite Stacking

*Week 4, Lesson 2 — Frontier & Future*

---

Yesterday we met perovskite — the newcomer that can be printed like ink, absorbs light like a black hole, and has a tunable bandgap that silicon engineers can only dream of. We also met its demons: moisture sensitivity, lead toxicity, and an operational lifetime measured in months rather than decades. So here's the question that's been driving the entire photovoltaics industry since about 2018: **what if you don't have to choose?**

What if, instead of asking perovskite to replace silicon, you just put it *on top*?

That's the tandem cell — and it's not a compromise. It's an ambush on the Shockley-Queisser limit from two directions at once. In April 2025, LONGi certified a perovskite-on-silicon tandem at 34.85% efficiency, shattering a barrier that single-junction silicon will never touch. Oxford PV, operating from a converted thin-film factory in Brandenburg an der Havel, Germany, has already shipped commercial tandem modules to utility-scale customers. This isn't lab fantasy anymore. It's product.

Let's tear the whole thing apart and understand why stacking two imperfect cells creates something better than either one alone.

## The Fundamental Problem: One Bandgap Isn't Enough

Recall from Day 12 the cruel mathematics of the Shockley-Queisser limit. A single-junction cell with a bandgap of 1.12 eV (silicon) can theoretically convert about 33% of incoming sunlight into electricity. Everything below the bandgap energy passes right through — those infrared photons are invisible to silicon. Everything far above the bandgap gets absorbed, but the excess energy above 1.12 eV is dumped as heat through a process called thermalization. A blue photon at 3.0 eV excites an electron, but that electron immediately relaxes down to the conduction band edge, shedding 1.88 eV of wasted heat into the crystal lattice.

Here's the brutal accounting for a silicon cell under standard sunlight: about **20% of the energy** in the solar spectrum is lost because photons have too little energy to be absorbed. Another **30%** is lost to thermalization — photons that are absorbed but carry more energy than silicon can use. The remaining losses come from recombination, resistance, and reflection. The theoretical ceiling is ~33%. The best lab silicon cells hit 26.8%. Commercial panels hover around 22-24%.

A tandem cell attacks the two biggest loss channels simultaneously. Put a wide-bandgap cell on top to catch the high-energy photons (blue, violet, UV) before they can thermalize. Let the transmitted lower-energy photons (red, infrared) pass through to a narrow-bandgap cell underneath that can actually use them. Two cells, two bandgaps, two bites at the solar spectrum. The theoretical limit for an optimized two-junction tandem under unconcentrated sunlight jumps to about **46%** — nearly half again higher than single-junction.

## Why Perovskite + Silicon Is the Dream Pairing

In Day 11, we covered III-V semiconductor tandems — gallium arsenide, indium phosphide, and their alloys — that have reached over 47% efficiency under concentrated light. They're magnificent. They also cost $50,000–$100,000 per square meter, which is why they live exclusively on spacecraft and niche concentrator systems. For terrestrial solar at $20–$50 per square meter of module, III-V tandems are a non-starter.

Perovskite changes the equation entirely. Here's why silicon-perovskite is such a natural marriage:

**Bandgap complementarity.** Silicon's bandgap is 1.12 eV. The optimal top-cell bandgap for a tandem on silicon, based on detailed-balance calculations, is somewhere between 1.65 and 1.75 eV. Perovskites — specifically formamidinium-cesium lead halide compositions like FA₀.₇₅Cs₀.₂₅Pb(I₀.₈Br₀.₂)₃ — can be tuned to exactly this range just by adjusting the iodide-to-bromide ratio. No other material system offers this kind of bandgap dial.

**Cost structure.** The perovskite top cell adds relatively little to the manufacturing cost of an existing silicon cell. The active layer is around 400–600 nm thick, deposited from solution or by co-evaporation. Estimates suggest the additional cost for the perovskite layers, transport layers, and recombination junction is roughly $0.02–$0.05 per watt — a modest increment on a silicon cell that already costs around $0.10–$0.15/W. If the tandem boosts module efficiency from 22% to 30%, the cost *per watt* actually drops, because you're spreading all your fixed costs (glass, frame, junction box, labor, shipping) over more watts from the same area.

**Infrastructure leverage.** The world already has roughly 700 GW of annual silicon cell manufacturing capacity. A tandem strategy doesn't require tearing that down. You add a perovskite deposition line — essentially a coating step — to existing silicon cell fabs. This is retrofitting, not revolution. It's why every major silicon manufacturer (LONGi, Trina, JA Solar, Hanwha Q Cells) is racing to develop tandem capability: it's a competitive moat built on top of existing assets.

## Two Terminals or Four? The Architecture Decision

There are two fundamentally different ways to wire a tandem cell, and the choice has profound implications for both physics and manufacturing.

### The 2-Terminal (Monolithic) Tandem

In a monolithic 2T tandem, the perovskite top cell is deposited directly onto the silicon bottom cell, with a thin recombination layer between them. The whole stack shares two electrical contacts — one on top, one on bottom — just like a single-junction cell. Electrically, it's two diodes in series.

This is elegant. It means existing module assembly lines can handle tandem cells with zero modification. The cell looks, from the outside, exactly like a regular silicon cell. Same shape, same contacts, same stringing process. This is a massive advantage for commercialization.

But there's a catch, and it's a big one: **current matching**. In a series circuit, the current is limited by the weakest link. Both subcells must generate the same photocurrent, or the excess current from the overproducing cell has nowhere to go and is wasted. Since the top cell absorbs blue light and the bottom absorbs red, and since the solar spectrum changes throughout the day (more blue at noon, more red at dawn and dusk), the current balance shifts constantly.

Optimizing a 2T tandem means carefully choosing the perovskite bandgap and thickness so the currents match under a *representative* spectrum — typically the AM1.5G standard. At 1.68 eV bandgap and ~500 nm thickness, researchers typically achieve matched currents around 19–20 mA/cm². But on a cloudy morning or at high latitude in winter, the spectrum shifts red, starving the perovskite top cell and limiting the tandem's output. Annual energy yield simulations show that current mismatch costs a well-designed 2T tandem about 1–2% in real-world energy harvest compared to the theoretical optimum.

The recombination layer itself is a piece of nanoscale engineering worth appreciating. Its job is to allow electrons from the top cell and holes from the bottom cell to meet and annihilate, completing the internal circuit. Most designs use a thin (10–20 nm) layer of indium tin oxide (ITO) or indium zinc oxide (IZO) — the same transparent conductors used in phone screens. This layer must be optically transparent, electrically conductive, and chemically compatible with both the perovskite above and the silicon surface treatments below. It also needs to withstand the thermal budget of any subsequent processing steps without degrading the perovskite.

### The 4-Terminal (Mechanically Stacked) Tandem

In a 4T tandem, the perovskite cell and silicon cell are fabricated completely independently, each with their own two contacts, and simply stacked physically. Four wires come out. Each cell operates at its own optimal voltage and current — no current matching required.

The physics advantage is real. Because neither cell constrains the other, the 4T tandem tolerates spectral variation much better. On that cloudy morning, the perovskite cell's current drops but the silicon cell just cranks harder at its own optimal point. Annual energy yield is typically 2–4% higher than an equivalent 2T design in high-latitude or variable-climate locations.

The manufacturing disadvantage is equally real. You now need two separate encapsulation systems. You need two sets of wiring, two maximum power point trackers (or a specialized dual-input inverter), and the optical losses from the extra glass/encapsulant layers between the cells eat into the efficiency gain. The perovskite top cell needs a transparent back contact, which means a second layer of ITO or a thin metal grid that inevitably shadows some light.

**The industry consensus, as of 2025, has tilted decisively toward 2-terminal.** The manufacturing simplicity is just too compelling. LONGi's 34.85% record, Oxford PV's commercial modules, and virtually every major manufacturer's development roadmap target 2T monolithic integration. The current-matching penalty is a tax worth paying for seamless compatibility with a trillion-dollar silicon supply chain.

## Inside the Stack: Layer by Layer

Let's walk through a state-of-the-art 2T monolithic perovskite/silicon tandem from top to bottom. Every layer matters. Total thickness, not counting the silicon wafer: roughly 1–2 micrometers.

**Anti-reflection coating (MgF₂ or LiF, ~110 nm).** Just like single-junction silicon cells, you need to minimize reflection. Magnesium fluoride is popular for its low refractive index (~1.38) and easy thermal evaporation.

**Transparent top electrode (ITO or IZO, ~70–100 nm).** This is the front contact for the perovskite cell. It must conduct current laterally to a metal grid at the cell edge while transmitting >90% of visible light.

**Electron transport layer (SnO₂ or C₆₀, ~20–30 nm).** This selectively extracts electrons from the perovskite while blocking holes. Tin dioxide deposited by atomic layer deposition (ALD) is the current favorite — conformal, pinhole-free, and processable at temperatures silicon can tolerate.

**Perovskite absorber (~400–600 nm).** The heart of the top cell. Typically a mixed-cation, mixed-halide composition like Cs₀.₀₅FA₀.₈₀MA₀.₁₅Pb(I₀.₈₃Br₀.₁₇)₃ with a bandgap of ~1.68 eV. Deposited either by spin-coating (lab scale), slot-die coating (pilot scale), or co-evaporation (the emerging industrial favorite, since it produces the most uniform films over large areas).

**Hole transport layer (Me-4PACz or PTAA, ~2–5 nm).** Self-assembled monolayers (SAMs) like Me-4PACz have revolutionized tandem design. This molecule is literally one molecule thick — it bonds to the surface below and presents a perfect energy level for extracting holes from the perovskite. It replaced older polymeric layers like Spiro-OMeTAD that were thick, expensive, and unstable.

**Recombination junction (ITO, ~10–20 nm).** The critical bridge. Electrons from the perovskite and holes from the silicon meet here and recombine. This layer also provides a chemical barrier between the perovskite process and the silicon surface.

**Silicon bottom cell (~150–180 μm).** Usually a heterojunction (HJT) or TOPCon architecture — both offer high voltages (>710 mV) that contribute to the tandem's total voltage. The front surface is textured with random pyramids for light trapping, as we covered on Day 7. Getting conformal perovskite deposition over these ~3 μm pyramids is one of the great engineering challenges of tandem fabrication.

**Rear contact and passivation.** Standard silicon back-end processing — aluminum or silver metallization over passivated contacts.

## The Texture Problem: Mountains Under a Thin Blanket

Here's something that looks trivial on paper but has consumed thousands of person-hours of research: silicon wafers have textured surfaces, and perovskite doesn't like that.

The random pyramid texture on a silicon wafer (peak-to-valley height of 1–5 μm) is essential for light trapping — it's the reason silicon cells absorb so well despite their relatively weak absorption coefficient. But when you try to deposit a 500 nm perovskite film over a surface with 3 μm features, you get uneven coverage. Thin spots on pyramid peaks. Pooling in valleys. Pinholes that short-circuit the cell.

The early tandem papers solved this crudely: polish the silicon front surface flat and accept the reflection penalty. This works, but you lose 1–2 mA/cm² of photocurrent from increased reflection — a painful sacrifice when you're fighting for every fraction of a percent.

The breakthrough came from two directions. First, **co-evaporation** of perovskite (dual-source evaporation of PbI₂ and FAI/CsBr in vacuum) produces beautifully conformal films that follow the pyramid texture like a coat of spray paint. Second, researchers developed **submicron textures** — polishing the silicon pyramids down to 0.5–1 μm height, which is small enough for solution-processed perovskite to cover uniformly while still providing significant anti-reflection benefit.

LONGi's record 34.85% cell uses a fully textured silicon bottom cell with a conformal perovskite top cell — proof that the texture problem is, if not fully solved, at least tamed.

## The Voltage Bonus: 1 + 1 > 2

One of the most satisfying aspects of tandem physics is the voltage arithmetic. In a 2T tandem, the open-circuit voltages of the two subcells add. A good silicon HJT bottom cell delivers about 720 mV. A good wide-bandgap perovskite top cell delivers about 1,200 mV. The tandem: ~1,920 mV — nearly 2 volts from a single cell under one sun.

But here's the counterintuitive part: the tandem's combined voltage is actually *higher* than what you'd get from the two cells operating independently. Why? Because in the tandem configuration, the silicon cell is only absorbing infrared photons that the perovskite transmitted. These photons are relatively close in energy to silicon's bandgap, meaning less thermalization loss per absorbed photon. The silicon cell runs "cooler" in a spectral sense — it sees a narrower, more favorable slice of the spectrum. This slightly boosts its voltage compared to a standalone silicon cell under full-spectrum light.

The net effect: a well-optimized tandem delivers about 34–35% of the incident solar energy as electricity, compared to 26–27% for the best single-junction silicon. That's not just an incremental improvement — it's a step change that fundamentally alters the economics of solar installations, because all area-dependent costs (land, racking, wiring, installation labor) are amortized over 30-40% more energy output.

## The Race: Who's Winning?

The perovskite-silicon tandem race is one of the most intense competitions in clean energy. Here's the leaderboard as of early 2026:

**LONGi Green Energy** — 34.85% (NREL-certified, April 2025). The Chinese giant has broken its own record multiple times. Their cell uses a monolithic 2T architecture on a textured silicon HJT bottom cell. LONGi has the manufacturing muscle to scale this first.

**Oxford PV** — 26.9% module efficiency record, 24.5% commercial modules shipping since September 2024. Their Brandenburg factory has a capacity of roughly 50-100 MW and they've delivered panels to a U.S. utility-scale customer — the first commercial deployment of tandem technology anywhere in the world. Their 72-cell panels produce about 20% more energy than standard silicon panels of the same size.

**Hanwha Q Cells** — Partnered with Helmholtz-Zentrum Berlin (HZB), targeting volume production by 2026. HZB has independently achieved >30% on small cells.

**Trina Solar** — 34.15% on a perovskite-HJT tandem, certified by ISFH. Quietly building pilot lines.

**CSEM/EPFL (Switzerland)** — 33.2% on a large-area (>1 cm²) cell, demonstrating that high efficiency isn't only achievable on postage-stamp-sized samples.

The pattern is clear: Chinese manufacturers are winning on cell-level records, while Oxford PV leads on commercialization. The real question isn't whether tandems will work — that's settled. It's whether they can be manufactured at costs competitive with plain silicon, at scale, with acceptable lifetimes.

## The Remaining Challenges

Manufacturing tandems is harder than manufacturing silicon cells, and the challenges are serious:

**Stability.** The perovskite top cell must survive 25+ years outdoors. As we discussed yesterday, perovskite degrades in moisture, heat, and UV light. In a tandem, the silicon bottom cell runs slightly cooler (the perovskite absorbs some of the heat-generating blue light), which helps. But module temperatures in sunny climates routinely hit 65–75°C, and the perovskite must endure this with encapsulation as its only shield. Oxford PV claims their modules pass IEC 61215 qualification testing — the same standard silicon modules must meet — including damp-heat tests at 85°C and 85% relative humidity for 1,000 hours. That's encouraging, but field data beyond a couple of years simply doesn't exist yet.

**Scalability.** Lab records are set on cells of ~1 cm². Commercial modules need ~2.5 m² of uniform perovskite film. The efficiency gap between small cells and large modules is still 8–10 percentage points. Closing that gap requires solving film uniformity, minimizing dead area between cells, and maintaining passivation quality across wafer-to-wafer variation.

**Lead.** Every perovskite solar cell contains lead — roughly 0.5–1 gram per square meter. A utility-scale installation covers tens of thousands of square meters. European regulations (RoHS directive) currently exempt photovoltaic panels, but that exemption is reviewed periodically. If encapsulation fails and rainwater leaches through, lead contamination is a real concern. Research into tin-based perovskites (replacing lead) is active but nowhere near competitive efficiency.

**Process integration.** Adding perovskite deposition to a silicon line means introducing new materials (organic cations, halide salts, fullerenes) into fabs designed for inorganic semiconductor processing. Contamination control, chemical compatibility, and thermal budget management are all real engineering problems. The perovskite layers must be deposited at temperatures below ~150°C to avoid damaging the silicon cell's passivation — a constraint that limits process options.

## The Surprising Economics

Here's the counterintuitive fact that makes tandems almost inevitable: **a tandem module that costs 20% more to manufacture but produces 30% more power is cheaper per watt than the silicon module it replaced.** And it's dramatically cheaper per watt at the *system* level, because the inverter, racking, wiring, land, permitting, and installation labor are all denominated in cost-per-watt. A 400 W tandem panel and a 300 W silicon panel cost nearly the same to install — the installer doesn't care what's inside the glass.

BloombergNEF and other analysts project that perovskite-silicon tandems could reach module-level cost parity with conventional silicon by 2028–2030, assuming current manufacturing scale-up trajectories hold. After that, every additional watt of efficiency is pure economic gain.

This is why the investment frenzy is real. Oxford PV has raised over $400 million. LONGi's R&D budget for tandems is undisclosed but estimated in the hundreds of millions. Hanwha Q Cells committed $100 million to their tandem program. The thesis is simple: whoever cracks volume manufacturing of reliable tandem modules first will have a product that makes everything else on the market obsolete.

## What Comes After?

The silicon-perovskite tandem is the *first* tandem most people will encounter. But it's not the last. Researchers are already stacking three junctions — perovskite on perovskite on silicon — targeting efficiencies above 40% under one sun. And in the nearer term, tandem technology is merging with other innovations that squeeze even more energy from each panel.

Tomorrow, we'll explore one of those innovations: **bifacial modules and tracking systems** — technologies that harvest light from both sides of a panel and follow the sun across the sky. When you combine bifacial design with tandem cells, the energy yield per installed square meter starts approaching territory that seemed like science fiction a decade ago.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-22.toml}}
