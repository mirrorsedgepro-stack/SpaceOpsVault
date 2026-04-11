---
title: Kill Chain Comparison
classification: UNCLASSIFIED // FOUO
difficulty: Advanced
prerequisites: [Space-Based Targeting, Counterspace Threats Overview]
section: 14
tags:
  - kill-chain
  - F2T2EA
  - Tomahawk
  - DF-21D
  - DF-26
  - Shahed
  - China
  - Iran
---

# Kill Chain Comparison

> [!abstract] Quick Summary
> Compares the kill chain architectures of Western forces, China, and Iran — highlighting how each relies on space differently and where vulnerabilities and asymmetries exist. Understanding adversary kill chains is the starting point for identifying where to apply counterspace and EW effects defensively.
> [!info] 🇺🇸 Western Kill Chain
> **FIND** (SIGINT sats · ISR · GMTI) → **FIX** (NGA imagery · GPS geoloc) → **TRACK** (SATCOM relay · Link 16) → **TARGET/ENGAGE** (GPS-guided munitions) → **ASSESS** (satellite BDA)

> [!warning] 🇨🇳 Chinese Kill Chain — ASBM vs Carrier Strike Group
> **FIND** (Yaogan SIGINT/EO · OTH radar) → **FIX** (electronic geoloc · SAR imagery) → **TRACK** (BeiDou datalink · Tianlian relay) → **TARGET/ENGAGE** (DF-21D/DF-26 · manoeuvring RV) → **ASSESS** (satellite imagery)
> *Potentially closes in under 30 min · uses entirely non-Western PNT and ISR infrastructure*

> [!note] 🇮🇷 Iranian Kill Chain
> **FIND** (drone ISR · SIGINT · proxy reporting) → **FIX** (approx coordinates) → **TRACK** (limited — static targets preferred) → **ENGAGE** (Shahed · ballistic missiles · GLONASS guidance) → **ASSESS** (limited BDA)

## Western (Tomahawk vs Land Target)

```
Satellite imagery → GPS coordinates → SATCOM relay
  → GPS + TERCOM + DSMAC guidance → Satellite BDA
```

Depends on: [[GPS]], [[SATCOM Architecture|WGS SATCOM]], NGA imagery

## China (DF-21D/DF-26 vs Carrier Strike Group)

```
Yaogan ELINT (TDOA detect ship radar)
  → Yaogan SAR / Gaofen optical (fix)
    → ELINT/ISR updates (track)
      → BeiDou coordinates (target)
        → BeiDou mid-course + manoeuvring warhead (engage)
          → SAR/optical BDA
```

- Potentially closes in **under 30 minutes** from ELINT detection to impact
- Uses **non-Western infrastructure** ([[BeiDou B3A and SMC|BeiDou]]/Yaogan/Gaofen)

> **Key difference**: Western GPS denial has **zero effect** on China's kill chain.

## Iran (Shahed)

```
Chinese satellite ISR (find)
  → BeiDou SMC coordinates (fix/retarget)
    → BeiDou B3A + Kometa-M CRPA + INS + 4G/Starlink (engage)
```

See [[Shahed Navigation Case Study]] for detailed analysis.

## Kill Chain Time Evolution

| Era | Time |
| --- | --- |
| Desert Storm | Days |
| Iraq 2003 | Hours |
| Current (Link 16/CEC) | Minutes |
| Future (JADC2/SDA) | Seconds |

> [!tip] Hot Tip
> China's kill chain (particularly for anti-ship ballistic missiles targeting carrier groups) depends heavily on space-based ISR (Yaogan SIGINT/EO) and over-the-horizon radar for initial targeting. Disrupting their space-based find/fix capability is a legitimate defensive option, not just an offensive one.

---

> [!warning]- Constraints, Limitations and Assumptions
> **Constraints:** Kill chain assessments for China and Iran are based on open-source analysis and assessed capabilities — actual employment doctrine and integration may differ.
>
> **Limitations:** Kill chains are theoretical constructs — real-world execution depends on training, C2 resilience, and adaptation under fire.
>
> **Assumptions:** Assumes each nation employs its kill chain as assessed — in conflict, improvisation and degradation of planned systems changes the picture significantly.

**Related:** [[Space-Based Targeting]] · [[Tomahawk Guidance]] · [[Shahed Navigation Case Study]] · [[BeiDou B3A and SMC]] · [[SIGINT Satellites by Nation]]
