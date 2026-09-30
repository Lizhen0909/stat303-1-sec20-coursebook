# NumPy Fundamentals practice kit

Follow [NumPy Fundamentals (Chapter 6)](https://lizhen0909.github.io/stat303-1-sec20-coursebook/numpy_fundamentals.html) and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/numpy_fundamentals.html#practice-activity-shapes-sales-and-search).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in Assignment B. Open `stat303-1` in VS Code and select the course environment (`stat303-1/.venv`). NumPy and pandas are required. Use this folder as the notebook working directory.

- numpy_examples.ipynb matches the current worked chapter, including conditional selection, dot products, and matrix multiplication, with saved outputs. Its coursebook links open the published textbook.
- activity06.ipynb is an unfinished student starter; complete the chapter's A–D tasks.
- data/country-capital-lat-long-population.csv is an unchanged historical course dataset from Datasets/, used only for extended capital-distance practice. It is not required for the in-class activity.

The images/ folder contains the illustrations used in numpy_examples.ipynb. Keep it beside the notebooks.

Restart the activity kernel, run all cells, save, and run `quarto render activity06.ipynb --to html`. Inspect the HTML and a copy opened outside the project folder, then submit activity06.html. The chapter is the single source of activity and grading instructions.

All sales and scores in the examples are synthetic teaching data. Coordinate-plane distances are not geographical distances in kilometers; the spherical bonus explains a more suitable model.
