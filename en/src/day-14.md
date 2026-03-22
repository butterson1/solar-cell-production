# Day 14: From Cell to Module — Encapsulation & Assembly

*Yesterday, we watched every cell on the production line get its mugshot taken — IV curves, electroluminescence portraits, photoluminescence scans — all in under a second. You now have bins full of tested, graded cells, sorted by current, voltage, and fill factor with obsessive precision. But here's the thing: a bare solar cell is about as useful outdoors as a bare CPU chip. It's a 150-micrometer-thick sliver of doped silicon with exposed metal contacts. Rain would corrode it. Wind would snap it. UV radiation would degrade its surface passivation within months. To survive 25–30 years on a rooftop in Antalya or a ground-mount array in Arizona, that fragile cell needs to be entombed inside a miniature engineering marvel. Today, we're building the module — the thing people actually bolt to their roofs — and the process turns out to be far more interesting than "stick cells between glass."*

## The Sandwich Nobody Thinks About

A finished solar module is, at its core, a laminated sandwich. But calling it a "sandwich" understates the precision involved — this is more like building a time capsule that must remain hermetically sealed while baking in 85°C desert heat and freezing in –40°C Arctic winters, for three decades straight, without anyone ever opening it for maintenance.

From front to back, the standard module stack looks like this:

1. **Front glass** — 3.2 mm tempered, low-iron, with anti-reflective coating
2. **Front encapsulant sheet** — 0.45–0.5 mm EVA or POE
3. **Cell strings** — interconnected solar cells
4. **Rear encapsulant sheet** — 0.45–0.5 mm EVA or POE
5. **Backsheet** (or rear glass for bifacial/glass-glass modules)

Each layer exists for specific, non-negotiable reasons. And the order in which they're assembled — and the physics of how they're bonded — determines whether the module generates power reliably for 30 years or develops bubbles, delamination, and corrosion within five.

## Step 1: Tabbing and Stringing — Wiring the Cells Together

Before anything gets layered or laminated, the cells need to be electrically connected. This is where **tabbing** and **stringing** come in, and it's the step where more cells get cracked than any other in the entire module line.

Here's the setup. Each cell has metal fingers and busbars on its front surface (from the screen-printing metallization step we covered on Day 8) and a full or patterned aluminum back contact. To connect cells in series — which you need to do because each cell produces only about 0.6–0.7 volts, and you want 30–50 volts from the module — you solder a thin copper ribbon from the front busbars of one cell to the rear contact of the next cell.

These copper ribbons are called **tabbing ribbons**: flat copper strips, typically 0.22–0.25 mm thick and 0.9–1.5 mm wide, pre-coated with a tin-lead or lead-free solder alloy. The ribbon width has been shrinking over the years as cell designs move from 4 busbars to 5, 9, 12, or even 16 busbars (multi-busbar or MBB designs). More busbars means shorter current paths across the cell surface, which reduces resistive losses and also means thinner ribbons can handle the lower current per busbar.

The **stringing machine** is one of the most mechanically complex tools on the module line. Here's what happens in roughly 2–3 seconds per cell:

1. A cell is picked from the sorted bin by a vacuum gripper and placed on a heated conveyor or platform.
2. Tabbing ribbons are fed from spools, cut to length, and fluxed (a chemical flux is sprayed or dipped to ensure the solder wets properly).
3. The ribbons are positioned on the cell's front busbars with sub-millimeter accuracy.
4. An infrared lamp, hot air jet, or laser heats the ribbon-to-busbar interface to about 180–220°C for conventional tin-lead solder, or 230–260°C for lead-free alternatives (SnBiAg is popular). The solder melts, wets the busbar metallization, and forms a bond.
5. The next cell is placed so its rear contact aligns with the trailing ends of the ribbons from the previous cell, and the same heating cycle bonds the ribbon to the back.

The result is a **string** — typically 10–12 cells connected in series, depending on the module format. A standard 72-cell module might have six strings of 12 cells each.

Here's why this step is terrifying for manufacturers: you're applying 200°C+ heat to a 150-micrometer silicon wafer while simultaneously pressing a metal ribbon onto it. The thermal expansion coefficient of copper (17 × 10⁻⁶ /°C) is roughly triple that of silicon (2.6 × 10⁻⁶ /°C). When the solder cools, the ribbon contracts far more than the silicon, bowing the cell into a gentle curve and inducing thermal stress. If the stress concentrates at a defect — a micro-crack from the wafering process, a laser-scribed groove, a handling nick — the crack propagates, and you've just destroyed a cell worth $0.15–0.20.

