"""Draw the figures for the Data Visualization I chapter (data_viz_1.ipynb).

    python teaching-materials/figures/make_data_viz_1_figures.py   (run from the repository root)

The chapter's opening figure, images/data-viz-1-numbers-vs-picture.png, is a
hand-drawn illustration and is not built here.
Writes one PNG to images/, prefixed data-viz-1-.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

PURPLE, PALE, HEADER, INK = "#4E2A84", "#F0EBF7", "#E3D9F0", "#231F2E"
MUTE = "#8A83A0"
MONO = "DejaVu Sans Mono"


def save(fig, name):
    fig.savefig(f"images/{name}", dpi=200, facecolor="white")
    plt.close(fig)
    print("wrote images/" + name)


# ================================================================ the library stack
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
