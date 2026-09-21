# Pandas Fundamentals practice kit

Follow the [Pandas Fundamentals chapter](https://lizhen0909.github.io/stat303-1-sec20-coursebook/pandas_fundamentals.html) and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/pandas_fundamentals.html#practice-activity-select-transform-and-explain).

1. Extract this folder inside your existing `stat303-setup` project and select the verified project Python environment. The examples require pandas; no additional package installation is needed after the setup chapters.
2. Use `stat303-pandas-fundamentals` as the notebook's working directory. Both notebooks belong beside the lowercase `data/` folder; verify the supplied file check before starting.
3. Run `pandas_examples.ipynb` for the worked lesson. Complete your own `activity04.ipynb` for the Canvas quiz; the chapter's A–D sections are the authoritative instructions.
4. Restart the activity notebook's kernel, run all cells, and save. From this folder in the terminal, run `quarto render activity04.ipynb --to html`. Inspect the HTML and a copy opened outside the folder, then submit only `activity04.html`.

The worked notebook has saved outputs; the activity starter intentionally leaves student work unfinished. The core lesson, activity, and independent exercises work with local files and require no live API. Keep supplied data unchanged.

## Data provenance

The three files under `data/` are unchanged copies from the course repository's `Datasets/` directory: `movie_ratings.csv`, `Top 10 Albums By Year.csv`, and `STAT303-1 survey for data analysis.csv`. They are historical course datasets. Movie data contain 2,228 records and 11 columns. Only the movie file is required for the in-class activity; albums and survey responses support Extended Practice.

The small screenings, ticket-prices, numeric-text, and quarterly-sales examples are invented teaching data defined directly in the notebook. Financial differences and ratios in the movie examples are based only on recorded gross and production budget; they are not estimates of actual profit.
