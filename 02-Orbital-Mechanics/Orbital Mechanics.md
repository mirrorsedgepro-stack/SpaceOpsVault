---
title: Orbital Mechanics
classification: UNCLASSIFIED // FOUO
difficulty: Foundational
prerequisites: []
section: 2
tags:
  - orbital-mechanics
  - LEO
  - MEO
  - GEO
  - HEO
  - cislunar
---

# Orbital Mechanics

> [!abstract] Quick Summary
> Covers the three primary orbital regimes (LEO, MEO, GEO), how orbital physics determines satellite coverage and vulnerability, and the emerging threat of rendezvous and proximity operations (RPO) as a tool of space coercion.

> [!info] Orbital Regime Stack — Low to High
> **🌍 LEO** · 160–2,000 km · ~90 min orbital period
> ↳ ISS (408 km) · SDA PWSA (~1,000 km) · Space Fence coverage
>
> *↑ Higher orbit = slower satellite · longer period ↑*
>
> **🛰️ MEO** · 2,000–35,786 km · 2–24 hrs
> ↳ GPS (20,200 km) · GLONASS (19,100 km) · Galileo (23,222 km)
>
> *↑*
>
> **🌐 GEO** · 35,786 km · 24 hrs — stationary relative to Earth
> ↳ WGS (5 × Pacific/Atlantic/Indian) · AEHF (6 sats) · MUOS (5 sats) · GSSAP (near-GEO)

## Orbital Regimes

| Regime            | Altitude                            | Period              | Key Occupants                                                                               |
| ----------------- | ----------------------------------- | ------------------- | ------------------------------------------------------------------------------------------- |
| **LEO**           | 160–2,000 km                        | ~90 min             | ISR, Starlink, ISS, debris                                                                  |
| **MEO**           | 2,000–35,786 km                     | 2–24 hrs            | [[GPS]], Galileo, GLONASS, [[BeiDou B3A and SMC\|BeiDou]]                                   |
| **GEO**           | ~35,786 km                          | 24 hrs (stationary) | [[SATCOM Architecture\|SATCOM]], [[Missile Warning and Tracking\|missile warning]], weather |
| **HEO** (Molniya) | Perigee ~500 km / Apogee ~40,000 km | ~12 hrs             | Russian comms, some missile warning                                                         |
| **Cislunar**      | >36,000 km to ~384,000 km           | Varies              | Emerging; Lagrange points of strategic interest                                             |

## Key Concepts

- **Inclination**: polar orbits ~90° give global coverage; sun-synchronous ~97° maintains consistent lighting for ISR
- **TLE (Two-Line Element)**: standard orbital data format shared via Space-Track.org — fundamental for coalition [[Space Domain Awareness|SDA]]
- **Conjunction assessment**: [[18th Space Defense Squadron]] issues warnings worldwide for dangerous close approaches
- **Delta-V**: velocity change required to manoeuvre; finite fuel budget makes manoeuvre decisions strategically significant

> [!tip] Hot Tip
> GEO satellites are geographically predictable — they sit at a fixed point in the sky and anyone with a compass, ephemeris data, and a directional antenna can point a jammer at them. When assessing SATCOM vulnerability, GEO links should be treated as the highest-risk segment for jamming and uplink interference.

## Rendezvous and Proximity Operations (RPO)

Deliberately manoeuvring close to another satellite — can be **cooperative** (servicing, inspection) or **hostile** (co-orbital weapon, signal interception).

> **Attribution challenge**: same satellite behaviours (approach, station-keeping) serve both purposes — the hardest problem in [[Space Domain Awareness|SDA]].

### Observed RPO Activity
- **Russia**: Cosmos 2576 synchronised orbit with USA 314 (2024); Cosmos 2558 co-planar with USA 326 since 2022; Cosmos 2581/2582 formation flying within 100m
- **China**: SJ-series satellites demonstrating advanced manoeuvring

See also [[Counterspace Threats Overview]] → Co-orbital / RPO category.

## Regime-Specific Notes

### LEO
- Most congested, highest debris concentration
- Objects pass overhead in ~10 min
- Most vulnerable to [[Counterspace Threats Overview|DA-ASAT]]

> [!tip] Hot Tip
> LEO constellations like Starlink are harder to jam than GEO because they are spread across hundreds of satellites and change position constantly — but they generate massive space traffic management challenges. In a conflict, debris from even a single DA-ASAT strike in LEO creates a cascading conjunction risk for the entire constellation.

### MEO
- Harsher radiation (Van Allen belts)
- [[GPS]] at ~20,200 km (55° inclination, 31+ satellites)
- Nuclear detonation here would create persistent radiation belts for years

### GEO
- Limited orbital slots regulated by ITU
- Objects persist indefinitely (no atmospheric drag)
- [[GSSAP]] satellites provide eyes-on inspection capability

### Cislunar
- Current [[Space Domain Awareness|SDA]] coverage minimal
- Both US and China investing
- Not yet an operational military domain

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Orbital mechanics are governed by physics — you cannot change an orbit instantly. Manoeuvre requires time and fuel, and a satellite's fuel budget is finite. Rapid manoeuvre to avoid a threat may exhaust a satellite's delta-V reserve and shorten its operational life.
>
> **Limitations:** LEO satellites only cover a point on Earth for minutes per pass — persistence over a target requires either a large constellation or cued tasking. A small constellation provides windows of coverage, not continuous surveillance.
>
> **Assumptions:** Assumes orbital data (TLEs) is current and accurate. Outdated TLEs degrade conjunction analysis, and adversaries capable of classified manoeuvre may not publish accurate ephemeris data — creating undetected conjunction risks.

---

## Knowledge Check

- [ ] Name the three orbital regimes and their altitude ranges
- [ ] Why are GEO satellites easier to jam than LEO satellites?
- [ ] What does RPO stand for, and why does it concern USSF?
- [ ] What is the approximate velocity of a LEO satellite?
- [ ] Why does a LEO satellite have limited dwell time over a target area?

> [!tip]- Answers *(click to reveal)*
> 1. **LEO** (160–2,000 km), **MEO** (2,000–35,786 km), **GEO** (35,786 km)
> 2. GEO satellites are stationary relative to Earth — their position is predictable and fixed, making it easy to aim a directional jammer at them. LEO satellites move rapidly across the sky, requiring a tracking jammer
> 3. **Rendezvous and Proximity Operations** — an adversary satellite manoeuvres close to a friendly satellite, potentially for intelligence collection, pre-positioning for attack, or physical interference
> 4. Approximately **7.8 km/s** (28,000 km/h)
> 5. At LEO altitudes, the satellite's high angular velocity means it passes over any fixed point in minutes — persistence requires a large constellation to ensure continuous coverage

**Related:** [[Introduction to Space]] · [[Space Domain Awareness]] · [[GSSAP]] · [[GPS]]
