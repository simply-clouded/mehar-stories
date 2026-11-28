"""Draws the pictures for "मेहर और चार दोस्त" (Mehar aur chaar dost). Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
FONT = "&apos;Baloo 2&apos;, &apos;Noto Sans Devanagari&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif"


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def word(x, y, text, color="#d8343f", size=44):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FONT}" font-weight="800" '
            f'font-size="{size}" fill="{color}" stroke="#ffffff" stroke-width="6" paint-order="stroke">{text}</text>')


def lakeside(gid, time="day", water=470, trees=True):
    """Grass, a few trees and the blue lake along the bottom."""
    out = [sky(time, gid)]
    out.append({"dusk": '<circle cx="480" cy="150" r="50" fill="#ffb35c"/>', "day": '<circle cx="500" cy="90" r="44" fill="#ffe38a"/>'}.get(time, ""))
    if trees:
        out.append(tree(60, 400, 1.2, "#2f8a4c") + tree(560, 400, 1.1, "#3f9a55"))
    out.append('<rect y="390" width="600" height="210" fill="#6aa84f"/><path d="M0,400 Q300,370 600,400 V410 H0 Z" fill="#5a9a42"/>')
    out.append(river(water))
    return out


def bush(x, y, s=1):
    """A round leafy bush, base centre at (x, y), to hide behind. About 220*s wide."""
    return g('<circle cx="-70" cy="-50" r="56" fill="#3f9a55"/><circle cx="70" cy="-50" r="56" fill="#3f9a55"/>'
             '<circle cx="0" cy="-80" r="70" fill="#4cbf6b"/><rect x="-110" y="-50" width="220" height="50" fill="#4cbf6b"/>'
             '<circle cx="-30" cy="-100" r="6" fill="#ff7fb6"/><circle cx="40" cy="-60" r="6" fill="#ff7fb6"/><circle cx="-80" cy="-40" r="6" fill="#ffd23f"/>', x, y, s)


def sack(x, y, s=1, peek=True, cut=False):
    """The hunter's sack on the ground, base at (x, y). peek=True: Dheemu's head pokes out."""
    p = []
    if peek:
        p.append('<rect x="-8" y="-118" width="16" height="30" rx="7" fill="#b9d68a"/><circle cx="0" cy="-124" r="16" fill="#b9d68a"/>'
                 '<circle cx="-6" cy="-127" r="3" fill="#2a3a1a"/><circle cx="6" cy="-127" r="3" fill="#2a3a1a"/>'
                 '<path d="M-5,-116 Q0,-120 5,-116" fill="none" stroke="#2a3a1a" stroke-width="2" stroke-linecap="round"/>')
    p.append('<path d="M-50,0 C-64,-40 -50,-90 -20,-100 L20,-100 C50,-90 64,-40 50,0 Z" fill="#a8774a"/>'
             '<path d="M-30,-30 q10,6 20,0 M10,-60 q10,6 20,0" fill="none" stroke="#8a5a3c" stroke-width="3" stroke-linecap="round"/>')
    if cut:
        p.append('<path d="M-24,-98 q-20,-10 -30,4 M24,-98 q18,-14 32,-2" fill="none" stroke="#c8a46a" stroke-width="5" stroke-linecap="round"/>')
    else:
        p.append('<path d="M-22,-96 Q0,-88 22,-96" fill="none" stroke="#c8a46a" stroke-width="6" stroke-linecap="round"/>')
    return g("".join(p), x, y, s)


def splash(x, y, s=1):
    return g("".join(f'<path d="M{dx},0 q{dx * 0.3:.0f},-40 {dx * 0.8:.0f},-56" fill="none" stroke="#bfe0ff" stroke-width="7" stroke-linecap="round"/>' for dx in (-50, -20, 20, 50))
             + '<ellipse cx="0" cy="4" rx="70" ry="14" fill="#7fc0ee"/>', x, y, s)


def leaping_deer(x, y, s=1):
    return f'<g transform="translate({x} {y}) rotate(-18)">{deer(0, 0, s)}</g>'


def palm_mouse(mx, my, ms):
    """Chintu sitting in Mehar's held-out hand (for mehar(..., arms="hold") at (mx, my), scale ms)."""
    return mouse(mx - 58 * ms - 30 * ms, my - 74 * ms + 6 * ms, 0.55 * ms)