Modern stringer machines mitigate this with controlled cooling ramps, optimized solder alloy formulations (some use low-melting-point indium-bismuth alloys at just 139°C), and **multi-busbar (MBB) designs** where 12–16 thin round wires replace the traditional flat ribbons. The round wires distribute stress more evenly and, counterintuitively, make better optical use of the cell surface because their circular cross-section reflects light back down toward the cell at low angles.

## Step 2: String Layout and Bus Ribbon Interconnection

Once you have your strings — say six strings of 12 cells — they need to be laid out in the module pattern and connected to each other. The strings are typically arranged in two or three groups (called **substrings**), with each substring containing an equal number of cells wired in series. Between substrings, thicker **bus ribbons** (2–4 mm wide, sometimes tinned copper braid) connect the strings and route current to the junction box location.

This layout step is increasingly automated. Robots pick up completed strings and place them onto the glass or encapsulant layer with millimeter precision. The spacing between strings matters — too close and you risk ribbon shorts; too far and you waste module area. A typical inter-string gap is 2–3 mm.

The substring architecture is not just an assembly convenience — it's **electrically critical** for the bypass diode strategy we'll discuss later. A typical 72-cell module has three substrings of 24 cells, each protected by one bypass diode. If one cell in a 24-cell substring gets shaded, the bypass diode activates and shorts out only that substring, preserving 2/3 of the module's output. Without this division, shading one cell could take down the entire module.

## Step 3: The Glass — Not Just Any Glass

The front cover of a solar module is its first line of defense, and it's not the glass from your kitchen window. Solar glass is **low-iron tempered glass**, and the "low-iron" part matters enormously. Ordinary soda-lime glass contains about 0.1% iron oxide (Fe₂O₃), which absorbs light in the near-infrared region where silicon cells still respond. Solar glass uses feedstock with iron content below 0.01% — sometimes as low as 0.008% — which pushes its transmittance above 91.5% across the solar spectrum compared to about 89% for standard glass.

That 2.5-percentage-point difference might sound trivial. It's not. Applied across a 2-square-meter module generating 550 watts, it represents roughly 14 watts — and over a 30-year lifetime in a decent solar location, that's about 500 kWh of energy. At grid-scale prices, low-iron glass pays for itself within the first year.

The glass is **tempered** — heated to 620°C and then rapidly quenched with air jets — which gives it about four times the mechanical strength of annealed glass and ensures that if it does break (from a hailstone, say), it shatters into small, relatively harmless granules rather than sharp shards. IEC 61215 requires modules to survive a 25 mm ice ball impacting at 23 m/s — equivalent to a severe hailstorm. The 3.2 mm tempered glass routinely passes this test.

Most front glass also gets an **anti-reflective coating** (ARC), typically a porous silica sol-gel layer about 120 nm thick, which reduces front-surface reflection from ~4% to ~2%. Some premium modules use **textured glass** with a pyramidal surface pattern that further reduces reflection and makes the module less angle-sensitive throughout the day.

## Step 4: The Encapsulant — EVA and Its Challengers

If the glass is the armor, the encapsulant is the embalming fluid. Its job is to optically couple the cells to the glass, cushion the cells against mechanical stress, block moisture ingress, and maintain electrical insulation — for decades.

**Ethylene-vinyl acetate (EVA)** has dominated this role since the 1980s. It's a copolymer with about 28–33% vinyl acetate content, supplied as a pre-cast film approximately 0.45 mm thick. In its as-delivered state, EVA is a soft, slightly tacky thermoplastic. During lamination, it melts, flows around the cells and ribbons, fills every gap and crevice, and then — critically — **crosslinks** via a peroxide-initiated free-radical reaction. The peroxide (typically tert-butyl peroxy-2-ethylhexanoate, sometimes called TBEC) decomposes at temperatures above 140°C, generating radicals that create covalent bonds between EVA polymer chains. The EVA transforms from a thermoplastic (which can re-melt) into a thermoset (which cannot). This crosslinking is irreversible and must achieve at least 65–85% gel content for adequate long-term performance.

Here's the surprising fact about EVA: **it degrades by producing acetic acid.** When exposed to UV light and heat over years, the vinyl acetate groups hydrolyze, releasing acetic acid — the same chemical that gives vinegar its smell. This acid corrodes the cell metallization, attacks the tin-oxide transparent conductive oxide in some cell designs, and causes the infamous **browning** (yellowing) of older modules. The acetic acid also lowers the encapsulant's volume resistivity, which can trigger **potential-induced degradation (PID)** — a voltage-driven leakage current that can destroy cells.

This is why the industry is increasingly shifting to **polyolefin elastomers (POE)**, which contain no vinyl acetate and therefore cannot produce acetic acid. POE has much lower moisture vapor transmission rates (~1/10th of EVA's), better volume resistivity (>10¹⁴ Ω·cm vs. EVA's ~10¹³), and superior PID resistance. The catch? POE costs roughly 15–25% more than EVA and requires different lamination parameters (lower crosslinking temperatures, different adhesion promoters). Many manufacturers now use a hybrid approach: **EPE** — a three-layer EVA/POE/EVA coextruded film that puts POE against the cell surface for moisture protection while using EVA on the outside for better glass adhesion.

