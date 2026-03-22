# Day 26: Space Solar & Concentrator PV — Harvesting Starlight

## The Sun Is Better in Space

Here's a number that should haunt every solar engineer on Earth: the sun delivers **1,361 watts per square meter** at the top of our atmosphere — the so-called solar constant. By the time that light fights through 100 kilometers of air, bounces off clouds, gets scattered by dust, and dims with the angle of your roof, a typical ground-based panel sees maybe 200–300 W/m² averaged over a day. On a good day in Arizona, you might hit 1,000 W/m² at noon. At night, you get zero.

In geostationary orbit, 35,786 km above the equator, a solar panel stares at that full 1,361 W/m² for roughly **99.5% of the year** — eclipsed by Earth's shadow for only a few weeks around the equinoxes, and even then for just 72 minutes at most. No clouds. No atmosphere. No night (almost). A solar panel in GEO collects 5 to 10 times more energy per year than the same panel on a rooftop in Germany.

This staggering advantage has been tantalizing physicists since **1941**, when Isaac Asimov wrote about a space station beaming energy to planets in his short story "Reason." The concept got its first serious engineering treatment from **Peter Glaser** in 1968, who proposed a satellite with a 5-km-wide solar collector beaming microwaves to a ground antenna. NASA studied it extensively in the late 1970s, crunched the numbers, and concluded: technically feasible, economically insane. Launching anything to orbit cost about **$54,000 per kilogram** on the Space Shuttle. The math just didn't close.

But launch costs have collapsed. SpaceX's Falcon 9 currently charges under **$3,000/kg** to low Earth orbit. Starship, if it delivers on its promises, aims for **$100–200/kg** — and Elon Musk has floated an aspirational target of $10/kg. Suddenly, the arithmetic of space solar power is being reworked by engineers worldwide.

## Solar Cells That Survive the Void

Before we dream about powering cities from orbit, let's talk about what solar cells actually work up there — because your standard residential silicon panel would be a terrible choice.

Space is savage. Beyond the atmosphere, solar cells face **cosmic rays, solar proton events, and trapped radiation in the Van Allen belts** — a constant bombardment of high-energy particles that knock atoms out of the crystal lattice, creating defects that degrade performance. An unshielded silicon cell would lose significant output within days. Even protected cells degrade: a typical mission budgets for **2–3% efficiency loss per year** from radiation damage.

The solution: **III-V multi-junction cells** built from gallium arsenide (GaAs) and related compounds like indium gallium phosphide (InGaP) and indium gallium arsenide (InGaAs). We covered multi-junction cells on Day 11, but space is where they truly earn their keep. A modern **triple-junction InGaP/GaAs/InGaAs cell** achieves around **30–32% efficiency** at beginning of life in space (under the AM0 spectrum, which is the unfiltered solar spectrum above the atmosphere). After 15 years in GEO, radiation degrades that to roughly **26–28%** — still far better than silicon would manage.

These cells are shockingly expensive on a per-area basis: roughly **$80,000–$130,000 per square meter**, compared to about $30/m² for commodity silicon cells. But in space, you're not optimizing for dollars-per-square-meter — you're optimizing for **watts per kilogram**. Every gram you launch costs money. A III-V cell delivers about **350–450 W/kg** on ultra-light substrates (some experimental cells reach 3,000 W/kg on flexible films), while a glass-fronted silicon module manages maybe 15–20 W/kg. When launch costs dominate your budget, the expensive-but-featherweight cell wins decisively.

The **International Space Station** runs on eight massive solar array wings spanning 2,500 m² total, originally generating about **120 kW** using silicon cells (they were designed in the 1990s, before III-V cells became standard). After decades of radiation exposure and micrometeorite hits, they'd degraded badly — so NASA has been overlaying new **ROSA (Roll-Out Solar Array)** panels using modern III-V cells since 2021 to restore power.

## Concentrator PV: Less Cell, More Light

Now here's an elegant question: if multi-junction cells can convert 46% of concentrated sunlight into electricity (the current lab record, held by **Fraunhofer ISE** and **NREL** using a four-junction cell), but cost $50,000+ per square meter, what if you just... used a lot less cell?

That's the fundamental insight behind **concentrator photovoltaics (CPV)**. Instead of covering a huge area with expensive semiconductor, you cover a huge area with *cheap optics* — lenses or mirrors — and focus all that light onto a tiny, ultra-efficient cell. A system at **500× concentration** needs 500 times less cell area. If your concentrating optics cost $50/m² and your cell costs $50,000/m², you've just replaced $50,000 of semiconductor with $50 of plastic and a cell the size of your thumbnail.

