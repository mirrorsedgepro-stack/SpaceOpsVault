---
title: Space-Based Targeting
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [Military Satellite Capabilities Overview, SIGINT and ELINT Overview]
section: 14
tags:
  - targeting
  - F2T2EA
  - kill-chain
  - space-enabled
---

# Space-Based Targeting

> [!abstract] Quick Summary
> Explains how space-based capabilities enable each phase of the F2T2EA kill chain — from finding and fixing targets through to assessing effects — and why space access is a prerequisite for precision strike. Loss of space support at any phase degrades or collapses the entire kill chain.

## Space Enables Every Step of F2T2EA

```mermaid
flowchart LR
    F["🔍 FIND\nSIGINT sats · GMTI\nISR constellation"]
    FX["📍 FIX\nNGA imagery\nELINT TDOA · GPS"]
    T["👁️ TRACK\nSATCOM relay\nData links"]
    TG["🎯 TARGET\nGPS coordinates\nto weapon"]
    E["💥 ENGAGE\nGPS guidance\nSATCOM updates"]
    A["📊 ASSESS\nSatellite BDA\nPre-impact imaging"]

    F --> FX --> T --> TG --> E --> A

    style F fill:#1a3a5c,color:#fff,stroke:#4a7ab5
    style FX fill:#1a3a5c,color:#fff,stroke:#4a7ab5
    style T fill:#1a3a5c,color:#fff,stroke:#4a7ab5
    style TG fill:#7a3a00,color:#fff,stroke:#c06000
    style E fill:#7a1a1a,color:#fff,stroke:#c03030
    style A fill:#1a5c1a,color:#fff,stroke:#3a9a3a
```

| Step | Space Contribution |
| --- | --- |
| **FIND** | ISR satellites, [[SIGINT Satellites by Nation\|ELINT triplets]], [[GMTI and AMTI\|GMTI]], AMTI |
| **FIX** | NGA imagery analysis, [[GPS]] coordinates from observer, SAR geolocation, ELINT TDOA |
| **TRACK** | ISR + [[SATCOM Architecture\|SATCOM]] relay, GMTI/AMTI radar via [[Tactical Data Links Overview\|data link]] |
| **TARGET** | PNT + SATCOM ([[GPS]] coordinates to weapon) |
| **ENGAGE** | GPS guidance + SATCOM in-flight updates |
| **ASSESS** | Satellite imagery BDA, missile pre-impact imaging via SATCOM |

> Without space, every step of the modern kill chain degrades or fails entirely.

> [!tip] Hot Tip
> Space-based targeting is not instantaneous — each phase of F2T2EA takes time, and that time is driven by satellite revisit rates, data downlink, processing, and decision cycles. When assessing kill chain timelines, satellite access windows are often the critical constraint, not weapons delivery time.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Space-based targeting products (GMTI, imagery, SIGINT) require access to classified systems and intelligence production pipelines — not available to all coalition partners at the same fidelity.
>
> **Limitations:** Space-based sensors cannot see inside buildings or underground — targeting hard and deeply buried targets requires complementary collection. Weather, camouflage, and deception all degrade space-based targeting.
>
> **Assumptions:** Assumes the target has not moved between collection and strike — for mobile targets, time-sensitive targeting processes must keep pace with target movement.

**Detailed pages:**
- [[GMTI and AMTI]]
- [[Tomahawk Guidance]]
- [[Kill Chain Comparison]]

**Related:** [[Tactical Data Links Overview]] · [[GPS]] · [[SATCOM Architecture]]
