---
title: Shahed Navigation Case Study
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Operational GNSS Employment, GNSS Constellations]
section: 10
tags:
  - Shahed
  - Geran-2
  - Iran
  - BeiDou
  - CRPA
  - drone-warfare
---

# Shahed-136 / Geran-2 — Navigation Case Study

> [!abstract] Quick Summary
> Analyses the navigation architecture of the Shahed-136 loitering munition as a case study in layered GNSS design — combining GLONASS, INS, and terrain-matching to achieve resilience against GPS jamming. Demonstrates how a low-cost threat system can defeat GPS-centric countermeasures through layered navigation.

## Layered Navigation Architecture

```
GNSS (primary)
  → INS (backup)
    → Anti-jam antenna (Kometa-M / Chinese CRPA)
      → RTK cellular (4G/3G centimetre accuracy)
        → BeiDou SMC (in-flight retargeting)
```

## GNSS Evolution

> [!tip] Hot Tip
> The Shahed uses GLONASS, not GPS — this means US GPS jammers have no effect on its navigation. Counter-drone planning must account for which GNSS constellation the threat uses. Assuming GPS denial protects you from all GNSS-guided threats is a dangerous assumption.

1. **Initial**: civilian GPS + GLONASS
2. **Improved**: added [[BeiDou B3A and SMC|BeiDou]] (triple-constellation)
3. **Current**: Iranian variants transitioned to **BeiDou B3A**

## Operational Record

| Theatre | Event |
| --- | --- |
| Ukraine | 4,652 drones neutralised May–Jul 2025 via EW + kinetic |
| Iran–Israel Jun 2025 ("Twelve-Day War") | [[BeiDou B3A and SMC|B3A]] rejected Israeli spoofing; **~98% positioning reliability** under heavy EW vs 70%+ GPS failure |
| RAF Akrotiri Mar 2026 | Strike debris confirmed Russian [[CRPA Anti-Jam Antennas|Kometa-M]] CRPA — confirming Russia–Iran technology transfer |

## Iranian BeiDou Timeline

| Period | Status |
| --- | --- |
| Pre-2021 | GPS-dependent |
| ~2021 | BeiDou incorporation |
| Jun 2025 | Full BeiDou-3 activation after GPS jamming exposure |
| 2025–26 | B3A integrated across Shahed/cruise missiles/ballistic weapons |

## Closed-Loop Kill Chain

> Chinese ISR detects target → [[BeiDou B3A and SMC|BeiDou SMC]] transmits coordinates → Iranian weapon adjusts route automatically

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Shahed technical specifications are assessed from captured munitions, open-source analysis, and Ukrainian battlefield reporting — specific parameters may have changed in later variants.
>
> **Limitations:** Terrain-matching (TERCOM-like) navigation requires pre-loaded terrain data — effective in mapped terrain, less so in featureless environments (open ocean, desert).
>
> **Assumptions:** Assumes the Shahed navigation architecture described reflects current production variants — Iran has iterated rapidly on Shahed design.

**Related:** [[Operational GNSS Employment]] · [[CRPA Anti-Jam Antennas]] · [[BeiDou B3A and SMC]] · [[Kill Chain Comparison]]
