"""Draws the pictures for "Mehar und der kleine Spatz". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
FONT = "&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif"
GREEN = "#3f9a55"
RUMPEL = "#2f8a8a"  # Rumpel's teal saddle cloth


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def word(x, y, text, color="#e0912a", size=48):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FONT}" font-weight="800" '
            f'font-size="{size}" fill="{color}" stroke="#ffffff" stroke-width="6" paint-order="stroke">{text}</text>')


def woods(gid, time="day"):
    """A sunny forest clearing."""
    return [sky(time, gid), '<circle cx="520" cy="80" r="44" fill="#ffe38a"/>' if time == "day" else "",
            tree(470, 440, 1.1, "#3fa45e"), tree(570, 450, 0.9, "#2f8a4c"),
            '<rect y="430" width="600" height="170" fill="#6aa84f"/><path d="M0,440 Q300,410 600,440 V450 H0 Z" fill="#5a9a42"/>']


def big_tree(x=120, shake=False):
    """Piepsi's tree: a tall trunk on the left with a long branch reaching right to about (x+200, 250)."""
    wig = '<path d="M{0},{1} q-10,-6 -20,0 M{0},{2} q-10,-6 -20,0" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>'
    out = (f'<path d="M{x - 30},600 C{x - 24},450 {x - 20},300 {x - 14},140 L{x + 22},140 C{x + 26},300 {x + 30},450 {x + 40},600 Z" fill="#7a5236"/>'
           f'<path d="M{x + 10},280 C{x + 80},260 {x + 150},250 {x + 230},250" fill="none" stroke="#7a5236" stroke-width="16" stroke-linecap="round"/>'
           f'<circle cx="{x}" cy="120" r="100" fill="{GREEN}"/><circle cx="{x + 110}" cy="90" r="70" fill="#4cbf6b"/>'
           f'<circle cx="{x - 80}" cy="190" r="60" fill="#4cbf6b"/><circle cx="{x + 230}" cy="226" r="34" fill="{GREEN}"/>')
    if shake:
        out += wig.format(x - 40, 330, 360) + wig.format(x + 80, 330, 360)
    return out


def hold_nest(cx, cy, s=1, eggs=3):
    return nest(cx, cy, s, eggs)


def notes(x, y, color="#ffe680"):
    return "".join(f'<g transform="translate({x + dx} {y + dy})"><ellipse cx="0" cy="0" rx="7" ry="5" fill="{color}"/><path d="M6,0 V-22 q8,2 10,8" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round"/></g>'
                   for dx, dy in ((0, 0), (34, -26), (70, -6)))


def rumpel(x, y, s=1, flip=False, trunk="up", eyes="open"):
    inner = elephant(0, 0, 1, trunk=trunk, eyes=eyes, blanket=RUMPEL)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def stuck(x, y, s=1, eyes="open", trunk="up"):
    """Rumpel sunk in mud up to his tummy: the mud is drawn in front of his legs."""
    mud = (f'<path d="M{x - 170*s:.0f},{y - 60*s:.0f} Q{x:.0f},{y - 90*s:.0f} {x + 200*s:.0f},{y - 60*s:.0f} L{x + 230*s:.0f},{y + 30} L{x - 200*s:.0f},{y + 30} Z" fill="#7a5236"/>'
           + "".join(f'<circle cx="{x + dx*s:.0f}" cy="{y - 50*s + dy:.0f}" r="{r}" fill="none" stroke="#a07a52" stroke-width="3"/>' for dx, dy, r in ((-120, 0, 8), (60, 10, 6), (140, -4, 7))))
    return rumpel(x, y, s, trunk=trunk, eyes=eyes) + mud


def vine(x1, y1, x2, y2):
    return (f'<path d="M{x1},{y1} Q{(x1 + x2) / 2},{max(y1, y2) + 30} {x2},{y2}" fill="none" stroke="#3f8a3a" stroke-width="7" stroke-linecap="round"/>'
            + "".join(f'<ellipse cx="{x1 + (x2 - x1) * t:.0f}" cy="{y1 + (y2 - y1) * t + 18:.0f}" rx="9" ry="5" fill="#5cb85c" transform="rotate(-30 {x1 + (x2 - x1) * t:.0f} {y1 + (y2 - y1) * t + 18:.0f})"/>' for t in (0.2, 0.45, 0.7)))


pics = {}

pics["cover"] = scene(woods("sky-c") + [big_tree(110),
    nest(330, 262, 0.8), sparrow(338, 236, 0.7),
    rumpel(470, 590, 0.55, flip=True, trunk="down"),
    mehar(250, 590, 1.0, arms="wave", eyes="happy"),
    frog(90, 590, 0.7), bee(180, 360, 1.0), woodpecker(152, 470, 0.7),
])

# 1. Piepsi on her three eggs
pics["01"] = scene(woods("sky-1") + [big_tree(120),
    nest(340, 262, 1.0), sparrow(350, 232, 0.8),
    '<path d="M400,170 q20,-20 40,-6" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
    mehar(420, 590, 1.1, arms="wave", mouth="open", look=-5),
])

# 2. Rumms! Rumpel shakes the tree, the nest falls
fall = f'<g transform="translate(320 330) rotate(25)">{nest(0, 0, 0.9)}</g>'
pics["02"] = scene(woods("sky-2") + [big_tree(120, shake=True),
    fall, sparrow(410, 230, 0.8, wings="up", mood="sad"),
    rumpel(330, 590, 0.95, flip=True, trunk="up"),
    word(290, 130, "Rumms! Rumms!", "#e0912a", 46),
    mehar(540, 590, 0.8, arms="up", mouth="oh", look=-5),
])

