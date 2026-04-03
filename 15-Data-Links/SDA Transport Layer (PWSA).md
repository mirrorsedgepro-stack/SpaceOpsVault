---
title: SDA Transport Layer (PWSA)
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [Link 16, SATCOM Architecture, Orbital Mechanics]
section: 15
tags:
  - SDA
  - PWSA
  - Link-16-from-space
  - JADC2
  - proliferated
aliases:
  - Proliferated Warfighter Space Architecture
  - PWSA
---

# SDA Transport Layer (PWSA)

> [!abstract] Quick Summary
> Describes the SDA Proliferated Warfighter Space Architecture (PWSA) Transport Layer — a LEO satellite constellation that provides BLOS Link 16 relay, low-latency data transport, and direct connectivity to the space layer without new terminals. It is the programme that makes Link 16 a global, space-enabled network rather than a line-of-sight-only system.

## Design Philosophy

- Cost per satellite: **~$14M** (deliberately cheap and proliferated for resilience)
- Uses **existing [[Link 16]] radios** — no new equipment needed at the tactical edge
- Every Link 16-equipped platform becomes a potential JADC2 node

## Tranches

| Tranche | Satellites | Status | Capability |
| --- | --- | --- | --- |
| **Tranche 0** | 28 | On orbit | First [[Link 16]] from space (Nov 2023); ~50% connectivity |
| **Tranche 1** | ~154 | Launching 2025–26 | ~42 on orbit; **Strategic Pause** in early 2026; **T1TL-A launch** (21 sats) April/May 2026 |
| **Tranche 2** | ~270+ | High-rate manufacturing | Sierra Space completed structures 3 months early; first launch **Sept 2026** |
| **Tranche 3** | ~72 (Tracking) | Contracted Dec 2025 | Persistent midcourse missile tracking |

> [!tip] Hot Tip
> The scarcity of **Optical Communication Terminals (OCTs)** and encryption devices remains the primary "critical path" for PWSA deployment in 2026. If coordinating with SDA, verify the OCT availability for specific satellite blocks.

## Tranche 1 Launch Campaign (Updated March 2026)

- First batch: 21 York Space Systems satellites launched **10 Sep 2025**
- Second batch: 21 Lockheed Martin satellites launched **15 Oct 2025**
- Launches paused late 2025 (vendor readiness issues)
- **10 Tranche 1 launches planned in 2026**: 6 Transport + 4 Tracking
- First Tranche 1 **missile tracking satellites** expected early 2026

## AN/PRC-161 BATS-D

> Handheld Link 16 radio — a **soldier in the jungle** can receive targeting data from a sensor on the other side of the world via the SDA constellation.

## Resilience Factors

- **Optical inter-satellite links**: laser in vacuum — **unjammable**
- **Proliferated constellation** (126+ satellites): no single point of failure
- L-band ground segment still theoretically jammable, but satellite transmits from overhead with power advantage
- Ground entry points: **jammable** — potential adversary target

## ADF Implications

Every RAAF/RAN Link 16 platform can potentially connect:
- F-35A, EA-18G, E-7A, F/A-18F
- Hobart-class DDG, Hunter-class FFG

Access depends on **Five Eyes agreements** and **crypto interoperability**.

> [!tip] Hot Tip
> The PWSA Transport Layer is a game-changer for BLOS comms — existing Link 16 terminals connect to space-relayed networks without modification. However, the constellation is still being built — don't plan operations in 2026-2027 as if full PWSA capability exists. Check current on-orbit count and coverage before planning.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** PWSA is a US programme — ADF access depends on bilateral agreements and may not include all capability tiers. The constellation is incomplete through the late 2020s — coverage is limited to priority areas initially.
>
> **Limitations:** LEO satellites have short contact windows (~10 minutes per pass for a single satellite) — the transport layer requires sufficient satellite density for continuous coverage, which Tranche 1 alone may not provide globally.
>
> **Assumptions:** Assumes PWSA satellites remain operational — LEO is a contested environment and the proliferated architecture is designed for resilience, but individual satellites can be lost.

**Related:** [[Tactical Data Links Overview]] · [[Link 16]] · [[Missile Warning and Tracking]] · [[Golden Dome Missile Defence]]
