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
    → Anti-jam antenna (12/16-element CRPA)
      → LTE/4G Modem (SIM card integration)
        → AI Terminal Guidance (structure recognition)
```

## Counter-EW: The CRPA Revolution (2025–2026)
To defeat Western/Ukrainian jamming, the Russian-made **Geran-2** (Shahed derivative) has undergone a rapid evolution:

- **16-Element CRPA**: Advanced **Controlled Reception Pattern Antenna** (internally mounted in fuselage center since late 2025) can create up to 15 "nulls" to ignore jammers.
- **Resilience**: 2026 reporting shows these units remain functional even when targeted by **over 100 coordinated jammers**.
- **LTE/4G Integration**: Use of commercial SIM cards (often from target-nation providers) allows the drone to transmit telemetry and receive mid-flight route updates via cellular networks, bypassing traditional RF jamming.
- **AI Terminal Guidance**: Late 2025 models integrated AI for target recognition, allowing the drone to home in on specific structures (e.g., power substations) even if GNSS is lost in the final phase of flight.

## Case Study: Geran-3 (Jet Variant)
- **Speed**: Mach 0.4 - 0.5 (500–600 km/h)
- **EW Impact**: High speed, combined with 16-element CRPA, reduces the "window of engagement" for ground-based EW.

> [!tip] Hot Tip
> The "hardened" Shahed/Geran is the baseline for modern loitering munitions. As of 2026, simple "bubble" jammers are ineffective. Kinetic interdiction or high-power microwave (HPM) are required to disrupt these platforms reliably.

## GNSS Evolution

1. **Initial**: civilian GPS + GLONASS
2. **Improved**: added [[BeiDou B3A and SMC|BeiDou]] (triple-constellation)
3. **Current**: Iranian variants transitioned to **BeiDou B3A** (essentially unjammable)

## Operational Record

| Theatre | Event |
| --- | --- |
| Ukraine | 4,652 drones neutralised May–Jul 2025 via EW + kinetic |
| Iran–Israel Jun 2025 ("Twelve-Day War") | [[BeiDou B3A and SMC|B3A]] rejected Israeli spoofing; **~98% positioning reliability** |
| Alabuga (Russia) | High-rate production of CRPA-equipped **Geran-2** using Chinese-made chipsets |

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
