# SpaceOpsVault

---

## Overview

SpaceOpsVault is a structured [Obsidian](https://obsidian.md) knowledge vault covering the full spectrum of military space operations — from orbital mechanics and satellite capabilities through to counterspace threats, tactical data links, and coalition frameworks. 

---

## Contents

| Section | Topics |
|---|---|
| `00-Home` | Map of Content, Study Dashboard, Flashcards, Interactive Features Demo |
| `01-Introduction` | Space as a military domain, the contested domain concept |
| `02-Orbital-Mechanics` | LEO/MEO/GEO regimes, RPO, orbital physics |
| `03-Satellite-Capabilities` | SATCOM (WGS, AEHF, MUOS, MILNET), GPS, missile warning |
| `04-USSF-Organisation` | USSF structure, USSPACECOM, ADF Space C2 |
| `05-Space-Doctrine` | JP 3-14, Spacepower 2020, Space Warfighting Framework |
| `06-Space-Domain-Awareness` | ATLAS, Space Fence, GSSAP, Silent Barker, SST Exmouth |
| `07-Counterspace-Threats` | DA-ASAT, directed energy, EW, cyber, RPO — China/Russia/US |
| `08-Coalition-Operations` | Operation Olympic Defender, Australia's space contribution |
| `09-GNSS` | GPS, GLONASS, BeiDou, Galileo — signals and vulnerabilities |
| `10-Operational-GNSS` | GNSS in contested environments, CRPA, Shahed case study |
| `11-RF-Spectrum` | Spectrum reference, satellite jamming techniques |
| `12-Radar-EW-EMSO` | EW fundamentals, ADF EW platforms, EMSO framework |
| `13-SIGINT-ELINT` | SIGINT disciplines, Five Eyes, ADF SIGINT platforms |
| `14-Space-Based-Targeting` | F2T2EA kill chain, GMTI/AMTI, Tomahawk, kill chain comparison |
| `15-Data-Links` | Link 16, Link 22, MADL, CEC/NIFC-CA, JREAP, SDA Transport Layer |
| `99-Reference` | Acronyms, quick reference tables, sources, 2026 developments |
| `Templates` | Standardised note template |

**65 notes** · **10 Mermaid diagrams** · **60+ flashcards** · **4 knowledge check self-tests**

---

## Features

### Native (no plugins required)
- **Mermaid diagrams** — org charts, kill chain flowcharts, orbital regime maps, SDA sensor networks, GNSS constellation comparison, data link taxonomy, and more
- **Collapsible CLA blocks** — every note has a Constraints, Limitations and Assumptions callout (collapsed by default)
- **Hot tips** — operationally specific insights embedded in each note
- **Difficulty ratings** — 🟢 Foundational · 🟡 Intermediate · 🔴 Advanced on every note and the home page
- **Self-test knowledge checks** with hidden answers on foundational topics
- **Learning trail** — structured 5-step onboarding path on the home page

### Bundled Plugins (activate on first open)
| Plugin | Purpose |
|---|---|
| [Dataview](https://github.com/blacksmithgu/obsidian-dataview) v0.5.68 | Study Dashboard — live tables of notes by difficulty, tag, and open tasks |
| [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) v1.13.9 | 60+ flashcards with SRS scheduling across all topic areas |
| [Obsidian Charts](https://github.com/phibr0/obsidian-charts) v3.9.0 | Radar chart comparing adversary counterspace capabilities |

---

## Getting Started

1. Install [Obsidian](https://obsidian.md) (free)
2. Clone or download this repo
3. Open Obsidian → **Open folder as vault** → select the `SpaceOpsVault` folder
4. When prompted, click **Trust author and enable plugins**
5. Open `00-Home/Space Operations Reference — Map of Content` and follow the learning trail

**New to space operations?** Follow the 5-step path on the home page before diving into specialist sections.

---

## Suggested Reading Order

| Step | Notes |
|---|---|
| 1 | Introduction to Space → Orbital Mechanics → Military Satellite Capabilities Overview |
| 2 | USSF Organisation → USSPACECOM → ADF Space C2 |
| 3 | Space Domain Awareness → Counterspace Threats Overview |
| 4 | SATCOM Architecture → GPS → Link 16 |
| 5 | Specialist sections by role/interest |

---

## Contributing

When adding new notes, follow the template in `Templates/Note Template.md`:
- Add `difficulty:` and `prerequisites:` to frontmatter
- Include a `> [!abstract] Quick Summary` callout after the heading
- Add at least one `> [!tip] Hot Tip` in a relevant section
- Add a `> [!warning]- Constraints, Limitations and Assumptions` block before the `**Related:**` line
- Update the Map of Content (`00-Home/Space Operations Reference — Map of Content.md`)

---

## Contributors

- **Gemini CLI** — Content modernization, technical updates, and vault maintenance (2026).
- **Claude Code** — Initial vault architecture, plugin configuration, and core content development.
