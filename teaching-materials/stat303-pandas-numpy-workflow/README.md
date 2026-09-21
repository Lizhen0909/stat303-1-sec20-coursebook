# NumPy and pandas Workflow practice kit

Follow [NumPy and pandas in a Real Workflow](https://lizhen0909.github.io/stat303-1-sec20-coursebook/numpy_pandas_workflow.html)
and its [complete activity instructions](https://lizhen0909.github.io/stat303-1-sec20-coursebook/numpy_pandas_workflow.html#practice-activity-from-messy-file-to-labeled-report).

Extract this folder inside your stat303-setup project and select its verified
environment. NumPy and pandas are required. Use this folder as the notebook
working directory.

- workflow_examples.ipynb is the chapter's worked examples with saved outputs, stage by stage. Its links open the published textbook rather than neighbouring chapter files. Running it writes `sales_raw.csv` into this folder; that file is the chapter's own messy input, created on purpose so the notebook needs no shipped data.
- activity07.ipynb is an unfinished student starter; complete the chapter's A–D tasks. Its first cell builds every input the activity needs: it writes `inventory_raw.csv` into this folder, creates the 200,000-row `orders` table used for the Part B timings, and defines the `warehouse` table and the `unit_costs` vector used in Parts C and D.

No data files ship with this kit. Both notebooks create whatever they read.

The chapter and this kit deliberately stay within the tools of the earlier
chapters: `.to_numpy()`, `pd.to_numeric()`, `pd.to_datetime()`, `.astype()`,
Boolean masks, `np.where()`, `np.select()`, broadcasting, `axis` aggregations,
the `@` matrix product, and `%timeit`. There is no `groupby` or `pivot_table`
here, since neither has been introduced yet. Two methods the chapter uses beyond
that list — `np.sort()` in Stage 5 and `np.percentile()` in the extended
practice — are introduced where they appear, with a link to the NumPy
Fundamentals section they extend and to the official reference page.

Restart the activity kernel, run all cells, save, and run
`quarto render activity07.ipynb --to html`. Inspect the HTML and a copy opened
outside the project folder, then submit activity07.html. The chapter is the
single source of activity and grading instructions.

The saved outputs in workflow_examples.ipynb came from NumPy 2.5.3 and pandas
3.0.5. Two of them depend on that version: text columns report the `str` dtype
rather than the older `object`, and `.to_numpy()` returns a read-only view, so
the Trap 3 cell shows a failed write instead of a silent one. On an older pandas
you will see `object` and a successful write; the chapter says so where it
matters.

All stores, orders, warehouses, prices, and discount rules are synthetic
teaching data. The timing numbers saved in workflow_examples.ipynb came from one
machine; your own measurements will differ, which is the reason the chapter asks
you to measure rather than to memorize a ratio.
