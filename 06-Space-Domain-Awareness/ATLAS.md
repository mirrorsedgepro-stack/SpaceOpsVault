---
title: ATLAS
classification: UNCLASSIFIED // FOUO
difficulty: Intermediate
prerequisites: [Space Domain Awareness]
section: 6
tags:
  - ATLAS
  - C2
  - SDA
  - L3Harris
  - Kronos
aliases:
  - Advanced Tracking and Launch Analysis System
---

# ATLAS (Advanced Tracking and Launch Analysis System)

> [!abstract] Quick Summary
> Covers ATLAS — the USSF's new SDA software that replaced the 1980s SPADOC system and serves as the fusion backbone for the combined space operations picture. Operationally relevant because any SDA product received from USSF partners flows through or is influenced by this system.

## Overview

- **Type**: C2 and sensor fusion platform for [[Space Domain Awareness|SDA]]
- **Contractor**: L3Harris (subcontractors: Omitron, Parsons)
- **Operator**: [[18th Space Defense Squadron]], Space Delta 2
- **Operational acceptance**: **September 2025**
- Replaced the 1979-era **SPADOC** (Space Defense Operations Center)

## Capabilities

- Machine-to-machine processing of commercial, civil, and military space data
- Enables rapid detect-track-identify of objects and adversary manoeuvres
- Foundational software for the broader Space C2 modernisation programme

> [!tip] Hot Tip
> ATLAS was declared operationally accepted in September 2025, but DOT&E noted SPADOC cannot yet be fully decommissioned — in early exercises, be prepared for some legacy data sources to still flow through SPADOC pathways. Verify which system produced any SDA product you receive.

## March 2026 Update: DOT&E Findings

A Pentagon DOT&E report (16 March 2026) found:
- ATLAS **lacks minimum viable capability** required to decommission SPADOC
- Testing revealed **deficiencies consistent with system immaturity**
- SPADOC is no longer used "operationally" but decommission plan still in work

## Kronos — New Parallel C2 Component

In May 2025, Space Force restructured the broader Space C2 programme into two tracks:
- **ATLAS**: foundational [[Space Domain Awareness|SDA]] and data processing
- **Kronos**: battlespace awareness, theatre support, active space defence capabilities
- First Kronos contracts expected **April 2026**

## Programme History

- Contract awarded: October 2018 ($53M initial)
- Originally planned operational by 2022
- Bedeviled by integration delays; designated a "troubled programme" by acquisition executive in 2023
- Year-long trial period at Delta 2 completed September 2025

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** ATLAS is a classified system — ADF access is via the combined space operations framework, not direct.
>
> **Limitations:** ATLAS is new and has limited operational history — anomalous behaviour or data quality issues may not yet be fully characterised. The transition from SPADOC means some institutional knowledge is still being transferred.
>
> **Assumptions:** Assumes the L3Harris-built system has been correctly integrated with all legacy sensor feeds; assumes ATLAS data latency is acceptable for the operational tempo of space event response.

**Related:** [[Space Domain Awareness]] · [[USSF Organisation]] · [[ATLAS and Kronos C2]]
