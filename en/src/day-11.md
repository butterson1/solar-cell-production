# Day 11: Multi-Junction & Tandem Cells — Stacking the Deck Against Thermodynamics

*Yesterday, we explored the world of thin films — solar cells that skip the wafer entirely and deposit semiconductors in layers measured in micrometers. Today, we go in the opposite direction conceptually: instead of simplifying, we stack. We layer multiple solar cells on top of each other, each one tuned to absorb a different slice of the solar spectrum, and in doing so we shatter efficiency ceilings that have constrained single-junction devices since the 1960s. This is the story of multi-junction and tandem cells — arguably the most elegant hack in all of photovoltaics, and the technology that may define the next decade of solar.*

## The Problem with Being Picky

To understand why stacking matters, you need to revisit a frustration we've been dancing around since Day 1. A single-junction silicon solar cell — no matter how perfectly made — can only convert about 29.4% of sunlight into electricity. That's the Shockley-Queisser limit for silicon's 1.12 eV bandgap, and it's not an engineering failure. It's physics.

Here's why. Sunlight isn't monochromatic. It's a chaotic spray of photons ranging from ultraviolet (around 3.5 eV) down through visible light and into the infrared (below 0.5 eV). A silicon cell with its 1.12 eV bandgap handles this spectrum with all the grace of a toll booth that only accepts $1 bills. Photons with less than 1.12 eV of energy? They sail right through the silicon — useless, unabsorbed. That's about 19% of the sun's energy just gone. Photons with *more* than 1.12 eV? They get absorbed, but their excess energy above the bandgap converts instantly to heat through a process called thermalization. A 3.0 eV ultraviolet photon hits silicon and generates one electron-hole pair worth 1.12 eV, while 1.88 eV — nearly two-thirds of that photon's energy — becomes waste heat.

Put together, sub-bandgap transmission and above-bandgap thermalization account for roughly 55% of the incoming solar energy. That's not a flaw in silicon specifically; *any* single-bandgap material faces this tradeoff. Choose a wide bandgap and you absorb fewer photons. Choose a narrow bandgap and you thermalize more of each photon you do absorb. The single-junction limit peaks at about 33.7% for an "ideal" bandgap around 1.34 eV.

The multi-junction idea is disarmingly simple: what if you stopped trying to find one perfect bandgap and instead used several?

## The Layer Cake: How Multi-Junction Cells Work

Picture a stack of solar cells, each made from a different semiconductor material, arranged from top to bottom in order of decreasing bandgap. The top cell might have a bandgap of 1.9 eV. It eagerly absorbs high-energy blue and ultraviolet photons, converting them to electricity with minimal thermalization because 1.9 eV is close to their actual energy. The red and infrared photons it can't absorb pass right through — but instead of being lost, they fall into the second cell below, which has a bandgap of, say, 1.4 eV. This middle cell grabs the photons in its range, and everything else passes down to a bottom cell with a bandgap around 1.0 eV, which mops up the near-infrared.

Each layer acts as a spectral filter for the layer below. The result is a device that samples the solar spectrum at multiple points instead of one, dramatically reducing both transmission and thermalization losses. A theoretical three-junction cell can reach about 49% efficiency. Go to four junctions and the limit pushes past 53%. At infinite junctions (a mathematical thought experiment), you'd approach 68% under unconcentrated sunlight — or 86% under maximum concentration.

The catch? Building these layer cakes is extraordinarily hard.

## III-V Semiconductors: The Aristocrats of Photovoltaics

The materials that make multi-junction cells possible come from Groups III and V of the periodic table: gallium, indium, aluminum (Group III) combined with arsenic, phosphorus, nitrogen, antimony (Group V). These III-V compound semiconductors offer something silicon cannot: tunable bandgaps. By adjusting the ratio of elements in an alloy — say, gallium indium phosphide (GaInP) — you can dial the bandgap to almost any value between 0.7 eV and 2.3 eV. It's like having an entire keyboard of notes instead of a single tuning fork.

The workhorse commercial multi-junction cell has three layers: gallium indium phosphide (GaInP) on top at 1.8-1.9 eV, gallium indium arsenide (GaInAs) in the middle at 1.4 eV, and germanium (Ge) on the bottom at 0.67 eV. This triple-junction design has powered nearly every high-value satellite launched since the early 2000s. Companies like Spectrolab (a Boeing subsidiary) and SolAero Technologies (now part of Rocket Lab) have shipped millions of these cells into orbit, where their roughly 30% efficiency under space conditions — AM0 spectrum, no atmosphere — justifies their eye-watering cost.

