"""Draws the pictures for "Mehar and the Blue Jackal". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
FONT = "&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif"
BLUE = "#3a4fc8"


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def word(x, y, text, color="#3a4fc8", size=48):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FONT}" font-weight="800" '
            f'font-size="{size}" fill="{color}" stroke="#ffffff" stroke-width="6" paint-order="stroke">{text}</text>')


def yard(gid):
    """The dyer's yard: washing lines of coloured cloth."""
    cloths = "".join(f'<path d="M{x},120 h50 l-4,{70 + (i % 2) * 20} h-42 Z" fill="{c}"/>'
                     for i, (x, c) in enumerate(((60, "#ef5350"), (130, "#ffd23f"), (200, BLUE), (390, "#4cbf6b"), (460, "#ff7fb6"), (530, BLUE))))
    return [sky("day", gid), '<path d="M20,120 Q300,140 590,120" fill="none" stroke="#7a5236" stroke-width="3"/>', cloths,
            '<rect y="430" width="600" height="170" fill="#d9b98a"/><path d="M0,430 Q300,410 600,430 V440 H0 Z" fill="#c9a776"/>']


def banana_leaf(x, y, s=1, angle=0):
    return (f'<g transform="translate({x} {y}) rotate({angle}) scale({s})"><path d="M0,0 C-20,-60 -10,-140 30,-180 C50,-120 40,-50 0,0 Z" fill="#4cbf6b"/>'
            '<path d="M0,0 C10,-60 20,-120 30,-180" fill="none" stroke="#2f8a4c" stroke-width="4"/></g>')


def mango_pile(x, y, s=1):
    return g("".join(f'<ellipse cx="{dx}" cy="{dy}" rx="16" ry="12" fill="{c}"/>' for dx, dy, c in
                     ((-30, 0, "#ffb13d"), (0, 0, "#ffc94d"), (30, 0, "#ffb13d"), (-15, -18, "#ffc94d"), (15, -18, "#ffb13d"))), x, y, s)


pics = {}

pics["cover"] = scene([sky("night", "sky-c"), sparkles(DOTS), moon(450, 120, 60, "happy"),
    hill("#2f5a3a", 470, 40, "#284e32"),
    dye_vat(120, 590, 0.6),
    jackal(300, 560, 1.15, BLUE, "proud", crown=True),
    mehar(470, 590, 1.05, arms="wave", eyes="happy", brush=BLUE),
])

# 1. The dyer's yard
pics["01"] = scene(yard("sky-1") + [
    dye_vat(110, 560, 0.7, "#ef5350"), dye_vat(470, 560, 0.7, "#ffd23f"), dye_vat(300, 600, 0.9, BLUE),
    mehar(300, 470, 1.0, arms="up", mouth="open"),
    paintbrush(180, 420, -30, BLUE, 1.2),
])

# 2. SPLOSH! Neelu falls in
legs_up = f'<g transform="translate(300 320) rotate(175) scale(0.9)">{jackal(0, 0, 1)}</g>'
pics["02"] = scene(yard("sky-2") + [
    legs_up,
    dye_vat(300, 600, 1.3, BLUE, splash=True),
    word(300, 90, "SPLOSH!", BLUE, 60),
    mehar(510, 590, 1.0, arms="up", mouth="oh", look=-5),
])

# 3. "I am King Neelu!"
pics["03"] = scene(jungle("day", "sky-3") + [
    rock(300, 500, 1.1),
    jackal(290, 400, 1.0, BLUE, "proud", drips=True),
    bunny(100, 570, 0.8), owl(500, 300, 0.6),
    elephant(430, 600, 0.55, trunk="up"),
    mehar(180, 590, 0.95, arms="down", mouth="soft", look=4),
])

# 4. Fan me!
pics["04"] = scene(jungle("day", "sky-4") + [
    rock(250, 500, 1.1),
    jackal(240, 400, 1.0, BLUE, "proud", crown=True),
    mango_pile(120, 560, 1.2),
    lion(450, 580, 0.8, "sorry", crown=False),
    banana_leaf(380, 430, 1.0, -30),
    mehar(100, 590, 0.9, arms="down", mouth="soft", look=5),
    word(240, 130, "Fan me!", "#e0912a", 44),
])

