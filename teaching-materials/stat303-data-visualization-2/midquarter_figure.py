"""Reproduce the chapter-opening survey figure with the course .venv Python.

Source: STAT 303-1 Section 20 mid-quarter survey results.md, Oct 22–26, 2026.
Only aggregate counts are used; all four panels have 15 respondents.
"""
from pathlib import Path
import os
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "stat303-mpl"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "images" / "data-viz-2-midquarter-feedback"
N = 15
PURPLE = "#4E2A84"
INK = "#242333"
MUTED = "#666477"

# Preserve ordinal order in A/B; rank counts in C/D (stable order for ties).
panels = [
    ("A", "How does the pace feel?", "One response per student",
     ["A little too fast", "About right", "Too slow (either level)"], [9, 6, 0]),
    ("B", "How does the workload compare?", "Compared with other courses at this level",
     ["Much heavier", "Somewhat heavier", "About the same", "Lighter (either level)"], [1, 8, 6, 0]),
    ("C", "Which components are helpful?", 'Rated “Very helpful” or “Helpful”',
     ["Assignments", "Poll Everywhere", "In-class activities", "Coursebook reading",
      "Canvas chapter quizzes", "Muddy-point review"], [13, 12, 12, 11, 8, 7]),
    ("D", "Which topics still feel shaky?", "Select all that apply; totals can exceed 100%",
     ["Copies vs. views", "Broadcasting", "Data types / cleaning", "Array shape / axes",
      "Transforming columns", "Boolean filtering"], [7, 6, 6, 5, 4, 3]),
]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "text.color": INK, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": INK,
                     "svg.fonttype": "none"})
fig, axes = plt.subplots(2, 2, figsize=(15, 10), sharex=True)
fig.patch.set_facecolor("white")
fig.subplots_adjust(left=.185, right=.945, top=.79, bottom=.16, wspace=.96, hspace=.65)

for ax, (letter, title, subtitle, labels, counts) in zip(axes.flat, panels):
    assert all(0 <= count <= N for count in counts)
    values = [100 * count / N for count in counts]
    ax.barh(range(len(labels)), values, height=.56, color=PURPLE, zorder=3)
    ax.set_yticks(range(len(labels)), labels)
    ax.set_ylim(len(labels) - .45, -.7)
    ax.set_xlim(0, 106)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.xaxis.set_major_formatter(PercentFormatter(100, decimals=0))
    ax.tick_params(axis="both", length=0, labelbottom=True, pad=8)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="#E6E4EB", linewidth=.8)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.text(0, 1.19, f"{letter}   {title}", transform=ax.transAxes,
            fontsize=12, weight="bold", ha="left")
    ax.text(0, 1.08, subtitle, transform=ax.transAxes,
            fontsize=9.2, color=MUTED, ha="left")
    for y, (value, count) in enumerate(zip(values, counts)):
        ax.text(value + 2, y, f"{value:.0f}% ({count})", va="center", fontsize=10)

fig.text(.045, .95, "ONE CLASS · FOUR QUESTIONS", fontsize=11, color=PURPLE, weight="bold")
fig.text(.045, .902, "Your mid-quarter feedback", fontsize=29, weight="bold")
fig.text(.045, .86, "STAT 303-1 · Section 20 · Fall 2026     |     15 respondents", fontsize=12, color=MUTED)
fig.supxlabel("Share of respondents", y=.105, fontsize=11, color=MUTED)
fig.text(.045, .06, "Each panel uses the same 0–100% scale. Labels show percentage (number of students).", fontsize=10, color=MUTED)
fig.text(.045, .035, "Source: mid-quarter survey, Oct 22–26, 2026. Panel D omits “None — I feel solid” (3 students, 20%).", fontsize=9, color=MUTED)

for extension in ("png", "svg"):
    fig.savefig(OUT.with_suffix(f".{extension}"), dpi=200, facecolor="white")
print(OUT.with_suffix(".png"))
