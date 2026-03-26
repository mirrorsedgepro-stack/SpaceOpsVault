---
title: RF Spectrum Reference
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [Introduction to Space]
section: 11
tags:
  - RF
  - spectrum
  - frequency-bands
---

# RF Spectrum Reference

> [!abstract] Quick Summary
> Provides a reference for the RF spectrum bands used by satellite and military communications systems, covering the propagation tradeoffs that determine which band is chosen for each mission. Understanding these tradeoffs is foundational to assessing SATCOM vulnerability and planning resilient communications architectures.

## Band Summary

| Band | Frequency | Weather | Bandwidth | Military Uses |
| --- | --- | --- | --- | --- |
| **UHF** | 300 MHz–3 GHz | Excellent | Very limited | NB SATCOM ([[SATCOM Architecture|MUOS]], [[ADF SATCOM Systems|IS-22]]), GNSS, tactical voice |
| **L-Band** | 1–2 GHz | Excellent | Low | All [[GNSS Constellations|GNSS]] signals, satellite phone |
| **S-Band** | 2–4 GHz | Very good | Moderate | TT&C, [[Space Fence]], LRDR, weather radar |
| **C-Band** | 4–8 GHz | Very good | 500 MHz | Legacy SATCOM, diplomatic comms |
| **X-Band** | 8–12 GHz | Good | 500 MHz | [[SATCOM Architecture|WGS]], [[ADF SATCOM Systems|Optus C1]], SAR, fire control radar |
| **Ku-Band** | 12–18 GHz | Moderate | Wide | Commercial SATCOM, UAV data links, Starlink |
| **Ka-Band** | 26.5–40 GHz | Poor | 3.5 GHz | [[SATCOM Architecture|WGS Ka]], Starlink, HTS military SATCOM |
| **EHF** | 30–300 GHz | Poor (by design) | Wide | [[SATCOM Architecture|AEHF]] (most jam-resistant; nuclear survivable) |

## Fundamental RF Tradeoff

> [!tip] Hot Tip
> Frequency determines capability and vulnerability in equal measure — Ka-band gives you gigabit data rates but rain fade can cut a link; UHF penetrates foliage but gives you kilobit speeds. When assessing a comms architecture, always ask what happens to each link in rain, jamming, and antenna-pointing degradation simultaneously.

> ↑ Frequency = ↑ bandwidth, ↓ antenna size, ↑ beam narrowing, ↑ weather sensitivity, ↑ atmospheric absorption

Higher frequency gives more data capacity but is more susceptible to rain fade and requires more precise pointing.

## Key Jamming Vulnerability by System

| System | Anti-Jam | Notes |
| --- | --- | --- |
| [[SATCOM Architecture|WGS]] | **NONE** | Most significant vulnerability |
| [[SATCOM Architecture|AEHF]] | Extremely difficult | Freq-hopping + phased arrays + nulling |
| [[SATCOM Architecture|MUOS]] | Moderate | Spread spectrum vs legacy UHF |
| [[GPS]] L1 C/A | **Critically vulnerable** | 1-watt jammer effective over several km |

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Spectrum access is nationally regulated — using frequencies outside allocated bands requires coordination and may conflict with civilian users.
>
> **Limitations:** Higher frequencies (Ka, EHF) are vulnerable to atmospheric attenuation (rain fade) — plan for degraded throughput in tropical and monsoon environments relevant to the Indo-Pacific.
>
> **Assumptions:** Assumes peacetime frequency coordination frameworks remain intact — in conflict, spectrum deconfliction with civilian users may break down.

**Related:** [[Satellite Jamming Techniques]] · [[Electronic Warfare Fundamentals]] · [[SATCOM Architecture]]
