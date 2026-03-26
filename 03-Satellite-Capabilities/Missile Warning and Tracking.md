---
title: Missile Warning and Tracking
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [Military Satellite Capabilities Overview, Orbital Mechanics]
section: 3
tags:
  - missile-warning
  - SBIRS
  - OPIR
  - SDA-tracking
  - Golden-Dome
---

# Missile Warning and Tracking

> [!abstract] Quick Summary
> Covers the space-based missile warning architecture — SBIRS, OPIR, and the SDA Tracking Layer — that provides the joint force with early warning and fire control quality tracking of ballistic and hypersonic threats. The transition to proliferated LEO tracking is reshaping this architecture through the late 2020s.

## Current Systems

- **SBIRS** (Space-Based Infrared System): [[Orbital Mechanics|GEO]] + HEO payloads — operational launch detection
- **Next-Gen OPIR**: replacing SBIRS at GEO

## Proliferated LEO Tracking

- **SDA Tracking Layer Tranche 3**: 72 proliferated [[Orbital Mechanics|LEO]] satellites ($3.5B, contracted late 2025) for persistent midcourse missile tracking
- See [[SDA Transport Layer (PWSA)]] for the broader constellation architecture

## Detection Chain

```
SBIRS/OPIR detects launch (seconds)
        ↓
Ground radars + proliferated LEO sensors
        ↓
Midcourse tracking
        ↓
Terminal defence handoff → Aegis / THAAD / Patriot
```

> [!tip] Hot Tip
> The transition from SBIRS to SDA Tracking Layer is not complete — both architectures are running in parallel through the late 2020s. In a briefing context, distinguish between "strategic" missile warning (SBIRS/OPIR) and "tactical" missile tracking (SDA/HBTSS) — they serve different customers and have different access paths for ADF planners.

## Golden Dome (March 2026 Update)

- Proposed multi-layer missile defence system combining space-based sensors, interceptors, and AI-enabled C2
- Cost estimate risen to **$185 billion** (up from $125B initial)
- Congress approved $25B for early development
- Boost-phase space-based interceptor prototypes contracted November 2025
- See [[Golden Dome Missile Defence]] for details

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Missile warning data from SBIRS is highly classified and tightly controlled — access for ADF planners requires specific authorisation and established data-sharing arrangements with USSPACECOM.
>
> **Limitations:** Current systems have difficulty tracking manoeuvring hypersonic glide vehicles (HGVs) — this is the specific gap HBTSS and the SDA Tracking Layer are designed to fill. Ground processing stations are potential single points of failure in the detection chain.
>
> **Assumptions:** Assumes adversaries do not conduct a simultaneous suppression campaign against both the satellite layer and the ground processing stations. Assumes the SDA Tracking Layer deployment timeline holds through the late 2020s.

**Related:** [[Space-Based Targeting]] · [[SDA Transport Layer (PWSA)]] · [[USSF Organisation]] · [[Golden Dome Missile Defence]]
