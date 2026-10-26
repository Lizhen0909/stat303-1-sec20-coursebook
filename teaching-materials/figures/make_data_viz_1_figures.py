"""Draw the figures for the Data Visualization I chapter (data_viz_1.ipynb).

    python teaching-materials/figures/make_data_viz_1_figures.py   (run from the repository root)

Both panels of the opening figure are built from one array of values generated
here, and every number printed in the table panel is read back out of that same
array, so the table and the plot cannot disagree.
Writes one PNG to images/, prefixed data-viz-1-.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

PURPLE, PALE, HEADER, INK = "#4E2A84", "#F0EBF7", "#E3D9F0", "#231F2E"
MUTE, GOLD = "#8A83A0", "#8F5F0E"
MONO = "DejaVu Sans Mono"


def save(fig, name):
    fig.savefig(f"images/{name}", dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote images/" + name)


# ---------------------------------------------------------------- the shared data
# Two groups of measurements, mixed into one unlabeled column: exactly the
# situation the chapter's histogram section uncovers.
rng = np.random.default_rng(303)
values = np.round(np.concatenate([rng.normal(39.0, 2.2, 120),
                                  rng.normal(48.5, 2.6, 80)]), 1)
rng.shuffle(values)

NROW, NCOL = 7, 6
shown = values[:NROW * NCOL]

fig = plt.figure(figsize=(12.0, 5.9))
grid = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.05], wspace=0.42,
                        left=0.045, right=0.975, top=0.88, bottom=0.185)

# ---------------------------------------------------------------- left: the numbers
left = fig.add_subplot(grid[0, 0])
left.set_xlim(0, 1); left.set_ylim(0, 1); left.axis("off")
left.set_title("The table", fontsize=15, color=PURPLE, fontweight="bold", pad=12)

left.add_patch(FancyBboxPatch((0.02, 0.34), 0.96, 0.60, boxstyle="round,pad=0.012",
                              facecolor=PALE, edgecolor=HEADER, linewidth=1.5))
for r in range(NROW):
    for c in range(NCOL):
        left.text(0.09 + c * 0.165, 0.885 - r * 0.079, f"{shown[r * NCOL + c]:.1f}",
                  ha="center", va="center", fontsize=11, color=INK, family=MONO)
left.text(0.5, 0.285, f"... and {len(values) - len(shown)} more rows",
          ha="center", va="center", fontsize=10.5, color=MUTE, style="italic")

left.add_patch(FancyBboxPatch((0.02, 0.09), 0.96, 0.16, boxstyle="round,pad=0.012",
                              facecolor="white", edgecolor=HEADER, linewidth=1.5))
left.text(0.5, 0.195, f"n = {len(values)}    mean = {values.mean():.1f}    "
                      f"median = {np.median(values):.1f}",
          ha="center", va="center", fontsize=10.5, color=PURPLE, family=MONO)
left.text(0.5, 0.125, f"sd = {values.std(ddof=1):.1f}    min = {values.min():.1f}    "
                      f"max = {values.max():.1f}",
          ha="center", va="center", fontsize=10.5, color=PURPLE, family=MONO)

# ---------------------------------------------------------------- right: the picture
right = fig.add_subplot(grid[0, 1])
right.hist(values, bins=20, color=PURPLE, edgecolor="white", linewidth=0.8)
right.set_xlabel("Measurement", fontsize=11.5, color=INK)
right.set_ylabel("Number of observations", fontsize=11.5, color=INK)
right.set_title("The picture", fontsize=15, color=PURPLE, fontweight="bold", pad=12)
right.tick_params(labelsize=10, colors=MUTE)
for side in ("top", "right"):
    right.spines[side].set_visible(False)
for side in ("left", "bottom"):
    right.spines[side].set_color(HEADER)

top = right.get_ylim()[1]
right.set_ylim(0, top * 1.28)
for peak, text in ((39.0, "group 1"), (48.5, "group 2")):
    right.annotate(text, xy=(peak, top * 1.01), xytext=(peak, top * 1.21),
                   ha="center", fontsize=11.5, color=GOLD, fontweight="bold",
                   arrowprops=dict(arrowstyle="-|>", color=GOLD, linewidth=1.8))

# ---------------------------------------------------------------- the bridge
lp, rp = left.get_position(), right.get_position()
gap = (lp.x1 + rp.x0) / 2
fig.add_artist(FancyArrowPatch((gap - 0.028, 0.52), (gap + 0.028, 0.52),
                               transform=fig.transFigure, arrowstyle="-|>",
                               mutation_scale=22, linewidth=2.4, color=PURPLE))
fig.text(gap, 0.565, "same 200\nvalues", ha="center", va="bottom",
         fontsize=10.5, color=PURPLE, style="italic", linespacing=1.3)

fig.text((lp.x0 + lp.x1) / 2, 0.05, "Says what the values are — one center, one spread.",
         ha="center", va="center", fontsize=12, color=INK)
fig.text((rp.x0 + rp.x1) / 2, 0.05, "Says what the values do — two groups in one column.",
         ha="center", va="center", fontsize=12, color=INK)

save(fig, "data-viz-1-numbers-vs-picture.png")


# ================================================================ 2. the library stack
# How a plotting call travels down to the pixels: pandas and seaborn are two
# front doors onto matplotlib, and matplotlib itself draws NumPy arrays.
BLUE, BLUE_PALE = "#1F5FAE", "#D5E9FE"

fig, ax = plt.subplots(figsize=(11.0, 8.1))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.set_xlim(0, 11); ax.set_ylim(0, 8.1); ax.axis("off")

BOX_L, BOX_R = 0.78, 10.85


def layer(x0, x1, y0, y1, name, tagline, code, face, edge, name_color, body_color,
          detail):
    """One library in the stack: its name, what it is, how you call it, why you would."""
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                boxstyle="round,pad=0.06,rounding_size=0.16",
                                facecolor=face, edgecolor=edge, linewidth=2.0))
    xm = (x0 + x1) / 2
    ax.text(xm, y1 - 0.45, name, ha="center", va="center", fontsize=17,
            family=MONO, fontweight="bold", color=name_color)
    ax.text(xm, y1 - 0.97, tagline, ha="center", va="center", fontsize=11.5,
            color=body_color)
    ax.text(xm, y1 - 1.56, code, ha="center", va="center", fontsize=11, family=MONO,
            color=INK, bbox=dict(boxstyle="round,pad=0.34", facecolor="white",
                                 edgecolor=HEADER, linewidth=1.1))
    ax.text(xm, y0 + 0.30, detail, ha="center", va="center", fontsize=10.5,
            color=body_color, style="italic")


# ---- the two front doors
layer(BOX_L, 5.55, 5.55, 7.85, "pandas",
      "a shortcut built into the data structures",
      'df.plot(kind="hist")', PALE, PURPLE, PURPLE, INK,
      "for a quick look at a DataFrame you already have")
layer(6.08, BOX_R, 5.55, 7.85, "seaborn",
      "a statistical layer for tidy DataFrames",
      'sns.histplot(data=df, x="col")', PALE, PURPLE, PURPLE, INK,
      "grouping, binning, and legends handled for you")

# ---- the engine every plot passes through
layer(BOX_L, BOX_R, 2.65, 4.95, "matplotlib",
      "the drawing engine: figures, axes, and pixels",
      "plt.hist(values)", PURPLE, PURPLE, "white", "#E2D8F0",
      "every plot in this chapter is drawn here, whichever library you called")

# ---- the foundation
ax.add_patch(FancyBboxPatch((BOX_L, 0.30), BOX_R - BOX_L, 1.75,
                            boxstyle="round,pad=0.06,rounding_size=0.16",
                            facecolor=BLUE_PALE, edgecolor=BLUE, linewidth=2.0))
ax.text(3.05, 1.62, "NumPy", ha="center", va="center", fontsize=17,
        family=MONO, fontweight="bold", color=BLUE)
ax.text(3.05, 1.10, "arrays of numbers", ha="center", va="center",
        fontsize=11.5, color=INK)
ax.text(3.05, 0.62, "matplotlib draws arrays, nothing else",
        ha="center", va="center", fontsize=10.5, color=BLUE, style="italic")
for k, v in enumerate([39.1, 39.5, 40.3, 36.7, 39.3, 38.9, 39.2, 34.1]):
    ax.add_patch(FancyBboxPatch((5.85 + k * 0.62, 0.90), 0.56, 0.54,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                facecolor="white", edgecolor=BLUE, linewidth=1.2))
    ax.text(6.13 + k * 0.62, 1.17, f"{v}", ha="center", va="center",
            fontsize=10.5, family=MONO, color=INK)

# ---- the arrows down the stack
for x in (3.16, 8.46):
    ax.add_patch(FancyArrowPatch((x, 5.49), (x, 5.01), arrowstyle="-|>",
                                 mutation_scale=20, linewidth=2.4, color=PURPLE))
    ax.text(x + 0.18, 5.25, "calls", ha="left", va="center", fontsize=10.5,
            color=PURPLE, style="italic")

ax.add_patch(FancyArrowPatch((5.4, 2.59), (5.4, 2.11), arrowstyle="-|>",
                             mutation_scale=20, linewidth=2.4, color=BLUE))
ax.text(5.58, 2.35, "converts your data to arrays", ha="left", va="center",
        fontsize=10.5, color=BLUE, style="italic")

# ---- the level scale down the side
ax.add_patch(FancyArrowPatch((0.44, 7.85), (0.44, 0.30), arrowstyle="-|>",
                             mutation_scale=16, linewidth=1.6, color=MUTE))
ax.text(0.20, 7.05, "you say less", rotation=90, ha="center", va="center",
        fontsize=10, color=MUTE)
ax.text(0.20, 1.35, "closer to the pixels", rotation=90, ha="center", va="center",
        fontsize=10, color=MUTE)

save(fig, "data-viz-1-plotting-stack.png")
