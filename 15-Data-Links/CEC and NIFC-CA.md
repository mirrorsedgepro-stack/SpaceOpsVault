---
title: CEC and NIFC-CA
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Tactical Data Links Overview, Link 16]
section: 15
tags:
  - CEC
  - NIFC-CA
  - Engage-on-Remote
  - Aegis
  - SM-6
  - E-2D
aliases:
  - Cooperative Engagement Capability
  - Naval Integrated Fire Control Counter Air
---

# CEC (Cooperative Engagement Capability)

> [!abstract] Quick Summary
> Covers the Cooperative Engagement Capability (CEC) and Naval Integrated Fire Control-Counter Air (NIFC-CA) — the fire-control quality data link architecture that enables Engage-on-Remote for naval air and missile defence. This is the architecture that allows an Aegis ship to shoot a missile guided by another ship's or aircraft's radar.

## How CEC Differs from Link 16

| Feature | [[Link 16]] | CEC |
| --- | --- | --- |
| Data type | **Processed tracks** | **Raw radar measurement data** |
| Quality | Situational awareness | **Fire-control quality** |
| Engagement | Requires own sensor | Enables **Engage-on-Remote (EOR)** |

> [!tip] Hot Tip
> CEC provides fire-control quality tracks (not just surveillance quality) — this is the key distinction from Link 16. With CEC, a ship can launch a missile guided by another ship's radar. This dramatically expands the defended area but requires a reliable, low-latency network link between shooters. Network degradation directly degrades the engagement envelope.

## Engage-on-Remote (EOR)

A ship launches a missile against a target detected **only by another platform's radar**.

- Extends engagement envelope from ship's radar horizon (~20–30 nm against sea-skimmers) to E-2D detection range (**200+ nm** at altitude)

---

# NIFC-CA (Naval Integrated Fire Control – Counter Air)

## Architecture

```
F-35C (stealth sensor, MADL)
  → E-2D Advanced Hawkeye (central node, AN/APY-9, CEC/TTNT/Link 16)
    → Aegis ships (CEC, EOR, SM-6)
```

## Kill Chain

1. F-35 penetrates → ESM detects SAM battery → geolocates
2. Passes targeting via [[MADL]]
3. E-2D generates fire-control track via CEC
4. Aegis DDG **200 nm away** launches SM-6 (guided by CEC)
5. F-35 provides BDA

## Vulnerability

> **Destroying/jamming the E-2D collapses the entire architecture.** NIFC-CA depends entirely on data links.

## ADF Relevance

- **Hobart-class DDG**: Aegis + [[Link 16]] / CEC planned
- **E-7A Wedgetail**: analogous to E-2D role
- **F-35A**: stealth sensor
- **Hunter-class FFG**: future
- **⚠️ RAN does not yet have CEC** — key future capability gap

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** CEC is a US Navy system — ADF access is through bilateral cooperation and Hobart-class integration programmes. Not all ADF surface combatants have CEC.
>
> **Limitations:** CEC requires low-latency network links — any significant delay between sensor and shooter degrades fire-control quality. Range between CEC nodes affects track fusion quality.
>
> **Assumptions:** Assumes the CEC network remains uncorrupted — a cyber attack that injects false tracks into CEC could cause fratricide or waste interceptors.

**Related:** [[Tactical Data Links Overview]] · [[MADL]] · [[Link 16]] · [[EW Against Data Links]]
