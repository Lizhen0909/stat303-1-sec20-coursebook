"""Draw images/join-types.png for the Combining Datasets chapter.

    python teaching-materials/figures/make_join_types_diagram.py   (run from the repository root)

Two small fellowship tables share the key FellowshipID; the four panels show which
rows each how= keeps. Purple rows match in both tables, blue rows exist only on the
left, gold rows only on the right, and NaN marks values with no partner.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

PURPLE, PALE, HEADER, INK = "#4E2A84", "#F0EBF7", "#E3D9F0", "#231F2E"
BLUE, BLUE_BG, GOLD, GOLD_BG, GREY = "#2B5C8A", "#E4EEF7", "#8F5F0E", "#F7EFDF", "#8A83A0"

left = [(1001, "Hiding"), (1002, "Gardening"), (1003, "Spells"), (1004, "Fireworks")]
right = [(1001, 50), (1002, 39), (1006, 2931), (1007, 6520), (1008, 51)]
skills = dict(left); ages = dict(right)
both = [k for k in skills if k in ages]
left_only = [k for k in skills if k not in ages]
right_only = [k for k in ages if k not in skills]
kind = {**{k: "both" for k in both}, **{k: "left" for k in left_only}, **{k: "right" for k in right_only}}
style = {"both": (PALE, INK), "left": (BLUE_BG, BLUE), "right": (GOLD_BG, GOLD)}

H = 0.34
fig, ax = plt.subplots(figsize=(13, 6.6))
ax.set_xlim(0, 13); ax.set_ylim(0.55, 6.6); ax.axis("off")

def cell(x, y, w, text, fill, color=INK, bold=False, mono=False):
    ax.add_patch(Rectangle((x, y), w, H, facecolor=fill, edgecolor="white", linewidth=1.5))
    ax.text(x + w / 2, y + H / 2, str(text), ha="center", va="center", fontsize=8.5 if bold else 9.5,
            color=color, fontweight="bold" if bold else "normal",
            family="DejaVu Sans Mono" if mono else "DejaVu Sans")

def table(x0, ytop, widths, header, rows):
    x = x0
    for w, h in zip(widths, header):
        cell(x, ytop, w, h, HEADER, PURPLE, bold=True); x += w
    for i, (k, *vals) in enumerate(rows):
        fill, color = style[kind[k]]
        x = x0
        for w, v in zip(widths, [k, *vals]):
            cell(x, ytop - (i + 1) * H, w, v, fill, GREY if v == "NaN" else color); x += w

# Inputs
ax.text(1.55, 6.3, "skills (left)", ha="center", fontsize=12, fontweight="bold", color=PURPLE)
table(0.3, 5.8, [1.3, 1.3], ["FellowshipID", "Skills"], left)
ax.text(4.75, 6.3, "ages (right)", ha="center", fontsize=12, fontweight="bold", color=PURPLE)
table(3.7, 5.8, [1.3, 1.1], ["FellowshipID", "Age"], right)
ax.text(7.2, 5.55, "skills.merge(ages, on=\"FellowshipID\", how=...)", ha="left", fontsize=11.5,
        family="DejaVu Sans Mono", color=INK, fontweight="bold")
for i, (lab, col, bg) in enumerate([("in both", INK, PALE), ("left only", BLUE, BLUE_BG), ("right only", GOLD, GOLD_BG)]):
    ax.add_patch(Rectangle((7.2 + i * 1.9, 4.95), 0.32, 0.26, facecolor=bg, edgecolor=col))
    ax.text(7.6 + i * 1.9, 5.08, lab, va="center", fontsize=10, color=col)

# Results
def rows_for(how):
    keys = {"inner": both, "left": list(skills), "right": list(ages),
            "outer": sorted(set(skills) | set(ages))}[how]
    return [(k, skills.get(k, "NaN"), ages.get(k, "NaN")) for k in keys]

for j, how in enumerate(["inner", "left", "right", "outer"]):
    x0 = 0.3 + j * 3.2
    r = rows_for(how)
    ax.text(x0 + 1.5, 3.62, f'how="{how}"  →  {len(r)} rows', ha="center", fontsize=11.5,
            fontweight="bold", color=PURPLE, family="DejaVu Sans Mono")
    table(x0, 3.12, [1.25, 1.0, 0.75], ["FellowshipID", "Skills", "Age"], r)

fig.savefig("images/join-types.png", dpi=200, bbox_inches="tight", facecolor="white")
print("wrote images/join-types.png")
