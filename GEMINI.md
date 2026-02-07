# Project S.C.O.P.E. (Science Classroom Observation & Performance Engine)

## 1. Project Overview
- **Goal:** Integrate and automate the workflow for middle school science teachers: [Material Creation -> Real-time Observation -> Assessment -> Record Entry].
- **Philosophy:** **Single Source of Truth (SSoT)**. A single Markdown file generates slides, worksheets, item banks, and evaluation systems.
- **Target:** Minimize administrative burden, maximize student interaction.

## 2. 🧠 Memory & Work Rules
- **Code-First Analysis:** Always check `components/` for Vue logic and `src/` for Python scripts before suggesting changes.
- **Sli.dev Convention:** Adhere to Sli.dev's Markdown structure and UnoCSS/Tailwind styling.
- **Sequential Logging:** Record every architectural decision, component addition, and roadmap progress in `DEV_LOG.md`.
- **Korean School Context:** Naturally use terms like '수행평가' (Performance Assessment), '지필평가' (Paper-and-pencil Test), '생기부' (School Records), and '나이스' (NEIS).
- **Design Consistency:** Follow the Emerald theme and Slate text color scheme.

## 3. Tech Stack
- **Presentation:** [Sli.dev](https://sli.dev/) (Markdown + Vue.js + UnoCSS/Tailwind)
- **Data Management:** Markdown Frontmatter + JSON/YAML
- **Automation:** Python (Pandoc, Jinja2)
- **UI/UX:** Vue 3 components, Tailwind CSS (Palette: Emerald, Slate, Amber, Blue)

## 4. Markdown Conventions & S.C.O.P.E. Engine
- **Workflow:** `YAML Data` -> `generate_lesson.py` -> `Markdown Slide` + `Exam HTML` + `PPTX`
- **Layouts:** Use standard layouts (`default`, `image-right`, `two-cols`).
- **Custom Components:**
  - `<VideoSegmentPlayer />`: Interactive YouTube segments.
  - `<LabCard />`: Step-by-step experiment visualization.
- **Quiz Tagging:**
  ```markdown
  ::: quiz {id: "m-01", type: "multiple-choice", difficulty: "mid"}
  Question...
  - [ ] Choice 1
  - [x] Correct Answer
  :::
  ```

## 5. Roadmap
- **Phase 1:** Optimization of lesson tools (Legacy HTML to Sli.dev Vue). [Completed: Mitosis, Meiosis, Mendel]
- **Phase 2:** Digitization of Assessment Plans (Metadata conversion). [Completed: Quiz Extractor & Exam Generator]
- **Phase 3:** Interactive Observation App (Real-time checklist UI).
- **Phase 4:** Automatic Report Generation (Jinja2 templates for School Records).
