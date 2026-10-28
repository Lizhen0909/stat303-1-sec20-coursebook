Paste this near the beginning of `data_viz_2.ipynb` in a Markdown cell:

```markdown
![One figure, four related questions: mid-quarter feedback from 15 students in STAT 303-1, Section 20. All panels share a percentage scale; labels include counts.](images/data-viz-2-midquarter-feedback.svg){#fig-midquarter-feedback width=80% fig-alt="Four horizontal bar charts summarize feedback from 15 students. Nine report a slightly fast pace, and nine report heavier workload. Assignments are rated helpful or very helpful by 13 students, followed by polls and activities at 12 each. Copies versus views is the most selected shaky topic, at seven students. Percentages use 15 as the denominator; the topic question allows multiple selections."}

One plot would tell only part of this story. These four panels let us see pace,
workload, helpful course components, and topics to revisit together. Each panel
has its own title and category labels, while all four share one figure and the
same percentage scale. This chapter shows how to build that structure with
`plt.subplots()` and the explicit `ax` interface.
```

The PNG is available at the same path with a `.png` extension. The SVG stays sharp
when resized. The figure uses aggregate survey counts, not individual responses.
Panels A/B preserve response order; panels C/D are ranked by count. Panel C combines
“Very helpful” and “Helpful”; panel D permits multiple selections and notes the
omitted “None” option. Percentages are computed from counts and rounded only for labels.

Rebuild from the repository root:

```bash
.venv/bin/python teaching-materials/stat303-data-visualization-2/midquarter_figure.py
```
