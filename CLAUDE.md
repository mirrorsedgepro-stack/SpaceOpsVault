# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Vault Is

**SpaceOpsVault** is an Obsidian knowledge vault — a collection of interlinked Markdown notes serving as a military space operations reference primer for ADF personnel engaging with the USSF. All content is **UNCLASSIFIED // FOR OFFICIAL USE ONLY**, current as of March 2026.

This is a pure content vault with no build system, tests, or scripts.

## Note Format

All notes follow a standard structure defined in `Templates/Note Template.md`:

```markdown
---
title: <Note Title>
classification: UNCLASSIFIED // FOUO
tags:
  - <relevant-tags>
aliases:
  - <alternate names>
---

# Title

## Overview

## Key Points

---

**Related:** [[Link1]], [[Link2]]
```

- Internal links use Obsidian wiki-link syntax: `[[Note Title]]`
- The home/index is `00-Home/Space Operations Reference — Map of Content.md`

## Directory Structure

Directories are numbered to enforce topic sequencing (foundational → advanced):

| Dir | Topic |
|-----|-------|
| `00-Home` | Master index (Map of Content) |
| `01-Introduction` | Space as a military domain |
| `02-Orbital-Mechanics` | LEO/MEO/GEO, RPO concepts |
| `03-Satellite-Capabilities` | SATCOM, GPS, missile warning, ADF systems |
| `04-USSF-Organisation` | USSF structure, USSPACECOM, ADF Space C2 |
| `05-Space-Doctrine` | JP 3-14, Spacepower 2020 |
| `06-Space-Domain-Awareness` | ATLAS, Space Fence, GSSAP, Silent Barker, 18th SDS, SST |
| `07-Counterspace-Threats` | Threat overview, China/Russia/US profiles, Russian EW |
| `08-Coalition-Operations` | Coalition space ops, Op Olympic Defender, ADF contribution |
| `09-GNSS` | GPS/GLONASS/BeiDou/Galileo constellations |
| `10-Operational-GNSS` | GNSS employment, CRPA antennas, Shahed case study |
| `11-RF-Spectrum` | Spectrum reference, satellite jamming |
| `12-Radar-EW-EMSO` | EW fundamentals, ADF EW platforms, EMSO framework |
| `13-SIGINT-ELINT` | SIGINT overview, Five Eyes, satellite reconnaissance |
| `14-Space-Based-Targeting` | Space-based targeting, GMTI/AMTI, kill chain |
| `15-Data-Links` | Link 16, Link 22, MADL, CEC/NIFC-CA, JREAP, PWSA |
| `99-Reference` | Acronyms, quick-reference tables, sources, current developments |
| `Templates` | Note template |

## Obsidian Configuration

`.obsidian/graph.json` defines 13 color groups for the knowledge graph, mapped to each directory. When adding a new directory, add a corresponding color group entry.

`.obsidian/app.json` enables line numbers and readable line length; preview mode is the default view.

## Conventions

- Every note should start with the YAML frontmatter block including `classification: UNCLASSIFIED // FOUO`
- Use `[[WikiLinks]]` for all cross-references between notes — this is what populates Obsidian's graph view
- The `99-Reference` directory contains the acronym list (`Acronym Reference.md`) — add new acronyms there when introducing them
- The `00-Home` Map of Content should be updated when adding new notes to reflect the new entry under the relevant section