## Step 5: Lamination — The Critical 15 Minutes

Lamination is the make-or-break step. Everything up to this point is reversible — you could unstick a misaligned string and fix it. After lamination, it's done. Whatever's inside that sandwich stays inside for 30 years.

The module stack — glass, front encapsulant, cell strings, rear encapsulant, backsheet — is assembled on a **layup table**, usually by robotic arms working in a cleanroom or semi-clean environment (dust particles trapped in the laminate cause visible defects and potential hotspots). The complete layup is then conveyed into a **vacuum laminator**.

The laminator is essentially a heated chamber split into two zones by a flexible silicone membrane. Here's the process, step by step:

**Phase 1 — Evacuation (3–5 minutes):** Both the upper and lower chambers are pumped down to approximately 0.5–1.0 mbar. This removes all air from between the layers. If air remains, it forms bubbles that become permanent defects — visible as white spots and acting as stress concentrators and moisture traps.

**Phase 2 — Heating and pressing (8–12 minutes):** The heated platen below raises the laminate temperature to 135–150°C. Once the EVA softens and begins flowing (around 70°C), the upper chamber is vented to atmospheric pressure while the lower chamber remains under vacuum. This pushes the flexible membrane down onto the module with approximately 1 atmosphere of pressure (~100 kPa) — the same force as having a small car parked on the module. The pressure squeezes the molten encapsulant uniformly around every cell, ribbon, and wire. As the temperature climbs above 140°C, the peroxide initiator in the EVA decomposes, and crosslinking begins.

**Phase 3 — Curing (5–8 minutes):** The laminate is held at 145–150°C to complete the crosslinking reaction. The target is typically >65% gel content, verified by solvent extraction tests (you dissolve a sample of cured EVA in toluene and weigh what doesn't dissolve — that's your crosslinked fraction). Under-cure means the EVA can delaminate or shift over time. Over-cure wastes cycle time and can cause excessive yellowing from thermal degradation of UV stabilizers.

The total lamination cycle is typically 15–22 minutes, making it the **single biggest bottleneck** in module assembly. A laminator typically holds 1–2 modules at a time, which means at 18 minutes per cycle, one laminator processes about 3.3 modules per hour. A factory producing 2 GW of modules per year (roughly 3.5 million modules) needs 20–30 laminators running in parallel, each costing $300,000–$500,000. Companies like Bürkle, Robert Bürkle GmbH, NPC, and 3S Swiss Solar have spent decades optimizing laminator designs to shave minutes off the cycle — because every minute saved translates directly to millions in capital equipment costs.

## Step 6: The Backsheet (or Rear Glass)

Behind the rear encapsulant sits the **backsheet**, the module's final barrier against moisture, UV, and mechanical damage from behind. The classic backsheet is a **TPT** laminate — Tedlar (polyvinyl fluoride) / PET (polyester) / Tedlar — developed by DuPont in the 1970s. The fluoropolymer Tedlar layers provide extraordinary UV resistance and moisture barrier properties, while the PET core adds mechanical strength and electrical insulation.

But Tedlar is expensive ($5–8 per square meter), and the industry has been steadily moving toward cheaper alternatives: **KPE** (Kynar PVDF / PET / EVA), **PPE** (PET / PET / EVA), and even **co-extruded polyolefin** backsheets. The cheapest options (PPE) can cost as little as $2–3 per square meter but have historically shown faster degradation in hot, humid climates — backsheet cracking has been the second most common field failure mode after junction box issues, according to data from PVEL's module reliability scorecard.

For bifacial modules — which capture light from both sides — the backsheet is replaced with a second sheet of glass, typically 2.0–2.5 mm thick (thinner than the front glass to save weight). **Glass-glass modules** are heavier (~28–32 kg for a 72-cell module vs. ~22–24 kg for glass-backsheet) but offer superior moisture protection, better fire ratings, and longer warranted lifetimes — some manufacturers now offer 30-year performance warranties on glass-glass designs versus 25 years for glass-backsheet.

## Step 7: Trimming, Framing, and the Junction Box

After lamination and cooldown, the module emerges as a rigid, sealed panel. But it's not finished yet. The edges need trimming — excess encapsulant and backsheet material that oozed out during lamination are cut flush. Then come three final components:

