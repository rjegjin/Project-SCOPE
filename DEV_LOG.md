# DEV_LOG.md - Project S.C.O.P.E.

## [2026-02-07] - Code Refactoring & Optimization
- **Action:** Reorganized project structure for better maintainability.
- **Details:**
    - Moved all Python scripts to `scripts/` directory.
    - Updated `build_all.py`, `generate_lesson.py`, `export_exam.py`, `export_ppt.py`, `quiz_extractor.py` to use **absolute paths** relative to the project root.
    - Modified `.bat` files to reference the new script locations.
    - Updated `README.md` to reflect the new structure.
- **Status:** Codebase is clean, modular, and path-safe.
