# Data Grouping and Aggregation practice kit

Follow [Data Grouping and Aggregation (Chapter 12)](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data%20aggregation.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data%20aggregation.html#practice-activity-split-summarize-and-compare).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in
Assignment B. Open `stat303-1` in VS Code and select the course environment
(`stat303-1/.venv`). NumPy, pandas, matplotlib, and seaborn are required; nothing new is
needed for this chapter. Use this folder as the notebook working directory, because the
notebooks read their data with the relative path `"data/gdp_lifeExpectancy.csv"`.

- data_aggregation_examples.ipynb is the chapter's worked examples with every output saved, in chapter order. Its links open the published textbook.
- activity12.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its setup cell loads the data and makes `gdp_1977`, the rows for 1977.
- data/gdp_lifeExpectancy.csv holds life expectancy, population, and GDP per capita for 142 countries every five years from 1952 to 2007 (the Gapminder data), with no missing values.

The saved outputs came from pandas 3.0.5, NumPy 2.5.3, matplotlib 3.11.2, and seaborn
0.13.2.

Restart the activity kernel, run all cells, save, and run
`quarto render activity12.ipynb --to html`. Inspect the HTML and a copy opened outside
the project folder, then submit activity12.html to the Data Grouping and Aggregation
Canvas quiz. The chapter is the single source of activity and grading instructions.
