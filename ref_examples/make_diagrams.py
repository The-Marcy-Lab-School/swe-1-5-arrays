"""
Regenerates the diagrams in this folder.

    python3 -m pip install matplotlib
    python3 ref_examples/make_diagrams.py

You do not need to run this to do the assignment. It is kept here so the
images can be rebuilt if they ever need changing.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

INK = "#1c1d1f"
MUTED = "#6b7280"
ACCENT = "#1d4ed8"
WARN = "#b91c1c"
OK = "#047857"
MONO = {"family": "monospace"}


def box(ax, x, y, w, h, label, edge=INK, face="white", fontsize=11):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02",
        linewidth=1.6, edgecolor=edge, facecolor=face, zorder=2,
    ))
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=fontsize, color=INK, zorder=3, **MONO)


def arrow(ax, start, end, color=ACCENT, style="-|>"):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle=style, mutation_scale=16,
        linewidth=1.6, color=color, zorder=4,
    ))


def new_panel(ax, title, color):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.text(0.2, 5.6, title, fontsize=12, color=color, fontweight="bold")


def rebinding_diagram(path):
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 3.6))

    new_panel(left, "lst = []   rebinds the name", WARN)
    left.text(0.2, 4.9, "the caller's list is untouched", fontsize=9.5, color=MUTED)
    box(left, 0.2, 3.2, 2.2, 0.9, "nums")
    box(left, 5.2, 3.2, 4.2, 0.9, "[1, 2, 3]")
    arrow(left, (2.4, 3.65), (5.2, 3.65))
    box(left, 0.2, 1.1, 2.2, 0.9, "lst", edge=WARN)
    box(left, 5.2, 1.1, 4.2, 0.9, "[]", edge=WARN)
    arrow(left, (2.4, 1.55), (5.2, 1.55), color=WARN)

    new_panel(right, "lst.clear()   changes the list", OK)
    right.text(0.2, 4.9, "both names see the change", fontsize=9.5, color=MUTED)
    box(right, 0.2, 3.2, 2.2, 0.9, "nums")
    box(right, 0.2, 1.1, 2.2, 0.9, "lst")
    box(right, 5.2, 2.15, 4.2, 0.9, "[]", edge=OK)
    arrow(right, (2.4, 3.65), (5.2, 2.75), color=OK)
    arrow(right, (2.4, 1.55), (5.2, 2.45), color=OK)

    fig.tight_layout()
    fig.savefig(path, dpi=160, facecolor="white")
    plt.close(fig)


def aliasing_diagram(path):
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    new_panel(ax, "Two names can point at one list", ACCENT)
    ax.text(0.2, 4.9, "other = nums  does not copy anything",
            fontsize=9.5, color=MUTED)

    box(ax, 0.2, 3.1, 2.2, 0.9, "nums")
    box(ax, 0.2, 1.3, 2.2, 0.9, "other")
    box(ax, 5.0, 2.2, 4.4, 0.9, "[1, 2, 3, 4]")
    arrow(ax, (2.4, 3.55), (5.0, 2.85))
    arrow(ax, (2.4, 1.75), (5.0, 2.45))
    ax.text(5.0, 1.4, "other.append(4) changes what\nboth names point at",
            fontsize=9.5, color=MUTED)

    fig.tight_layout()
    fig.savefig(path, dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    from pathlib import Path

    here = Path(__file__).parent
    rebinding_diagram(here / "rebinding-vs-mutating.png")
    aliasing_diagram(here / "two-names-one-list.png")
    print("wrote rebinding-vs-mutating.png and two-names-one-list.png")
