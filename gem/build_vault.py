import os

# Define the root directory for the vault
vault_root = "Space_Operations_Reference"

# Define the folder structure and file contents
vault_files = {
    # ---------------------------------------------------------
    # 01. TEMPLATES
    # ---------------------------------------------------------
    "01_Templates/Intelligence_Note_Template.md": r"""---
aliases: []
tags: []
system_type: 
status: 
vulnerability: 
---
# {{title}}

### Executive Summary
*(Brief overview of the system, threat, or concept)*

### Technical Specifications
* **Key Detail 1:**
* **Key Detail 2:**

### Strategic Implications
*(How this impacts allied operations or vulnerabilities)*

---
*Related:* [[Space_Operations_MOC]]
""",

    # ---------------------------------------------------------
    # 00. MOCs and DASHBOARDS
    # ---------------------------------------------------------
    "00_MOCs/Space_Operations_MOC.md": r"""---
aliases: [Master Index, Home]
tags: [MOC]
---
# Space Operations Reference MOC
**UNCLASSIFIED // FOR OFFICIAL USE ONLY | Refreshed March 2026**

Welcome to the Space Operations Reference Vault. This knowledge base covers space domain awareness, military satellite systems, counterspace threats, GNSS, electronic warfare, SIGINT, and tactical data links. It is prepared as a reference primer for ADF personnel engaging with the United States Space Force.

## 🌌 10. Fundamentals
* [[100_Introduction_to_Space]]
* [[200_Orbital_Mechanics]]
* [[1000_RF_Spectrum]]

## 🛰️ 20. Capabilities
* [[300_Military_Satellite_Capabilities]]
* [[600_Space_Domain_Awareness]]
* [[900_GNSS_and_Navigation]]
* [[1400_Tactical_Data_Links]]
* [[1300_Space_Based_Targeting]]

## ⚠️ 30. Threats & Electronic Warfare
* [[700_Counterspace_Threats]]
* [[1100_Radar_EW_and_EMSO]]
* [[1200_SIGINT_and_ELINT]]

## 🏛️ 40. Organization & Doctrine
* [[400_USSF_and_ADF_Organisation]]
* [[500_Space_Doctrine]]
* [[800_Coalition_Space_Operations]]

## 📚 99. Reference
* [[Acronym_Reference]]
""",

    "00_MOCs/Command_Dashboard.md": r"""---
aliases: [Dashboard]
tags: [dashboard]
---
# 🌐 Space Operations Command Dashboard
*Welcome to the automated intelligence hub. This page updates in real-time as you add or modify notes in the vault.*

---

### ⚠️ Active Threat Intelligence
*Automatically lists all notes tagged with `#threats` or `#EW`, sorted by the most recently updated.*

```dataview
TABLE 
    file.mtime AS "Last Updated",
    file.folder AS "Category"
FROM #threats OR #EW
SORT file.mtime DESC
LIMIT 5
