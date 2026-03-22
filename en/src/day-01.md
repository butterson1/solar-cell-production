# Day 1: What Is a Solar Cell, Really? Photons In, Electrons Out

---

## The Most Important Invention You Take for Granted

Somewhere on Earth right now, a photon that left the Sun's surface 8 minutes and 20 seconds ago is slamming into a thin slab of silicon and knocking an electron loose. That electron is being swept into a wire, joining trillions of others in a river of current that's charging a phone, running a factory, or keeping someone's lights on. No combustion. No turbine. No moving parts at all. Just light in, electricity out.

This is the photovoltaic effect, and it is — without exaggeration — one of the most elegant energy conversions in all of physics. A solar cell doesn't *generate* energy the way a coal plant does. It *converts* it, directly, from electromagnetic radiation to electrical current in a single quantum-mechanical step. No intermediate heat. No steam. No spinning metal. The simplicity is almost offensive.

And yet, if you asked most people how a solar cell actually works, you'd get vague gestures toward "sunlight hits the panel" and maybe something about silicon. Today we're going to crack this thing open — not at the hand-wavy level, but at the level where you actually *understand* what's happening inside that dark blue slab on your neighbor's roof.

---

## Photons: Tiny Bullets of Energy

Let's start with sunlight itself. What we call "sunlight" is a flood of photons — discrete packets of electromagnetic energy — spanning a range of wavelengths. The Sun's surface burns at about 5,778 Kelvin (roughly 5,500°C), and like any hot object, it radiates energy according to its temperature. The peak of its emission spectrum falls right around 500 nanometers — blue-green visible light.

Here's the critical thing about photons: each one carries a specific amount of energy determined by its wavelength. Short wavelength (blue, ultraviolet) = more energy. Long wavelength (red, infrared) = less. The relationship is beautifully simple: E = hf, where h is Planck's constant (6.626 × 10⁻³⁴ joule-seconds) and f is the frequency. A photon of red light at 700nm carries about 1.77 electron-volts (eV) of energy. A photon of blue light at 450nm carries about 2.76 eV. An infrared photon at 1100nm? Only 1.13 eV.

Why do these specific numbers matter? Because silicon — the material in about 95% of all solar cells ever made — has a bandgap of 1.12 eV. That number is the entire reason the solar industry exists.

---

## The Bandgap: Nature's Bouncer

To understand the bandgap, you need to think about what electrons do inside a crystal.

In a silicon crystal, atoms are locked in a diamond-cubic lattice — each silicon atom bonded to four neighbors, sharing electrons in neat covalent bonds. The electrons in these bonds are stuck. They're in what physicists call the *valence band*: the energy range where electrons are bound to atoms and can't move freely. An electron sitting in the valence band is doing its job holding the crystal together, but it's useless for conducting electricity.

Above the valence band is the *conduction band* — an energy range where electrons are free to roam through the crystal, carrying current. Between these two bands is the bandgap: a forbidden zone where no electron states exist. In silicon, this gap is 1.12 eV wide.

Think of it like a nightclub with a strict cover charge. If a photon shows up carrying at least 1.12 eV, it can "pay" to promote an electron from the valence band to the conduction band. The electron is now free to conduct. If the photon carries less than 1.12 eV? Bounced. It passes through the silicon or gets absorbed as useless heat.

This is why silicon is transparent to infrared light beyond about 1100nm — those photons simply don't have enough energy to clear the bandgap. They sail right through as if the silicon weren't there.

But here's the counterintuitive part: photons with *MORE* than 1.12 eV also waste energy. A blue photon carrying 2.76 eV will promote an electron across the 1.12 eV bandgap, but the excess 1.64 eV doesn't generate more electricity. It's lost as heat — the electron quickly "thermalizes" down to the bottom of the conduction band, shedding its extra energy as lattice vibrations (phonons). This is called *thermalization loss*, and it's the single biggest reason solar cells can't convert 100% of sunlight into electricity.

