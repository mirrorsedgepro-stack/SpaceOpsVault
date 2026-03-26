---
title: Operational GNSS Employment
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [GNSS Constellations, GPS]
section: 10
tags:
  - GNSS
  - drone-warfare
  - navigation
  - arms-race
---

# Operational GNSS Employment

> [!abstract] Quick Summary
> Covers how GNSS is actually employed on the modern battlefield — the navigation arms race between jammers and anti-jam receivers, and lessons from drone warfare in Ukraine and the Middle East. Essential reading for understanding how GNSS denial shapes operational planning and what resilience measures are required.

## Navigation Arms Race (Drone Warfare)

The evolution of navigation in contested environments follows an escalatory ladder:

```
Civilian GPS (easily jammed)
  → INS backup (accuracy degrades over time)
    → Multi-constellation (harder to deny all simultaneously)
      → CRPA anti-jam (filters jamming sources)
        → RTK cellular (centimetre accuracy via 4G/3G)
          → BeiDou B3A (rejects spoofing)
            → BeiDou SMC (two-way in-flight retargeting)
```

Each step represents an adversary response to the previous countermeasure — a textbook measure/countermeasure cycle.

> [!tip] Hot Tip
> Ukraine has shown that GNSS-dependent drones can be defeated by local jamming — but also that operators quickly adapt (inertial backup, visual navigation, terrain following). Expect any adversary with basic EW capability to deploy GPS jammers in the first hours of conflict. Plan around it, not through it.

See:
- [[Shahed Navigation Case Study]] — detailed case study
- [[CRPA Anti-Jam Antennas]] — Kometa-M and Chinese alternatives
- [[BeiDou B3A and SMC]] — the current apex of the arms race

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Anti-jam GNSS receivers (CRPA, M-Code) require specific military-grade hardware — not all ADF platforms have them. Retrofitting is costly and time-consuming.
>
> **Limitations:** Even CRPA antennas can be overcome by sufficiently powerful or directional jamming. Inertial navigation degrades over time without GNSS correction — position error grows at ~1–3nm per hour for typical INS.
>
> **Assumptions:** Assumes training has prepared operators to navigate under GNSS denial — this is not universally true across the joint force.

**Related:** [[GNSS Constellations]] · [[GPS]] · [[EW Against Data Links]]