def hug():
    return '<path d="M0,0 q-6,-8 -12,0 q6,10 12,14 q6,-4 12,-14 q-6,-8 -12,0 Z" fill="#ff7fb6"/>'


pics = {}

pics["cover"] = scene(lakeside("sky-c", "dusk", 500) + [
    deer(150, 500, 0.85),
    mehar(330, 510, 1.0, arms="wave", eyes="happy"),
    tortoise(470, 500, 0.7),
    mouse(560, 500, 0.6, flip=True),
    crow(250, 230, 0.8, wings="up"),
])

# 1. Four friends by the blue lake
pics["01"] = scene(lakeside("sky-1", "day", 480) + [
    deer(120, 480, 0.8),
    tortoise(290, 480, 0.6),
    mouse(400, 480, 0.6),
    crow(300, 300, 0.7, wings="up"),
    mehar(500, 480, 0.95, arms="wave", mouth="open", look=-4),
])

# 2. "Kaanv! Chitru is caught in the hunter's net!"
pics["02"] = scene([sky("dusk", "sky-2"), '<circle cx="480" cy="150" r="50" fill="#ffb35c"/>',
    tree(420, 470, 1.0, "#2f8a4c"), tree(560, 470, 1.2, "#3f9a55"),
    '<rect y="460" width="600" height="140" fill="#5a9a42"/>',
    deer(480, 580, 0.6, mood="sad"), net(500, 585, 210, 140, "net2"),
    crow(200, 300, 1.4, wings="up"),
    word(200, 130, "काँव! काँव!", "#ffffff", 50),
])

# 3. Running: Chintu in Mehar's hand, Kaaku leads, Dheemu slowly behind
pics["03"] = scene(lakeside("sky-3", "day", 520, trees=False) + [
    '<path d="M40,460 C200,430 350,470 590,430" fill="none" stroke="#c9a776" stroke-width="30" stroke-linecap="round" opacity="0.8"/>',
    crow(160, 200, 0.75, flip=True, wings="up"),
    mehar(250, 500, 1.1, arms="hold", mouth="open", look=-3, flip=True),
    mouse(338, 418, 0.5, flip=True),
    tortoise(500, 470, 0.55),
    word(500, 360, "धीरे-धीरे...", "#2f8a4c", 34),
])

# 4. Kutar, kutar! Free! ...but dhap, dhap, the hunter is coming
pics["04"] = scene([sky("dusk", "sky-4"), '<circle cx="120" cy="150" r="50" fill="#ffb35c"/>',
    tree(80, 470, 1.1, "#2f8a4c"), tree(560, 470, 1.3, "#3f9a55"),
    '<rect y="460" width="600" height="140" fill="#5a9a42"/>',
    hunter_shadow(560, 470, 0.55),
    tree(500, 480, 1.0, "#2f8a4c"),
    deer(220, 580, 0.8),
    net(240, 590, 260, 130, "net4", torn=True),
    mouse(400, 590, 0.75, mood="chew", flip=True),
    rope_heap(360, 596, 0.6),
    word(440, 130, "धप! धप! धप!", "#2b2440", 46),
])

