# Data Visualization I practice kit

Follow [Data Visualization I: Choosing and Drawing a Single Plot](https://lizhen0909.github.io/stat303-1-sec20-coursebook/data_viz_1.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/data_viz_1.html#practice-activity-choose-draw-and-defend-a-plot).

Extract this folder inside `stat303-1/chapters/`, the course folder you built in
Assignment B. Open `stat303-1` in VS Code and select the course environment
(`stat303-1/.venv`). pandas, matplotlib, and seaborn are required. Use this folder
as the notebook working directory.

- data_viz_1_examples.ipynb is the chapter's worked examples with every plot saved, in chapter order. Its links open the published textbook rather than neighbouring chapter files.
- activity08.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its setup cell imports the three libraries and loads the penguins data, so there is nothing else to prepare.

**No data files ship with this kit, and none are needed.** Every plot uses the Palmer
penguins dataset that comes with seaborn: `sns.load_dataset("penguins")` returns it as a
DataFrame. The first call downloads the file and caches it under your user account, so
the first run needs a network connection and later runs do not. If you prefer to work
from a file you control, save the same table as `penguins.csv` beside the notebook and
read it with `pd.read_csv("penguins.csv")` — the chapter points this out where the data
is loaded, and nothing after that line changes.

If an import fails, check the selected notebook kernel first, then install the packages
into the project environment:

```bash
python -m pip install pandas matplotlib seaborn
```

The saved outputs came from pandas 3.0.5, matplotlib 3.11.2, and seaborn 0.13.2. Plots
drawn by a different seaborn version may differ slightly in styling — colours, fonts, and
default figure size — without changing what the picture says.

The penguin measurements are real observations from Palmer Station, Antarctica, published
by Gorman, Williams, and Fraser (2014); the year-by-year counts in the line-plot section
are invented teaching data.

Restart the activity kernel, run all cells, save, and run
`quarto render activity08.ipynb --to html`. Inspect the HTML and a copy opened outside
the project folder, confirming that every plot appears, then submit activity08.html to
the Data Visualization I Canvas quiz. The chapter is the single source of activity and
grading instructions.
