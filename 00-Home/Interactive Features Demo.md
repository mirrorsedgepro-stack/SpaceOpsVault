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

## 🟢 Text Block Diagrams — Native

Obsidian renders callout blocks, tables, and Unicode text natively. These are fully readable in both source and preview mode, work on all platforms, and require no plugins.

### Flow — F2T2EA Kill Chain

> [!info] F2T2EA Kill Chain — Space at Every Step
> **🔍 FIND** → **📍 FIX** → **👁️ TRACK** → **🎯 TARGET** → **💥 ENGAGE** → **📊 ASSESS**
>
> ISR sats · GMTI · NGA imagery · GPS · SATCOM relay · data links · PNT to weapon · GPS guidance · satellite BDA

> [!tip] Every step in the kill chain has a dedicated note. Click through to [[Space-Based Targeting]], [[GMTI and AMTI]], or [[GPS]].

---

### Hierarchy — USSF Command Structure

> [!info] USSF Command Structure
> **🌟 Chief of Space Operations** · Gen Saltzman
> ├── **⚔️ Combat Forces Command (CFC)** · Peterson SFB
> │   ├── Delta 2 · SDA
> │   ├── Delta 3 · EW
> │   ├── Delta 4 · Missile Warning
> │   ├── Delta 8 · SATCOM
> │   └── Delta 9 · Orbital Warfare
> ├── **🛰️ Space Systems Command (SSC)** · LA AFB
> ├── **🎓 STARCOM** · Peterson SFB
> └── **🔗 US Space Forces-Space (S4S)** · Vandenberg SFB
> &nbsp;&nbsp;&nbsp;&nbsp;╌╌▶ **🌐 USSPACECOM** · Combatant Command
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── CSpOC · Combined Space Ops Centre
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── 🇦🇺 AUSSpOC (ADF embed)

---

### Taxonomy — Counterspace Threat Categories

> [!info] Counterspace Threat Taxonomy
> **Kinetic DA-ASAT**
> ↳ Direct-ascent missiles · creates persistent debris · China, Russia, India, US
>
> **Non-Kinetic / Directed Energy**
> ↳ Laser dazzle/blind sensors · HPM damages electronics · no debris
>
> **Electronic Warfare**
> ↳ Uplink jamming · downlink jamming · GPS spoofing
>
> **Cyber**
> ↳ Ground station attacks · command injection · data manipulation
>
> **Co-orbital RPO**
> ↳ Intelligence collection · pre-positioning · latent attack capability

---

### Timeline — SDA Architecture Evolution

| Year | Milestone |
|---|---|
| **2021** | Russia destroys Cosmos 1408 — 1,500+ fragments created |
| **2023** | Silent Barker constellation launched · GSSAP expanded to 6 sats · First SDA Tranche 0 Link 16 relay from space |
| **2025** | ATLAS operationally accepted (Sep) · SDA Tranche 1 first batches launched (Sep/Oct) · Tranche 3 $3.5B contract (Dec) |
| **2026** | 10 × Tranche 1 launches planned · Kronos C2 contracts expected (Apr) · Predictive SDA AI/ML declared S4S priority |
| **2029** | Tranche 2 initial launches expected |

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

> [!info] Adversary Counterspace Capability Comparison *(open-source assessment · 1–5 scale)*
>
> | Threat Domain | 🇨🇳 China | 🇷🇺 Russia | 🇮🇷 Iran |
> |---|:---:|:---:|:---:|
> | Kinetic DA-ASAT | ●●●●● | ●●●●● | ●● |
> | Directed Energy | ●●●● | ●●● | ● |
> | EW / Jamming | ●●●● | ●●●●● | ●●●● |
> | Cyber | ●●●●● | ●●●● | ●●● |
> | Co-orbital RPO | ●●●●● | ●●●● | ● |

---

## What's Already Implemented in This Vault

| Feature | Where |
|---|---|
| Text flow chain — F2T2EA kill chain | [[Space-Based Targeting]] |
| Text hierarchy — USSF org structure | [[USSF Organisation]] |
| Text hierarchy — ADF Space C2 | [[ADF Space C2]] |
| Text hierarchy — Coalition OOD network | [[Coalition Space Operations]] |
| Text tier block — SATCOM architecture | [[SATCOM Architecture]] |
| Text tier block — Orbital regime stack | [[Orbital Mechanics]] |
| Text tier block — Data link LOS/BLOS | [[Tactical Data Links Overview]] |
| Text tier block — GNSS constellations | [[GNSS Constellations]] |
| Dot-matrix capability table — counterspace | [[Counterspace Threats Overview]] |
| Multi-callout kill chain comparison | [[Kill Chain Comparison]] |
| SDA sensor network text block | [[Space Domain Awareness]] |
| Collapsible CLAs | All content notes (change `[!warning]` to `[!warning]-`) |
| Self-test checkboxes | This note — copy the format to any topic note |
| Dataview dashboard | [[Study Dashboard]] |

---

**Related:** [[Space Operations Reference — Map of Content]] · [[Study Dashboard]] · [[Key Systems Quick Reference]]