Right there, before we've even built anything, physics has already capped our efficiency. Too-red photons are wasted. Too-blue photons partially wasted. Only a narrow band around the bandgap energy is used efficiently. This fundamental limit — the Shockley-Queisser limit — caps a single-junction silicon cell at about 33.7% efficiency under standard sunlight. We'll dig deep into this on Day 12, but for now, just know that every solar cell ever made is fighting this constraint.

---

## The Hole Story (Literally)

When a photon kicks an electron into the conduction band, it leaves behind a *hole* — a vacancy in the valence band where an electron used to be. This hole behaves like a positive charge carrier. Neighboring electrons can hop into the hole, which effectively moves the hole in the opposite direction. So now you have two charge carriers: a free electron (negative) and a hole (positive).

Together, they're called an *electron-hole pair*, and creating them is the easy part. The hard part is separating them before they recombine. Left to their own devices, the electron will fall back into the hole within microseconds, releasing its energy as heat or a photon (this is how LEDs work, actually — the reverse process). A solar cell that generates electron-hole pairs but can't separate them is just a fancy space heater.

So how do you separate them? You build a one-way valve for charges. And that valve is the p-n junction.

---

## The p-n Junction: A Built-In Electric Field

Pure silicon is a lousy conductor. It has very few free carriers at room temperature — about 1.5 × 10¹⁰ per cubic centimeter, compared to copper's ~8.5 × 10²² free electrons per cm³. That's twelve orders of magnitude less. To make it useful, we *dope* it — intentionally contaminate it with specific impurities.

Add a tiny amount of phosphorus (which has 5 outer electrons, vs. silicon's 4), and you get **n-type silicon**: each phosphorus atom donates one extra free electron. Typical doping levels are about 1 phosphorus atom per million silicon atoms, but that's enough to boost free electron density by a factor of roughly a million.

Add boron instead (3 outer electrons), and you get **p-type silicon**: each boron atom creates one hole. Same idea, opposite charge carrier.

Now here's where the magic happens. Take a wafer of p-type silicon and create a thin n-type layer on top (we'll cover how in Day 6). At the boundary — the p-n junction — something remarkable occurs spontaneously.

Free electrons from the n-side diffuse across into the p-side, where they fall into holes. Free holes from the p-side diffuse into the n-side, where they capture electrons. This diffusion strips away mobile carriers near the junction, leaving behind the fixed charged atoms: positive phosphorus ions on the n-side, negative boron ions on the p-side. This creates a thin zone — the *depletion region*, typically 0.1 to 1 micrometer wide — with a built-in electric field pointing from n to p.

This electric field is the solar cell's secret weapon. It's a permanent, maintenance-free charge separator. Any electron-hole pair generated in or near the depletion region gets ripped apart: the field pushes electrons toward the n-side and holes toward the p-side. No external power needed. No moving parts. Just the electrostatics of the junction itself.

The built-in voltage across this junction is about 0.6 to 0.7 volts for silicon — which is why a single silicon solar cell produces roughly 0.5 to 0.6 volts under load. Want 20 volts for your panel? Wire about 36 cells in series. That's exactly what manufacturers do.

---

## Putting It All Together: Photon to Circuit

Let's walk through the complete journey:

1. A photon (say, 2.0 eV, orange-ish light at 620nm) enters the cell through the top surface.

2. It penetrates into the silicon — how deep depends on its wavelength. Blue light is absorbed within the first 1-2 micrometers. Red light penetrates 10+ micrometers. Infrared can go 100+ micrometers before being absorbed.

3. The photon is absorbed by a silicon atom, transferring its energy to an electron and promoting it to the conduction band. A hole is left behind. The excess energy (2.0 - 1.12 = 0.88 eV) is lost as heat.

4. The electron and hole wander randomly through the crystal (diffusing). If they're within a *diffusion length* of the p-n junction (typically 100-300 micrometers in good silicon), they have a solid chance of reaching the depletion region before recombining.

5. The built-in electric field grabs them: electron to the n-side, hole to the p-side.

6. The electron exits through the top metal contact (those thin silver lines you see on solar cells), flows through the external circuit — powering whatever's connected — and returns through the bottom contact, where it recombines with a hole. Cycle complete.

