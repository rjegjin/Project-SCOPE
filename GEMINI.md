# Project S.C.O.P.E. - AI Context & Rules

## 1. Project Overview
- **Goal:** Automate science lesson material creation using a "Single Source of Truth" approach.
- **Core Engine:** `S.C.O.P.E. Engine` converts `YAML` data into `Sli.dev Slides`, `HTML Exams`, and `PPTX`.

## 2. 🧠 Memory & Work Protocol (CRITICAL)
**Gemini MUST adhere to the following workflow for every session:**

### 🚨 Rule 1: Initialization (Start)
- **Action:** At the beginning of *every* chat or task, **READ `DEV_LOG.md` FIRST**.
- **Reason:** To restore the exact context, understand the latest architectural decisions, and continue work seamlessly.

### 🚨 Rule 2: Termination (End)
- **Action:** Before finishing a task involving code changes, file creation, or structural updates, **APPEND to `DEV_LOG.md`**.
- **Format:**
  ```markdown
  ## [YYYY-MM-DD] - Task Name
  - **Action:** Summary of what was done.
  - **Details:** Specific files created, bugs fixed, or features added.
  - **Status:** Current project state and next steps.
  ```
- **Constraint:** Do not ask the user if they want to log. **Just do it.**

## 3. Architecture & Conventions
- **Engine Logic:**
  - Input: `data/*.yaml`
  - Logic: `build_all.py` (orchestrates `generate_lesson.py`, `export_exam.py`, `export_ppt.py`)
  - Output: `units/*.md`, `output/*.html`, `output/*.pptx`
- **Sli.dev:**
  - Components: Use `<VideoSegmentPlayer>` for YouTube, `<LabCard>` for experiments.
  - Styling: Tailwind CSS (Emerald/Amber theme) via `styles/index.css` and `uno.config.ts`.
- **Git:**
  - Always check `git status` before committing.
  - Commit messages should be descriptive: `feat:`, `fix:`, `docs:`, `refactor:`.

## 4. Roadmap Status
- **Phase 1 (Legacy Migration):** ✅ Complete (Mitosis, Meiosis, Mendel).
- **Phase 2 (Automation Engine):** ✅ Complete (YAML -> Multi-output).
- **Phase 3 (Expansion):** 🚧 Ready to deploy to Vercel & add more units.
