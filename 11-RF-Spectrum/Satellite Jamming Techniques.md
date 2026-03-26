---
title: Satellite Jamming Techniques
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [RF Spectrum Reference, Counterspace Threats Overview]
section: 11
tags:
  - jamming
  - SATCOM
  - bent-pipe
  - EW
---

# Satellite Jamming Techniques

> [!abstract] Quick Summary
> Covers the four main satellite jamming techniques — uplink, downlink, bent-pipe, and on-orbit — explaining how each works, who uses them, and what detection and mitigation options exist. Understanding these techniques is essential for assessing SATCOM vulnerability and planning for degraded communications environments.

## Four Methods

### 1. Uplink Jamming
- High-power signal directed **toward the satellite**
- Affects **all users** in the satellite footprint
- Requires reaching ~36,000 km (for [[Orbital Mechanics|GEO]])
- Needs significant transmit power

### 2. Downlink Jamming
- Jams the signal **at the ground receiver**
- Much **less power** needed than uplink
- Effects are **localised** to the jammer's vicinity

> [!tip] Hot Tip
> Downlink jamming is the easiest counterspace technique — it only needs to be near the ground terminal, not near the satellite. A jammer in a vehicle parked near a satellite ground station or embarked terminal can deny comms without any space capability whatsoever. Physical security of ground terminals matters as much as electronic protection.

### 3. Bent-Pipe Exploitation
- Most GEO SATCOM uses **transparent transponders** that simply amplify and retransmit
- Jamming signal is **amplified by the satellite itself** and retransmitted to all ground receivers
- **Devastating against [[SATCOM Architecture|WGS]]** (no anti-jam / no onboard processing)

### 4. On-Orbit Jamming
- Co-orbital platform jams at **close range**
- **Most threatening** — hardest to counter
- Linked to [[Orbital Mechanics|RPO]] and co-orbital threats

## Electromagnetic Fratricide

> The US jammed **its own satellites 261 times** in 2015 — illustrating the complexity of spectrum management in operations.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Detecting and attributing jamming requires spectrum monitoring equipment and technical expertise — not all units have organic EMSO capability.
>
> **Limitations:** Distinguishing intentional jamming from unintentional interference (equipment malfunction, nearby transmitters) requires analysis. Mitigation options (antenna nulling, frequency change, alternate satellite) all take time and may not be available in the field.
>
> **Assumptions:** Assumes the affected system has some jam-reporting and escalation mechanism — many legacy systems do not.

**Related:** [[RF Spectrum Reference]] · [[Electronic Warfare Fundamentals]] · [[US Counterspace Offensive]] · [[Russian EW Systems]]