And about that cost: a III-V triple-junction cell runs approximately $50-100 per watt. Compare that to a standard silicon cell at roughly $0.15-0.25 per watt. The III-V cell is 200-400 times more expensive. Why? The manufacturing process — metalorganic chemical vapor deposition, or MOCVD — grows the crystal one atomic layer at a time inside a reactor chamber at 600-700°C, using toxic organometallic precursors like trimethylgallium and arsine gas. Growth rates crawl at about 1-2 micrometers per hour. The germanium substrates alone cost around $100 for a 100 mm wafer. This is boutique fabrication, not mass production.

## The Six-Junction Record Holder

In 2020, researchers at the National Renewable Energy Laboratory (NREL) in Golden, Colorado, demonstrated the most efficient solar cell ever measured: a six-junction device that hit 47.1% efficiency under 143 suns of concentration. Each junction was a precisely tuned III-V alloy, with bandgaps stepping from 2.15 eV at the top down to 0.69 eV at the bottom, like a staircase descending through the solar spectrum.

What made this device remarkable wasn't just the number of junctions but the engineering trick used to build it. Three of the layers were lattice-matched to the germanium substrate — meaning their crystal lattices had nearly identical atomic spacings, so they could be grown without defects. The other three were intentionally lattice-*mis*matched, using a technique called inverted metamorphic multijunction (IMM). The cell was grown upside-down, then peeled off its substrate, flipped, and bonded to a handle. The mismatched layers use graded buffer layers to slowly transition between lattice constants, keeping defect densities below 10⁶ per square centimeter — low enough that they don't destroy performance.

At 47.1%, this cell converts nearly half of all incoming concentrated light into electricity. For context, a gasoline engine in your car converts about 25-35% of fuel energy into motion. The best natural gas power plants hit about 60%. A six-junction solar cell under concentration is competitive with the most efficient thermal machines humanity has ever built — and it has no moving parts, no combustion, no emissions, no noise.

## Enter the Tandem: Perovskite on Silicon

Here's the surprising twist in this story. The most commercially important multi-junction cell isn't going to be an exotic III-V stack costing $100/W. It's going to be a two-junction tandem that puts a perovskite layer on top of a conventional silicon cell — and it may cost barely more than the silicon cell alone.

Perovskites — the crystalline materials we'll explore in depth on Day 21 — have a remarkable property: their bandgap is tunable across a wide range (1.2 to 2.3 eV) simply by changing the chemical composition of the precursor solution. A perovskite with a bandgap around 1.68 eV turns out to be nearly perfect as a top cell for silicon (1.12 eV) in a two-junction tandem. The perovskite captures the blue and green photons, generates current with low thermalization, and passes red and infrared light to the silicon bottom cell. Together, they cover the spectrum far more efficiently than either could alone.

The theoretical efficiency limit for a perovskite-silicon tandem is around 43% — well above the 29.4% limit for silicon alone. In practice, the records have been climbing at a breathtaking pace. In April 2025, LONGi — the world's largest solar manufacturer — certified a perovskite-silicon tandem cell at 34.85% efficiency, setting the current world record. JinkoSolar followed at 34.76% in late 2025. These numbers already demolish the best single-junction silicon cell ever made (26.81%, by LONGi in 2024).

What makes this genuinely revolutionary is the potential cost. Unlike III-V cells that require expensive MOCVD growth on germanium substrates, perovskite layers can be deposited from solution — spin-coated, slot-die coated, or even inkjet-printed onto the silicon cell's surface. The raw materials (lead, iodine, methylammonium, formamidinium) cost practically nothing. The processing temperatures are low, around 100-150°C, compared to 1,400°C for the silicon cell underneath. In principle, you could retrofit an existing silicon cell production line with a perovskite deposition step and produce tandem cells for perhaps 10-20% more than the cost of the silicon cell alone.

## The Current-Matching Problem

There's a fundamental engineering constraint that governs all monolithic (two-terminal) tandem cells, and it's worth understanding because it explains many of the design decisions in this field.

In a monolithic tandem, the two sub-cells are connected in series — like batteries stacked end-to-end. The voltage adds (good), but the current must be identical through both cells (tricky). If the top cell generates 20 mA/cm² and the bottom cell generates 18 mA/cm², the entire device is limited to 18 mA/cm². The extra 2 mA/cm² the top cell could produce is simply wasted. This current-matching requirement means you have to carefully engineer the thickness and bandgap of the top cell so that it absorbs exactly the right fraction of photons to produce the same current as the bottom cell.

