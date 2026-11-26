"""Draws the pictures for "Mehar and the Lion in the Well". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
STARS = [(70, 80, 9), (190, 150, 7), (300, 50, 10), (400, 190, 7), (540, 240, 8)]


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, r, "#ffe680") for x, y, r in STARS]


def night_jungle(gid):
    out = night(gid)
    out.append(tree(60, 470, 1.25, "#24563f", "#3b2a20") + tree(560, 470, 1.15, "#24563f", "#3b2a20"))
    out.append('<rect y="460" width="600" height="140" fill="#2f5a3a"/><path d="M0,470 Q300,440 600,470 V480 H0 Z" fill="#284e32"/>')
    return out


def reflection():
    """What you see in the well water: the moon and an upside-down angry lion."""
    return ('<rect x="-110" y="-180" width="220" height="60" fill="#1c2a4a"/>'
            + moon(60, -150, 12, "happy", glow=False)
            + f'<g transform="translate(-10 -150) scale(0.22 -0.22) translate(0 150)">{lion(0, 0, 1, "angry", crown=True)}</g>')


pics = {}

pics["cover"] = scene(night_jungle("sky-cover") + [
    moon(470, 110, 55, "happy"),
    well(380, 560, 0.85),
    lion(150, 560, 0.85, "proud"),
    bunny(510, 575, 0.7),
    mehar(300, 585, 1.05, arms="wave", eyes="happy"),
])

# 1. The magic book
pics["01"] = scene([bedroom("#2d2a5a"), window_frame(380, 60, 180, 210, "".join(night("sky-1w"))),
    mehar(230, 565, 1.45, arms="down", mouth="open", look=2),
    magic_book(230, 520, 0.6),
])

# 2. The jungle: today it is Hasi's turn
pics["02"] = scene(jungle("dusk", "sky-2") + [
    owl(80, 300, 0.7),
    elephant(430, 560, 0.75, trunk="down", eyes="closed"),
    bunny(270, 560, 1.0, ear_flop=True, eyes="closed"),
    '<path d="M232,470 l-12,-6 M310,470 l12,-6" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>',
    mehar(130, 570, 1.25, mouth="oh", look=4),
])

# 3. The lion roars
pics["03"] = scene(jungle("dusk", "sky-3") + [
    rock(300, 470, 1.6),
    lion(300, 300, 1.05, "roar"),
    '<path d="M410,140 q20,-10 40,0 M420,110 q30,-14 60,0 M180,140 q-20,-10 -40,0 M170,110 q-30,-14 -60,0" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.8"/>',
    bunny(110, 575, 0.75, ear_flop=True),
    owl(500, 560, 0.6, eyes="closed"),
])

# 4. Mehar whispers a plan
pics["04"] = scene(jungle("dusk", "sky-4") + [
    '<rect x="330" y="440" width="110" height="70" rx="12" fill="#8a5a3c"/><ellipse cx="385" cy="440" rx="55" ry="14" fill="#b07a52"/>',
    bunny(385, 445, 1.0),
    mehar(250, 575, 1.4, arms="down", mouth="soft", look=5),
    '<path d="M320,300 q14,-8 22,0 M326,286 q18,-12 30,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>',
    '<circle cx="490" cy="250" r="28" fill="#fffbe6"/><text x="490" y="262" text-anchor="middle" font-family="Baloo 2, sans-serif" font-weight="800" font-size="34" fill="#e0912a">!</text>',
])

# 5. Very, very slowly
pics["05"] = scene([sky("dusk", "sky-5"), '<circle cx="480" cy="420" r="70" fill="#ff9a5a" opacity="0.9"/>', moon(120, 110, 40, "sleepy"),
    hill("#5a9a42", 470, 50, "#4b8a38"),
    flower(380, 560, 1.3, PAINT["pink"]), flower(440, 570, 1.1, PAINT["purple"]), flower(520, 560, 1.2, PAINT["orange"]),
    bunny(330, 575, 0.9, eyes="closed"),
    zzz(360, 440, "#ffffff"),
    mehar(170, 580, 1.3, arms="down", eyes="happy", mouth="smile"),
])

# 6. Why are you late?
pics["06"] = scene(night_jungle("sky-6") + [
    moon(500, 90, 45, "happy"),
    rock(170, 520, 1.2),
    lion(170, 400, 0.9, "angry"),
    bunny(390, 575, 0.9, ear_flop=True),
    mehar(510, 585, 1.2, arms="down", mouth="soft", look=-5),
])

# 7. Show me this other lion!
pics["07"] = scene(night_jungle("sky-7") + [
    moon(470, 90, 45, "happy"),
    well(470, 560, 0.7),
    lion(140, 575, 0.8, "angry"),
    bunny(270, 585, 0.6),
    mehar(340, 590, 1.05, arms="up", mouth="open", look=6),
])

# 8. A lion in the water
pics["08"] = scene(night("sky-8") + [
    lion(300, 420, 1.0, "angry"),
    well(300, 640, 1.6, inside=reflection(), roof=False),
    '<path d="M140,250 q-20,-14 -36,4 M460,250 q20,-14 36,4" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.7"/>',
])

# 9. SPLASH!
splash = "".join(f'<path d="M{x},{y} q-7,12 0,16 q7,-4 0,-16 Z" fill="#9cc7ff"/>' for x, y in ((180, 330), (230, 290), (300, 270), (370, 290), (420, 330), (260, 250), (340, 245)))
in_water = ('<rect x="-110" y="-180" width="220" height="60" fill="#2a3f6a"/>'
            + f'<g transform="translate(0 -128) scale(0.42)">{lion(0, 0, 1, "sorry", crown=False, wet=True)}</g>')
pics["09"] = scene(night("sky-9") + [
    well(300, 640, 1.6, inside=in_water, roof=False),
    splash,
    '<text x="300" y="215" text-anchor="middle" font-family="Baloo 2, sans-serif" font-weight="800" font-size="56" fill="#9cc7ff">SPLASH!</text>',
])

# 10. Moti's trunk to the rescue
pics["10"] = scene(night_jungle("sky-10") + [
    moon(520, 90, 40, "happy"),
    well(380, 600, 1.0, roof=False, inside=('<rect x="-110" y="-180" width="220" height="60" fill="#2a3f6a"/>' + f'<g transform="translate(0 -128) scale(0.32)">{lion(0, 0, 1, "sorry", crown=False, wet=True)}</g>')),
    elephant(150, 590, 0.75, trunk="down"),
    '<path d="M258,470 C290,420 340,410 365,445" fill="none" stroke="#9fabc8" stroke-width="18" stroke-linecap="round"/>',
    bunny(520, 590, 0.6),
    mehar(470, 595, 0.95, arms="up", mouth="open", look=-5),
])

# 11. Sorry, and friends
basket = ('<path d="M-50,0 L-40,-40 L40,-40 L50,0 Z" fill="#c98a4b"/><path d="M-44,-20 H44" stroke="#a06d3b" stroke-width="3"/>'
          '<ellipse cx="-20" cy="-48" rx="16" ry="12" fill="#ffb13d"/><ellipse cx="10" cy="-52" rx="16" ry="12" fill="#ffc94d"/>'
          '<path d="M24,-46 q22,-24 30,0" fill="none" stroke="#ffe34d" stroke-width="10" stroke-linecap="round"/>')
pics["11"] = scene(jungle("day", "sky-11") + [
    lion(200, 570, 0.9, "happy", crown=False, wet=True),
    g(basket, 330, 575, 1),
    bunny(420, 575, 0.8),
    mehar(510, 585, 1.15, arms="wave", eyes="happy"),
    '<path d="M110,240 q20,-30 40,0 q20,-30 40,0 q-40,40 -40,40 q0,0 -40,-40 Z" fill="#ff7fb6" transform="translate(30 -60) scale(0.8)"/>',
])

# 12. Back home, a new picture in the book
pics["12"] = scene([bedroom("#2d2a5a"), window_frame(60, 50, 240, 260, "".join(night("sky-12w")) + moon(160, 140, 55, "sleepy")),
    mehar_in_bed(330, 450, 1.0, eyes="closed"),
    magic_book(430, 425, 0.55, glow=True, title=""),
    zzz(240, 370),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
