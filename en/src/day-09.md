# Day 9: Cell Architectures — PERC, TOPCon, HJT

*Over the past eight days, you've followed silicon from a quartzite mine to a screen-printed, metallized solar cell. But here's the thing: we've been describing a "standard" aluminum back-surface field (Al-BSF) cell — a design that peaked around 20% efficiency and is now, in 2025, essentially a museum piece. The real solar industry has moved on, split into three warring factions — PERC, TOPCon, and HJT — each betting billions of dollars on a different answer to the same question: how do you stop electrons from dying at surfaces?*

---

## The Enemy: Surface Recombination

Before we dive into the alphabet soup, you need to understand the problem all three architectures are trying to solve, because it's the same problem, and it's infuriating.

When you generate an electron-hole pair by absorbing a photon (Day 1), that pair needs to survive long enough to reach the p-n junction, get separated, and flow out through the metal contacts (Day 8). In the bulk of a high-purity monocrystalline silicon wafer, a minority carrier can live for several milliseconds — an eternity in semiconductor terms, enough time to diffuse several hundred micrometers. The bulk isn't the problem.

The surfaces are the problem. Silicon's crystal lattice terminates abruptly at every surface, leaving behind "dangling bonds" — unsatisfied silicon atoms with unpaired electrons that act like traps. Any electron or hole that wanders near a surface is overwhelmingly likely to recombine there, its energy wasted as heat. The recombination velocity at an untreated silicon surface can exceed 10⁶ cm/s. For comparison, a well-passivated surface can achieve recombination velocities below 2 cm/s. That's a factor of 500,000.

The front surface of a cell was largely solved in Days 6 and 7: the phosphorus-doped emitter, the silicon nitride ARC, and the surface texturing together keep the front-side recombination velocity manageable. The *rear* surface is where the three architectures diverge — and where most of the efficiency gains of the past decade have come from.

In the old Al-BSF cell, the rear was simply covered in aluminum paste and fired, creating a p⁺ back-surface field that provided modest passivation (recombination velocity ~200–500 cm/s) and reflected maybe 60–70% of photons that reached the back. It worked, but it was leaving at least 2–4 percentage points of absolute efficiency on the table. That's the gap PERC, TOPCon, and HJT are each trying to close — and at utility-scale, every 0.1% of absolute efficiency is worth roughly $0.002–0.003 per watt, which across a 50 GW production line translates to $100–150 million per year in module value.

---

## PERC: The Incumbent That Changed Everything

**Passivated Emitter and Rear Cell** (PERC) was invented in 1983 by Martin Green's group at the University of New South Wales — the same lab that has held the silicon cell efficiency record more times than any other. But it took nearly 30 years for PERC to go from lab curiosity to manufacturing reality. The concept is deceptively simple: instead of covering the entire rear with aluminum, deposit a thin dielectric passivation layer (typically aluminum oxide, Al₂O₃, 5–20 nm thick, followed by silicon nitride) and then open local contact points through the dielectric using laser ablation.

Here's why this works so well. Aluminum oxide carries a fixed negative charge density of roughly 10¹² to 10¹³ charges per cm² at the interface with p-type silicon. This negative charge repels minority carrier electrons away from the rear surface — a phenomenon called "field-effect passivation." Combined with the chemical passivation that Al₂O₃ provides (saturating dangling bonds), the rear surface recombination velocity drops from ~300 cm/s in Al-BSF to below 10 cm/s in PERC. That alone is worth about 0.8–1.0% absolute efficiency.

But there's a second benefit that's equally important: the dielectric stack acts as an internal mirror. Photons in the near-infrared (900–1200 nm) that pass through the entire wafer without being absorbed — long-wavelength photons that silicon absorbs weakly — now bounce off the dielectric/aluminum reflector with 90–96% efficiency instead of the ~65% of a bare aluminum BSF. These reflected photons get a second pass through the wafer, dramatically improving the long-wavelength response. This "optical gain" adds another 0.3–0.5% absolute efficiency.

