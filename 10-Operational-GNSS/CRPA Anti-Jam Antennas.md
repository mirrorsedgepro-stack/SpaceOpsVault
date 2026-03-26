---
title: CRPA Anti-Jam Antennas
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Operational GNSS Employment, Electronic Warfare Fundamentals]
section: 10
tags:
  - CRPA
  - Kometa-M
  - anti-jam
  - Russia
  - China
---

# CRPA (Controlled Reception Pattern Antenna)

> [!abstract] Quick Summary
> Details Controlled Reception Pattern Antennas (CRPA) — the primary hardware solution for GPS anti-jam — covering how they work, Russian (Kometa-M) and Chinese equivalents, and the escalating technical contest between jammers and anti-jam receivers. Directly relevant to assessing platform vulnerability and force modernisation priorities.

## How CRPA Works

- Multi-element antenna array **digitally shaping reception** to reject interference while maintaining GNSS sensitivity
- **N-element CRPA rejects N−1 independent jamming sources**
  - 4-element → rejects 3
  - 16-element → rejects 15
- Defending against a 16-element CRPA requires **16+ spatially separated jammers** (extremely difficult)
- Interference rejection: **40–50 dB** (100–300× reduction in jamming effectiveness)

## Kometa-M (Russian CRPA)

- **Manufacturer**: VNIIR-Progress, Cheboksary, Russia
- **Constellations**: GLONASS/GPS/Galileo/SBAS (L1)

| Spec | Value |
| --- | --- |
| Variants | 4, 8, 12, 16-element |
| Weight (4-element) | ~370g |
| Dimensions | 152 × 152 × 15mm |
| Power | 12W |

### Proliferation Timeline

| Period | Variant | Platform |
| --- | --- | --- |
| 2022 | 4-element | Orlan-10 UAV |
| 2024 | 8-element | [[Shahed Navigation Case Study|Shahed]] |
| Apr 2025 | 12-element | UMPK glide bombs |
| 2025–26 | 16-element | Next-gen weapons |

## Chinese Alternative

- **TDXL-KGR1101**: ~$3,290 USD
- Widespread commercial availability makes sanctions countermeasures **ineffective**

> [!tip] Hot Tip
> CRPA technology is widely available — Russia, China, and even Iran have fielded anti-jam GPS receivers on their systems. Don't assume that GPS jamming will only affect friendly forces; adversaries have been investing in GNSS protection as long as we have.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** US CRPA design details are export-controlled — ADF access is via FMS and subject to ITAR. Some platforms cannot physically accommodate CRPA antennas due to form factor.
>
> **Limitations:** CRPA provides significant improvement but is not absolute — sufficiently powerful broadband jammers can still overcome CRPA null-steering.
>
> **Assumptions:** Assumes CRPA-equipped platforms are properly maintained and calibrated — field degradation of CRPA performance is a real but underacknowledged risk.

**Related:** [[Operational GNSS Employment]] · [[Shahed Navigation Case Study]] · [[Russia Counterspace Threat]] · [[GPS]]
