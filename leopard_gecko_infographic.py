"""
Leopard Gecko Care Dashboard
----------------------------
A Python data-visualisation project exploring key leopard gecko
care requirements and biological characteristics.

Technologies:
    - Python
    - Pandas
    - Matplotlib

Author: Your Name
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


# ============================================================
# 1. DATA
# ============================================================

facts = {
    "Average length (cm)": 25,
    "Typical lifespan (years)": 15,
    "Warm zone (°C)": 31,
    "Cool zone (°C)": 24,
}

diet = pd.DataFrame({
    "Food": [
        "Crickets",
        "Dubia roaches",
        "Mealworms",
        "Superworms"
    ],
    "Frequency": [
        "Regular",
        "Regular",
        "Regular",
        "Occasional"
    ]
})


# ============================================================
# 2. COLOUR PALETTE
# ============================================================

BG = "#F7F3EC"
CARD = "#FFFFFF"
TEXT = "#2D2926"
MUTED = "#77716B"
ACCENT = "#B8753D"
GREEN = "#607A5B"
LIGHT_ACCENT = "#EBD8C4"


# ============================================================
# 3. FIGURE SETUP
# ============================================================

fig = plt.figure(figsize=(12, 15), facecolor=BG)

# Main canvas
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 150)
ax.axis("off")


# ============================================================
# 4. HELPER FUNCTIONS
# ============================================================

def card(x, y, width, height, colour=CARD):
    """Create a rounded information card."""
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.6,rounding_size=2",
        linewidth=0,
        facecolor=colour
    )
    ax.add_patch(patch)


def text(
    x,
    y,
    value,
    size=12,
    weight="normal",
    colour=TEXT,
    align="left"
):
    """Add consistently formatted text."""
    ax.text(
        x,
        y,
        value,
        fontsize=size,
        fontweight=weight,
        color=colour,
        ha=align,
        va="center"
    )


# ============================================================
# 5. HEADER
# ============================================================

text(
    8, 140,
    "LEOPARD GECKO",
    size=30,
    weight="bold"
)

text(
    8, 134,
    "A data-driven visual guide to Eublepharis macularius",
    size=13,
    colour=MUTED
)

# Accent line
ax.plot(
    [8, 92],
    [130, 130],
    linewidth=3,
    color=ACCENT
)


# ============================================================
# 6. KEY METRICS
# ============================================================

metrics = [
    ("AVERAGE LENGTH", "25 cm"),
    ("TYPICAL LIFESPAN", "15 yrs"),
    ("WARM ZONE", "31°C"),
    ("COOL ZONE", "24°C"),
]

x_positions = [8, 29, 50, 71]

for x, (label, value) in zip(x_positions, metrics):

    card(x, 112, 18, 14, LIGHT_ACCENT)

    text(
        x + 2,
        122,
        label,
        size=8,
        weight="bold",
        colour=GREEN
    )

    text(
        x + 2,
        116,
        value,
        size=18,
        weight="bold"
    )


# ============================================================
# 7. TEMPERATURE VISUALISATION
# ============================================================

card(8, 82, 50, 25)

text(
    11,
    101,
    "TEMPERATURE GRADIENT",
    size=11,
    weight="bold",
    colour=GREEN
)

text(
    11,
    96,
    "A thermal gradient allows the gecko to regulate its",
    size=10,
    colour=MUTED
)

text(
    11,
    92,
    "body temperature by moving between warmer and cooler areas.",
    size=10,
    colour=MUTED
)

# Temperature bar
bar_x = 13
bar_y = 86
bar_width = 40

ax.plot(
    [bar_x, bar_x + bar_width],
    [bar_y, bar_y],
    linewidth=12,
    solid_capstyle="round",
    color=LIGHT_ACCENT
)

# Warm marker
ax.scatter(
    bar_x + bar_width * 0.78,
    bar_y,
    s=180,
    color=ACCENT,
    zorder=5
)

# Cool marker
ax.scatter(
    bar_x + bar_width * 0.25,
    bar_y,
    s=180,
    color=GREEN,
    zorder=5
)

text(
    bar_x,
    83,
    "Cool zone\n22–26°C",
    size=9,
    colour=GREEN
)

text(
    bar_x + bar_width,
    83,
    "Warm zone\n30–32°C",
    size=9,
    colour=ACCENT,
    align="right"
)


# ============================================================
# 8. DIET DATA
# ============================================================

card(62, 80, 30, 27)

text(
    65,
    100,
    "DIET",
    size=11,
    weight="bold",
    colour=GREEN
)

text(
    65,
    97,
    "Common feeder insects",
    size=10,
    colour=MUTED
)

# Simple horizontal visualisation
food_scores = {
    "Crickets": 90,
    "Dubia roaches": 90,
    "Mealworms": 75,
    "Superworms": 45
}

y = 94

for food, score in food_scores.items():

    text(
        65,
        y,
        food,
        size=8
    )

    ax.plot(
        [65, 65 + score / 5],
        [y - 2, y - 2],
        linewidth=5,
        solid_capstyle="round",
        color=ACCENT
    )

    y -= 3.2


# ============================================================
# 9. HABITAT
# ============================================================

card(8, 51, 84, 24)

text(
    11,
    69,
    "NATURAL HABITAT",
    size=11,
    weight="bold",
    colour=GREEN
)

text(
    11,
    63,
    "Leopard geckos are terrestrial reptiles native to dry and rocky",
    size=11
)

text(
    11,
    59,
    "regions of Afghanistan, Pakistan, Iran and parts of northwest India.",
    size=11
)

text(
    11,
    55,
    "Their natural environment influences their preference for warm hides,",
    size=10,
    colour=MUTED
)

text(
    11,
    52,
    "secure shelters and relatively dry conditions.",
    size=10,
    colour=MUTED
)


# ============================================================
# 10. BIOLOGY
# ============================================================

card(8, 23, 40, 24, LIGHT_ACCENT)

text(
    11,
    42,
    "BIOLOGY",
    size=11,
    weight="bold",
    colour=GREEN
)

biology_facts = [
    "Movable eyelids",
    "Fat-storing tail",
    "Terrestrial lifestyle",
    "No adhesive toe pads"
]

y = 37

for item in biology_facts:
    text(
        12,
        y,
        f"• {item}",
        size=9.5
    )
    y -= 3.8


# ============================================================
# 11. RESPONSIBLE CARE
# ============================================================

card(52, 23, 40, 24)

text(
    55,
    42,
    "RESPONSIBLE CARE",
    size=11,
    weight="bold",
    colour=GREEN
)

care_points = [
    "Provide multiple hides",
    "Maintain a temperature gradient",
    "Offer appropriately sized insects",
    "Provide fresh water",
    "Monitor weight and behaviour"
]

y = 38

for item in care_points:
    text(
        56,
        y,
        f"• {item}",
        size=8.5
    )
    y -= 3.3


# ============================================================
# 12. FOOTER
# ============================================================

ax.plot(
    [8, 92],
    [17, 17],
    linewidth=1,
    color=LIGHT_ACCENT
)

text(
    8,
    12,
    "PYTHON DATA VISUALISATION PROJECT",
    size=8,
    weight="bold",
    colour=ACCENT
)

text(
    92,
    12,
    "Python • Pandas • Matplotlib",
    size=8,
    colour=MUTED,
    align="right"
)

text(
    50,
    5,
    "Created for educational purposes • Always research current veterinary guidance",
    size=8,
    colour=MUTED,
    align="center"
)


# ============================================================
# 13. EXPORT
# ============================================================

plt.savefig(
    "leopard_gecko_infographic.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=BG
)

plt.show()