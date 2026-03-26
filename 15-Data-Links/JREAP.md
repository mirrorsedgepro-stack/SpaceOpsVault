---
title: JREAP
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Link 16, SATCOM Architecture]
section: 15
tags:
  - JREAP
  - BLOS
  - Link-16-extension
aliases:
  - Joint Range Extension Applications Protocol
  - MIL-STD-3011
  - STANAG 5518
---

# JREAP (Joint Range Extension Applications Protocol)

> [!abstract] Quick Summary
> Explains JREAP — the protocol that extends Link 16 beyond line-of-sight using SATCOM, enabling BLOS connectivity for ground forces and distributed operations. It is the primary mechanism for connecting rear-area headquarters to the forward tactical picture using existing Link 16 infrastructure.

Extends [[Link 16]] J-series messages over SATCOM, IP, or serial links for **BLOS** tactical data exchange.

## Variants

| Variant | Transport | Notes |
| --- | --- | --- |
| JREAP-A | Half-duplex SATCOM | |
| JREAP-B | Full-duplex serial | |
| **JREAP-C** | **TCP/IP** | Most common; runs over any IP bearer |

## Operational Impact

> **Without JREAP**: [[Link 16]] data stays within LOS.
> **With JREAP-C over [[SATCOM Architecture|WGS]]**: HQ in Canberra sees the same Link 16 picture as a ship in the Philippine Sea.

## Limitation

Inherits vulnerabilities of the transport medium — **SATCOM jamming breaks JREAP**.

See [[Satellite Jamming Techniques]] and [[EW Against Data Links]].

> [!tip] Hot Tip
> JREAP adds latency relative to native Link 16 — the SATCOM relay introduces delay that matters for time-critical tracks. In a fast-moving air picture, JREAP-relayed tracks may be slightly stale compared to LOS Link 16. Operators using JREAP should know the expected latency of their relay path.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** JREAP requires a SATCOM relay path — it is dependent on WGS or commercial SATCOM availability. In a SATCOM-denied environment, JREAP connectivity is lost.
>
> **Limitations:** JREAP bandwidth over SATCOM is limited compared to LOS Link 16 — track capacity and update rates may be reduced. Latency varies with SATCOM path length (GEO vs LEO relay).
>
> **Assumptions:** Assumes SATCOM availability and sufficient bandwidth for JREAP — in a congested or contested SATCOM environment, JREAP may be deprioritised.

**Related:** [[Tactical Data Links Overview]] · [[Link 16]] · [[SATCOM Architecture]] · [[SDA Transport Layer (PWSA)]]
