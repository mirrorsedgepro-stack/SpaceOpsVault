---
title: EW Against Data Links
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Electronic Warfare Fundamentals, Tactical Data Links Overview, Link 16]
section: 15
tags:
  - EW
  - data-links
  - kill-chain
  - jamming
  - EMCON
---

# EW Against Data Links — Breaking the Kill Chain

> [!abstract] Quick Summary
> Examines how electronic warfare attacks are applied against tactical data links — jamming, spoofing, and exploitation — and the defensive techniques used to maintain link integrity in a contested EM environment. Understanding these attack vectors is essential for planning resilient data link architectures and recognising EW activity during operations.

> **Jamming data links is more efficient than shooting down platforms.**

## Four Attack Strategies

### 1. Break Sensor-to-Shooter Link
Jam [[CEC and NIFC-CA|CEC]] or [[Link 16]] — shooter has weapons but no targets.

- [[Russian EW Systems|Krasukha-4]] (X/Ku, 300 km)
- Murmansk-BN (HF, 5,000 km — threatens [[Link 22]])
- [[Russian EW Systems|Tirada-2S]] (SATCOM uplink — threatens [[JREAP]])

### 2. Deny GPS to Degrade Weapon Accuracy
Jam L-band; JDAM CEP degrades from ~10m to **>100m** (INS only).

- [[Russian EW Systems|Tobol]] (persistent GPS denial, 100+ km)
- [[Russian EW Systems|R-330Zh Zhitel]], Pole-21
- Commercial jammers **<$100**

### 3. Target Emitters via Data Link Detection
Detect [[Link 16]] L-band emissions via ESM → direction-find → fire anti-radiation missile or SAM at emitter.

### 4. Overwhelm Through Complexity
Launch 100s of simultaneous targets — saturate TDMA time slots in [[Link 16]] network; track quality degrades; kill chain slows.

> This explains China's/Russia's investment in **mass salvos** of cruise missiles and cheap drones.

## The Central Paradox

> **More connectivity = more effective kill chain = more emissions = more vulnerability**

> [!tip] Hot Tip
> EW against data links is as much about psychology as physics — a jammer that disrupts a network for 30 seconds at a critical moment (missile engagement window) can cause a missed shot even if the link recovers immediately after. Adversaries time EW attacks to the engagement timeline, not just to cause general disruption.

## Solution: Adaptive EMCON

| Level | Environment | Behaviour |
| --- | --- | --- |
| **Full emission** | Permissive | Maximum connectivity |
| **Selective emission** | Contested | Transmit only when essential; use [[MADL]] for stealth |
| **EMCON silent** | Denied | Receive only or no emissions at all |

## SDA Link 16 from Space — Resilience

- Optical inter-satellite links: **unjammable** (laser in vacuum)
- Proliferated constellation: no single point of failure
- L-band ground segment still theoretically jammable
- Ground entry points: **jammable** — potential adversary target

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Defensive EW (jamming mitigation, link frequency management) requires spectrum management authority and specialist JEMSO skills — not organic to most unit headquarters.
>
> **Limitations:** Frequency hopping (Link 16) is effective against narrowband jamming but not against wideband barrage — a sufficiently powerful broadband jammer can degrade Link 16 regardless.
>
> **Assumptions:** Assumes operators recognise and correctly report link degradation as potential EW activity — in practice, link problems are often misattributed to equipment failure rather than adversary action.

**Related:** [[Tactical Data Links Overview]] · [[Electronic Warfare Fundamentals]] · [[Russian EW Systems]] · [[Link 16]] · [[CEC and NIFC-CA]]