The key manufacturing addition is just two steps: depositing the Al₂O₃/SiNₓ rear passivation stack (using atomic layer deposition or PECVD, adding ~$0.005–0.008/W) and laser-opening the contact holes (using a pulsed laser, typically 532 nm Nd:YAG, with spot sizes of ~50 μm). That's it. The rest of the line — texturing, diffusion, front ARC, screen printing — stays essentially identical to Al-BSF. This backward compatibility is why PERC conquered the industry so quickly: you could retrofit existing production lines for $10–20 million, compared to $100+ million for a greenfield TOPCon or HJT line.

By 2020, PERC had gone from near-zero to over 80% of global cell production. LONGi Green Energy, the world's largest solar manufacturer, bet the company on PERC and won spectacularly, growing from a mid-tier player to a $60 billion market cap giant. Production PERC cells routinely hit 23.0–23.5% efficiency, with LONGi's record at 24.06%. But that number is important: 24% is uncomfortably close to PERC's practical ceiling.

The problem is fundamental. PERC still uses a homogeneous phosphorus diffusion for its front emitter, creating a relatively heavy doping at the surface (~10²⁰ atoms/cm³) that causes significant Auger recombination — a three-body process where an electron recombines with a hole by transferring its energy to a third carrier. This front-surface recombination, plus the remaining losses at the local rear contacts, puts PERC's theoretical maximum around 24.5%. The industry is already at 23.5% in production, meaning PERC has used up about 95% of its headroom. The well is running dry.

---

## TOPCon: The Heir Apparent

**Tunnel Oxide Passivated Contact** (TOPCon) — sometimes called "passivated contact" or "poly-Si on oxide" — is PERC's most likely successor, and by early 2026, it has already overtaken PERC in new production capacity additions.

The core idea is beautiful in its physics. Instead of opening holes in the rear dielectric and making local metal-silicon contacts (which are recombination hotspots), TOPCon creates a "passivated contact" — a contact that extracts current *without* the metal ever touching the silicon wafer's surface. Here's how:

1. **Tunnel oxide:** Grow an ultra-thin silicon dioxide layer on the rear surface — just 1.0–1.5 nm thick, about 5–7 atomic layers. This oxide is thin enough that electrons can quantum-mechanically tunnel through it, but thick enough to chemically passivate the surface (saturating dangling bonds) and provide a barrier to hole transport.

2. **Doped poly-Si:** Deposit a layer of heavily n-doped polycrystalline silicon (50–200 nm thick, doped to ~10²⁰ cm⁻³ with phosphorus) on top of the tunnel oxide. This poly-Si layer does two things: it provides a reservoir of free electrons that creates a strong field-effect passivation (repelling holes away from the rear surface), and it serves as a lateral transport layer to carry current to the metal contacts.

3. **Metallize on poly-Si:** The screen-printed metal contacts touch only the poly-Si layer, never the crystalline wafer. The recombination-prone metal-semiconductor interface is now separated from the absorber by the tunnel oxide, dropping the "contact recombination" to near-zero.

The result is a rear surface recombination current density (J₀) of just 2–5 fA/cm², compared to 20–50 fA/cm² for PERC's local contacts and ~200 fA/cm² for Al-BSF. This enables open-circuit voltages (Voc) of 710–720 mV in production, versus 680–690 mV for PERC. Since efficiency is proportional to Voc × Jsc × FF, that voltage gain alone is worth 1.0–1.5% absolute efficiency.

Production TOPCon cells now routinely hit 25.0–25.5%, with JinkoSolar holding the record at 26.89% (independently confirmed by ISFH, announced November 2024). The theoretical limit for single-junction TOPCon is around 28.7%, so there's still meaningful headroom.

The manufacturing challenge is that tunnel oxide. Growing a uniform 1.2 nm oxide over a 182 mm × 182 mm (or 210 mm × 210 mm) wafer is extraordinarily difficult. The oxide must be pinhole-free — a single pinhole creates a "shunt" that bleeds current and kills voltage. The industry has converged on two approaches: thermal oxidation in a tube furnace (growing the oxide at 600°C in a controlled O₂/N₂ atmosphere) and LPCVD for the poly-Si deposition. These tools are large, expensive (a single LPCVD tube costs $2–5 million), and finicky — temperature uniformity across a 1,200-wafer batch must be held to ±2°C.

