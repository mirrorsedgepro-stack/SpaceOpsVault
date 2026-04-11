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

> [!info] F2T2EA Kill Chain — Space at Every Step
> **🔍 FIND** → **📍 FIX** → **👁️ TRACK** → **🎯 TARGET** → **💥 ENGAGE** → **📊 ASSESS**
>
> ISR sats · GMTI · NGA imagery · GPS · SATCOM relay · data links · PNT to weapon · GPS guidance · satellite BDA

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

> [!file] SDP 3-101 Targeting — Local Copy
> Attach a locally-saved copy of SDP 3-101 (Space-Based Targeting doctrine) in the [[Local Document Library]] using `Ctrl+P` → **Add file link**.

**Related:** [[Tactical Data Links Overview]] · [[GPS]] · [[SATCOM Architecture]]
