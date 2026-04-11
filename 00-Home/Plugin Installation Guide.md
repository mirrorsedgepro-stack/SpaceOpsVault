---
title: Plugin Installation Guide
classification: UNCLASSIFIED // FOUO
tags:
  - meta
  - setup
  - plugins
aliases:
  - Plugin Setup
  - Install Plugins
---

# Plugin Installation Guide

> [!warning] Do This First — One-Time Setup
> Community plugins are disabled by default in Obsidian. You must turn off Restricted Mode once before any plugin links below will work.
>
> **Settings → Community Plugins → Turn off Restricted Mode**

---

## How to Install a Plugin

1. Click any **Install** link below — it opens directly in Obsidian's plugin browser
2. Click **Install**, then **Enable**
3. Repeat for each plugin
4. Return here and tick the checkbox when done

---

## Required Plugins (already used by this vault)

These three are queried by existing notes — install them first.

- [ ] [Dataview](obsidian://show-plugin?id=dataview) — powers the [[Study Dashboard]] reading lists and task tracker
- [ ] [Spaced Repetition](obsidian://show-plugin?id=obsidian-spaced-repetition) — powers the [[Flashcards]] review system
- [ ] [Charts](obsidian://show-plugin?id=obsidian-charts) — renders charts in [[Interactive Features Demo]]

---

## New Starter Workflow Plugins

These unlock the study log and calendar workflow described in [[Space Operations Reference — Map of Content]].

- [ ] [Templater](obsidian://show-plugin?id=templater-obsidian) — auto-fills note titles, dates, and difficulty fields when creating new notes; required for Study Log Template
- [ ] [Calendar](obsidian://show-plugin?id=calendar) — adds a calendar panel (right sidebar); click any date to open or create that day's study log

---

## Navigation & Organisation Plugins

- [ ] [File Tree Alternative](obsidian://show-plugin?id=file-tree-alternative) — replaces the default file explorer with a cleaner folder-first tree; better for navigating the numbered directories
- [ ] [Folder Note](obsidian://show-plugin?id=folder-note-plugin) — click a folder in the file tree to open an overview note for that topic area
- [ ] [Tag Wrangler](obsidian://show-plugin?id=tag-wrangler) — right-click any tag to rename, merge, or explore it across all notes
- [ ] [Daily Notes Viewer](obsidian://show-plugin?id=daily-notes-viewer) — browse past study logs in a scrollable timeline view

---

## Writing & Editing Plugins

- [ ] [Auto Link Title](obsidian://show-plugin?id=auto-link-title) — when you paste a URL, automatically fetches and inserts the page title as the link text
- [ ] [Natural Language Dates](obsidian://show-plugin?id=nldates-obsidian) — type `@today` or `@next monday` and it converts to a formatted date link
- [ ] [Better Word Count](obsidian://show-plugin?id=better-word-count) — shows word/character count for selected text in the status bar

---

## Appearance Plugins

- [ ] [Style Settings](obsidian://show-plugin?id=obsidian-style-settings) — exposes theme customisation options (font size, spacing, colour accents) for the Things theme
- [ ] [Typography](obsidian://show-plugin?id=typography) — improves reading typography for long-form notes

---

## File Linking Plugin

- [ ] [Better File Link](obsidian://show-plugin?id=obsidian-file-link) — attach and embed local files (PDFs, documents, images) directly in notes via command palette; powers the [[Local Document Library]] offline reference system in this vault

> [!tip] How to use Better File Link
> 1. Position your cursor where you want the file link inserted
> 2. Open the command palette (`Ctrl+P`) and run **Add file link**
> 3. Browse to your locally saved PDF or document and select it
> 4. Toggle **Embed** if you want the file to render inline rather than as a link
> 5. Use **Check for broken file links** periodically to validate all your local paths

---

## Export Plugin

- [ ] [Pandoc](obsidian://show-plugin?id=pandoc) — export notes to PDF, Word, or HTML; requires [Pandoc](https://pandoc.org/installing.html) to be installed on your machine separately

---

## Quick Install — All at Once

If you prefer to browse manually: **Settings → Community Plugins → Browse**, then search each name below.

| Plugin | ID | Purpose |
|--------|----|---------|
| Dataview | `dataview` | Dynamic tables and task lists |
| Spaced Repetition | `obsidian-spaced-repetition` | Flashcard reviews |
| Charts | `obsidian-charts` | Data visualisation |
| Templater | `templater-obsidian` | Smart note templates |
| Calendar | `calendar` | Daily study logs |
| Better File Link | `obsidian-file-link` | Link/embed local PDFs and documents |
| File Tree Alternative | `file-tree-alternative` | Better folder navigation |
| Folder Note | `folder-note-plugin` | Folder overview notes |
| Tag Wrangler | `tag-wrangler` | Tag management |
| Daily Notes Viewer | `daily-notes-viewer` | Study log timeline |
| Auto Link Title | `auto-link-title` | Auto-title pasted URLs |
| Natural Language Dates | `nldates-obsidian` | Plain-English date entry |
| Better Word Count | `better-word-count` | Selection word count |
| Style Settings | `obsidian-style-settings` | Theme customisation |
| Typography | `typography` | Reading typography |
| Pandoc | `pandoc` | Export to PDF/Word |

---

**Related:** [[Space Operations Reference — Map of Content]] · [[Study Dashboard]] · [[Interactive Features Demo]]
