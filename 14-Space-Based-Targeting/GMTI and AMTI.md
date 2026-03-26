---
title: GMTI and AMTI
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Space-Based Targeting, Orbital Mechanics]
section: 14
tags:
  - GMTI
  - AMTI
  - JSTARS
  - space-based
  - E-7A
---

# GMTI and AMTI

> [!abstract] Quick Summary
> Covers Ground Moving Target Indicator (GMTI) and Air Moving Target Indicator (AMTI) from space — the emerging capability to track moving ground and air targets from LEO satellites, replacing or complementing manned ISR. This is a rapidly evolving area with significant implications for how ADF integrates into US space-based ISR architecture.

## GMTI (Ground Moving Target Indicator)

- E-8C JSTARS **retired 2023**; replacement is **space-based GMTI**
- Joint USSF/NRO programme
- GMTI-specific satellites planned **2028**
- Joint Mission Management Center being built (NGA, Springfield VA)
- **$1B+** FY2026 budget
- Survivability advantage: satellites harder to target than aircraft at 40,000 ft

## AMTI (Air Moving Target Indicator)

- Traditionally E-3/[[ADF EW Platforms|E-7A]] role
- Space-based AMTI prototypes on orbit (May 2025)
- Estimated operational: early 2030s
- $2.2B budget consideration
- USAF cancelled E-7 procurement in FY2026 budget — Congress pushing back

> **E-7A Wedgetail**: RAAF fleet remains **critical** regardless of US space-based AMTI decisions.

## Golden Dome Integration

Both GMTI and AMTI are now being accelerated under the [[Golden Dome Missile Defence]] programme, with the $185B cost estimate partly driven by additional AMTI and space data network requirements.

> [!tip] Hot Tip
> Space-based GMTI/AMTI is still maturing — current systems have revisit gaps that allow targets to move between passes. The SDA Tracking Layer partially addresses this for missile tracking, but broad-area moving target indication from space is not yet persistent. Plan for revisit gaps when using space-based GMTI.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** GMTI/AMTI satellites are high-value national assets — tasking them for specific operational targets requires high-level approval and competing with other intelligence customers.
>
> **Limitations:** Space-based GMTI has resolution and revisit limitations — it can indicate that something is moving and approximately where, but cannot always determine what type of vehicle.
>
> **Assumptions:** Assumes the target is outdoors and moving during the satellite's collection window — a target that stops moving or takes cover during the overhead pass will not be detected.

**Related:** [[Space-Based Targeting]] · [[ADF EW Platforms]] · [[Golden Dome Missile Defence]]
