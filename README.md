# Data Science I with Python — STAT 303-1, Section 20

Free coursebook by Lizhen Shi for Northwestern University's Department of Statistics and Data Science. This edition retains the original teaching material and saved outputs while updating the setup sequence and assignments.

**Read the book:** https://lizhen0909.github.io/stat303-1-sec20-coursebook/

## Repository contents

- `_quarto.yml`, `index.qmd`, and chapter/appendix notebooks: editable book sources.
- `Datasets/`, `images/`, and referenced root-level data files: materials used in the active chapters. Geographic shapefiles include all companion files.
- `docs/`: the published HTML book and its required browser assets. GitHub Pages serves this directory from `main`.
- `references.bib`, `NU_Stat_logo.png`, and `LICENSE.txt`: bibliography, branding, and original license.

The initial `docs/` pages are copied unchanged from the original published repository. The original repository and website remain available and unchanged.

## Teaching sequence

- Assignment A reviews prerequisite Python skills.
- Chapters 1–2 cover VS Code, a Quarto refresher, project environments, packages, and paths.
- Assignment B has students build the `stat303-1` course folder (one shared `.venv`, with `chapters/` and `assignments/`) that every later kit goes into; download `downloads/assignment-b-setup.zip`. Kit sources live in `teaching-materials/`.
- Assignments C–G cover Pandas, NumPy, visualization, cleaning/preparation, and wrangling (formerly B–F).
- `downloads/setup-practice.zip` contains only the two chapter practice notebooks and their data.
- Chapters 4–5 have local practice kits: `downloads/pandas-fundamentals-practice.zip` and `downloads/numpy-fundamentals-practice.zip`. Each contains a worked notebook and an unfinished activity starter.
- Chapter practice instructions and formal assignment instructions each have one authoritative coursebook page. Instructor quiz artifacts are not public website resources.

## Update the book

1. Install [Quarto](https://quarto.org/docs/get-started/).
2. Edit the relevant notebook or `index.qmd`. If changing code results, run the relevant cells in Jupyter and save their outputs.
3. From the repository root, run:

   ```sh
   quarto render --to html
   ```

4. Review `docs/index.html` and the changed pages. Commit and push the source changes together with the updated `docs/` files. GitHub Pages republishes automatically.

Rendering preserves saved notebook outputs (`execute.enabled: false`). Some examples deliberately demonstrate errors, access live services, or refer to historical local paths; rebuilding the website does not require re-running those examples. Executing every notebook from scratch is a separate task: existing examples include `datasets`/`Datasets` case differences, Windows path separators, and files outside the repository. These teaching-source issues have not been silently rewritten during cleanup.

The old `requirements.txt` belonged to an unrelated, outdated TensorFlow environment and has been removed. Install the Python packages needed for the particular examples you wish to run. No Python package installation is needed just to read the published book.

## Provenance and license

Cleaned from [Lizhen0909/nu-stat303-1-sec20-coursebook](https://github.com/Lizhen0909/nu-stat303-1-sec20-coursebook), commit `1742b20f70d12eb90119c7ac5e97307e8cba7e1f`. The original preface acknowledges Professor Arvind Krishna's foundational materials. The original Creative Commons Attribution-ShareAlike 4.0 license is retained in `LICENSE.txt`.