# 5. Everyone runs, but slow Dheemu is put in the sack
pics["05"] = scene([sky("dusk", "sky-5"),
    tree(80, 470, 1.1, "#2f8a4c"),
    '<rect y="460" width="600" height="140" fill="#5a9a42"/>',
    hunter_shadow(420, 590, 1.0, bag=True),
    '<circle cx="342" cy="338" r="13" fill="#b9d68a"/><circle cx="337" cy="335" r="2.6" fill="#2a3a1a"/><circle cx="347" cy="335" r="2.6" fill="#2a3a1a"/>'
    '<path d="M337,345 Q342,341 347,345" fill="none" stroke="#2a3a1a" stroke-width="2" stroke-linecap="round"/>',
    leaping_deer(60, 520, 0.5),
    crow(160, 140, 0.6, flip=True, wings="up"),
    mehar(170, 590, 0.85, arms="up", mouth="oh", look=3),
    bush(170, 600, 0.95),
    word(160, 300, "अरे नहीं!", "#ffffff", 38),
])

# 6. Mehar has an idea
pics["06"] = scene(lakeside("sky-6", "dusk", 520) + [
    deer(110, 520, 0.7, mood="sad"),
    mehar(300, 530, 1.15, arms="down", eyes="closed", mouth="soft"),
    crow(470, 520, 0.8, flip=True, mood="sad"),
    mouse(540, 520, 0.6, flip=True, mood="sad"),
    '<circle cx="400" cy="230" r="34" fill="#fffbe6"/><path d="M386,270 l-12,22 l24,-14 Z" fill="#fffbe6"/>'
    '<text x="400" y="246" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="44" fill="#d8343f">?</text>',
])

# 7. Chitru plays sick; Kaaku sits on him
pics["07"] = scene(lakeside("sky-7", "dusk", 520) + [
    deer(250, 470, 0.95, pose="lie", eyes="closed"),
    crow(240, 400, 0.6, wings="up"),
    word(330, 300, "काँव! काँव!", "#ffffff", 34),
    mehar(530, 470, 0.8, arms="down", eyes="happy", mouth="smile", look=-4),
    bush(530, 480, 0.8),
])

# 8. The hunter puts the sack down and tiptoes to Chitru
pics["08"] = scene(lakeside("sky-8", "dusk", 520) + [
    deer(100, 470, 0.7, pose="lie", eyes="closed"),
    crow(90, 410, 0.45),
    hunter_shadow(330, 500, 0.7),
    sack(500, 500, 0.75),
    mouse(420, 500, 0.5),
    mehar(560, 410, 0.6, arms="down", mouth="oh", look=-4),
    bush(560, 420, 0.55),
])

# 9. Chhapaak! Dheemu dives into the lake, Chitru leaps away
pics["09"] = scene(lakeside("sky-9", "dusk", 470) + [
    sack(480, 460, 0.7, peek=False, cut=True), mouse(400, 460, 0.55, mood="chew", flip=True),
    splash(250, 520, 1.1),
    f'<g transform="translate(250 490) rotate(25)">{tortoise(0, 0, 0.6, mouth="open")}</g>',
    leaping_deer(70, 420, 0.6),
    mehar(540, 410, 0.75, arms="up", eyes="happy", mouth="open"),
    word(250, 380, "छपाक!", "#ffffff", 52),
])

# 10. The hunter goes home empty-handed; everybody hugs
pics["10"] = scene(lakeside("sky-10", "dusk", 530) + [
    hunter_shadow(560, 400, 0.35, flip=True),
    '<text x="540" y="270" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="30" fill="#2b2440">?</text>',
    deer(130, 520, 0.75, eyes="closed"),
    mehar(290, 530, 1.05, arms="hold", eyes="happy", mouth="open"),
    tortoise(400, 530, 0.55, blush=True),
    mouse(230, 530, 0.5),
    crow(380, 300, 0.6, wings="up"),
    g(hug(), 290, 260, 1.5),
])

# 11. Back in bed
pics["11"] = scene([bedroom("#2d2a5a"), window_frame(320, 60, 230, 230, "".join(night("sky-11w")) + moon(430, 150, 50, "sleepy")),
    mehar_in_bed(230, 470, 0.85, eyes="closed"),
    zzz(110, 370),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
