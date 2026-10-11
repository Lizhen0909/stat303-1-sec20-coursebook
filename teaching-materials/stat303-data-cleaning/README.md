# Data Cleaning practice kit

Follow [Data Cleaning (Chapter 10)](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data_cleaning.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data_cleaning.html#practice-activity-find-fill-and-defend).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in
Assignment B. Open `stat303-1` in VS Code and select the course environment
(`stat303-1/.venv`). Use this folder as the notebook working directory, because every
notebook reads its data with a relative path such as `"data/GDP_missing_data.csv"`.

This chapter needs two packages beyond pandas, NumPy, matplotlib, and seaborn. Install
them once into the course environment, from the VS Code terminal with that environment
active:

```bash
python -m pip install scikit-learn scipy
```

- data_cleaning_examples.ipynb is the chapter's worked examples with every output saved, in chapter order. Its links open the published textbook.
- activity10.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its setup cell loads the three datasets and builds the small `enrollments` table that Part C uses.
- data/GDP_missing_data.csv holds country indicators for 155 countries with values deliberately removed; data/GDP_complete_data.csv holds the same countries with those values present, so a fill can be checked against the truth.
- data/College.csv holds statistics for 777 US colleges, from *An Introduction to Statistical Learning*; its first column is the college name.

The saved outputs came from pandas 3.0.5, NumPy 2.5.3, scikit-learn 1.9.1, SciPy 1.18.1,
matplotlib 3.11.2, and seaborn 0.13.2.

Restart the activity kernel, run all cells, save, and run
`quarto render activity10.ipynb --to html`. Inspect the HTML and a copy opened outside
the project folder, then submit activity10.html to the Data Cleaning Canvas quiz. The
chapter is the single source of activity and grading instructions.
