# Combining Datasets practice kit

Follow [Combining Datasets (Chapter 14)](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data%20wrangling.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Data%20wrangling.html#practice-activity-stack-match-and-check).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in
Assignment B. Open `stat303-1` in VS Code and select the course environment
(`stat303-1/.venv`). NumPy, pandas, matplotlib, and seaborn are required; nothing new is
needed for this chapter. Use this folder as the notebook working directory, because the
notebooks read their data with relative paths such as `"data/gdp_lifeExpec_Asia.csv"`.

- combining_datasets_examples.ipynb is the chapter's worked examples with every output saved, in chapter order. Its links open the published textbook.
- activity14.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its setup cell reads the five continent files into a dictionary, `pieces`, and loads `capitals`.
- data/gdp_lifeExpec_*.csv are the Gapminder data (life expectancy, population, and GDP per capita every five years from 1952 to 2007) split into one file per continent, without a continent column.
- data/country-capital-lat-long-population.csv lists 234 countries and territories with their capital cities, coordinates, and capital populations. Country names are written differently from the Gapminder files, which Part B explores.

The saved outputs came from pandas 3.0.5, NumPy 2.5.3, matplotlib 3.11.2, and seaborn
0.13.2.

Restart the activity kernel, run all cells, save, and run
`quarto render activity14.ipynb --to html`. Inspect the HTML and a copy opened outside
the project folder, then submit activity14.html to the Combining Datasets Canvas quiz.
The chapter is the single source of activity and grading instructions.
