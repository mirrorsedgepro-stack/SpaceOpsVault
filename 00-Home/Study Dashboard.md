---
title: Study Dashboard
classification: UNCLASSIFIED // FOUO
tags:
  - meta
  - dashboard
  - study
---

# Study Dashboard

> [!info] Requires Dataview Plugin
> The tables below generate dynamically from note frontmatter — they update automatically as notes are added or changed.

---

## 🟢 Start Here — Foundational Notes

```dataview
TABLE
  join(prerequisites, ", ") AS "Read First",
  join(tags, " · ") AS "Tags"
FROM ""
WHERE difficulty = "Foundational" AND file.name != "Study Dashboard"
SORT file.name ASC
```

---

## 🟡 Intermediate Notes

```dataview
TABLE
  join(prerequisites, ", ") AS "Prerequisites",
  join(tags, " · ") AS "Tags"
FROM ""
WHERE difficulty = "Intermediate" AND file.name != "Study Dashboard"
SORT section ASC
```

---

## 🔴 Advanced Notes

```dataview
TABLE
  join(prerequisites, ", ") AS "Prerequisites",
  join(tags, " · ") AS "Tags"
FROM ""
WHERE difficulty = "Advanced" AND file.name != "Study Dashboard"
SORT section ASC
```

---

## Browse by Topic

### Counterspace & Threats

```dataview
TABLE difficulty, join(prerequisites, ", ") AS "Prerequisites"
FROM #counterspace OR #ASAT OR #threats
SORT difficulty ASC
```

### Space Domain Awareness

```dataview
TABLE difficulty, join(prerequisites, ", ") AS "Prerequisites"
FROM #SDA OR #space-catalogue
SORT difficulty ASC
```

### Navigation & GNSS

```dataview
TABLE difficulty, join(prerequisites, ", ") AS "Prerequisites"
FROM #GNSS OR #GPS
SORT difficulty ASC
```

### Data Links & Comms

```dataview
TABLE difficulty, join(prerequisites, ", ") AS "Prerequisites"
FROM #data-link OR #SATCOM OR #Link-16
SORT difficulty ASC
```

### ADF-Specific

```dataview
TABLE difficulty, join(prerequisites, ", ") AS "Prerequisites"
FROM #ADF
SORT difficulty ASC
```

---

## My Progress — Open Self-Tests

> *Tracks all unchecked checkboxes across the vault. Complete the [[Interactive Features Demo]] self-test to see this in action.*

```dataview
TASK FROM ""
WHERE !completed AND file.name != "Study Dashboard"
GROUP BY file.link
SORT file.name ASC
```

---

**Related:** [[Space Operations Reference — Map of Content]] · [[Interactive Features Demo]] · [[Acronym Reference]]
