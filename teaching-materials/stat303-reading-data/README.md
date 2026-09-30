# Reading Data practice kit

Use the [Reading Data chapter](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Reading_data.html) for the lesson and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/Reading_data.html#practice-activity-read-inspect-and-export-movie-data) for the graded task list.

## Open and run

1. Extract this folder and place it inside `stat303-1/chapters/`, the course folder you built in Assignment B. Open `stat303-1` in VS Code.
2. Select the course environment (`stat303-1/.venv`) as the notebook kernel. The core examples and activity need pandas; no NumPy knowledge or additional package installation is required.
3. Use `stat303-reading-data` as the notebook's working directory. Both notebooks belong beside the lowercase `data/` folder. Use `Path.cwd()` and the supplied file check to verify the location.
4. Run `reading_examples.ipynb` to follow the worked examples. Complete your own `activity03.ipynb` using the chapter's A–D instructions.
5. Restart, run all, and save your activity. From this folder in the terminal, run `quarto render activity03.ipynb --to html`. Inspect the result and upload only `activity03.html` to the Canvas quiz.

Keep the included `images/` folder beside `reading_examples.ipynb`. It contains the data-structure and DataFrame-versus-Series figures used in the worked examples; these figures display locally without an internet connection.

The examples write `movies_export.csv` and `movies_with_index.csv` beside the notebooks. Rerunning an export replaces that generated file; the inputs under `data/` are not modified. The activity also writes `movies_export.csv` from the same original dataset.

The HTML-reading extension is optional and needs an HTML parser such as lxml. Its code is shown in Markdown, so running all ordinary example cells does not require that parser or network access. The local JSON example uses pandas alone.

## Files Used in This Chapter

- `movie_ratings.csv`: 2,228 movie records and 11 columns used to practice importing, inspecting, summarizing, and exporting a table.
- `movie_ratings_semicolon.txt`: the same movie records with semicolon delimiters, used to diagnose and correct an import problem.
- `movies_preview.json` and `movies_preview.html`: five movie records with Title, IMDB Rating, and Production Budget, used to compare how JSON and HTML readers return tables in the optional extension.
- `Top 10 Albums By Year.csv`: used in extended practice to inspect album records, interpret quartiles, and calculate a track-weighted mean duration.
- `bestseller_books.txt`: used in extended practice to identify a delimiter, inspect extra index columns, and verify an export.

Only the two full movie files are required for the in-class activity. The example notebook includes the chapter text; the activity notebook intentionally contains unfinished student work rather than worked solutions.