The whole process takes roughly a microsecond from photon absorption to current flow. And it happens about 10²¹ times per second in a typical solar panel on a sunny day — that's a sextillion electron-hole pairs, every second, generating maybe 300-400 watts of power.

---

## Why This Is Harder Than It Sounds

The physics is elegant, but actually building a good solar cell means fighting losses at every stage:

**Optical losses:** About 30% of sunlight hitting bare silicon bounces right off — silicon is quite reflective (it's shiny, like metal). That's why real cells have anti-reflective coatings and textured surfaces (Day 7). Those dark blue or black cells you see? That color IS the anti-reflective coating doing its job.

**Recombination losses:** Every electron-hole pair that recombines before reaching the junction is wasted. Recombination happens at crystal defects, grain boundaries, and especially at surfaces. The entire history of solar cell improvement, from the first 6% efficient cell at Bell Labs in 1954 to today's 26.8% record for single-crystal silicon (set by LONGi in 2024), is largely a story of reducing recombination.

**Resistive losses:** Current flowing through silicon and through those thin metal contacts generates heat (I²R losses). Make the contacts too thin and resistance goes up. Make them too thick and they shade the cell, blocking photons. This is a genuine engineering tradeoff.

**Spectral mismatch:** As we discussed, photons below 1.12 eV are useless, and photons above 1.12 eV waste their excess energy. Together, these two effects alone throw away over 50% of incoming solar energy before any engineering imperfections even enter the picture.

A modern commercial silicon solar cell — the kind rolling off production lines at LONGi, JinkoSolar, or Trina Solar by the hundreds of millions — converts about 22-24% of incoming sunlight to electricity. The best lab cells push toward 27%. That might sound low, but remember: the theoretical max for single-junction silicon is 29.4% (the detailed-balance limit accounting for silicon's specific properties), and we're at 91% of that theoretical ceiling. There's not much room left.

---

## The Surprising Part

Here's something that catches people off guard: **solar cells work worse when they're hot.**

You'd think more sun = more heat = more energy, but the bandgap of silicon actually *shrinks* as temperature rises (from 1.12 eV at 25°C to about 1.08 eV at 75°C). This sounds like it should help — more photons can clear a lower bandgap — but the voltage drops faster than the current gains. The net effect: silicon solar cells lose about 0.3-0.5% of their power output for every degree Celsius above 25°C. On a scorching 45°C roof, that's a 6-10% performance hit.

This is why solar panels in cool, sunny climates (think: high-altitude deserts, or spring days with clear skies) outperform what you'd expect, and why panels on black rooftops in Phoenix underperform their ratings. It's also why some next-generation cell designs (heterojunction cells, or HJT) are prized for their lower temperature coefficients — but that's a story for Day 9.

---

## The Numbers That Matter

To ground this in real hardware: a standard silicon solar cell today is about 182mm × 182mm (the M10 format) or 210mm × 210mm (the M12/G12 format). It's roughly 150-180 micrometers thick — about twice the thickness of a human hair. It produces around 0.5 volts and 10-12 amps, giving roughly 5-6 watts per cell. A typical 72-cell residential panel produces 400-580 watts.

The global solar industry produced about 600 GW of solar panels in 2025 — enough to power roughly 100 million American homes if they all ran at once. That's a number that was considered delusional just a decade ago, when annual production was 50 GW.

And every single one of those watts starts the same way: a photon from an 8-minute-old beam of sunlight kicking a single electron across a 1.12 eV bandgap in a crystal of silicon. The rest is engineering.

---

## Tomorrow's Preview

Now that you understand what a solar cell *does*, the obvious question is: where does the silicon come from? The answer starts in the most mundane place imaginable — a pile of sand — and ends in one of the most energy-intensive industrial processes on Earth. Tomorrow, we trace silicon's journey from beach sand to semiconductor-grade material, and you'll learn why the phrase "made from sand" dramatically understates the difficulty.

*See you on Day 2.* ⚡

---

## 🧪 Test Your Understanding

{{#quiz quizzes/day-01.toml}}
