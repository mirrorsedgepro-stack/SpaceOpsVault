---
title: MADL
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Tactical Data Links Overview, Link 16]
section: 15
tags:
  - MADL
  - F-35
  - LPI
  - LPD
  - stealth
aliases:
  - Multifunction Advanced Data Link
---

# MADL (Multifunction Advanced Data Link)

> [!abstract] Quick Summary
> Describes MADL — the F-35's LPI/LPD directional data link that enables covert formation sharing without the detection signature of Link 16. For ADF F-35A operators, understanding MADL's gateway limitations is critical to ensuring F-35-derived targeting data reaches coalition partners.

- **Frequency**: Ku-band directional
- **Key feature**: **LPI/LPD** (Low Probability of Intercept/Detection)
- **Users**: F-35; planned for B-21 Raider, B-2
- **NOT compatible** with [[Link 16]] — requires gateway translation (e.g. Open Systems Gateway)

## Tactical Concept

> F-35s near the adversary use MADL between themselves; the **rearmost F-35** translates to [[Link 16]] for legacy platforms — forward aircraft **never emit Link 16** (preserving stealth).

> [!tip] Hot Tip
> MADL only communicates between F-35s — it cannot share data with non-F-35 platforms directly. To get F-35 MADL tracks onto a coalition Link 16 network, a designated F-35 must translate from MADL to Link 16, which requires careful positioning (usually rearward) to avoid exposing the Link 16 emission from the formation.

## Operational Validation

- **NATO Ramstein Flag (April 2025)**: F-35 MADL → gateway → ground C2 → rocket artillery — **sensor-to-shooter in minutes**

## Role in NIFC-CA

See [[CEC and NIFC-CA]] — F-35C uses MADL to pass targeting to E-2D, which translates to [[CEC and NIFC-CA|CEC]] for Aegis engagement.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** MADL is an F-35-only link — only nations with F-35 fleets can participate. Gateway functions require deliberate network design and role assignment.
>
> **Limitations:** MADL is directional — it requires the transmitting and receiving F-35s to be within each other's beam coverage. Network geometry matters.
>
> **Assumptions:** Assumes F-35 formation geometry and tactics enable MADL connectivity — in a fluid air battle, maintaining MADL geometry is not always possible.

**Related:** [[Tactical Data Links Overview]] · [[Link 16]] · [[CEC and NIFC-CA]] · [[Electronic Warfare Fundamentals]]
