"""Draws the pictures for "Mehar and the Moon in the Lake". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
FONT = "&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif"
KING = "#7a4fc8"  # Gajraj's purple saddle cloth (Moti's is red)


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def word(x, y, text, color="#3f7be8", size=48):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FONT}" font-weight="800" '
            f'font-size="{size}" fill="{color}" stroke="#ffffff" stroke-width="6" paint-order="stroke">{text}</text>')


def gajraj(x, y, s=1, flip=False, trunk="up", eyes="open", crown=True):
    """Gajraj the elephant king: the kit elephant with a purple cloth and a little gold crown."""
    inner = elephant(0, 0, 1, trunk=trunk, eyes=eyes, blanket=KING)
    if crown:
        inner += '<path d="M72,-168 L72,-190 L84,-178 L94,-196 L104,-178 L116,-190 L116,-168 Z" fill="#ffd23f" stroke="#d49a12" stroke-width="2"/>'
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def burrow(x, y, s=1, squashed=False):
    """A bunny burrow: a little earth mound with a round door."""
    if squashed:
        inner = ('<path d="M-60,0 C-50,-16 -34,-8 -22,-20 C-8,-6 8,-24 24,-10 C36,-18 52,-6 60,0 Z" fill="#a8774a"/>'
                 '<ellipse cx="0" cy="-4" rx="34" ry="9" fill="#7a5236" opacity="0.6"/>'
                 '<ellipse cx="-44" cy="-4" rx="8" ry="4" fill="#8a5a3c"/><ellipse cx="44" cy="-2" rx="6" ry="3" fill="#8a5a3c"/>')
    else:
        inner = ('<path d="M-54,0 C-54,-56 54,-56 54,0 Z" fill="#a8774a"/>'
                 '<path d="M-18,0 C-18,-28 18,-28 18,0 Z" fill="#3b2a20"/>'
                 '<path d="M-40,-30 q6,-10 14,-12" fill="none" stroke="#c99a6a" stroke-width="4" stroke-linecap="round"/>')
    return g(inner, x, y, s)


def lake(y=400, night_=True):
    """A lake from the waterline y down to the bottom."""
    return river(y, "#2f6fb0" if night_ else "#3f8fd0", "#6fb0e8" if night_ else "#7fc0ee")


def shore(y=400):
    return f'<path d="M0,{y - 30} Q300,{y - 50} 600,{y - 30} V{y + 6} H0 Z" fill="#4f8a3f"/>'


def dust(x, y, s=1):
    return g("".join(f'<circle cx="{dx}" cy="{dy}" r="{r}" fill="#e8d6b0" opacity="0.85"/>' for dx, dy, r in ((-24, 0, 16), (0, -12, 20), (26, -2, 14), (8, 8, 12))), x, y, s)


def footprint(x, y, s=1):
    return g('<ellipse cx="0" cy="0" rx="30" ry="12" fill="#6b4a2e" opacity="0.5"/>'
             + "".join(f'<ellipse cx="{dx}" cy="-10" rx="6" ry="4" fill="#6b4a2e" opacity="0.5"/>' for dx in (-16, 0, 16)), x, y, s)


def dry_tree(x, y, s=1):
    return g('<path d="M-8,0 L-6,-120 M-6,-80 L-40,-120 M-6,-100 L30,-140 M20,-128 L34,-118" fill="none" stroke="#7a5236" stroke-width="10" stroke-linecap="round"/>'
             '<circle cx="-40" cy="-124" r="8" fill="#b59a5a"/><circle cx="32" cy="-144" r="10" fill="#b59a5a"/>', x, y, s)


def hug():
    return '<path d="M0,0 q-6,-8 -12,0 q6,10 12,14 q6,-4 12,-14 q-6,-8 -12,0 Z" fill="#ff7fb6"/>'


pics = {}

pics["cover"] = scene(night("sky-c") + [moon(470, 120, 60, "happy"),
    shore(400), lake(400), moon_in_water(420, 480, 46),
    rock(150, 420, 0.7),
    bunny(150, 345, 0.8),
    mehar(260, 430, 1.0, arms="wave", eyes="happy"),
    gajraj(470, 405, 0.6, flip=True, trunk="down"),
])

# 1. A dry, dusty jungle
pics["01"] = scene([sky("day", "sky-1"), '<circle cx="480" cy="110" r="62" fill="#ffcf5c"/><circle cx="480" cy="110" r="90" fill="#ffcf5c" opacity="0.25"/>',
    '<rect y="430" width="600" height="170" fill="#d9b98a"/><path d="M0,440 Q300,410 600,440 V450 H0 Z" fill="#c9a776"/>',
    dry_tree(70, 440, 1.0), dry_tree(540, 440, 0.8),
    pond(160, 520, 110, 26, dry=True),
    gajraj(390, 560, 0.75, trunk="down"),
    mehar(130, 590, 0.9, arms="down", mouth="oh", look=5),
    "".join(f'<path d="M{x},{y} q-6,10 0,14 q6,-4 0,-14 Z" fill="#9cc7ff"/>' for x, y in ((92, 360), (170, 370))),
])

# 2. STOMP! over the burrows
pics["02"] = scene([sky("dusk", "sky-2"), moon(530, 200, 40, "sad"),
    '<rect y="400" width="600" height="200" fill="#4f8a3f"/>', lake(500, True), moon_in_water(470, 550, 30),
    burrow(90, 480, 0.9, squashed=True), burrow(330, 490, 0.8, squashed=True), burrow(470, 470, 0.7),
    gajraj(210, 480, 0.85),
    dust(90, 460, 1.2), dust(300, 470, 1.0),
    word(300, 130, "STOMP! STOMP!", "#7a4fc8", 52),
    bunny(560, 480, 0.55, ear_flop=True), bunny(40, 560, 0.5, ear_flop=True),
])

# 3. Hasi's squashed home
pics["03"] = scene(night("sky-3") + [moon(480, 120, 50, "sad"),
    hill("#2f5a3a", 470, 30),
    burrow(150, 520, 1.3, squashed=True),
    footprint(100, 560, 1.2), footprint(260, 575, 1.0), footprint(420, 560, 1.1),
    bunny(340, 560, 1.15, ear_flop=True),
    '<path d="M368,488 q-4,8 0,10 q4,-2 0,-10 Z" fill="#7fb3ff"/><path d="M324,488 q-4,8 0,10 q4,-2 0,-10 Z" fill="#7fb3ff"/>',
    mehar(450, 590, 1.1, arms="hold", mouth="soft", look=-4),
    g(hug(), 400, 370, 1.4),
])

# 4. The moon up there and the moon down here
pics["04"] = scene(night("sky-4") + [moon(300, 120, 66, "happy"),
    shore(400), lake(400), moon_in_water(300, 490, 52),
    '<path d="M300,200 C330,280 330,380 300,450" fill="none" stroke="#fff3c4" stroke-width="3" stroke-dasharray="6 10" opacity="0.6"/>',
    mehar(120, 440, 1.0, arms="up", mouth="open", look=5),
    bunny(500, 400, 0.75),
    '<circle cx="200" cy="230" r="26" fill="#fffbe6"/><text x="200" y="244" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="36" fill="#3f7be8">!</text>',
])

# 5. Hasi on the rock: "I bring a message from the Moon!"
pics["05"] = scene(night("sky-5") + [moon(110, 100, 50, "happy"),
    shore(470), lake(470), moon_in_water(150, 540, 34),
    rock(150, 470, 0.9),
    bunny(150, 365, 0.9, ear_flop=False),
    '<path d="M196,300 q20,-14 34,-4 M200,320 q26,-6 38,8" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
    gajraj(500, 480, 0.8, flip=True),
    mehar(285, 500, 0.75, arms="down", mouth="smile", look=-4, legs=True),
])

# 6. Gajraj peeks into the lake
pics["06"] = scene(night("sky-6") + [moon(520, 90, 46, "happy"),
    shore(380), lake(380), moon_in_water(360, 470, 48),
    gajraj(160, 410, 0.9, trunk="down"),
    mehar(470, 400, 0.85, arms="wave", mouth="open", look=-5),
    word(360, 280, "Oh!", "#ffe680", 52),
])

# 7. SPLISH! The moon wobbles to pieces
pics["07"] = scene(night("sky-7") + [moon(520, 90, 46, "happy"),
    shore(380), lake(380), moon_in_water(330, 470, 48, wobble=True),
    gajraj(130, 410, 0.9, trunk="down"),
    word(330, 300, "SPLISH!", "#7fc0ee", 56),
    "".join(f'<path d="M{x},{y} q-6,10 0,14 q6,-4 0,-14 Z" fill="#9cc7ff"/>' for x, y in ((250, 340), (290, 320), (380, 330), (420, 350))),
    bunny(520, 380, 0.6),
])

# 8. Mehar: "Walk softly."
pics["08"] = scene(night("sky-8") + [moon(110, 100, 46, "happy"),
    hill("#2f5a3a", 480, 30),
    gajraj(440, 590, 0.95, flip=True, trunk="down"),
    mehar(180, 590, 1.15, arms="hold", mouth="open", look=4),
    bunny(70, 590, 0.75),
    "".join(f'<path d="M{x},{y} l-4,-14 M{x + 10},{y} l4,-14" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.8"/>' for x, y in ((360, 600), (470, 600))),
])

# 9. Tiptoe around the burrows
pics["09"] = scene([sky("dusk", "sky-9"), moon(520, 90, 40, "happy"),
    '<rect y="380" width="600" height="220" fill="#4f8a3f"/>',
    '<path d="M0,420 C200,400 260,560 600,520" fill="none" stroke="#c9a776" stroke-width="40" stroke-linecap="round" opacity="0.8"/>',
    burrow(160, 540, 0.9), burrow(330, 590, 0.9), burrow(80, 600, 0.7),
    gajraj(470, 520, 0.6, trunk="down"),
    gajraj(220, 440, 0.4, crown=False), gajraj(70, 430, 0.35, crown=False),
    bunny(250, 560, 0.6),
    mehar(560, 590, 0.75, arms="wave", eyes="happy"),
    word(300, 130, "tiptoe, tiptoe!", "#ffe680", 40),
])

# 10. "It's only a reflection!" Everybody laughs
pics["10"] = scene(night("sky-10") + [moon(300, 100, 50, "happy"),
    shore(420), lake(420), moon_in_water(300, 510, 40),
    gajraj(450, 430, 0.85, flip=True, eyes="closed"),
    bunny(250, 420, 0.8),
    mehar(110, 440, 1.0, arms="up", eyes="happy", mouth="open"),
    word(300, 210, "Ha ha ha!", "#ffe680", 44),
])

# 11. Back home: a tiny moon in the glass of water
glass = ('<path d="M372,356 L380,436 Q400,446 420,436 L428,356 Z" fill="#cfe8ff" opacity="0.55" stroke="#ffffff" stroke-width="3"/>'
         '<rect x="376" y="380" width="48" height="52" fill="#9fc8f0" opacity="0.5"/>'
         + moon_in_water(400, 396, 12))
pics["11"] = scene([bedroom("#2d2a5a"), window_frame(300, 60, 240, 230, "".join(night("sky-11w")) + moon(420, 150, 50, "sleepy")),
    '<rect x="350" y="436" width="130" height="14" rx="5" fill="#8a5a3c"/>', glass,
    mehar_in_bed(230, 470, 0.85, eyes="closed", friend=bunny(80, -8, 0.4, eyes="closed")),
    zzz(110, 370),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