### How It Works: The Anatomy of a CPV Module

A high-concentration PV (HCPV) module looks nothing like a conventional flat panel. Picture a metal frame holding an array of **Fresnel lenses** — those flat, ridged lenses you've seen in overhead projectors and lighthouse beacons. Each lens, typically 10–20 cm across and just a few millimeters thick, focuses sunlight down to a spot about **1 cm²**. At that focal point sits a multi-junction cell (usually triple- or quadruple-junction III-V) mounted on a heat spreader, because concentrating 500 suns onto a square centimeter generates intense thermal load.

The concentration ratio matters enormously. At **500×**, you need your tracking to be accurate within about ±0.5°. At **1,000×**, the tolerance tightens to ±0.3°. This is why every HCPV system sits on a **dual-axis solar tracker** — a motorized mount that follows the sun across the sky with arc-minute precision. The tracker adds cost and mechanical complexity, but it also means the system captures direct normal irradiance (DNI) all day, squeezing more energy from every sunny hour.

Here's the counterintuitive part: **CPV systems don't work well in cloudy climates**. Conventional silicon panels can use diffuse light — the scattered photons from overcast skies — reasonably well. But a Fresnel lens can only focus *direct beam* sunlight. Diffuse light comes from all directions and can't be concentrated. This makes CPV a technology for the **"sun belt"** — deserts, arid highlands, places with DNI above 2,000 kWh/m²/year. Think Sahara, Arabian Peninsula, Australian outback, American Southwest, and parts of western China.

### The Efficiency Crown

No other commercial PV technology comes close to CPV's raw efficiency numbers. Production modules from companies like **Soitec** (before they exited the market) and **Suncore Photovoltaics** have demonstrated **38.9% module efficiency** at concentrator standard test conditions — far above the 22–24% of top silicon modules. The **system** efficiency, accounting for tracking losses, optical losses, and thermal derating, lands around **28–32%**.

But — and this is the fatal "but" — the **levelized cost of electricity (LCOE)** from CPV has struggled to beat conventional silicon. Silicon module prices have collapsed so relentlessly (from ~$4/W in 2008 to under $0.10/W for utility-scale modules today) that CPV's efficiency advantage can't overcome silicon's sheer manufacturing scale. In 2012, there was about 350 MW of CPV installed worldwide. By 2020, new installations had slowed to a trickle. Companies like **Amonix**, **SolFocus**, and **Soitec's CPV division** have shut down or pivoted.

CPV isn't dead — it's niche. It remains compelling where land is extremely expensive (efficiency means fewer acres), where temperatures are extreme (multi-junction cells handle heat better than silicon), or in **hybrid CPV-thermal systems** that capture the waste heat for industrial processes or desalination. And the technology lives on in a crucial descendant: **micro-CPV**, where tiny concentrator optics are integrated directly onto chips, potentially enabling high-efficiency modules no thicker than conventional panels.

## The Grand Dream: Space-Based Solar Power

Let's return to orbit. The vision of **space-based solar power (SBSP)** goes like this: park a gigantic solar array in geostationary orbit, convert sunlight to electricity, convert electricity to microwaves (or lasers), beam them down to a **rectifying antenna ("rectenna")** on Earth's surface, and convert back to electricity. A 24/7, weather-independent clean power source feeding the grid.

The engineering challenges are, frankly, biblical in scale.

### Challenge 1: Size

To deliver **1 GW** of power to the grid (about the output of one nuclear reactor), you need to collect roughly 3–4 GW of sunlight in orbit (accounting for conversion and transmission losses). At 30% cell efficiency, that's about **10 million square meters** of solar array — a square 3.2 km on a side. The International Space Station, the largest structure humans have ever built in space, spans about 2,500 m². An SBSP satellite would be **4,000 times larger**.

### Challenge 2: Wireless Power Transmission

Beaming power 36,000 km through the atmosphere isn't science fiction — it's physics. **Microwave power transmission** at 2.45 GHz or 5.8 GHz can pass through clouds, rain, and atmosphere with about **80–85% efficiency** for the atmospheric transit itself. But the total chain — DC to microwave to propagation to rectenna back to DC — currently manages about **40–50% end-to-end efficiency** in laboratory demonstrations.

