---
title: GPS
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [Military Satellite Capabilities Overview, GNSS Constellations]
section: 3
tags:
  - GPS
  - PNT
  - M-Code
  - GNSS
  - navigation
---

# GPS (Global Positioning System)

> [!abstract] Quick Summary
> Details the GPS signal structure, military M-Code, and the key vulnerabilities that make GPS the most actively contested space-based capability in current conflicts. Understanding GPS limitations is foundational to planning resilient operations in a degraded PNT environment.

## Architecture

- **31+ satellites** at ~20,200 km ([[Orbital Mechanics|MEO]]), 55° inclination
- Operated by [[USSF Organisation|USSF]]

## Signals

| Signal | Type | Accuracy | Notes |
| --- | --- | --- | --- |
| **L1 C/A** | Open civilian | ~3–5 m | Extremely weak (~−160 dBW) |
| **L2C** | Civilian modernised | Improved | Dual-frequency ionospheric correction |
| **L5** | Aviation safety | Sub-metre | Aviation integrity |
| **M-Code** | Encrypted military | Enhanced | Anti-jam, anti-spoof |
| **P(Y)** | Legacy military | ~1 m | Being superseded by M-Code |

## Vulnerabilities

- GPS signals are the **weakest RF signal** in the military architecture (~−160 dBW at Earth surface)
- A **1-watt jammer** can deny GPS over several km
- Trivially spoofed on civilian signals
- Russia dramatically expanded GPS jamming since 2024 across Baltic, Middle East, Black Sea, Ukraine

> [!tip] Hot Tip
> GPS jamming is the lowest-cost, highest-return counterspace option — a $500 jammer can deny GPS to a ~50km radius. Never plan an operation that is solely dependent on GPS for navigation or timing. Always identify your backup PNT source (INS, DME, celestial, terrain-referenced) before the operation begins.

## GPS IIIF

- Deploying with **M-Code** regional military protection
- Enhanced anti-jam and anti-spoof for military users

> [!tip] Hot Tip
> M-Code provides dramatically better anti-jam performance than the standard P(Y) code, but it requires specific military-grade receivers — verify your platform's receiver type before assuming M-Code capability. Many legacy ADF platforms still carry P(Y)-only receivers and will not benefit from M-Code improvements.

## The GPS Paradox

> Simultaneously the **most capable** (M-Code) and **most targeted** (due to deep dependency) GNSS system.

See also [[GNSS Constellations]] for comparison with [[BeiDou B3A and SMC|BeiDou]], GLONASS, and Galileo.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** M-Code access requires US-approved military receivers — not all ADF platforms are equipped. Selective Availability Anti-Spoofing Module (SAASM) or M-Code receiver procurement is subject to US export controls.
>
> **Limitations:** GPS is vulnerable to jamming (signal is ~20dB below the noise floor at Earth's surface), spoofing, and intentional denial. No GPS signal penetrates buildings reliably — indoor positioning and timing are always degraded. Hypersonic and high-dynamic manoeuvring environments stress receiver tracking loops.
>
> **Assumptions:** Assumes the 24+ satellite constellation remains healthy — a kinetic ASAT campaign targeting GPS MEO satellites would constitute a strategic attack with global consequences. Assumes adversaries are not conducting active spoofing, which is significantly harder to detect than jamming.

**Related:** [[GNSS Constellations]] · [[Operational GNSS Employment]] · [[EW Against Data Links]] · [[Tomahawk Guidance]]