# 3. Mehar catches the nest
pics["03"] = scene(woods("sky-3") + [big_tree(120),
    mehar(250, 590, 1.0, arms="up", mouth="open", look=2), nest(250, 372, 0.95),
    sparrow(340, 360, 0.7, wings="up"),
    rumpel(500, 590, 0.6, trunk="up", eyes="closed"),
    word(470, 300, "Ha ha!", "#9a9db0", 40),
    word(250, 130, "Puh!", "#e0912a", 50),
])

# 4. "Zusammen sind wir groß!"
pics["04"] = scene(woods("sky-4") + [big_tree(120),
    nest(340, 262, 1.0), sparrow(420, 250, 0.8, mood="sad"),
    mehar(330, 590, 1.25, arms="hold", mouth="open", look=3),
])

# 5. The team: Klopf, Summi, Quaki
pics["05"] = scene(woods("sky-5") + [tree(110, 470, 1.3, "#2f8a4c"),
    woodpecker(130, 330, 0.9),
    bee(470, 260, 1.6),
    rock(470, 600, 0.6), frog(470, 535, 1.0),
    mehar(300, 590, 1.1, arms="down", mouth="soft", look=4),
    sparrow(240, 380, 0.6, wings="up"),
    word(300, 130, "Wir machen mit!", "#e0912a", 40),
])

# 6. Summi hums a lullaby
pics["06"] = scene([sky("dusk", "sky-6"), tree(80, 470, 1.2, "#2f8a4c"), tree(560, 470, 1.1, GREEN),
    '<rect y="460" width="600" height="140" fill="#5a9a42"/>',
    rumpel(270, 590, 1.1, trunk="down", eyes="closed"),
    bee(400, 330, 1.2), notes(430, 280),
    zzz(470, 220),
    mehar(530, 590, 0.75, arms="down", eyes="happy"),
])

# 7. Tock-tock-tock! Rumpel spins around
pics["07"] = scene([sky("dusk", "sky-7"),
    tree(80, 480, 1.3, "#2f8a4c"), tree(520, 480, 1.3, GREEN),
    '<rect y="470" width="600" height="130" fill="#5a9a42"/>',
    woodpecker(96, 380, 0.7, pecking=True), woodpecker(504, 380, 0.7, flip=True, pecking=True),
    word(110, 250, "Tock!", "#ffe680", 34), word(490, 250, "Tock!", "#ffe680", 34),
    rumpel(300, 590, 0.85, trunk="up"),
    '<path d="M180,540 a120,30 0 1,0 240,0" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="10 10" opacity="0.7"/>',
    '<text x="300" y="330" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="48" fill="#ffffff">? ?</text>',
])

# 8. "Quak! Quak!" by a muddy hole
pics["08"] = scene([sky("dusk", "sky-8"), tree(540, 470, 1.2, GREEN),
    '<rect y="430" width="600" height="170" fill="#5a9a42"/>',
    mud_pit(170, 520, 150, 34),
    frog(170, 480, 0.9, croak=True),
    word(170, 380, "Quak! Quak!", "#ffe680", 40),
    rumpel(500, 590, 0.75, flip=True, trunk="up"),
    '<circle cx="330" cy="300" r="26" fill="#fffbe6"/><text x="330" y="313" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="34" fill="#e0912a">?</text>',
])

# 9. PLATSCH! Stuck in the mud
pics["09"] = scene([sky("dusk", "sky-9"), tree(70, 470, 1.2, "#2f8a4c"),
    '<rect y="430" width="600" height="170" fill="#5a9a42"/>',
    stuck(290, 590, 1.0, trunk="up"),
    "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#7a5236"/>' for x, y, r in ((130, 400, 12), (170, 360, 9), (440, 380, 11), (480, 340, 8), (300, 330, 7))),
    word(300, 130, "PLATSCH!", "#7a5236", 60),
    frog(540, 590, 0.6),
])

# 10. "Es tut mir leid, Piepsi."
pics["10"] = scene([sky("dusk", "sky-10"),
    '<rect y="430" width="600" height="170" fill="#5a9a42"/>',
    stuck(200, 600, 0.95, trunk="down"),
    '<path d="M304,482 q-5,10 0,13 q5,-3 0,-13 Z" fill="#7fb3ff"/>',
    mehar(470, 590, 1.0, arms="hold", mouth="soft", look=-4),
    sparrow(400, 360, 0.8, flip=True, wings="up"),
])

# 11. Hau-ruck! Everybody pulls
pics["11"] = scene([sky("day", "sky-11"), '<circle cx="520" cy="80" r="44" fill="#ffe38a"/>',
    '<rect y="430" width="600" height="170" fill="#6aa84f"/>',
    stuck(150, 600, 0.8, trunk="down"),
    vine(265, 560, 560, 470),
    mehar(410, 590, 0.95, arms="hold", mouth="open", look=-3),
    frog(500, 590, 0.6), woodpecker(560, 590, 0.55, flip=True),
    bee(470, 400, 0.9, flip=True), sparrow(530, 400, 0.6, flip=True, wings="up"),
    word(300, 130, "Hau-ruck! PLOPP!", "#e0912a", 46),
])

# 12. Back in bed; a sparrow on the window sill
pics["12"] = scene([bedroom("#2d2a5a"), window_frame(320, 60, 230, 230, "".join(night("sky-12w")) + moon(430, 150, 50, "sleepy")),
    sparrow(400, 306, 0.6, flip=True),
    mehar_in_bed(230, 470, 0.85, eyes="closed"),
    zzz(110, 370),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
