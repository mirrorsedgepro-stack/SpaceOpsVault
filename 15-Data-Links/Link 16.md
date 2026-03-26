---
title: Link 16
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [Tactical Data Links Overview, RF Spectrum Reference]
section: 15
tags:
  - Link-16
  - TDMA
  - L-band
  - data-link
aliases:
  - MIL-STD-6016
  - STANAG 5516
---

# Link 16

> [!abstract] Quick Summary
> Details Link 16 — the primary NATO/coalition tactical data link for air operations — covering its TDMA architecture, J-series messages, anti-jam characteristics, and the critical vulnerability of its L-band emissions to detection. It is the most widely fielded data link in coalition operations and the baseline for understanding all other links.

## Technical Specifications

- **Standard**: MIL-STD-6016 / STANAG 5516
- **Frequency**: L-band 960–1215 MHz
- **Access method**: TDMA (128 time slots/sec)
- **Frequency hopping**: across 51 frequencies
- **Range**: **Line-of-sight only** natively — requires [[JREAP]] or [[SDA Transport Layer (PWSA)|SDA]] for BLOS

## Anti-Jam

- **Good** against narrowband jamming (frequency hopping)
- **Vulnerable** to wideband barrage across 960–1215 MHz

## J-Series Messages

| NPG | Function |
| --- | --- |
| NPG 3 | Surveillance tracks |
| NPG 6 | Targeting |
| NPG 10 | EW coordination |
| NPG 14–15 | Voice |

## Key Milestones

- **First transmitted from space**: November 2023 by [[SDA Transport Layer (PWSA)|SDA Tranche 0]]
- This means existing Link 16 radios can connect to the space layer — no new equipment needed

> [!tip] Hot Tip
> The SDA Tranche 0 satellite first relayed Link 16 in November 2023 — existing Link 16 terminals can connect to the space layer without new radios. If you have Link 16 today, you can use space-based BLOS relay now.

## Detection Vulnerability

> L-band emissions detectable by adversary ESM → direction-finding → platform targeting → order-of-battle analysis.

This is why:
- F-22 was **receive-only**
- F-35 uses [[MADL]] operationally and only translates to Link 16 from rearward positions

> [!tip] Hot Tip
> Link 16 emissions in L-band are detectable at significant range by adversary ESM — in a contested environment, transmitting on Link 16 is not covert. Platforms should understand that their position can be estimated from their Link 16 emissions alone, which is why F-22 was receive-only and F-35 uses MADL operationally.

## ADF Platforms

F-35A, F/A-18F, EA-18G, E-7A, P-8A, MQ-4C, Hobart-class DDG, future Hunter-class FFG

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Link 16 encryption (TSEC) requires current crypto loads — expired or missing crypto prevents network participation. JTIDS terminal time slot allocation must be coordinated before operations.
>
> **Limitations:** Link 16 is line-of-sight only natively (~300nm between aircraft) — BLOS requires JREAP relay or SDA space layer, both of which add latency. Wideband barrage jamming across 960-1215 MHz can degrade Link 16 regardless of frequency hopping.
>
> **Assumptions:** Assumes all participants have synchronised network time — Link 16 TDMA is time-critical and desynchronisation breaks the network.

**Related:** [[Tactical Data Links Overview]] · [[JREAP]] · [[SDA Transport Layer (PWSA)]] · [[MADL]] · [[EW Against Data Links]]
