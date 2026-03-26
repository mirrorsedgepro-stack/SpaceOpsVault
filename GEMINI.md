# GEMINI.md

## Project Overview

**SpaceOpsVault** is an Obsidian-based knowledge management system serving as a military space operations reference primer. It is specifically tailored for Australian Defence Force (ADF) personnel engaging with the United States Space Force (USSF). The content is formatted as interlinked Markdown notes, current as of March 2026, and is classified as **UNCLASSIFIED // FOR OFFICIAL USE ONLY**.

The vault is structured to provide a logical learning progression, from foundational concepts (Orbital Mechanics, Introduction to Space) to advanced operational topics (Counterspace Threats, Electronic Warfare, SIGINT, and Tactical Data Links).

## Directory Structure

The vault uses a numbered directory system to enforce a logical sequence of topics:

| Directory | Description |
| :--- | :--- |
| `00-Home` | Master index (Map of Content), Study Dashboard, and feature demos. |
| `01` - `02` | **Foundations**: Introduction to the domain and Orbital Mechanics. |
| `03` | **Satellite Capabilities**: SATCOM, GPS, and Missile Warning systems. |
| `04` - `05` | **Organisation & Doctrine**: USSF/ADF structure and space power doctrine. |
| `06` | **Space Domain Awareness**: Key sensors and C2 platforms (ATLAS, Space Fence). |
| `07` | **Counterspace Threats**: Adversary capabilities (China, Russia) and EW systems. |
| `08` | **Coalition Operations**: International frameworks like Operation Olympic Defender. |
| `09` - `10` | **GNSS**: Detailed look at GPS, BeiDou, and operational anti-jamming. |
| `11` - `13` | **RF & Intelligence**: Spectrum management, Jamming, Radar, and SIGINT/ELINT. |
| `14` - `15` | **Tactical Employment**: Space-based targeting and Tactical Data Links (Link 16/22, MADL). |
| `99-Reference` | Acronyms, quick-reference tables, and source lists. |
| `Templates` | Standardized layouts for new notes. |
| `gem` | Supporting scripts for vault maintenance (e.g., `build_vault.py`). |

## Key Files

- **`00-Home/Space Operations Reference — Map of Content.md`**: The primary entry point and comprehensive index for the entire vault.
- **`CLAUDE.md`**: Contains specific instructions and context for AI assistants operating within this workspace.
- **`Templates/Note Template.md`**: The mandatory template for all new knowledge entries.
- **`99-Reference/Acronym Reference.md`**: Central repository for all domain-specific terminology.

## Usage & Conventions

### Note Standards
- **Frontmatter**: Every note must contain a YAML block with `title`, `classification` (default: `UNCLASSIFIED // FOUO`), and relevant `tags`.
- **Linking**: Use Obsidian's `[[WikiLink]]` syntax for all internal cross-references. This is critical for maintaining the knowledge graph.
- **Style**: Use Callouts (e.g., `> [!info]`, `> [!warning]`) for highlights, tips, and critical warnings.
- **Acronyms**: New acronyms should be added to the `Acronym Reference.md` in the `99-Reference` directory.

### Automation
- The `gem/` directory contains `build_vault.py`. While the vault is primarily a content project, this script is used for structural management or initial setup.
- The vault is designed to be used with Obsidian plugins such as **Dataview** (for the Study Dashboard) and **Mermaid** (for diagrams).

### Classification Warning
All content is **UNCLASSIFIED // FOR OFFICIAL USE ONLY**. Ensure any additions or modifications adhere to these distribution guidelines and do not include higher-classified material.