**The aluminum frame.** Most modules get an extruded aluminum alloy (typically 6063-T5) frame that snaps or is adhesive-bonded around the perimeter. The frame provides mechanical rigidity for mounting, protects the glass edges from chipping during handling, and gives the module a defined mounting interface. Silicone sealant or butyl tape fills the gap between the glass edge and the frame, preventing moisture ingress. Frameless glass-glass modules skip this step entirely and are mounted with clamps, saving about $3–5 per module and 1–2 kg of aluminum.

**The junction box.** This small plastic enclosure (typically rated IP67 or IP68) is adhesive-bonded to the rear of the module, directly over the points where the bus ribbons exit the laminate. Inside the junction box sit the **bypass diodes** — typically three Schottky diodes for a 72-cell module, one per substring. When a substring is shaded or contains a failing cell, the bypass diode provides an alternative current path, preventing the shaded cells from overheating as reverse-biased hotspots.

The choice of bypass diode matters more than you might expect. Standard silicon p-n diodes have a forward voltage drop of about 0.6–0.7 V, meaning when they're active, you lose that voltage times the string current in heat — which is dissipated inside the junction box. A 10-amp current through a 0.7 V diode generates 7 watts of heat in a small plastic enclosure. **Schottky diodes** have lower forward voltage (0.3–0.4 V), reducing this waste heat almost by half. Some modern modules use **intelligent bypass devices** — integrated circuits from companies like STMicroelectronics and Maxim Integrated that reduce the voltage drop to near zero and can even perform per-cell optimization.

The junction box also contains the output cables (typically MC4-compatible connectors with 4 mm² or 6 mm² cross-section copper conductors) and potting compound (silicone or polyurethane) that seals the internal connections against moisture.

## Step 8: Final Testing and Sorting

The finished module goes through its own version of the cell testing we covered yesterday, but at the module level. A **module flash tester** — essentially a large solar simulator with a uniformly illuminated area of 2+ square meters — fires a xenon flash while the module's IV curve is swept. The resulting power rating goes on the nameplate label and determines the module's sale value.

Module flash testers have their own accuracy challenges. The uniformity requirement across a 2 m² area is demanding — Class AAA simulators at the module level cost $150,000–$400,000. And because the flash duration must be long enough to sweep the IV curve of a high-capacitance module (all those parallel-connected cells act as a large capacitor), module simulators use **long-pulse** or **continuous** simulators rather than the millisecond xenon flashes used for individual cells.

Modules are binned by power output, typically in 5-watt increments (e.g., 545 W, 550 W, 555 W), and this binning is one of the things customers care most about. A 1% power sorting tolerance on a 550 W module means ±5.5 W per module, which across a 100 MW solar farm (roughly 180,000 modules) could mean a MW-scale difference in total plant output.

## The Economics of Assembly

Here's a number that should surprise you: the cell-to-module (CTM) power **ratio can actually exceed 100%**. Wait — how can a module produce more power than the sum of its individual cells?

It comes down to optics. When cells are encapsulated, several things change. The glass and encapsulant have a higher refractive index (~1.5) than air (~1.0), which reduces reflection losses at the cell surface. Light that hits the spaces between cells can be reflected by the white backsheet back up to the glass surface, where total internal reflection can redirect it toward a cell. And anti-reflective coatings on the glass add another few tenths of a percent. These optical gains can amount to 2–4%, while the losses from cell-to-cell spacing, ribbon shadowing, resistive losses in interconnections, and string mismatch typically total 1–3%. The net result for a well-designed module is a CTM ratio of 100–102% — the module literally produces slightly more power than the cells would individually.

This wasn't always the case. A decade ago, CTM ratios were typically 97–98%, and module assembly was purely a value-destroying step. The improvement came from a combination of MBB interconnection (less ribbon shadowing), half-cut cells (lower resistive losses), denser cell spacing, higher-reflectance backsheets, and better glass coatings. It's a beautiful example of system-level engineering turning what was once a necessary evil into a net positive.

The bill of materials for a standard 550 W module breaks down roughly as: cells (~55–60% of module cost), glass (~8–10%), encapsulant (~5–7%), backsheet (~3–5%), frame (~4–6%), junction box and cables (~3–4%), and labor plus overhead (~10–15%). At current market prices, the total module cost is approximately $0.09–0.13 per watt — meaning a 550 W module sells for about $50–72. The cell-to-module conversion adds roughly $0.02–0.03/W, or about $11–17 per module.

## Tomorrow's Preview

We've now followed a solar cell from bare tested wafer to a finished, weather-sealed, tested module ready for shipping. But we've been looking at this process one step at a time, as if through a microscope. Tomorrow, we zoom out — way out — and walk the entire factory floor from sand delivery to shipping dock. Day 15 will map the complete factory layout: how all these individual steps connect, where the buffer stocks sit, what the material flows look like, and why a modern 10 GW cell-and-module factory is one of the most precisely choreographed manufacturing operations on the planet.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-14.toml}}
