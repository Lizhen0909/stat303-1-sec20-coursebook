"""Draw images/reshaping-long-wide.png for the Data Reshaping chapter.

    python teaching-materials/figures/make_reshaping_diagram.py   (run from the repository root)

The long table on the left and the wide table on the right hold the chapter's
three-country example; Canada 2005 is highlighted in both so the eye can follow
one value through the reshape.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

PURPLE, PALE, HEADER, GOLD, GOLD_BG, INK = "#4E2A84", "#F0EBF7", "#E3D9F0", "#8F5F0E", "#F7EFDF", "#231F2E"

long_rows = [("USA", 2000, 76.8), ("USA", 2005, 77.5), ("USA", 2010, 78.5),
             ("Canada", 2000, 79.2), ("Canada", 2005, 80.1), ("Canada", 2010, 81.0),
             ("Mexico", 2000, 74.1), ("Mexico", 2005, 75.2), ("Mexico", 2010, 76.5)]
wide_rows = [("Canada", 79.2, 80.1, 81.0), ("Mexico", 74.1, 75.2, 76.5), ("USA", 76.8, 77.5, 78.5)]

fig, ax = plt.subplots(figsize=(11, 5.4))
ax.set_xlim(0, 11); ax.set_ylim(0, 5.4); ax.axis("off")
H = 0.42  # row height

def cell(x, y, w, text, fill, bold=False, color=INK):
    ax.add_patch(Rectangle((x, y), w, H, facecolor=fill, edgecolor="white", linewidth=2))
    ax.text(x + w / 2, y + H / 2, str(text), ha="center", va="center", fontsize=11,
            fontweight="bold" if bold else "normal", color=color, family="DejaVu Sans")

def table(x0, ytop, widths, header, rows, highlight):
    x = x0
    for w, h in zip(widths, header):
        cell(x, ytop, w, h, HEADER, bold=True, color=PURPLE); x += w
    for i, row in enumerate(rows):
        x = x0
        for j, (w, v) in enumerate(zip(widths, row)):
            hit = highlight(i, j)
            cell(x, ytop - (i + 1) * H, w, v, GOLD_BG if hit else PALE, bold=hit, color=GOLD if hit else INK)
            x += w

# Long table
ax.text(1.55, 5.05, "Long: 9 rows × 3 columns", ha="center", fontsize=13, fontweight="bold", color=PURPLE)
table(0.2, 4.45, [1.0, 0.85, 0.85], ["country", "year", "lifeExp"], long_rows,
      lambda i, j: i == 4)
ax.text(1.55, 0.25, "one row per country-year", ha="center", fontsize=10.5, style="italic", color=INK)

# Wide table
ax.text(8.85, 5.05, "Wide: 3 rows × 3 year columns", ha="center", fontsize=13, fontweight="bold", color=PURPLE)
table(7.0, 3.6, [1.0, 0.9, 0.9, 0.9], ["country", "2000", "2005", "2010"], wide_rows,
      lambda i, j: i == 0 and j == 2)
ax.text(8.85, 1.95, "one row per country", ha="center", fontsize=10.5, style="italic", color=INK)

# Arrows
ax.add_patch(FancyArrowPatch((3.25, 3.4), (6.75, 3.4), arrowstyle="-|>", mutation_scale=22,
                             linewidth=2.5, color=PURPLE))
ax.text(5.0, 3.6, "pivot()", ha="center", fontsize=12.5, fontweight="bold", family="DejaVu Sans Mono", color=PURPLE)
ax.text(5.0, 3.05, "year values become columns", ha="center", fontsize=10, color=INK)
ax.add_patch(FancyArrowPatch((6.75, 2.2), (3.25, 2.2), arrowstyle="-|>", mutation_scale=22,
                             linewidth=2.5, color=GOLD))
ax.text(5.0, 2.4, "melt()", ha="center", fontsize=12.5, fontweight="bold", family="DejaVu Sans Mono", color=GOLD)
ax.text(5.0, 1.85, "year columns become rows", ha="center", fontsize=10, color=INK)

fig.savefig("images/reshaping-long-wide.png", dpi=200, bbox_inches="tight", facecolor="white")
print("wrote images/reshaping-long-wide.png")
