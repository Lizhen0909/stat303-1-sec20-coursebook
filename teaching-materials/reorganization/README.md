# Pandas and NumPy chapter reorganization

The book now teaches Pandas Fundamentals → Pandas Intermediate → NumPy Fundamentals → NumPy Speedup Pandas. `_quarto.yml` selects the new files.

All four original notebook files remain byte-for-byte unchanged, and `original-sha256.json` records their hashes. They live in `originals/` beside this document, each under its own original name, rather than in the repository root. Moving them there cleared the root of notebooks that were not part of the book and removed the need for the `_bk` suffix that `numpy_fundamentals.ipynb` had carried to avoid colliding with the active chapter. Verify them from the repository root with:

```bash
python3 -c "import json,hashlib,pathlib; d=pathlib.Path('teaching-materials/reorganization/originals'); [print(('MATCH' if hashlib.sha256((d/k).read_bytes()).hexdigest()==v else 'MISMATCH'), k) for k,v in json.load(open('teaching-materials/reorganization/original-sha256.json')).items()]"
```

| Original (in `originals/`) | Active notebook | Change |
|---|---|---|
| `Pandas.ipynb` | `pandas_fundamentals.ipynb` | Navigation and transition wording only |
| `data_types_in_pandas.ipynb` | `reorganization/pandas_intermediate_superseded.ipynb` | Pandas-first transformations, no NumPy dependency in core examples; retained final-project NLP resource. Superseded as the active chapter; see **Published Intermediate revision** below |
| `numpy_fundamentals.ipynb` | `numpy_fundamentals.ipynb` | Copy with updated introduction, navigation, and explicit legacy assessment naming. Same filename in both columns: the original is distinguished by living in `originals/` |
| `vectorized_numpy.ipynb` | `numpy_speedup_pandas.ipynb` | Full pandas → NumPy → pandas workflow with correctness checks and measured performance |

`Numpy.ipynb` and `pandas_numpy_workflow.ipynb` were deleted. Neither was in `_quarto.yml` and neither was a recorded original: the first was a superseded NumPy draft, and the second a near-twin of the active `numpy_pandas_workflow.ipynb` whose name differed only in word order, which made it easy to edit by mistake. Both remain in git history.

## Content destinations

- Pandas arithmetic, alignment, conditional updates, mapping, replacement, functions/lambda/apply, ranking, sorting, strings, dates, copies, correlation, and survey practice: Pandas Intermediate.
- Advanced NLP (regex, web-table example, NLTK setup, tokenization, stop words, stemming/lemmatization, sentiment, POS and named entities): retained within Pandas Intermediate as a **Final Project Resource**, analogous to geospatial plotting in visualization. The original example code and saved outputs are retained; cells are tagged `final-project-resource` to identify separate setup/execution requirements.
- Array construction, shapes, indexing, views/copies, broadcasting, reductions, reshape, concatenation, and the original NumPy activity: copied NumPy Fundamentals.
- Conversion, dtype/missing-value handling, label restoration, numerical functions, conditional arrays, matrix multiplication, and controlled benchmarks: NumPy Speedup Pandas.
- Shopping: labeled pandas example in Pandas Intermediate; full worked loop/pandas/matrix comparison and report in NumPy Speedup Pandas.
- Movies: independent matrix-aggregation practice with verified dataset column names and explicit missing-data policy.
- Random generation/distributions, simulation and bootstrap: optional extension in NumPy Speedup Pandas. Uses a local seeded generator. Gross minus production budget is labeled as such, not accounting profit.
- Repetitive benchmark demonstrations and generic function catalogs were consolidated. All original content remains available in the backup notebooks.

## Existing teaching materials

Activity filenames now match Quarto's chapter numbering: Pandas Intermediate uses `activity05.ipynb`, NumPy Fundamentals `activity06.ipynb`, and the Pandas + NumPy workflow `activity07.ipynb`. The chapters no longer describe the NumPy assessment as a legacy Chapter 5. Canvas quizzes are configured outside this repository and still expect their earlier upload filenames, so they must be updated there by hand. Existing coverage maps describe the earlier revisions; this document records the current chapter mapping.

## Validation

- Executed 25 core Pandas Intermediate, 48 NumPy Fundamentals, and 16 NumPy Speedup Pandas worked code cells in independent IPython sessions using the workspace environment; saved fresh outputs. All 89 passed.
- Verified complete-case movie rating–genre means against an independent pandas reference: 980 retained rows, no exclusions for these fields.
- Worked checks cover result equality, row-label restoration after sorting, product alignment after reordering, zero denominators, nullable data, standard-deviation conventions, round-trip CSV export, and conversion-inclusive versus array-only timing.
- NLP resource requires external packages/corpora and live web data; its original examples were retained, not re-executed. This does not affect execution of the core lesson.
- Full Quarto HTML render and rendered navigation checks are recorded after completion below.
- Full 25-page Quarto HTML book render completed successfully. Used `--no-clean` to retain existing rendered backup pages.
- All local HTML links and fragment targets in the four active copied/new chapters resolve, including the NLP final-project anchor. Original notebook SHA-256 hashes still match.
- Browser-based visual inspection was unavailable because no browser surface was connected; validation covered the rendered HTML structure and navigation rather than screenshots.

## Published Intermediate revision

The active Pandas Intermediate chapter is `pandas_intermediate.ipynb`, adapted from the supplied transformations Markdown, with a Fundamentals-style setup and activity. Its student kit is `downloads/pandas-intermediate-practice.zip`.

Chapter filenames are published URLs, so the drafting suffixes were removed. The chapter formerly named with a `_reorganized` suffix is now `pandas_fundamentals.ipynb`, and the one formerly named with a `_claude` suffix is now `pandas_intermediate.ipynb`. The practice kit lost the same suffix and is now `stat303-pandas-intermediate`, shipped as `pandas-intermediate-practice.zip`. The earlier Intermediate draft that previously held the `pandas_intermediate.ipynb` name now lives beside this document as `pandas_intermediate_superseded.ipynb`. It is not part of the book and is not rendered, so it has no published page; it remains here only as a source for supplementary ranking, sorting, string/date, performance, and NLP material.