The conversion cost from a PERC line to TOPCon is roughly $30–50 million for a 5 GW facility, compared to $150–250 million for a greenfield TOPCon line. Chinese manufacturers — Jolywood, Jinko, Trina, Tongwei, JA Solar — have been converting PERC lines to TOPCon at a furious pace. By the end of 2025, global TOPCon capacity exceeded 500 GW, surpassing PERC in new installations for the first time. The transition happened in about three years, one of the fastest technology shifts in industrial history.

There's one subtlety worth noting: most production TOPCon cells are "rear-junction" designs, where the p-n junction is at the rear (between the n-type wafer and the p-type emitter formed by boron diffusion at the front). This is the opposite of PERC, which uses a p-type wafer with a front-side n-type emitter. The shift from p-type to n-type wafers matters for two reasons. First, n-type silicon doesn't suffer from light-induced degradation (LID) — the boron-oxygen complex that plagues p-type wafers and causes 1–3% power loss in the first year. Second, n-type silicon has higher minority carrier lifetimes (>1 ms vs. ~0.1 ms for p-type Cz), which is essential for extracting the full benefit of the passivated contact. The downside: n-type wafers cost 5–10% more because the phosphorus doping of the ingot is trickier to control than boron doping.

---

## HJT: The Elegant Outsider

**Heterojunction Technology** (HJT, sometimes called SHJ for silicon heterojunction) is the most elegant of the three architectures, and also the most different from traditional cell manufacturing. Where PERC and TOPCon are evolutionary — adding passivation layers to a fundamentally similar process flow — HJT is a different animal entirely.

The idea came from Sanyo (now Panasonic) in the early 1990s, commercialized as "HIT" cells. The concept borrows from thin-film technology: instead of using diffusion furnaces to create doped regions at 800–900°C, HJT deposits ultra-thin layers of hydrogenated amorphous silicon (a-Si:H) onto the crystalline silicon wafer at low temperatures — below 200°C for the entire process after texturing.

The HJT stack, from rear to front:

1. **Metal contacts** (screen-printed or plated, on TCO)
2. **Transparent conductive oxide** (TCO, typically indium tin oxide, ITO, ~75 nm)
3. **p-doped a-Si:H** (~5–10 nm)
4. **Intrinsic a-Si:H** (i-layer, ~5–8 nm) — the passivation magic
5. **n-type crystalline silicon wafer** (130–150 μm)
6. **Intrinsic a-Si:H** (i-layer, ~5–8 nm)
7. **n-doped a-Si:H** (~5–10 nm)
8. **TCO** (~75 nm)
9. **Metal contacts**

The critical layer is the intrinsic (undoped) amorphous silicon — just 5–8 nm of a-Si:H deposited by PECVD. This layer provides the best surface passivation known to science for crystalline silicon: implied Voc values above 750 mV, compared to 720 mV for the best TOPCon. The hydrogen in the a-Si:H saturates virtually every dangling bond at the c-Si surface, achieving surface recombination velocities below 2 cm/s.

The numbers speak for themselves. LONGi achieved 27.30% efficiency on an HJT cell in late 2024, and several manufacturers have pushed past 26% in production. The theoretical limit for single-junction HJT is the same as any crystalline silicon cell (~29.4%), but HJT gets closer to it because of its superior passivation.

Here's the counterintuitive surprise: **HJT cells have fewer processing steps than PERC or TOPCon.** A typical HJT line has just 4–5 main steps:

1. Texturing & cleaning
2. a-Si:H deposition (4 layers in one PECVD tool: i/n on one side, i/p on the other)
3. TCO sputtering (both sides)
4. Metallization (screen printing or plating, both sides)
5. (Optional) light annealing

Compare this to PERC's ~10 steps or TOPCon's ~12 steps. The simplicity is stunning. But there's a catch — actually, several catches.

**The temperature constraint:** Because amorphous silicon crystallizes (and loses its passivation properties) above ~200°C, the entire process after a-Si:H deposition must stay cold. This rules out conventional silver paste firing at 750–850°C. HJT cells require special low-temperature silver pastes that cure at 150–200°C. These pastes have higher resistivity than fired pastes (requiring more silver per cell — about 15–20 mg/W versus 10–13 mg/W for TOPCon) and cost more per kilogram. Silver consumption is HJT's Achilles heel.

