"""Draw the figures for the Pandas Intermediate chapter (pandas_intermediate.ipynb).

    python teaching-materials/figures/make_pandas_intermediate_figures.py   (run from the repository root)

Every number in a figure is computed here with pandas from the chapter's own
example data, so a figure cannot drift from the code cell it illustrates.
Writes ten PNGs to images/, all prefixed pandas-intermediate-.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch
import numpy as np
import pandas as pd

PURPLE, PALE, HEADER, GOLD, GOLD_BG, INK = "#4E2A84", "#F0EBF7", "#E3D9F0", "#8F5F0E", "#F7EFDF", "#231F2E"
MUTE, FILL_BG = "#8A83A0", "#D9CCEB"
MONO = "DejaVu Sans Mono"
H = 0.42  # row height


def canvas(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax


def cell(ax, x, y, w, text, fill, bold=False, color=INK, size=11, mono=False, edge="white"):
    ax.add_patch(Rectangle((x, y), w, H, facecolor=fill, edgecolor=edge, linewidth=2))
    ax.text(x + w / 2, y + H / 2, str(text), ha="center", va="center", fontsize=size,
            fontweight="bold" if bold else "normal", color=color,
            family=MONO if mono else "DejaVu Sans")


def label(ax, x, y, text, size=11, color=PURPLE, bold=True, ha="center", mono=False, style="normal"):
    ax.text(x, y, text, ha=ha, va="center", fontsize=size, color=color,
            fontweight="bold" if bold else "normal", style=style,
            family=MONO if mono else "DejaVu Sans")


def arrow(ax, a, b, color=PURPLE, width=2.2):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=18, linewidth=width, color=color))


def fmt(v):
    if pd.isna(v):
        return "NaN"
    return f"{v:,.0f}" if float(v).is_integer() else f"{v:g}"


def frame_table(ax, x0, ytop, df, colw, idxw, kinds=None, title=None, title_mono=True, title_size=12, index=True):
    """Draw a DataFrame with its index on the left. kinds(row_label, col) -> plain | match | fill | nan."""
    if title:
        label(ax, x0 + idxw + colw * len(df.columns) / 2, ytop + H + 0.32, title, size=title_size, mono=title_mono)
    for j, c in enumerate(df.columns):
        cell(ax, x0 + idxw + j * colw, ytop, colw, c, HEADER, bold=True, color=PURPLE, mono=True)
    for i, r in enumerate(df.index):
        y = ytop - (i + 1) * H
        if index:
            label(ax, x0 + idxw - 0.12, y + H / 2, str(r), size=11, ha="right", mono=True)
        for j, c in enumerate(df.columns):
            v = df.loc[r, c]
            k = kinds(r, c) if kinds else "plain"
            if k == "plain" and pd.isna(v):
                k = "nan"
            style = {"plain": (PALE, INK, False), "match": (GOLD_BG, GOLD, True),
                     "fill": (FILL_BG, PURPLE, True), "nan": ("white", MUTE, False)}[k]
            cell(ax, x0 + idxw + j * colw, y, colw, fmt(v), style[0], bold=style[2], color=style[1], mono=True)
            if k == "nan":
                ax.add_patch(Rectangle((x0 + idxw + j * colw + 0.04, y + 0.04), colw - 0.08, H - 0.08,
                                       facecolor="none", edgecolor=HEADER, linewidth=1.2))


def save(fig, name):
    fig.savefig(f"images/{name}", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote images/" + name)


# ---------------------------------------------------------------- 1. vectorized column arithmetic
business_df = pd.DataFrame({
    'Product':         ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones'],
    'Units_Sold':      [150, 300, 200, 500, 250],
    'Price_per_Unit':  [1200, 800, 600, 400, 200],
}).set_index('Product')
business_df['Total_Revenue'] = business_df['Units_Sold'] * business_df['Price_per_Unit']

fig, ax = canvas(10.5, 3.6)
hi = 'Phone'
kinds = lambda r, c: "match" if r == hi else "plain"
top = 2.55
frame_table(ax, 0.1, top, business_df[['Units_Sold']], 1.5, 1.35, kinds)
label(ax, 3.3, top - 2.5 * H, "×", size=24)
frame_table(ax, 3.65, top, business_df[['Price_per_Unit']], 1.75, 0, kinds, index=False)
label(ax, 5.75, top - 2.5 * H, "=", size=24)
frame_table(ax, 6.1, top, business_df[['Total_Revenue']], 1.75, 0, kinds, index=False)
r = business_df.loc[hi]
label(ax, 9.55, top - 2 * H + H / 2, f"{r.Units_Sold} × {r.Price_per_Unit:,}\n= {r.Total_Revenue:,}",
      size=11, color=GOLD, mono=True)
arrow(ax, (8.75, top - 2 * H + H / 2), (7.95, top - 2 * H + H / 2), color=GOLD, width=1.8)
label(ax, 4.75, 3.35, "business_df['Units_Sold'] * business_df['Price_per_Unit']", size=11.5, mono=True)
save(fig, "pandas-intermediate-vectorized-columns.png")

# ---------------------------------------------------------------- 2. axis=0 versus axis=1
quarterly_sales = pd.DataFrame({
    'Q1': [100, 150, 200, 120, 180],
    'Q2': [110, 140, 220, 130, 190],
    'Q3': [120, 160, 210, 140, 200],
    'Q4': [130, 170, 230, 150, 210],
}, index=['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E'])
down, across = quarterly_sales.sum(), quarterly_sales.sum(axis=1)

fig, ax = canvas(12.4, 4.5)
CW, IW, top = 0.78, 1.15, 3.35
for x0, title in [(0.1, "quarters.sum()   # axis=0, the default"),
                  (6.6, "quarters.sum(axis=1)")]:
    frame_table(ax, x0, top, quarterly_sales, CW, IW)
    label(ax, x0 + IW + 2 * CW, top + H + 0.42, title, size=11.5, mono=True)
# left: arrows down each column, one result per column
x0 = 0.1
for j, c in enumerate(quarterly_sales.columns):
    cx = x0 + IW + j * CW + CW / 2
    arrow(ax, (cx, top - 5 * H - 0.02), (cx, top - 5 * H - 0.47), color=GOLD, width=1.8)
    cell(ax, x0 + IW + j * CW, top - 6 * H - 0.45, CW, down[c], GOLD_BG, bold=True, color=GOLD, mono=True)
label(ax, x0 + IW - 0.12, top - 6 * H - 0.45 + H / 2, "result", size=10, color=GOLD, ha="right")
label(ax, x0 + IW + 2 * CW, top - 7 * H - 0.6, "one value per column: collapses the rows", size=10.5,
      color=INK, bold=False, style="italic")
# right: arrows across each row, one result per row
x0 = 6.6
for i, rlab in enumerate(quarterly_sales.index):
    cy = top - (i + 1) * H + H / 2
    arrow(ax, (x0 + IW + 4 * CW + 0.02, cy), (x0 + IW + 4 * CW + 0.4, cy), color=GOLD, width=1.8)
    cell(ax, x0 + IW + 4 * CW + 0.44, top - (i + 1) * H, 0.85, across[rlab], GOLD_BG, bold=True, color=GOLD, mono=True)
cell(ax, x0 + IW + 4 * CW + 0.44, top, 0.85, "Total", GOLD_BG, bold=True, color=GOLD, mono=True)
label(ax, x0 + IW + 2.4 * CW, top - 7 * H - 0.6, "one value per row: lines up as a new column", size=10.5,
      color=INK, bold=False, style="italic")
save(fig, "pandas-intermediate-axis-direction.png")

# ---------------------------------------------------------------- 3 and 4. alignment and fill_value
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]}, index=[0, 1, 2])
df2 = pd.DataFrame({'B': [5, 10, 15, 20], 'C': [100, 200, 300, 400]}, index=[1, 2, 3, 4])
plain_sum, filled_sum = df1 + df2, df1.add(df2, fill_value=0)
both = lambda r, c: r in df1.index and c in df1.columns and r in df2.index and c in df2.columns
in_one = lambda r, c: (r in df1.index and c in df1.columns) != (r in df2.index and c in df2.columns)
in_kind = lambda r, c: "match" if both(r, c) else "plain"

for result, title, name, kind in [
    (plain_sum, "df1 + df2", "pandas-intermediate-alignment-nan.png",
     lambda r, c: "match" if both(r, c) else "nan"),
    (filled_sum, "df1.add(df2, fill_value=0)", "pandas-intermediate-fill-value.png",
     lambda r, c: "match" if both(r, c) else "fill" if in_one(r, c) else "nan"),
]:
    fig, ax = canvas(10.6, 3.5)
    top = 2.55
    frame_table(ax, 0.1, top, df1, 0.8, 0.4, in_kind, title="df1")
    label(ax, 2.35, top - 2.5 * H, "+", size=26)
    frame_table(ax, 2.6, top, df2, 0.8, 0.4, in_kind, title="df2")
    label(ax, 4.85, top - 2.5 * H, "=", size=26)
    frame_table(ax, 5.1, top, result, 0.8, 0.4, kind, title=title)
    # legend
    lx, ly = 8.15, top - 0.2
    entries = [(GOLD_BG, GOLD, "label in both: added"),
               ((FILL_BG, PURPLE, "label in one: 0 stands in") if "fill" in name else None),
               ("white", MUTE, "no partner: NaN" if "nan" in name else "in neither: still NaN")]
    for k, e in enumerate([e for e in entries if e]):
        ax.add_patch(Rectangle((lx, ly - k * 0.5), 0.32, 0.3, facecolor=e[0], edgecolor=HEADER, linewidth=1.5))
        label(ax, lx + 0.45, ly - k * 0.5 + 0.15, e[2], size=10, color=INK, bold=False, ha="left")
    save(fig, name)

# ---------------------------------------------------------------- 5. what r looks like
rng = np.random.default_rng(303)
n = 60
x = rng.uniform(0, 10, n)
xc = np.linspace(0, 10, n)
panels = [
    ("Close to +1", "rise together", x, x + rng.normal(0, 1.0, n)),
    ("Close to −1", "one rises, the other falls", x, 10 - x + rng.normal(0, 1.0, n)),
    ("Close to 0", "no linear pattern", x, np.random.default_rng(5).uniform(0, 10, n)),  # unrelated draw
    ("Close to 0", "but a strong curve", xc, (xc - 5) ** 2 / 2.5 + rng.normal(0, 0.6, n)),
]
fig, axes = plt.subplots(1, 4, figsize=(13, 3.7))
for a, (head, sub, px, y) in zip(axes, panels):
    r = pd.Series(px).corr(pd.Series(y))
    print(f"  {head}, {sub}: r = {r:.3f}")
    a.scatter(px, y, s=34, color=PURPLE, alpha=0.75, edgecolor="white", linewidth=0.7)
    a.set_facecolor(PALE)
    a.set_xticks([]); a.set_yticks([])
    for side in ["top", "right"]:
        a.spines[side].set_visible(False)
    for side in ["left", "bottom"]:
        a.spines[side].set_color(PURPLE); a.spines[side].set_linewidth(2)
    a.set_title(f"r = {r:.2f}".replace("-", "−") + f"\n{head}: {sub}", fontsize=12, color=PURPLE,
                fontweight="bold", loc="center", pad=10)
    a.set_xlabel("x", color=MUTE); a.set_ylabel("y", color=MUTE)
fig.tight_layout(w_pad=2.2)
save(fig, "pandas-intermediate-correlation-patterns.png")

# ---------------------------------------------------------------- 6. map versus replace
s = pd.Series(['Tech', 'Retail', 'Other'])
labels = {'Tech': 'Technology', 'Retail': 'Consumer Retail'}
mapped, replaced = s.map(labels), s.replace(labels)

fig, ax = canvas(12.2, 3.2)
top, W = 2.2, 1.9
def series(x0, values, title, kinds):
    label(ax, x0 + 0.35 + W / 2, top + H + 0.32, title, size=11.5, mono=True)
    cell(ax, x0 + 0.35, top, W, "value", HEADER, bold=True, color=PURPLE, mono=True)
    for i, v in enumerate(values):
        label(ax, x0 + 0.23, top - (i + 1) * H + H / 2, str(i), size=11, ha="right", mono=True)
        k = kinds[i]
        fill, color, bold = {"plain": (PALE, INK, False), "match": (GOLD_BG, GOLD, True),
                             "nan": ("white", MUTE, False)}[k]
        cell(ax, x0 + 0.35, top - (i + 1) * H, W, fmt(v) if pd.isna(v) else v, fill, bold=bold, color=color,
             mono=True, edge=HEADER if k == "nan" else "white")
series(0.0, s, "s", ["plain", "plain", "match"])
# dictionary box
ax.add_patch(FancyBboxPatch((2.75, top - 3 * H + 0.05), 3.3, 3 * H + 0.1, boxstyle="round,pad=0.08",
                            facecolor="white", edgecolor=PURPLE, linewidth=1.8))
label(ax, 4.4, top + H + 0.32, "labels", size=11.5, mono=True)
for i, (k, v) in enumerate(labels.items()):
    label(ax, 4.4, top - i * H - 0.02, f"'{k}' → '{v}'", size=10, color=INK, bold=False, mono=True)
label(ax, 4.4, top - 2 * H - 0.02, "no key for 'Other'", size=10, color=GOLD, bold=True, style="italic")
arrow(ax, (2.3, top - 1.5 * H), (2.7, top - 1.5 * H))
arrow(ax, (6.15, top - 1.0 * H), (6.6, top - 0.4 * H))
arrow(ax, (6.15, top - 2.0 * H), (6.6, top - 2.6 * H))
series(6.6, mapped, "s.map(labels)", ["plain", "plain", "nan"])
series(9.35, replaced, "s.replace(labels)", ["plain", "plain", "match"])
label(ax, 6.6 + 0.35 + W / 2, top - 4 * H - 0.05, "unmatched → NaN", size=10.5, color=INK, bold=False, style="italic")
label(ax, 9.35 + 0.35 + W / 2, top - 4 * H - 0.05, "unmatched → unchanged", size=10.5, color=INK, bold=False, style="italic")
save(fig, "pandas-intermediate-map-vs-replace.png")

# ---------------------------------------------------------------- 7. apply(axis=1) passes each row
financial_df = pd.DataFrame({'Revenue': [1000, 1500, 800], 'Expenses': [980, 1200, 790]})
def cap_expenses(row):
    return min(row['Expenses'], row['Revenue'] * 0.95)
capped = financial_df.apply(cap_expenses, axis=1)
row0 = financial_df.loc[0]

fig, ax = canvas(12.4, 2.9)
top = 1.95
frame_table(ax, 0.1, top, financial_df, 1.0, 0.35, lambda r, c: "match" if r == 0 else "plain",
            title="financial_df")
# the row as a Series
arrow(ax, (2.55, top - H / 2), (3.0, top - H / 2), color=GOLD)
label(ax, 4.45, top + H + 0.32, "row  (a Series)", size=11.5, mono=True)
for i, (k, v) in enumerate(row0.items()):
    label(ax, 4.2, top - i * H + H / 2, k, size=10.5, ha="right", mono=True)
    cell(ax, 4.3, top - i * H, 0.85, fmt(v), GOLD_BG, bold=True, color=GOLD, mono=True)
# the function call
arrow(ax, (5.25, top), (5.6, top), color=GOLD)
ax.add_patch(FancyBboxPatch((5.7, top - 0.55), 3.6, 1.2, boxstyle="round,pad=0.08",
                            facecolor="white", edgecolor=PURPLE, linewidth=1.8))
label(ax, 7.5, top + 0.38, "cap_expenses(row)", size=11.5, mono=True)
label(ax, 7.5, top - 0.02, f"min({fmt(row0.Expenses)}, {fmt(row0.Revenue)} × 0.95)", size=10.5, color=INK,
      bold=False, mono=True)
label(ax, 7.5, top - 0.38, f"= {fmt(capped[0])}", size=11, color=GOLD, mono=True)
# result
arrow(ax, (9.45, top), (9.95, top), color=GOLD)
res = pd.DataFrame({'Capped_Expenses': capped})
frame_table(ax, 10.35, top, res, 2.3, 0.0, lambda r, c: "match" if r == 0 else "plain")
label(ax, 6.2, -0.05, "Rows 1 and 2 go through the same call, one at a time: one returned value per row.",
      size=10.5, color=INK, bold=False, style="italic")
save(fig, "pandas-intermediate-apply-rows.png")

# ---------------------------------------------------------------- 8. the default, axis=0, passes each column
def value_range(column):
    return column.max() - column.min()
ranges = financial_df[['Revenue', 'Expenses']].apply(value_range)
col0 = financial_df['Revenue']

fig, ax = canvas(11.8, 2.9)
top = 1.95
frame_table(ax, 0.1, top, financial_df, 1.0, 0.35, lambda r, c: "match" if c == 'Revenue' else "plain",
            title="financial_df")
# the column as a Series
arrow(ax, (2.55, top - 1.5 * H), (3.0, top - 1.5 * H), color=GOLD)
label(ax, 3.95, top + H + 0.32, "column  (a Series)", size=11.5, mono=True)
for i, v in enumerate(col0):
    label(ax, 3.45, top - i * H + H / 2, str(i), size=10.5, ha="right", mono=True)
    cell(ax, 3.55, top - i * H, 0.85, fmt(v), GOLD_BG, bold=True, color=GOLD, mono=True)
# the function call
arrow(ax, (4.6, top - H / 2), (4.95, top - H / 2), color=GOLD)
ax.add_patch(FancyBboxPatch((5.05, top - 1.0), 3.3, 1.2, boxstyle="round,pad=0.08",
                            facecolor="white", edgecolor=PURPLE, linewidth=1.8))
label(ax, 6.7, top - 0.07, "value_range(column)", size=11.5, mono=True)
label(ax, 6.7, top - 0.47, f"{fmt(col0.max())} − {fmt(col0.min())}", size=10.5, color=INK, bold=False, mono=True)
label(ax, 6.7, top - 0.83, f"= {fmt(ranges['Revenue'])}", size=11, color=GOLD, mono=True)
# result: one value per column
arrow(ax, (8.55, top - H / 2), (9.0, top - H / 2), color=GOLD)
label(ax, 10.1, top + H + 0.32, "result  (a Series)", size=11.5, mono=True)
for i, (k, v) in enumerate(ranges.items()):
    label(ax, 9.95, top - i * H + H / 2, k, size=10.5, ha="right", mono=True)
    cell(ax, 10.05, top - i * H, 0.9, fmt(v), GOLD_BG if i == 0 else PALE, bold=i == 0,
         color=GOLD if i == 0 else INK, mono=True)
label(ax, 5.9, -0.05, "The Expenses column goes through the same call: one returned value per column.",
      size=10.5, color=INK, bold=False, style="italic")
save(fig, "pandas-intermediate-apply-columns.png")

# ---------------------------------------------------------------- 9. DataFrame.apply versus Series.apply
fig, ax = canvas(12.4, 3.5)
top = 2.35
first = lambda r, c: "match" if r == 0 else "plain"

# left panel: a whole row per call
label(ax, 2.75, top + H + 0.78, "DataFrame.apply(func, axis=1)", size=12, mono=True)
frame_table(ax, 0.1, top, financial_df, 1.0, 0.35, first, title="financial_df")
arrow(ax, (2.55, top - H / 2), (3.0, top - H / 2), color=GOLD)
label(ax, 4.15, top + H + 0.32, "row  (a Series)", size=11.5, mono=True)
for i, (k, v) in enumerate(financial_df.loc[0].items()):
    label(ax, 3.9, top - i * H + H / 2, k, size=10.5, ha="right", mono=True)
    cell(ax, 4.0, top - i * H, 0.9, fmt(v), GOLD_BG, bold=True, color=GOLD, mono=True)
label(ax, 2.6, top - 3 * H - 0.3, "one whole row per call", size=11, color=PURPLE)
label(ax, 2.6, top - 3 * H - 0.68, "inside the function: row['Revenue'], row['Expenses']",
      size=10.5, color=INK, bold=False, style="italic")

ax.plot([6.2, 6.2], [-0.1, top + H + 0.95], color=HEADER, linewidth=2)

# right panel: one value per call
label(ax, 9.5, top + H + 0.78, "Series.apply(func)", size=12, mono=True)
frame_table(ax, 6.7, top, financial_df[['Revenue']], 1.15, 0.35, first,
            title="financial_df['Revenue']", title_size=11.5)
for i, v in enumerate(financial_df['Revenue']):
    cy = top - i * H - H / 2
    arrow(ax, (8.3, cy), (8.8, cy), color=GOLD if i == 0 else MUTE, width=2.2 if i == 0 else 1.6)
    ax.add_patch(FancyBboxPatch((8.9, cy - H / 2 + 0.09), 2.5, H - 0.18, boxstyle="round,pad=0.03",
                                facecolor="white", edgecolor=PURPLE if i == 0 else HEADER, linewidth=1.6))
    label(ax, 9.5, cy, f"Call {i + 1}", size=10.5, color=PURPLE if i == 0 else MUTE, ha="right")
    label(ax, 9.7, cy, f"x = {fmt(v)}", size=10.5, color=GOLD if i == 0 else INK,
          bold=i == 0, ha="left", mono=True)
label(ax, 9.3, top - 3 * H - 0.3, "one value per call", size=11, color=PURPLE)
label(ax, 9.3, top - 3 * H - 0.68, "inside the function: x is a single number",
      size=10.5, color=INK, bold=False, style="italic")
save(fig, "pandas-intermediate-dataframe-vs-series-apply.png")

# ---------------------------------------------------------------- 10. apply versus a whole-column expression
revenue = financial_df['Revenue']
discounted = revenue * 0.9

fig, ax = canvas(12.9, 4.4)
top = 3.0
ax.plot([6.35, 6.35], [0.05, top + 1.45], color=HEADER, linewidth=2)

# left: one Python call per value
label(ax, 3.1, top + 1.3, "ROW BY ROW", size=12.5)
label(ax, 3.1, top + 0.85, "financial_df['Revenue'].apply(tenth_off)", size=11, mono=True, color=INK)
cell(ax, 0.6, top, 1.1, "Revenue", HEADER, bold=True, color=PURPLE, mono=True)
centers = [2.9, 1.9, 0.9]
for i, v in enumerate(revenue):
    ry = top - (i + 1) * H + H / 2
    label(ax, 0.5, ry, str(i), size=10.5, ha="right", mono=True)
    cell(ax, 0.6, top - (i + 1) * H, 1.1, fmt(v), PALE, mono=True)
    arrow(ax, (1.8, ry), (2.35, centers[i]), color=GOLD, width=1.8)
    ax.add_patch(FancyBboxPatch((2.45, centers[i] - 0.26), 3.4, 0.52, boxstyle="round,pad=0.06",
                                facecolor="white", edgecolor=PURPLE, linewidth=1.6))
    label(ax, 4.15, centers[i], f"tenth_off({fmt(v)}) = {fmt(discounted.iloc[i])}", size=10.5,
          color=INK, bold=False, mono=True)
label(ax, 3.1, 0.2, "one Python call for every value: the overhead repeats",
      size=10.5, color=INK, bold=False, style="italic")

# right: one operation on the whole array
label(ax, 9.7, top + 1.3, "WHOLE COLUMN", size=12.5)
label(ax, 9.7, top + 0.85, "financial_df['Revenue'] * 0.9", size=11, mono=True, color=INK)
def array_box(y, values, text_color, edge):
    ax.add_patch(FancyBboxPatch((7.0, y - 0.3), 5.4, 0.6, boxstyle="round,pad=0.06",
                                facecolor="white", edgecolor=edge, linewidth=1.8))
    label(ax, 9.7, y, "[ " + "   ".join(fmt(v) for v in values) + " ]", size=11.5,
          color=text_color, mono=True)
array_box(top - 0.05, revenue, INK, HEADER)
label(ax, 9.7, top + 0.45, "the whole column, stored as one array", size=10.5, color=MUTE, bold=False)
arrow(ax, (9.7, top - 0.43), (9.7, top - 0.72), color=GOLD)
ax.add_patch(FancyBboxPatch((7.6, top - 1.45), 4.2, 0.7, boxstyle="round,pad=0.06",
                            facecolor=PALE, edgecolor=PURPLE, linewidth=1.8))
label(ax, 9.7, top - 0.97, "one compiled array operation", size=11)
label(ax, 9.7, top - 1.28, "× 0.9", size=11, mono=True, color=GOLD)
arrow(ax, (9.7, top - 1.6), (9.7, top - 1.9), color=GOLD)
array_box(top - 2.25, discounted, GOLD, PURPLE)
label(ax, 9.7, 0.2, "one operation on the whole array: the loop runs in compiled code",
      size=10.5, color=INK, bold=False, style="italic")

label(ax, 6.35, -0.25, "Both give the same answer. pandas stores each column as a NumPy array, "
                       "and a column expression hands that array straight to NumPy.",
      size=11, color=PURPLE, bold=False, style="italic")
save(fig, "pandas-intermediate-apply-vs-vectorized.png")