This creates a real-world vulnerability. The solar spectrum changes throughout the day — more blue at noon, more red at sunrise and sunset. Clouds scatter blue light more than red. In a single-junction cell, these spectral shifts barely matter. In a tandem cell, they can push the current match out of alignment and reduce instantaneous efficiency by a few percent. Researchers have modeled annual energy yield and found that well-designed tandems still handily beat single-junction cells in every climate, but the "headline efficiency" measured under standard test conditions overstates the field advantage slightly.

One solution is to go four-terminal instead of two-terminal: wire the top and bottom cells independently, each with their own maximum-power-point tracker. This eliminates current matching entirely but adds wiring complexity and cost. The industry is heavily betting on the two-terminal monolithic approach for simplicity, while using the four-terminal architecture primarily in research settings.

## The Commercialization Race

As of early 2026, exactly one company has shipped commercial perovskite-silicon tandem modules: Oxford PV, a UK-founded startup manufacturing in Brandenburg an der Havel, Germany. In September 2024, they delivered their first batch — about 100 kW — to a utility-scale customer in the United States. Their commercial modules achieve 24.5% module efficiency (remember, module efficiency is always lower than cell efficiency due to spacing, wiring, and encapsulation losses), with a certified record module at 26.9%.

Oxford PV plans to scale to GW-level production by 2027, but they're far from alone. LONGi, JinkoSolar, and Canadian Solar are all developing tandem production lines. The Chinese manufacturers have an enormous advantage: they already operate hundreds of gigawatts of silicon cell capacity. Adding a perovskite top cell is an *incremental* upgrade to their existing lines, not a ground-up factory build.

The key unsolved challenge is durability. Silicon modules carry 25-30 year warranties and have demonstrated 0.3-0.5% degradation per year in the field. Perovskites, historically, degrade much faster — they're sensitive to moisture, oxygen, UV light, and heat. Oxford PV has publicly targeted a 20-year module lifetime by 2028, but achieving the 25-year warranties the market expects for utility-scale solar remains an open question. Accelerated aging tests suggest modern encapsulation techniques (edge seals, barrier films, butyl rubber) can dramatically extend perovskite lifetimes, but decades of real-world field data simply don't exist yet.

## Beyond Two: The Triple-Junction Future

If two junctions are better than one, what about three? Perovskite-perovskite-silicon triple-junction cells are already being developed in labs. The concept adds a wide-bandgap perovskite (~2.0 eV) on top of a mid-bandgap perovskite (~1.5 eV), on top of silicon (~1.12 eV). The theoretical limit pushes to about 51% — halfway to converting every photon perfectly.

In practice, triple-junction tandem cells are still in the low-20s efficiency range, mainly because the wide-bandgap perovskite formulations suffer from excessive defect densities and voltage losses. But the pace of perovskite research is ferocious — more papers are published on perovskite solar cells than on any other photovoltaic technology — and the gap between lab records and theoretical limits is closing faster than anyone predicted.

## The Counterintuitive Truth

Here's the fact that surprises most people: the most efficient solar cells in history — those 47.1% six-junction III-V monsters — are essentially irrelevant to the future of solar energy. They're magnificent scientific achievements, but at $50-100/W they'll remain confined to spacecraft and military drones. The technology that will actually change the world is the comparatively modest perovskite-silicon tandem, operating at 30-35% efficiency but manufactured at near-silicon costs.

This is the central lesson of solar economics: efficiency isn't everything. What matters is *cost per kilowatt-hour of electricity delivered over 25+ years*. A 35% tandem cell that costs $0.30/W is radically more valuable than a 47% cell that costs $80/W. The perovskite-silicon tandem is set to increase the energy output of a standard rooftop installation by 20-30% with minimal additional cost — and that's the kind of improvement that reshapes energy markets.

## What's Coming Tomorrow

We've now covered the full menagerie of solar cell types — silicon, thin-film, multi-junction, and tandem. But how good can they actually get? Is there an ultimate ceiling? Tomorrow, we dive into the Shockley-Queisser limit — the most important equation in photovoltaics — and the ingenious tricks researchers are using to blow past it: hot carriers, multiple exciton generation, photon upconversion, and more. We'll learn why the theoretical maximum efficiency of a solar cell is either 33%, 46%, 68%, or 86%, depending on how many rules you're willing to bend.

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-11.toml}}
