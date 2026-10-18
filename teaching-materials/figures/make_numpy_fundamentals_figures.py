"""Draw the figures for the NumPy Fundamentals chapter (numpy_fundamentals.ipynb).

    python teaching-materials/figures/make_numpy_fundamentals_figures.py   (run from the repository root)

Every shape shown in a figure is computed here with NumPy itself, so a figure
cannot drift from the rule it illustrates. Writes PNGs to images/, all
prefixed numpy-.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
import numpy as np

PURPLE, PALE, HEADER, GOLD, GOLD_BG, INK = "#4E2A84", "#F0EBF7", "#E3D9F0", "#8F5F0E", "#F7EFDF", "#231F2E"
MUTE, FILL_BG = "#8A83A0", "#D9CCEB"
MONO = "DejaVu Sans Mono"
H = 0.52  # row height


def canvas(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax


def cell(ax, x, y, w, text, fill, bold=False, color=INK, size=13, mono=True, dashed=False):
    ax.add_patch(Rectangle((x, y), w, H, facecolor=fill, edgecolor="white", linewidth=2))
    if dashed:  # an axis the shorter shape does not have: an empty slot, drawn inside the cell
        ax.add_patch(Rectangle((x + 0.07, y + 0.06), w - 0.14, H - 0.12, facecolor="white",
                               edgecolor=HEADER, linewidth=1.4, linestyle=(0, (4, 3))))
    ax.text(x + w / 2, y + H / 2, str(text), ha="center", va="center", fontsize=size,
            fontweight="bold" if bold else "normal", color=color,
            family=MONO if mono else "DejaVu Sans")


def label(ax, x, y, text, size=11, color=PURPLE, bold=False, ha="center", va="center", mono=False, style="normal"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color,
            fontweight="bold" if bold else "normal", style=style,
            family=MONO if mono else "DejaVu Sans", linespacing=1.5)


def arrow(ax, a, b, color=PURPLE, width=2.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16, linewidth=width, color=color))


def save(fig, name):
    fig.savefig(f"images/{name}", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote images/" + name)


# ---------------------------------------------------------------- 1. the broadcasting rules
shape_a, shape_b = (2, 3, 4), (1, 4)
aligned_b = (1,) * (len(shape_a) - len(shape_b)) + shape_b
result = np.broadcast_shapes(shape_a, shape_b)
assert result == np.empty(shape_a).__add__(np.empty(shape_b)).shape  # the rule, checked by NumPy

W, HT = 11.0, 5.6
fig, ax = canvas(W, HT)
CW, LW, x0, top = 1.15, 1.45, 0.45, 3.55      # cell width, label width, left edge, top of the grid
xcol = [x0 + LW + j * CW for j in range(len(shape_a))]
right = xcol[-1] + CW

label(ax, 0.3, 5.22, "Broadcasting rules", size=18, color=INK, bold=True, ha="left")
label(ax, 0.3, 4.75, "NumPy lines the two shapes up on their right-hand side and compares one dimension at a time.",
      size=12, color=MUTE, ha="left")

# which way the comparison runs
label(ax, (xcol[0] + right) / 2, 4.24, "compare right to left", size=11, color=PURPLE, style="italic")
arrow(ax, (right - 0.1, 3.93), (xcol[0] + 0.1, 3.93), color=PURPLE, width=1.8)

rows = [
    ("a.shape", [str(d) for d in shape_a], False),
    ("b.shape", ["\u2014"] + [str(d) for d in shape_b], False),
    ("b aligned", [str(d) for d in aligned_b], False),
    ("result", [str(d) for d in result], True),
]
for i, (name, values, is_result) in enumerate(rows):
    y = top - (i + 1) * H
    cell(ax, x0, y, LW, name, HEADER, color=PURPLE, bold=True, size=12)
    for j, v in enumerate(values):
        blank = v == "\u2014"
        new_one = name == "b aligned" and j < len(shape_a) - len(shape_b)
        cell(ax, xcol[j], y, CW, v,
             GOLD_BG if new_one else FILL_BG if is_result else PALE,
             bold=is_result or new_one, color=MUTE if blank else GOLD if new_one else PURPLE if is_result else INK,
             dashed=blank)

# why each column came out the way it did
bottom = top - len(rows) * H
for j, note in enumerate(["missing \u2192 1", "1 \u2192 3", "4 = 4"]):
    label(ax, xcol[j] + CW / 2, bottom - 0.3, note, size=10.5,
          color=GOLD if j == 0 else MUTE, bold=j == 0, mono=True)

# the rule itself, stated beside the example
label(ax, right + 0.75, 2.72, "Each pair must be equal,\nor one of them must be 1.",
      size=14, color=INK, bold=True, ha="left")
label(ax, right + 0.75, 1.68, "A 1 takes the other size \u2014 no data is copied.\n"
                              "Equal sizes stay as they are.\n"
                              "Any other pair is a ValueError.",
      size=11.5, color=MUTE, ha="left")

label(ax, 0.3, 0.58, f"Different numbers of dimensions can still broadcast: "
                     f"{shape_a} with {shape_b} gives {result}.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-broadcasting-rules.png")


# ---------------------------------------------------------------- the One Factor per Row or per Column example
units = np.array([[2, 3, 4],      # store 0: 2 notebooks, 3 pens, 4 folders
                  [5, 1, 2]])     # store 1
prices = np.array([10.0, 20.0, 5.0])          # one price PER PRODUCT
store_factors = np.array([1.0, 0.9])          # one multiplier PER STORE
revenue = units * prices
adjusted = revenue * store_factors[:, None]

RED = "#9B2F4A"
CW, GH = 0.82, 0.52   # grid cell width, grid row height


def num(v):
    return f"{v:g}" if float(v).is_integer() and abs(v) >= 1000 else (f"{v:.1f}" if isinstance(v, float) else str(v))


def grid(ax, x, ytop, values, fill, color, title=None, cw=CW, faded=None, bold=False, size=12,
         title_mono=True, title_size=11):
    """Draw a 2D array of cells with its top-left corner at (x, ytop). Returns its width."""
    values = np.atleast_2d(values)
    if title:
        label(ax, x + cw * values.shape[1] / 2, ytop + 0.14, title, size=title_size, mono=title_mono,
              bold=True, va="bottom")
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            dim = faded(i, j) if faded else False
            y = ytop - (i + 1) * GH
            ax.add_patch(Rectangle((x + j * cw, y), cw, GH, facecolor=fill, edgecolor="white",
                                   linewidth=2, alpha=0.4 if dim else 1.0))
            ax.text(x + j * cw + cw / 2, y + GH / 2, num(values[i, j]), ha="center", va="center",
                    fontsize=size, fontweight="bold" if bold and not dim else "normal",
                    color=MUTE if dim else color, family=MONO)
    return cw * values.shape[1]


def op(ax, x, y, symbol, size=22, color=INK):
    label(ax, x, y, symbol, size=size, color=color, bold=True)


# ---------------------------------------------------------------- 2. a row stretches down
W, HT = 13.5, 3.6
fig, ax = canvas(W, HT)
top, mid = 2.25, 2.25 - GH   # top of every grid, and the vertical middle of a two-row grid

label(ax, 0.3, 3.30, "A row stretches down", size=18, color=INK, bold=True, ha="left")
label(ax, 0.3, 2.95, "revenue = units * prices          (2, 3) * (3,)  \u2192  (2, 3)",
      size=12, color=MUTE, ha="left", mono=True)

x = 0.35
x += grid(ax, x, top, units, PALE, INK, title="units: (2, 3)") + 0.3
op(ax, x + 0.18, mid, "*"); x += 0.6
x += grid(ax, x, top, prices, GOLD_BG, GOLD, title="prices: (3,)") + 0.35
arrow(ax, (x - 0.05, mid), (x + 0.6, mid), color=MUTE, width=1.6); x += 0.85
x += grid(ax, x, top, np.broadcast_to(prices, units.shape), GOLD_BG, GOLD,
          title="prices acts like (2, 3)", faded=lambda i, j: i > 0) + 0.3
op(ax, x + 0.18, mid, "="); x += 0.6
x += grid(ax, x, top, revenue, FILL_BG, PURPLE, title="revenue: (2, 3)", bold=True)

label(ax, 0.35, 0.85, "Right-aligned, (3,) is read as (1, 3): the missing leading dimension acts like 1, so the "
                      "one row of prices repeats\ndown every row of units. Each price stays with its own product "
                      "column.",
      size=12, color=INK, ha="left", va="top")
save(fig, "numpy-broadcasting-row.png")


# ---------------------------------------------------------------- 3. a column stretches across
W, HT = 12.6, 4.75
fig, ax = canvas(W, HT)
top, mid = 2.90, 2.90 - GH

label(ax, 0.3, 4.45, "A column stretches across", size=18, color=INK, bold=True, ha="left")
label(ax, 0.3, 4.02, "adjusted = revenue * store_factors[:, None]          (2, 3) * (2, 1)  \u2192  (2, 3)",
      size=12, color=MUTE, ha="left", mono=True)

x = 1.0
x += grid(ax, x, top, store_factors[:, None], GOLD_BG, GOLD,
          title="store_factors[:, None]\n(2, 1)") + 0.35
arrow(ax, (x - 0.05, mid), (x + 0.6, mid), color=MUTE, width=1.6); x += 0.85
x += grid(ax, x, top, np.broadcast_to(store_factors[:, None], revenue.shape), GOLD_BG, GOLD,
          title="acts like\n(2, 3)", faded=lambda i, j: j > 0) + 0.3
op(ax, x + 0.18, mid, "*"); x += 0.6
x += grid(ax, x, top, revenue, PALE, INK, title="revenue: (2, 3)") + 0.3
op(ax, x + 0.18, mid, "="); x += 0.6
x += grid(ax, x, top, adjusted, FILL_BG, PURPLE, title="adjusted: (2, 3)", bold=True)

label(ax, 0.35, 1.37, "revenue * store_factors fails: right-aligned, (2, 3) and (2,) compare 3 against 2.",
      size=12.5, color=RED, bold=True, ha="left")
label(ax, 0.35, 0.90, "A plain (2,) vector always lines up with the columns. Adding the second dimension, "
                      "store_factors[:, None], makes it\na (2, 1) column, so each store's multiplier travels "
                      "across its own row.",
      size=12, color=INK, ha="left", va="top")
save(fig, "numpy-broadcasting-column.png")


# ---------------------------------------------------------------- 4. both inputs stretch
store_prices = store_factors[:, None] * prices

W, HT = 10.6, 3.95
fig, ax = canvas(W, HT)
top, mid = 2.55, 2.55 - GH

label(ax, 0.3, 3.65, "Both inputs can stretch", size=18, color=INK, bold=True, ha="left")
label(ax, 0.3, 3.24, "store_prices = store_factors[:, None] * prices          (2, 1) * (3,)  →  (2, 3)",
      size=12, color=MUTE, ha="left", mono=True)

x = 0.95
left_x = x
x += grid(ax, x, top, np.broadcast_to(store_factors[:, None], store_prices.shape), GOLD_BG, GOLD,
          title="store_factors[:, None]: (2, 1)", faded=lambda i, j: j > 0) + 0.3
op(ax, x + 0.18, mid, "*"); x += 0.6
mid_x = x
x += grid(ax, x, top, np.broadcast_to(prices, store_prices.shape), GOLD_BG, GOLD,
          title="prices: (3,)", faded=lambda i, j: i > 0) + 0.3
op(ax, x + 0.18, mid, "="); x += 0.6
x += grid(ax, x, top, store_prices, FILL_BG, PURPLE, title="store_prices: (2, 3)", bold=True)

bottom = top - 2 * GH
label(ax, left_x + 1.23, bottom - 0.28, "the column repeats across", size=10.5, color=MUTE)
label(ax, mid_x + 1.23, bottom - 0.28, "the row repeats down", size=10.5, color=MUTE)

label(ax, 0.4, 0.62, "Right-aligned, (2, 1) and (1, 3) hold a 1 in every pair, so both inputs stretch and the "
                     "result is larger than either one.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-broadcasting-both.png")


# ---------------------------------------------------------------- 5. the same rule in three dimensions
three_weeks = np.array([[[2, 3, 4], [5, 1, 2]],     # week 1: store 0, store 1
                        [[3, 2, 5], [4, 2, 1]],     # week 2
                        [[1, 4, 3], [6, 2, 2]]])    # week 3
stacked_shape, column_shape = three_weeks.shape, store_factors[:, None].shape
stacked_aligned = (1,) * (len(stacked_shape) - len(column_shape)) + column_shape
stacked_result = (three_weeks * store_factors[:, None]).shape

W, HT = 10.6, 4.6
fig, ax = canvas(W, HT)
LW, CW, x0, top = 1.45, 1.15, 0.4, 3.35
xcol = [x0 + LW + j * CW for j in range(len(stacked_shape))]
right = xcol[-1] + CW

label(ax, 0.3, 4.38, "Higher dimensions follow the same rule", size=18, color=INK, bold=True, ha="left")
label(ax, 0.3, 3.95, "a = three_weeks (3, 2, 3)          b = store_factors[:, None] (2, 1)",
      size=11.5, color=MUTE, ha="left", mono=True)

for j, name in enumerate(["axis 0", "axis 1", "axis 2"]):
    label(ax, xcol[j] + CW / 2, top + 0.2, name, size=10, color=MUTE, mono=True)

rows = [("a.shape", [str(d) for d in stacked_shape], False),
        ("b.shape", ["—"] + [str(d) for d in column_shape], False),
        ("b aligned", [str(d) for d in stacked_aligned], False),
        ("result", [str(d) for d in stacked_result], True)]
for i, (name, values, is_result) in enumerate(rows):
    y = top - (i + 1) * H
    cell(ax, x0, y, LW, name, HEADER, color=PURPLE, bold=True, size=12)
    for j, v in enumerate(values):
        blank = v == "—"
        new_one = name == "b aligned" and j < len(stacked_shape) - len(column_shape)
        cell(ax, xcol[j], y, CW, v, GOLD_BG if new_one else FILL_BG if is_result else PALE,
             bold=is_result or new_one,
             color=MUTE if blank else GOLD if new_one else PURPLE if is_result else INK, dashed=blank)

label(ax, right + 0.7, 2.62, "b stretches on axis 0: 1 → 3\nb stretches on axis 2: 1 → 3",
      size=13, color=INK, bold=True, ha="left")
label(ax, right + 0.7, 1.62, "Axis 1 already matches: 2 and 2.\n"
                             "A plain (2,) would align as (1, 1, 2)\nand fail against the 3 products.",
      size=11.5, color=MUTE, ha="left")

label(ax, 0.3, 0.5, "NumPy matches positions from the right. It never searches for an axis of the same size.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-broadcasting-3d.png")


# ---------------------------------------------------------------- 6. the anatomy of an np.where() call
from matplotlib.patches import FancyBboxPatch

MONO_W = 0.602 / 72          # DejaVu Sans Mono advance width, in inches per point of font size


def token_width(text, size, pad=0.22):
    return len(text) * MONO_W * size + 2 * pad


# (text, boxed argument?, fill, colour, which side its label sits on, the label)
PIECES = [
    ("np.where", True, HEADER, PURPLE, "above", "the function"),
    ("(", False, None, None, None, None),
    ("passing", True, GOLD_BG, GOLD, "above", "the condition:\na True/False array"),
    (",", False, None, None, None, None),
    ("'Pass'", True, FILL_BG, PURPLE, "below", "the value where\nthe condition is True"),
    (",", False, None, None, None, None),
    ("'Needs review'", True, FILL_BG, PURPLE, "below", "the value where\nthe condition is False"),
    (")", False, None, None, None, None),
]
TOK = 14          # font size inside the call
GAP = 0.1         # space between pieces
widths = [token_width(t, TOK) if boxed else len(t) * MONO_W * TOK + 0.14
          for t, boxed, *_ in PIECES]
bar_inner = sum(widths) + GAP * (len(PIECES) - 1)

W, HT = bar_inner + 3.4, 5.15
fig, ax = canvas(W, HT)
bar_h, bar_y = 0.62, 2.5
bar_top = bar_y + bar_h
x = (W - bar_inner) / 2

label(ax, 0.3, 4.78, "Anatomy of an np.where() call", size=18, color=INK, bold=True, ha="left")
label(ax, 0.3, 4.35, "One call, three arguments: the condition, and the two values to choose between.",
      size=12, color=MUTE, ha="left")

ax.add_patch(FancyBboxPatch((x - 0.3, bar_y - 0.06), bar_inner + 0.6, bar_h + 0.12,
                            boxstyle="round,pad=0.08,rounding_size=0.18",
                            facecolor=PALE, edgecolor=HEADER, linewidth=1.5))
below_rows = [(2.10, 1.98), (1.55, 1.43)]   # staggered, so the two notes never collide
below_i = 0
for (text, boxed, fill, color, side, note), w in zip(PIECES, widths):
    cx = x + w / 2
    if boxed:
        ax.add_patch(FancyBboxPatch((x, bar_y), w, bar_h,
                                    boxstyle="round,pad=0,rounding_size=0.12",
                                    facecolor=fill, edgecolor="white", linewidth=1.6))
        ax.text(cx, bar_y + bar_h / 2, text, ha="center", va="center", fontsize=TOK,
                fontweight="bold", color=color, family=MONO)
        if side == "above":
            arrow(ax, (cx, 3.50), (cx, bar_top + 0.08), color=MUTE, width=1.6)
            label(ax, cx, 3.62, note, size=11, color=INK, va="bottom")
        else:
            tip, text_y = below_rows[below_i]; below_i += 1
            arrow(ax, (cx, bar_y - 0.08), (cx, tip), color=MUTE, width=1.6)
            label(ax, cx, text_y, note, size=11, color=INK, va="top")
    else:
        ax.text(cx, bar_y + bar_h / 2, text, ha="center", va="center", fontsize=TOK,
                color=MUTE, family=MONO)
    x += w + GAP

label(ax, 0.3, 0.4, "The condition is an array, so the answer is too: one value per position, "
                    "the shape of the condition.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-where-anatomy.png")


# ---------------------------------------------------------------- 7. np.where() position by position
exam_scores = np.array([55, 82, 91, 47, 76, 88])
passing = exam_scores >= 60
pass_labels = np.where(passing, 'Pass', 'Needs review')

W, HT = 12.7, 5.6
fig, ax = canvas(W, HT)
LW, CW, x0 = 2.0, 1.68, 0.35
xcol = [x0 + LW + j * CW for j in range(len(exam_scores))]

label(ax, 0.3, 5.35, "np.where() decides one position at a time", size=18, color=INK, bold=True, ha="left")
label(ax, 0.3, 4.92, "pass_labels = np.where(passing, 'Pass', 'Needs review')",
      size=12, color=MUTE, ha="left", mono=True)

row_y = [3.62, 2.52, 1.42]                       # bottom edge of each row of cells
for j in range(len(exam_scores)):
    label(ax, xcol[j] + CW / 2, row_y[0] + H + 0.26, str(j), size=10, color=MUTE, mono=True)
label(ax, x0 + LW - 0.15, row_y[0] + H + 0.26, "position", size=10, color=MUTE, ha="right")

def branch(j):
    return (FILL_BG, PURPLE) if passing[j] else (GOLD_BG, GOLD)

rows = [("exam_scores", [str(v) for v in exam_scores], lambda j: (PALE, INK), False, 11),
        ("passing", [str(v) for v in passing], branch, True, 11),
        ("pass_labels", ["'" + v + "'" for v in pass_labels], branch, True, 10)]
for (name, values, colors, bold, size), y in zip(rows, row_y):
    cell(ax, x0, y, LW, name, HEADER, color=PURPLE, bold=True, size=12)
    for j, v in enumerate(values):
        fill, color = colors(j)
        cell(ax, xcol[j], y, CW, v, fill, bold=bold, color=color, size=size)

for j in range(len(exam_scores)):
    cx = xcol[j] + CW / 2
    arrow(ax, (cx, row_y[0] - 0.06), (cx, row_y[1] + H + 0.06), color=MUTE, width=1.3)
    arrow(ax, (cx, row_y[1] - 0.06), (cx, row_y[2] + H + 0.06), color=MUTE, width=1.3)
label(ax, x0 + LW - 0.15, (row_y[0] + row_y[1] + H) / 2, "exam_scores >= 60",
      size=10, color=MUTE, ha="right", mono=True)
label(ax, x0 + LW - 0.15, (row_y[1] + row_y[2] + H) / 2, "'Pass' if True,\nelse 'Needs review'",
      size=10, color=MUTE, ha="right", mono=True)

label(ax, 0.35, 0.75, "Each position is decided on its own, and the labels come back in the same order, "
                      "with the same\nshape as the condition. One compiled pass, no Python loop and "
                      "no if statement.",
      size=12, color=INK, bold=True, ha="left", va="top")
save(fig, "numpy-where-positions.png")


# ---------------------------------------------------------------- 8. np.select(): the first true condition wins
conditions = [exam_scores >= 90, exam_scores >= 60]
choices = ['High score', 'Pass']
score_groups = np.select(conditions, choices, default='Needs review')
swapped = np.select([exam_scores >= 60, exam_scores >= 90], ['Pass', 'High score'],
                    default='Needs review')

W, HT = 12.9, 6.25
fig, ax = canvas(W, HT)
LW, CW, x0 = 2.45, 1.68, 0.35
xcol = [x0 + LW + j * CW for j in range(len(exam_scores))]

label(ax, 0.3, 5.97, "np.select() takes the first condition that is True", size=18, color=INK,
      bold=True, ha="left")
label(ax, 0.3, 5.56, "score_groups = np.select(conditions, choices, default='Needs review')",
      size=12, color=MUTE, ha="left", mono=True)

row_y = [4.42, 3.62, 2.92, 2.22, 1.42]        # scores, condition 1, condition 2, default, result
for j in range(len(exam_scores)):
    label(ax, xcol[j] + CW / 2, row_y[0] + H + 0.26, str(j), size=10, color=MUTE, mono=True)
label(ax, x0 + LW - 0.15, row_y[0] + H + 0.26, "position", size=10, color=MUTE, ha="right")

cell(ax, x0, row_y[0], LW, "exam_scores", HEADER, color=PURPLE, bold=True, size=12)
for j, v in enumerate(exam_scores):
    cell(ax, xcol[j], row_y[0], CW, v, PALE, color=INK, size=11)

# which rule decides each position: 0 or 1 for a condition, 2 for the default
winner = [0 if conditions[0][j] else 1 if conditions[1][j] else 2 for j in range(len(exam_scores))]
ladder = [("1.  >= 90\n→ 'High score'", lambda j: conditions[0][j]),
          ("2.  >= 60\n→ 'Pass'", lambda j: conditions[1][j]),
          ("default\n→ 'Needs review'", lambda j: True)]
for k, (name, holds) in enumerate(ladder):
    y = row_y[k + 1]
    cell(ax, x0, y, LW, name, HEADER, color=PURPLE, bold=True, size=11)
    for j in range(len(exam_scores)):
        decided = winner[j] == k
        spent = winner[j] < k                      # an earlier rule already took this position
        text = "True" if holds(j) else "False"
        if k == 2:
            text = "used" if decided else "—"
        cell(ax, xcol[j], y, CW, text,
             GOLD_BG if decided else PALE,
             bold=decided, color=GOLD if decided else MUTE if spent or not holds(j) else INK, size=11)
        if decided:
            ax.add_patch(Rectangle((xcol[j] + 0.03, y + 0.03), CW - 0.06, H - 0.06,
                                   facecolor="none", edgecolor=GOLD, linewidth=1.8))

cell(ax, x0, row_y[4], LW, "score_groups", HEADER, color=PURPLE, bold=True, size=12)
for j, v in enumerate(score_groups):
    cell(ax, xcol[j], row_y[4], CW, "'" + v + "'", FILL_BG, color=PURPLE, bold=True, size=10)

label(ax, 0.35, 0.92, f"Position 2 is the one to watch: 91 is True on both rules, and the first one wins.",
      size=12, color=INK, bold=True, ha="left")
label(ax, 0.35, 0.45, f"List >= 60 first and that same score becomes '{swapped[2]}'. "
                      f"Put the most specific condition first.",
      size=12, color=RED, bold=True, ha="left")
save(fig, "numpy-select-first-true.png")


# ---------------------------------------------------------------- 9. np.select(): the two lists pair up
W, HT = 9.6, 4.6
fig, ax = canvas(W, HT)
LW, CW, x0 = 1.75, 2.6, 0.35
xpair = [x0 + LW, x0 + LW + CW]
right = x0 + LW + 2 * CW

label(ax, 0.3, 4.25, "conditions and choices pair up by position", size=18, color=INK,
      bold=True, ha="left")
label(ax, 0.3, 3.83, "np.select(conditions, choices, default='Needs review')",
      size=12, color=MUTE, ha="left", mono=True)

y_cond, y_choice, y_default = 2.78, 1.58, 0.70
cell(ax, x0, y_cond, LW, "conditions", HEADER, color=PURPLE, bold=True, size=12)
cell(ax, x0, y_choice, LW, "choices", HEADER, color=PURPLE, bold=True, size=12)
cell(ax, x0, y_default, LW, "default", HEADER, color=PURPLE, bold=True, size=12)
for j, (cond, choice) in enumerate(zip(["exam_scores >= 90", "exam_scores >= 60"], choices)):
    cell(ax, xpair[j], y_cond, CW, cond, GOLD_BG, color=GOLD, bold=True, size=11)
    cell(ax, xpair[j], y_choice, CW, "'" + choice + "'", FILL_BG, color=PURPLE, bold=True, size=11)
    cx = xpair[j] + CW / 2
    arrow(ax, (cx, y_cond - 0.08), (cx, y_choice + H + 0.08), color=MUTE, width=1.6)
    label(ax, cx, (y_cond + y_choice + H) / 2, f"  item {j}", size=10, color=MUTE, ha="left", mono=True)
cell(ax, xpair[0], y_default, 2 * CW, "'Needs review'", PALE, color=INK, bold=True, size=11)

label(ax, right + 0.2, y_cond + H / 2, "one Boolean array\nper rule", size=10.5, color=MUTE, ha="left")
label(ax, right + 0.2, y_choice + H / 2, "the label that rule\nhands out", size=10.5, color=MUTE, ha="left")
label(ax, right + 0.2, y_default + H / 2, "used where every\ncondition is False", size=10.5, color=MUTE, ha="left")

label(ax, 0.35, 0.32, "The two lists are read together, item by item: same length, same order.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-select-pairing.png")


# ---------------------------------------------------------------- 10. vstack adds rows, hstack adds columns
class_a = np.array([[85, 90], [78, 82]])
class_b = np.array([[92, 88]])
combined_class = np.vstack([class_a, class_b])
new_quiz = np.array([[95], [80], [91]])
with_new_quiz = np.hstack([combined_class, new_quiz])

BW = 0.86   # cell width inside a stacked block


def block(ax, x, ytop, arr, new=None, label_text=None, size=12):
    """Draw a 2D array; new(i, j) marks the cells that the stack just added."""
    arr = np.atleast_2d(arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            fresh = new(i, j) if new else False
            cell(ax, x + j * BW, ytop - (i + 1) * GH, BW, arr[i, j],
                 GOLD_BG if fresh else PALE, bold=fresh, color=GOLD if fresh else INK, size=size)
    if label_text:
        label(ax, x + BW * arr.shape[1] / 2, ytop + 0.2, label_text, size=11, color=PURPLE,
              bold=True, mono=True, va="bottom")
    return BW * arr.shape[1]


W, HT = 11.3, 6.9
fig, ax = canvas(W, HT)

label(ax, 0.3, 6.60, "np.vstack adds rows, np.hstack adds columns", size=18, color=INK,
      bold=True, ha="left")
label(ax, 0.3, 6.20, "Gold marks what each call brought in.", size=12, color=MUTE, ha="left")

TOP = 5.15                      # top edge of the input blocks in both panels
GAPY = 0.12                     # the seam between the two stacked inputs on the left

# ---- left panel: vstack
xa = 0.8
wa = BW * class_a.shape[1]
label(ax, xa, 5.90, "np.vstack([class_a, class_b])", size=12.5, color=INK, bold=True,
      mono=True, ha="left")
block(ax, xa, TOP, class_a)
label(ax, xa + wa + 0.2, TOP - GH, "class_a (2, 2)", size=11, color=PURPLE, bold=True,
      mono=True, ha="left")
b_top = TOP - 2 * GH - GAPY
block(ax, xa, b_top, class_b, new=lambda i, j: True)
label(ax, xa + wa + 0.2, b_top - GH / 2, "class_b (1, 2)", size=11, color=GOLD, bold=True,
      mono=True, ha="left")
arrow(ax, (xa + wa / 2, b_top - GH - 0.16), (xa + wa / 2, b_top - GH - 0.72), color=MUTE, width=1.8)
res_top = b_top - GH - 0.82
block(ax, xa, res_top, combined_class, new=lambda i, j: i == combined_class.shape[0] - 1)
label(ax, xa + wa + 0.2, res_top - 1.5 * GH, "combined_class (3, 2)", size=11, color=PURPLE,
      bold=True, mono=True, ha="left")
label(ax, xa + wa / 2, res_top - 3 * GH - 0.3, "(2, 2) + (1, 2)  \u2192  (3, 2)",
      size=12, color=PURPLE, bold=True, mono=True)

# ---- right panel: hstack
xb = 5.9
wb = BW * combined_class.shape[1]
label(ax, xb, 5.90, "np.hstack([combined_class, new_quiz])", size=12.5, color=INK, bold=True,
      mono=True, ha="left")
block(ax, xb, TOP, combined_class)
label(ax, xb + wb / 2, TOP + 0.16, "combined_class (3, 2)", size=11, color=PURPLE, bold=True,
      mono=True, va="bottom")
block(ax, xb + wb + 0.45, TOP, new_quiz, new=lambda i, j: True)
label(ax, xb + wb + 0.45 + BW + 0.2, TOP - 1.5 * GH, "new_quiz (3, 1)", size=11, color=GOLD,
      bold=True, mono=True, ha="left")
wtot = BW * with_new_quiz.shape[1]
arrow(ax, (xb + wtot / 2, TOP - 3 * GH - 0.16), (xb + wtot / 2, TOP - 3 * GH - 0.72),
      color=MUTE, width=1.8)
res_top_b = TOP - 3 * GH - 0.82
block(ax, xb, res_top_b, with_new_quiz, new=lambda i, j: j == with_new_quiz.shape[1] - 1)
label(ax, xb + wtot + 0.2, res_top_b - 1.5 * GH, "with_new_quiz (3, 3)", size=11, color=PURPLE,
      bold=True, mono=True, ha="left")
label(ax, xb + wtot / 2, res_top_b - 3 * GH - 0.3, "(3, 2) + (3, 1)  \u2192  (3, 3)",
      size=12, color=PURPLE, bold=True, mono=True)

label(ax, 0.3, 0.35, "vstack needs the same number of columns; hstack needs the same number of rows. "
                     "Anything else is an error.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-vstack-hstack.png")


# ---------------------------------------------------------------- 11. np.concatenate: the axis that grows
W, HT = 10.2, 4.75
fig, ax = canvas(W, HT)
SW, SL = 0.95, 1.75        # shape-cell width, name-column width

label(ax, 0.3, 4.42, "np.concatenate names the axis that grows", size=18, color=INK,
      bold=True, ha="left")
label(ax, 0.3, 4.05, "Entries along the named axis add up; every other axis must already match.",
      size=12, color=MUTE, ha="left")


def shape_panel(x0, heading, note, rows, join_axis):
    """rows: [(name, shape), (name, shape), ('result', shape)] for one concatenate call."""
    xs = [x0 + SL, x0 + SL + SW]
    label(ax, x0, 3.62, heading, size=14, color=GOLD, bold=True, mono=True, ha="left")
    label(ax, x0 + 1.25, 3.62, note, size=11.5, color=MUTE, ha="left")
    for j, head in enumerate(["axis 0", "axis 1"]):
        label(ax, xs[j] + SW / 2, 3.30, head, size=10,
              color=GOLD if j == join_axis else MUTE, bold=j == join_axis, mono=True)
    ys = [2.76, 2.16, 1.43]
    for (name, shape), y in zip(rows, ys):
        cell(ax, x0, y, SL, name, HEADER, color=PURPLE, bold=True, size=11)
        for j, size_j in enumerate(shape):
            on_axis = j == join_axis
            cell(ax, xs[j], y, SW, size_j, GOLD_BG if on_axis else PALE,
                 bold=on_axis, color=GOLD if on_axis else INK, size=12)
    label(ax, x0 - 0.12, ys[1] + H / 2, "+", size=16, color=INK, bold=True, ha="right")
    label(ax, x0 - 0.12, ys[2] + H / 2, "=", size=16, color=INK, bold=True, ha="right")
    ax.plot([x0, xs[1] + SW], [ys[1] - 0.14] * 2, color=HEADER, linewidth=1.6)
    a, b = rows[0][1][join_axis], rows[1][1][join_axis]
    label(ax, xs[join_axis] + SW / 2, ys[2] - 0.28, f"{a} + {b}", size=10.5, color=GOLD,
          bold=True, mono=True, va="top")
    other = 1 - join_axis
    label(ax, xs[other] + SW / 2, ys[2] - 0.28, "must match", size=10.5, color=MUTE, va="top")


shape_panel(0.6, "axis=0", "joins rows, like np.vstack",
            [("class_a", class_a.shape), ("class_b", class_b.shape),
             ("combined_class", combined_class.shape)], join_axis=0)
shape_panel(5.6, "axis=1", "joins columns, like np.hstack",
            [("combined_class", combined_class.shape), ("new_quiz", new_quiz.shape),
             ("with_new_quiz", with_new_quiz.shape)], join_axis=1)

label(ax, 0.3, 0.42, "The wrappers pick the axis for you; np.concatenate makes you say it, "
                     "and works the same way for any number of axes.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-concatenate-axis.png")


# ---------------------------------------------------------------- 12. an integer drops the axis, a slice keeps it
grades = np.array([[88, 92, 79],
                   [95, 84, 91]])
dropped, kept = grades[:, 1], grades[:, 1:2]

W, HT = 9.9, 4.8
fig, ax = canvas(W, HT)
GW = 0.8

label(ax, 0.3, 4.48, "An integer drops the axis; a slice keeps it", size=18, color=INK,
      bold=True, ha="left")
label(ax, 0.3, 4.08, "Both selections pull the same two numbers out of column 1.",
      size=12, color=MUTE, ha="left")

gx, gtop = 0.6, 3.30
label(ax, gx + 1.5 * GW, gtop + 0.16, "grades (2, 3)", size=11, color=PURPLE, bold=True,
      mono=True, va="bottom")
for i in range(grades.shape[0]):
    for j in range(grades.shape[1]):
        picked = j == 1
        cell(ax, gx + j * GW, gtop - (i + 1) * GH, GW, grades[i, j],
             GOLD_BG if picked else PALE, bold=picked, color=GOLD if picked else INK, size=12)

RX = 4.6
for y_top, values, call, note, vertical in [
        (2.95, dropped, "grades[:, 1]", "shape (2,)\nthe column axis is gone", False),
        (1.85, kept, "grades[:, 1:2]", "shape (2, 1)\nthe column axis is kept", True)]:
    flat = np.ravel(values)
    rows = len(flat) if vertical else 1
    cols = 1 if vertical else len(flat)
    label(ax, RX, y_top + 0.16, call, size=11.5, color=INK, bold=True, mono=True,
          ha="left", va="bottom")
    for k, v in enumerate(flat):
        x = RX + (0 if vertical else k * GW)
        y = y_top - ((k + 1) * GH if vertical else GH)
        cell(ax, x, y, GW, v, GOLD_BG, bold=True, color=GOLD, size=12)
    arrow(ax, (gx + 3 * GW + 0.12, gtop - GH), (RX - 0.25, y_top - rows * GH / 2),
          color=MUTE, width=1.6)
    label(ax, RX + cols * GW + 0.3, y_top - rows * GH / 2, note, size=11, color=MUTE, ha="left")

label(ax, 0.3, 0.35, "Same two numbers either way \u2014 only the shape differs. Keep the axis when the "
                     "result has to broadcast back down a column.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-drop-vs-keep-axis.png")


# ---------------------------------------------------------------- 13. a slice is a view, a mask is a copy
original = np.array([1, 2, 3, 4, 5])
subset = original[1:4]
subset[0] = 999                      # the view writes straight through
mask_result = original[original > 2]
mask_result[0] = -1                  # the copy keeps the edit to itself

VW = 0.66   # cell width in this figure


def strip(ax, x, ytop, values, name, hot=(), tag=None, tag_color=MUTE, offset=0, dim=False):
    """One 1-D array drawn as a row of cells, with its name above and an optional tag beside."""
    label(ax, x, ytop + 0.12, name, size=11, color=MUTE if dim else INK, bold=True, mono=True,
          ha="left", va="bottom")
    for k, v in enumerate(values):
        hotcell = k in hot
        cell(ax, x + (offset + k) * VW, ytop - GH, VW, v, GOLD_BG if hotcell else PALE,
             bold=hotcell, color=GOLD if hotcell else INK, size=11)
    if tag:
        label(ax, x + (offset + len(values)) * VW + 0.2, ytop - GH / 2, tag, size=10.5,
              color=tag_color, ha="left")


W, HT = 11.9, 6.3
fig, ax = canvas(W, HT)

label(ax, 0.3, 5.98, "A slice is a window; a mask is a copy", size=18, color=INK,
      bold=True, ha="left")
label(ax, 0.3, 5.58, "Both start from the same array. Only one of them writes through to it.",
      size=12, color=MUTE, ha="left")

xl, xr = 0.5, 6.4
for x, head in [(xl, "basic slicing \u2192 view"), (xr, "Boolean mask \u2192 copy")]:
    label(ax, x, 5.15, head, size=13, color=PURPLE, bold=True, ha="left")

# ---- left panel: the view
strip(ax, xl, 4.55, [1, 2, 3, 4, 5], "original")
strip(ax, xl, 3.70, [2, 3, 4], "subset = original[1:4]", offset=1,
      tag="a window on\npositions 1\u20133", tag_color=GOLD)
label(ax, xl, 3.05, "subset[0] = 999", size=12, color=INK, bold=True, mono=True, ha="left")
strip(ax, xl, 2.45, subset, "subset", hot={0}, offset=1)
strip(ax, xl, 1.60, original, "original", hot={1}, tag="changed too", tag_color=GOLD)
label(ax, xl, 0.85, "The window writes through to the array.",
      size=11.5, color=INK, bold=True, ha="left")

# ---- right panel: the copy
strip(ax, xr, 4.55, original, "original", hot={1})
strip(ax, xr, 3.70, [999, 3, 4, 5], "mask_result = original[original > 2]",
      tag="a new array\nof its own", tag_color=GOLD)
label(ax, xr, 3.05, "mask_result[0] = -1", size=12, color=INK, bold=True, mono=True, ha="left")
strip(ax, xr, 2.45, mask_result, "mask_result", hot={0})
strip(ax, xr, 1.60, original, "original", hot={1}, tag="untouched", tag_color=MUTE)
label(ax, xr, 0.85, "The copy keeps its edits to itself.",
      size=11.5, color=INK, bold=True, ha="left")

label(ax, 0.3, 0.3, "np.shares_memory(a, b) answers which one you are holding; .copy() makes the "
                    "question moot.",
      size=12, color=INK, bold=True, ha="left")
save(fig, "numpy-view-vs-copy.png")