In June 2023, **Caltech's SSPD-1 (Space Solar Power Demonstrator)** made history by wirelessly transmitting power in space using its **MAPLE** array — lightweight microwave transmitters built on flexible substrates with custom CMOS integrated circuits. The team even detected a signal on the roof of their building on campus in Pasadena as the satellite passed overhead. It was a detection, not useful power — but it proved the concept works with hardware light enough to actually launch.

### Challenge 3: Cost

Even with Starship economics, the numbers are daunting. A 2024 NASA study estimated that a first-generation SBSP system would cost **$400 billion or more** — roughly the combined GDP of Denmark and Finland. A 2025 paper in *Joule* was more optimistic, calculating that a fully mature system using 10 GHz microwave transmission could, after a decade of technology development, deliver electricity at **9.4 ¢/kWh** — competitive with other clean energy sources, though still above the cheapest terrestrial solar at 2–3 ¢/kWh.

The killer variable is launch cost. At $3,000/kg (current Falcon 9 pricing), launching the 10,000+ tonnes of hardware for a 1 GW satellite would cost **$30 billion in launch fees alone** — before you've built a single solar cell. At $100/kg (Starship aspirational), that drops to $1 billion. At $10/kg? Now you're talking about $100 million to launch a gigawatt to orbit. The dream's economic viability is essentially a bet on launch cost curves.

### Who's Actually Doing This?

Japan is the furthest along. **JAXA's OHISAMA project** is scheduled to demonstrate wireless solar power transmission from a 180 kg satellite in low Earth orbit — with the satellite slated for launch in **2026**. The European Space Agency's **SOLARIS** program is conducting feasibility studies. China has announced plans for a **megawatt-class orbital test by 2030** and has built a ground-based test facility at **Bishan, Chongqing** for microwave power transmission experiments.

In the private sector, **Virtus Solis** is designing modular orbital solar power stations sized for Starship launches. The UK's **Space Energy Initiative** has proposed a constellation of satellites delivering 2 GW. And Caltech continues developing lightweight, foldable solar array and transmitter technology.

## The Surprising Convergence

Here's what makes this story interesting: space solar and concentrator PV, seemingly different technologies, are converging on the same physics. Both use **multi-junction III-V cells**. Both obsess over **watts per kilogram** (for launch) or **watts per dollar of cell** (for CPV). Both need precision **beam steering** — tracking the sun for CPV, pointing microwaves for SBSP. And both compete against the relentless cost decline of conventional silicon.

The most likely near-term winner isn't an either/or — it's a hybrid. Imagine perovskite-silicon tandem cells (Day 22) manufactured at silicon-like costs but with 35%+ efficiency, mounted on CPV-style micro-concentrators, launched on Starship-class rockets. Each technology feeds the others.

And there's one more application where space solar is already here, right now, and utterly dominant: **powering every satellite, space station, rover, and probe humanity has ever sent beyond Earth**. From the ISS to the Mars rovers to the Juno probe orbiting Jupiter (with the largest solar arrays ever sent to the outer solar system, generating 500 W from 43 m² at Jupiter's feeble sunlight — only 4% as intense as at Earth), space-grade solar cells are the unquestioned power source of space exploration. We've been doing space solar power for 65 years. We just haven't beamed it home yet.

## Key Takeaways

- **Space gets 5–10× more energy** per unit area than ground-based solar due to no atmosphere, no weather, and near-continuous sunlight
- **III-V multi-junction cells** dominate space applications: 30–32% efficiency, radiation-hardened, extremely lightweight (350–450 W/kg)
- **Concentrator PV** uses cheap optics to focus 500–1000× sunlight onto tiny, expensive, ultra-efficient cells — achieving 39% module efficiency but struggling on cost vs. commodity silicon
- **Space-based solar power** could deliver 24/7 clean energy via microwave beaming, but requires solving massive scale, cost, and launch challenges
- **Caltech's SSPD-1** (2023) and **Japan's OHISAMA** (2026) represent the first real hardware demonstrations of wireless power from space
- **Launch cost is the key variable**: at $10/kg to orbit, SBSP becomes economically plausible

---

*Tomorrow: Day 27 takes us into the labs where the future is being invented — from quantum dot cells to organic photovoltaics to radical ideas that might make everything we've learned obsolete. What's in the lab today, and what might be on your roof in 2035?*

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-26.toml}}