**The equipment cost:** PECVD tools for a-Si:H deposition must achieve angstrom-level thickness uniformity across large wafers, with sub-ppm control of doping gases (silane, trimethylboron, phosphine). The leading equipment suppliers — Meyer Burger (Swiss), Maxwell (Chinese), and Sumitomo (Japanese) — sell these tools for $15–25 million each. ITO sputtering targets use expensive indium ($300–600/kg). A complete HJT line costs roughly $80–120 million per GW, compared to $50–70 million per GW for TOPCon.

**The indium question:** Each HJT cell requires about 200–300 mg of indium (via ITO). Global indium production is roughly 900 tonnes per year. If HJT were to reach 500 GW of annual production, it would need about 1,500 tonnes of indium — far more than the entire current supply. This is a genuine scaling bottleneck that the industry is attacking with alternative TCOs (aluminum-doped zinc oxide, AZO, or hydrogen-doped indium oxide, IOH) and thinner ITO layers.

---

## The Scorecard: Head to Head

Let's put real numbers on this:

| Metric | PERC | TOPCon | HJT |
|--------|------|--------|-----|
| Production efficiency (2025) | 23.0–23.5% | 25.0–25.5% | 25.0–26.0% |
| Record cell efficiency | 24.06% | 26.89% | 27.30% |
| Typical Voc | 680–690 mV | 710–720 mV | 740–750 mV |
| Process steps | ~10 | ~12 | ~5 |
| Max process temperature | 850°C | 850°C | 200°C |
| Silver consumption (mg/W) | 12–15 | 10–13 | 15–20 |
| Capex per GW | $40–60M | $50–70M | $80–120M |
| Wafer type | p-type | n-type | n-type |
| Temperature coefficient | −0.38%/°C | −0.32%/°C | −0.26%/°C |
| Bifaciality factor | 70% | 80–85% | 90–95% |

That last row deserves attention. HJT's symmetric structure (passivated contacts on both sides) makes it naturally bifacial — it can capture light from both the front and rear, which matters enormously for ground-mounted utility installations where albedo (reflected light from the ground) can boost energy yield by 5–15%. HJT's temperature coefficient is also the best: for every degree Celsius above 25°C, HJT loses only 0.26% of its power, versus 0.38% for PERC. In hot climates — the Middle East, India, Australia — this translates to 3–5% more annual energy production.

---

## The Market Reality: Why TOPCon Is Winning (For Now)

Despite HJT's technical superiority in several metrics, TOPCon is dominating the capacity buildout. The reason is brutally practical: conversion economics. China's solar manufacturers had hundreds of GW of PERC production lines that could be converted to TOPCon for $6–10 per watt of capacity. Building new HJT lines costs $80–120 per watt of capacity from scratch, and PERC lines can't be converted to HJT — the equipment is entirely different.

The math was simple. Tongwei, the world's largest cell manufacturer with over 80 GW of capacity, announced in 2023 that it would convert its entire PERC fleet to TOPCon. JinkoSolar, JA Solar, Trina — all made the same bet. By the time HJT manufacturers like Huasun, Risen, and Maxwell scaled up, the TOPCon juggernaut was already at 500+ GW.

But the race isn't over. HJT's silver consumption — its biggest cost disadvantage — is being attacked from multiple angles. Copper plating (replacing screen-printed silver entirely) could cut metallization costs by 70–80%. SmartWire Connection Technology (SWCT), pioneered by Meyer Burger, uses thin copper wires instead of busbars, reducing silver to below 5 mg/W. And as we'll see in Day 11 and Day 22, HJT is the natural bottom cell for perovskite-silicon tandems — the technology most likely to break 30% efficiency in mass production.

The next five years will determine whether TOPCon's head start cements its dominance or HJT leapfrogs it with tandem stacking. Either way, Al-BSF is dead, PERC is dying, and the future belongs to passivated contacts.

---

## Looking Ahead

Tomorrow, we leave crystalline silicon behind entirely — at least for a day. **Day 10: Thin-Film Alternatives** dives into cadmium telluride (CdTe), copper indium gallium selenide (CIGS), and amorphous silicon — technologies that take a completely different approach to the cost-efficiency tradeoff. Why did First Solar bet $5 billion on a technology made from a toxic heavy metal? How did CdTe become the cheapest solar technology per watt in certain climates? And why does thin-film stubbornly refuse to die despite crystalline silicon's crushing cost reductions? The answers are more interesting than you'd expect.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-09.toml}}
