# Data Preparation practice kit

Follow [Data Preparation (Chapter 11)](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data_preparation.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data_preparation.html#practice-activity-bin-encode-and-rescale).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in
Assignment B. Open `stat303-1` in VS Code and select the course environment
(`stat303-1/.venv`). NumPy, pandas, matplotlib, and seaborn are required; nothing new is
needed for this chapter. Use this folder as the notebook working directory, because the
notebooks read their data with the relative path `"data/College.csv"`.

- data_preparation_examples.ipynb is the chapter's worked examples with every output saved, in chapter order. Its links open the published textbook.
- activity11.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its setup cell loads the college data and marks the impossible 118% graduation rate as missing, as Data Cleaning decided.
- data/College.csv holds statistics for 777 US colleges, from *An Introduction to Statistical Learning*; its first column is the college name. It is the same file the Data Cleaning kit uses.

The saved outputs came from pandas 3.0.5, NumPy 2.5.3, matplotlib 3.11.2, and seaborn
0.13.2.

Restart the activity kernel, run all cells, save, and run
`quarto render activity11.ipynb --to html`. Inspect the HTML and a copy opened outside
the project folder, then submit activity11.html to the Data Preparation Canvas quiz. The
chapter is the single source of activity and grading instructions.
