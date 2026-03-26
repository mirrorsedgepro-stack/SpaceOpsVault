---
title: Electronic Warfare Fundamentals
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [RF Spectrum Reference]
section: 12
tags:
  - EW
  - EA
  - ES
  - EP
  - EMCON
---

# Electronic Warfare Fundamentals

> [!abstract] Quick Summary
> Introduces the three EW pillars — Electronic Support (ES), Electronic Attack (EA), and Electronic Protection (EP) — and how they interact in the space context. Understanding these fundamentals is the foundation for all spectrum operations planning.

## Three Pillars

| Pillar | Full Name | Function | Examples |
| --- | --- | --- | --- |
| **ES/ESM** | Electronic Support | Passive intercept, direction finding, ELINT, COMINT, geolocation | [[Australian SIGINT Platforms\|MC-55A]], F-35A AN/ASQ-239 |
| **EA/ECM** | Electronic Attack | Noise jamming, deception jamming, DRFM, directed energy | [[ADF EW Platforms\|EA-18G]] ALQ-99, [[Russian EW Systems\|Krasukha-4]] |
| **EP/ECCM** | Electronic Protection | Frequency hopping, spread spectrum, adaptive nulling, EMCON, LPI/LPD | [[SATCOM Architecture\|AEHF]], [[MADL]], [[CRPA Anti-Jam Antennas\|CRPA]] |

## Key Concepts

- **J/S ratio**: if jamming-to-signal exceeds receiver processing gain, receiver is denied
- **Burn-through range**: distance at which radar power overcomes jamming
- **EMCON**: minimise RF emissions to avoid detection — itself a form of EP; key tradeoff with data link connectivity
- **LPI/LPD**: Low Probability of Intercept/Detection — e.g. [[MADL]] on F-35

## The Central Paradox

> **More connectivity = more effective kill chain = more emissions = more vulnerability**

Solution: **adaptive EMCON** — see [[EW Against Data Links]].

> [!tip] Hot Tip
> ES (listening) is always on — even when you're not jamming, you're being characterised. Every time an ADF platform transmits (radar, Link 16, SATCOM terminal), it's adding to an adversary's electronic order of battle picture. Emission discipline is a form of EP.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** EA authorities require specific approval chains — jamming, even defensive jamming, has escalatory implications and must be authorised.
>
> **Limitations:** ES cannot distinguish between all signal types in a dense electromagnetic environment — modern battlefields have hundreds of emitters.
>
> **Assumptions:** Assumes operators understand their own systems' emission signatures — in practice, EMCON discipline is inconsistently applied.

**Related:** [[ADF EW Platforms]] · [[EMSO Framework]] · [[EW Against Data Links]] · [[Russian EW Systems]]
