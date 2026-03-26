---
title: Interactive Features Demo
classification: UNCLASSIFIED // FOUO
tags:
  - meta
  - demo
  - interactive
---

# Interactive Features Demo

> [!info] About This Note
> This note demonstrates the interactive and visual features in this vault. Features marked 🟢 **Native** work out of the box in any Obsidian install. Features marked 🔵 **Plugin** use one of the three community plugins already bundled in this vault — **Dataview**, **Spaced Repetition**, and **Charts** — which activate automatically on first open.

---

## 🟢 Mermaid Diagrams — Native

Obsidian renders [Mermaid.js](https://mermaid.js.org) diagrams natively. No plugins required.

### Flowchart — F2T2EA Kill Chain

```mermaid
flowchart LR
    F["🔍 FIND\nSIGINT sats · GMTI\nISR constellation"]
    FX["📍 FIX\nNGA imagery\nELINT TDOA · GPS"]
    T["👁️ TRACK\nSATCOM relay\nData links"]
    TG["🎯 TARGET\nGPS coordinates\nto weapon"]
    E["💥 ENGAGE\nGPS guidance\nSATCOM updates"]
    A["📊 ASSESS\nSatellite BDA\nPre-impact imaging"]

    F --> FX --> T --> TG --> E --> A

    style F fill:#1a3a5c,color:#fff,stroke:#4a7ab5
    style FX fill:#1a3a5c,color:#fff,stroke:#4a7ab5
    style T fill:#1a3a5c,color:#fff,stroke:#4a7ab5
    style TG fill:#7a3a00,color:#fff,stroke:#c06000
    style E fill:#7a1a1a,color:#fff,stroke:#c03030
    style A fill:#1a5c1a,color:#fff,stroke:#3a9a3a
```

> [!tip] Every coloured node in the kill chain has a dedicated note. Click through to [[Space-Based Targeting]], [[GMTI and AMTI]], or [[GPS]].

---

### Graph — USSF Command Structure

```mermaid
graph TD
    CSO["🌟 Chief of Space Operations\nGen Saltzman"]

    CSO --> CFC["⚔️ Combat Forces Command\nCFC — Peterson SFB"]
    CSO --> SSC["🛰️ Space Systems Command\nSSC — LA AFB"]
    CSO --> STAR["🎓 STARCOM\nPeterson SFB"]
    CSO --> S4S["🔗 US Space Forces-Space\nS4S — Vandenberg SFB"]

    S4S -.->|"USSF component to"| USC["🌐 USSPACECOM\nCombatant Command"]

    CFC --> D2["Delta 2 · SDA"]
    CFC --> D3["Delta 3 · EW"]
    CFC --> D4["Delta 4 · Missile Warning"]
    CFC --> D8["Delta 8 · SATCOM"]
    CFC --> D9["Delta 9 · Orbital Warfare"]

    USC --> CSpOC["CSpOC\nCombined Space Ops Centre"]
    CSpOC --> AUS["🇦🇺 AUSSpOC\n(ADF embed)"]

    style CSO fill:#1a3a5c,color:#fff
    style S4S fill:#3a1a5c,color:#fff
    style USC fill:#5c1a1a,color:#fff
    style CSpOC fill:#5c1a1a,color:#fff
    style AUS fill:#1a5c1a,color:#fff
```

---

### Mind Map — Counterspace Threat Taxonomy

```mermaid
mindmap
  root((Counterspace\nThreats))
    Kinetic
      DA-ASAT missiles
      Creates debris fields
      China · Russia · India · US
    Non-Kinetic
      Directed energy
      Laser dazzle / blind
      HPM electronics damage
    Electronic Warfare
      Uplink jamming
      Downlink jamming
      GPS spoofing
    Cyber
      Ground station attacks
      Command injection
      Data manipulation
    Co-orbital RPO
      Intelligence collection
      Pre-positioning
      Latent attack capability
```

---

### Timeline — SDA Architecture Evolution

```mermaid
timeline
    title Space Domain Awareness: Key Milestones
    2021 : Russia destroys Cosmos 1408
         : 1,500+ fragments created
    2023 : Silent Barker constellation launched
         : GSSAP fleet expanded to 6 satellites
         : First SDA Tranche 0 Link 16 relay from space
    2025 : ATLAS declared operationally accepted (Sep)
         : SDA Tranche 1 first batches launched (Sep/Oct)
         : Tranche 3 $3.5B contract awarded (Dec)
    2026 : 10 Tranche 1 launches planned
         : Kronos C2 contracts expected (Apr)
         : Predictive SDA AI/ML declared S4S priority
    2029 : Tranche 2 initial launches expected
```

---

## 🟢 Collapsible Callouts — Native

Add a `-` after the callout type to make it **collapsed by default**. A `+` forces it open. This is useful for CLAs or supplementary detail you don't want to show every reader immediately.

> [!warning]- Constraints, Limitations and Assumptions *(click to expand)*
> **Constraints:** Mermaid diagrams render in Obsidian's Preview/Reading mode — they appear as raw code in source/editing mode.
>
> **Limitations:** Complex diagrams with many nodes can become slow to render. Mermaid's timeline diagram type requires Obsidian v1.4+.
>
> **Assumptions:** Assumes Obsidian is up to date — older versions may not support all Mermaid diagram types shown here.

> [!example]- Example: Collapsible Hot Tip *(click to expand)*
> This tip is hidden by default — useful when you want to preserve the "think before you peek" discipline for self-study. The `-` suffix collapses it; a `+` suffix forces it open even if the user has previously closed it.

---

## 🟢 Self-Test Checkboxes — Native

Obsidian renders interactive checkboxes. These persist their state — checking one actually saves to the file.

### Knowledge Check: Space Fundamentals

Complete these without looking at your notes:

- [ ] Name the three unique military advantages of space
- [ ] What is the Kármán line altitude?
- [ ] What does USSF stand for, and when was it established?
- [ ] Name the four USSF Field Commands and their HQ locations
- [ ] What is the difference between USSF and USSPACECOM?
- [ ] What are the five counterspace threat categories?
- [ ] Why does WGS have a critical SATCOM vulnerability?
- [ ] What GNSS signal does the Shahed-136 use — and why does that matter?

> [!tip]- Answers *(click to reveal)*
> 1. Persistence, Global Reach, Speed
> 2. 100 km (Kármán line)
> 3. United States Space Force, established 20 December 2019
> 4. CFC (Peterson), SSC (LA AFB), STARCOM (Peterson), S4S (Vandenberg)
> 5. USSF organises/trains/equips; USSPACECOM employs forces operationally
> 6. Kinetic DA-ASAT, Directed Energy, Electronic Warfare, Cyber, Co-orbital RPO
> 7. WGS has no anti-jam protection — it is the most exploitable SATCOM vulnerability
> 8. GLONASS — GPS jamming has zero effect on GLONASS-guided munitions

---

## 🟢 Note Transclusion — Native

Obsidian can embed (transclude) any note or section inline using `![[Note]]`. This means you can build a "dashboard" that pulls live content from multiple notes without duplicating it.

**Example** — the quick reference table from [[Key Systems Quick Reference]] can be embedded anywhere:
```
![[Key Systems Quick Reference]]
```
*(Remove the backticks and the table renders live inline.)*

You can also embed specific headings:
```
![[SATCOM Architecture#WGS (Wideband Global SATCOM)]]
```

---

## 🔵 Dataview — Study Dashboard

> [!info] Requires Plugin
> Install **Dataview** via Obsidian Settings → Community Plugins → Browse → search "Dataview". Free and open source.

Once installed, queries like this generate **live, dynamic tables** from your note frontmatter:

### All Foundational Notes
````
```dataview
TABLE prerequisites, tags
FROM "" WHERE difficulty = "Foundational"
SORT file.name ASC
```
````

### All Advanced Notes (sorted by section)
````
```dataview
TABLE difficulty, prerequisites
FROM "" WHERE difficulty = "Advanced"
SORT section ASC
```
````

### Notes by Tag
````
```dataview
TABLE file.name AS "Note", difficulty
FROM #counterspace OR #SDA
SORT difficulty ASC
```
````

### Reading Progress Tracker
````
```dataview
TASK FROM ""
WHERE !completed
GROUP BY file.link
```
````
*(This lists all unchecked checkboxes grouped by note — turns your self-test checklists into a live progress tracker.)*

---

## 🔵 Spaced Repetition Flashcards

> [!info] Requires Plugin
> Install **Obsidian Spaced Repetition** (by st3v3nmw) via Community Plugins.

Any note can contain flashcards using `::` (inline) or `?` (block) syntax. These integrate with a spaced repetition algorithm for active recall training.

**Inline cards** (term :: definition):
```
DA-ASAT :: Direct-Ascent Anti-Satellite missile — physically destroys a satellite, creating debris
MUOS :: Mobile User Objective System — 5 GEO satellites, 3G-like UHF SATCOM, AUS hosts one of four ground stations
CSpOC :: Combined Space Operations Centre — the coalition watch floor at Vandenberg SFB
F2T2EA :: Find, Fix, Track, Target, Engage, Assess — the kill chain framework
```

**Block cards** (question on one line, `?` separator, answer below):
```
What makes WGS critically vulnerable?
?
WGS has no anti-jam protection — it operates in unprotected X/Ka band. A threat actor with a
directional jammer and knowledge of the satellite's location can deny it without any space capability.
```

---

## 🔵 Charts

> [!info] Requires Plugin
> Install **Obsidian Charts** via Community Plugins.

Renders inline bar, line, pie, and radar charts from YAML data blocks. Example use: threat actor capability radar chart, orbital debris growth over time, satellite count by constellation.

```chart
type: radar
labels: [Kinetic ASAT, Directed Energy, EW/Jamming, Cyber, Co-orbital RPO]
series:
  - title: China
    data: [5, 4, 4, 5, 5]
  - title: Russia
    data: [5, 3, 5, 4, 4]
  - title: Iran
    data: [2, 1, 4, 3, 1]
width: 60%
```
*(Requires Charts plugin to render — appears as a radar chart comparing counterspace capability by domain.)*

---

## What's Already Implemented in This Vault

| Feature | Where |
|---|---|
| Mermaid F2T2EA flowchart | [[Space-Based Targeting]] |
| Mermaid USSF org chart | [[USSF Organisation]] |
| Collapsible CLAs | All content notes (change `[!warning]` to `[!warning]-`) |
| Self-test checkboxes | This note — copy the format to any topic note |
| Dataview dashboard | [[Study Dashboard]] |

---

**Related:** [[Space Operations Reference — Map of Content]] · [[Study Dashboard]] · [[Key Systems Quick Reference]]
