# Data Reshaping practice kit

Follow [Data Reshaping (Chapter 13)](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data_reshaping.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data_reshaping.html#practice-activity-long-wide-and-back).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in
Assignment B. Open `stat303-1` in VS Code and select the course environment
(`stat303-1/.venv`). NumPy, pandas, matplotlib, and seaborn are required; nothing new is
needed for this chapter. Use this folder as the notebook working directory, because the
notebooks read their data with the relative path `"data/gdp_lifeExpectancy.csv"`.

- data_reshaping_examples.ipynb is the chapter's worked examples with every output saved, in chapter order. Its links open the published textbook.
- activity13.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its setup cell loads the data and builds `rainfall`, a small made-up table of monthly rainfall for four cities, used in Part C.
- data/gdp_lifeExpectancy.csv holds life expectancy, population, and GDP per capita for 142 countries every five years from 1952 to 2007 (the Gapminder data). It is the same file the Data Grouping and Aggregation kit uses.

The saved outputs came from pandas 3.0.5, NumPy 2.5.3, matplotlib 3.11.2, and seaborn
0.13.2.

Restart the activity kernel, run all cells, save, and run
`quarto render activity13.ipynb --to html`. Inspect the HTML and a copy opened outside
the project folder, then submit activity13.html to the Data Reshaping Canvas quiz. The
chapter is the single source of activity and grading instructions.
