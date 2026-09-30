# Data Visualization II practice kit

Follow [Data Visualization II: Interfaces, Subplots, and Multi-Panel Figures](https://lizhen0909.github.io/stat303-1-sec20-coursebook/data_viz_2.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/data_viz_2.html#practice-activity-build-and-defend-a-multi-panel-figure).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in
Assignment B. Open `stat303-1` in VS Code and select the course environment
(`stat303-1/.venv`). pandas, matplotlib, and seaborn are required. Use this folder
as the notebook working directory.

- data_viz_2_examples.ipynb is the chapter's worked examples with every figure saved, in chapter order. Its links open the published textbook rather than neighbouring chapter files.
- activity09.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its setup cell imports the three libraries, loads the penguins data, and defines the `numeric_cols` list that Part C loops over.

**No data files ship with this kit, and none are needed.** As in Data Visualization I,
every figure uses the Palmer penguins dataset that comes with seaborn:
`sns.load_dataset("penguins")` returns it as a DataFrame. The first call downloads the
file and caches it under your user account, so the first run needs a network connection
and later runs do not.

If an import fails, check the selected notebook kernel first, then install the packages
into the project environment:

```bash
python -m pip install pandas matplotlib seaborn
```

The saved figures came from pandas 3.0.5, matplotlib 3.11.2, and seaborn 0.13.2. A
different matplotlib or seaborn version may lay panels out slightly differently — spacing,
fonts, and default colours — without changing what the figures demonstrate.

Restart the activity kernel, run all cells, save, and run
`quarto render activity09.ipynb --to html`. Inspect the HTML and a copy opened outside
the project folder, confirming that every figure appears and nothing is cut off, then
submit activity09.html to the Data Visualization II Canvas quiz. The chapter is the
single source of activity and grading instructions.

The penguin measurements are real observations from Palmer Station, Antarctica, published
by Gorman, Williams, and Fraser (2014).