# 5. Why not just be yourself?
pics["05"] = scene(jungle("dusk", "sky-5") + [
    jackal(380, 580, 1.4, BLUE, "sorry", crown=True),
    mehar(150, 590, 1.3, arms="down", mouth="soft", look=5),
    '<path d="M250,300 q14,-8 22,0 M256,286 q18,-12 30,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>',
])

# 6. The jackals sing to the moon
howlers = "".join(f'<g transform="translate({x} {y}) scale({s})"><path d="M-20,0 C-20,-30 -10,-44 0,-46 L6,-66 L12,-48 C20,-46 24,-36 22,0 Z" fill="#1c2549"/></g>' for x, y, s in ((440, 330, 1.2), (500, 320, 1.0), (550, 335, 1.1)))
pics["06"] = scene(night("sky-6") + [moon(480, 140, 60, "happy"),
    '<path d="M300,340 Q450,300 600,330 V600 H300 Z" fill="#24305a"/>', howlers,
    word(490, 260, "Aa-ooo!", "#ffe680", 34),
    hill("#2f5a3a", 500, 30),
    jackal(170, 580, 1.15, BLUE, "scared", crown=True),
    '<circle cx="300" cy="300" r="26" fill="#fffbe6"/><text x="300" y="313" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="34" fill="#3f7be8">?</text>',
])

# 7. AAA-OOO!
howling = f'<g transform="translate(300 560) rotate(-20) scale(1.1)">{jackal(0, 0, 1, BLUE, "scared")}</g>'
pics["07"] = scene(night("sky-7") + [moon(480, 120, 55, "happy"),
    hill("#2f5a3a", 500, 30),
    howling,
    word(300, 110, "AAA-OOO!", "#ffe680", 56),
    owl(90, 580, 0.7, wings="up"), bunny(520, 590, 0.8),
])

# 8. Mehar stands up for Neelu
pics["08"] = scene(jungle("dusk", "sky-8") + [
    lion(470, 580, 0.95, "angry", crown=False),
    jackal(90, 590, 0.95, BLUE, "sorry"),
    mehar(270, 590, 1.15, arms="hold", mouth="open", look=4),
])

# 9. Washing the blue away
pics["09"] = scene([sky("day", "sky-9"), '<circle cx="520" cy="80" r="44" fill="#ffe38a"/>', hill("#6aa84f", 380, 30),
    river(430),
    '<path d="M150,430 q80,40 180,10" fill="none" stroke="#5a6fe0" stroke-width="10" stroke-linecap="round" opacity="0.6"/>',
    jackal(220, 500, 1.0, mood="happy"),
    water_over(100, 360, 470),
    mehar(420, 520, 1.0, arms="up", eyes="happy", mouth="open", legs=False),
    water_over(340, 520, 480),
    bunny(560, 380, 0.6), lion(80, 380, 0.5, "happy", crown=False),
    "".join(f'<path d="M{x},{y} q-7,12 0,16 q7,-4 0,-16 Z" fill="#9cc7ff"/>' for x, y in ((180, 330), (300, 300), (360, 340), (470, 330))),
])

# 10. Back home, a painting of Neelu singing to the moon
easel = ('<path d="M440,470 L480,250 M560,470 L520,250 M500,470 V260" stroke="#8a5a3c" stroke-width="8" stroke-linecap="round"/>'
         '<rect x="420" y="230" width="160" height="140" rx="6" fill="#fffdf4" stroke="#d8cfae" stroke-width="3"/>'
         '<rect x="430" y="240" width="140" height="120" fill="#2b2f7a"/>' + moon(540, 270, 18, "happy", glow=False)
         + jackal(470, 355, 0.4, mood="happy"))
pics["10"] = scene([bedroom("#2d2a5a"), window_frame(40, 50, 220, 240, "".join(night("sky-10w")) + moon(150, 140, 50, "sleepy")),
    mehar_in_bed(240, 470, 0.9, eyes="closed"),
    easel,
    zzz(150, 390),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
