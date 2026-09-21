# Pandas Intermediate practice kit

Follow [Pandas Intermediate (Chapter 5)](https://lizhen0909.github.io/stat303-1-sec20-coursebook/pandas_intermediate.html) and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/pandas_intermediate.html#practice-activity-calculate-align-and-explain).

Extract this folder inside your stat303-setup project and select its verified environment. pandas is the only analysis dependency, and no package installation beyond the setup chapters is required. Use this folder as the notebook working directory.

- pandas_intermediate_examples.ipynb is the chapter's worked lesson with saved outputs. Its links open the published textbook rather than neighbouring chapter files.
- activity05.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its supplied cell creates every input the activity needs: the `sales` table for Part A, the `quarter_sales` and `adjustments` tables whose labels drive the Part B alignment work, the `department_labels` mapping used in Part C, and the six-row `campaigns` table used in Part D.

No data files ship with this kit. All inputs are created in Python, so the notebooks read nothing from disk.

Restart the activity kernel, run all cells, save, and run `quarto render activity05.ipynb --to html`. Inspect the HTML and a copy opened outside the project folder, then submit activity05.html. The chapter is the single source of activity and grading instructions.

All products, departments, prices, quarterly figures, and advertising campaigns are synthetic teaching data. The correlation in Part D describes six invented observations and is not evidence about real advertising.
