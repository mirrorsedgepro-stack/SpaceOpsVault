---
title: MILNET
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [SATCOM Architecture]
section: 3
tags:
  - SATCOM
  - MILNET
  - SpaceX
  - proliferated
  - 2026-update
aliases:
  - USSF MILNET
---

# MILNET

> [!abstract] Quick Summary
> Introduces MILNET, the USSF/SpaceX dedicated 480-satellite military LEO communications constellation announced December 2025, designed to be survivable in a contested environment. This programme will reshape joint SATCOM architecture in the early 2030s and has direct implications for ADF access planning.

## Overview

MILNET is a dedicated military communications satellite constellation being developed jointly by the U.S. Space Force and SpaceX, announced December 2025. It represents a shift toward purpose-built, proliferated LEO military SATCOM separate from the commercial Starlink network.

## Key Parameters

| Parameter | Detail |
|---|---|
| Satellites | 480 (initial constellation) |
| Orbit | LEO (~550 km, similar to Starlink) |
| Operator | SpaceX (government-contracted) |
| First launch | Mid-2026 (projected) |
| Initial Operating Capability | Late 2027 (projected) |
| Full Operating Capability | TBD |

## Rationale

- Provides a **dedicated, hardened** military communications layer distinct from the commercial Starlink service
- Addresses concerns that commercial Starlink is subject to SpaceX's own usage policies (as demonstrated in Ukraine 2022–2023, where SpaceX restricted Starlink use near Crimea)
- Designed to be **resilient and survivable** in a contested environment — proliferated architecture reduces single-point-of-failure risk
- Complements the [[SDA Transport Layer (PWSA)]] rather than replacing it; PWSA handles missile tracking and BLOS Link 16 relay, MILNET focuses on broadband communications

> [!tip] Hot Tip
> MILNET's key advantage over WGS is proliferation — destroying a handful of GEO satellites can deny WGS, but neutralising 480 LEO satellites is a far more complex and costly adversary campaign. Watch this programme closely as it will reshape SATCOM architecture in the early 2030s and will likely determine whether ADF retains interoperable SATCOM access post-WGS.

## Relationship to Existing SATCOM

- Fills the gap between [[SATCOM Architecture|WGS]] (high-capacity GEO, vulnerable to jamming) and [[SATCOM Architecture|MUOS]] (narrowband, legacy)
- WGS has no anti-jam protection and is a known vulnerability; a proliferated LEO mesh is significantly harder to jam than a small number of GEO satellites
- Expected to carry [[Link 16]] and potentially higher-bandwidth waveforms

## Concerns and Open Questions

- **Classification and control**: How will MILNET data be separated from commercial Starlink traffic on shared ground infrastructure?
- **Allied access**: Whether coalition partners (including ADF) will have terminal access is unconfirmed as of March 2026
- **Spectrum**: Frequency plan not yet publicly disclosed

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** MILNET does not yet exist — all parameters are projected and subject to change. Allied access, including for ADF, has not been confirmed as of March 2026. Terminal specifications and security protocols have not been publicly disclosed.
>
> **Limitations:** LEO satellites have shorter contact windows per pass than GEO — network software must seamlessly hand off between satellites, introducing complexity and potential failure modes. Coverage at high latitudes may be uneven depending on orbital inclination.
>
> **Assumptions:** Assumes SpaceX meets projected launch timelines, which have historically been optimistic. Assumes military and commercial Starlink traffic can be effectively separated and secured at both the space and ground segments.

**Related:** [[SATCOM Architecture]] · [[SDA Transport Layer (PWSA)]] · [[ADF SATCOM Systems]] · [[Satellite Jamming Techniques]] · [[SDA Tranche 1 Launch Campaign]]
