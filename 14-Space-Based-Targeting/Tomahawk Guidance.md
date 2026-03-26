---
title: Tomahawk Guidance
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Space-Based Targeting, GPS]
section: 14
tags:
  - Tomahawk
  - TLAM
  - guidance
  - INS
  - TERCOM
  - DSMAC
  - GPS
---

# Tomahawk Guidance (BGM-109 TLAM)

> [!abstract] Quick Summary
> Details the Tomahawk Land Attack Missile guidance architecture — INS, TERCOM, GPS, and DSMAC — explaining how space-based inputs combine with other sensors to achieve precision strike even under GPS denial. With RAN acquiring Tomahawk for Hobart and Hunter class ships, this is directly relevant to ADF strike planning.

## Four Complementary Guidance Systems

| System | Space Dependency | Function | Accuracy |
| --- | --- | --- | --- |
| **INS** | None | Baseline navigation; degrades over time | Drifts |
| **TERCOM** | Indirect (satellite-derived maps) | Radar altimeter terrain matching; corrects INS drift | Good |
| **[[GPS]]** | **Direct** | ~10m accuracy; rapid mission planning (min vs hrs) | ~10m |
| **DSMAC** | Indirect (satellite imagery) | Terminal camera vs pre-loaded imagery | ~3m CEP |

## Block IV/V Enhancements

- **Two-way SATCOM datalink**: enables in-flight retargeting, missile loitering, pre-impact imagery to commander
- Anti-jam GPS receivers

## ADF Relevance

- RAN acquiring Tomahawk for **Hobart-class DDG** and **Hunter-class FFG**
- Dependent on [[GPS]] and [[SATCOM Architecture|SATCOM]] for in-flight updates
- See [[EW Against Data Links]] for vulnerabilities when GPS/SATCOM are jammed

> [!tip] Hot Tip
> Tomahawk's multi-modal guidance is a model for GPS-resilient design — it does not rely solely on GPS. When evaluating any precision weapon's GPS vulnerability, ask what happens when GPS is denied: does it miss entirely, or does it degrade gracefully to the next guidance mode? Tomahawk degrades gracefully.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Tomahawk employment requires pre-loaded mission data (terrain maps, target coordinates, DSMAC images) — this requires time and intelligence that may not be available in a rapidly developing scenario.
>
> **Limitations:** TERCOM requires terrain variation — it is less effective over flat featureless terrain (open desert, ocean). DSMAC requires the target to look like the reference image — significant structural changes or camouflage can cause terminal guidance failure.
>
> **Assumptions:** Assumes GPS is available for the cruise phase of flight — extended GPS denial along the flight path degrades CEP.

**Related:** [[Space-Based Targeting]] · [[GPS]] · [[Kill Chain Comparison]] · [[EW Against Data Links]]
