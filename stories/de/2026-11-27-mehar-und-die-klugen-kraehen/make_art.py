"""Draws the pictures for "Mehar und die klugen Krähen". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
FONT = "&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif"


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def word(x, y, text, color="#e0912a", size=48):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FONT}" font-weight="800" '
            f'font-size="{size}" fill="{color}" stroke="#ffffff" stroke-width="6" paint-order="stroke">{text}</text>')


def nest(x, y, s=1, eggs=0):
    e = "".join(f'<ellipse cx="{-20 + i*20}" cy="-14" rx="10" ry="13" fill="#cfe3f2" stroke="#9fb8c8" stroke-width="1.5"/>' for i in range(eggs))
    return g(e + '<path d="M-60,-10 Q0,40 60,-10 Q0,6 -60,-10 Z" fill="#8a5a2c"/>'
             '<path d="M-56,-8 q20,10 40,4 M-10,0 q20,8 50,-6 M-50,4 q30,14 70,2" fill="none" stroke="#b07a42" stroke-width="3" stroke-linecap="round"/>', x, y, s)


def crow_tree(gid, time="day", nest_eggs=0, hole=True):
    out = [sky(time, gid)]
    if time == "day":
        out.append('<circle cx="520" cy="80" r="44" fill="#ffe38a"/>')
    out.append('<rect y="500" width="600" height="100" fill="#6aa84f"/><path d="M0,505 Q300,480 600,505 V512 H0 Z" fill="#5a9a42"/>')
    out.append('<path d="M240,520 C250,400 250,250 260,120 L340,120 C350,250 350,400 360,520 Z" fill="#7a5236"/>'
               '<path d="M330,260 C400,250 440,240 480,230" fill="none" stroke="#7a5236" stroke-width="22" stroke-linecap="round"/>'
               '<circle cx="300" cy="90" r="110" fill="#2f8a4c"/><circle cx="150" cy="140" r="80" fill="#3f9a55"/><circle cx="460" cy="130" r="80" fill="#3f9a55"/>')
    if hole:
        out.append('<ellipse cx="300" cy="490" rx="36" ry="26" fill="#2a1a10"/>')
    out.append(nest(450, 236, 1.0, nest_eggs))
    return out


pics = {}

pics["cover"] = scene(crow_tree("sky-c") + [
    crow(410, 226, 0.7), crow(490, 226, 0.7, flip=True),
    crow(150, 300, 0.8, wings="up", holding=necklace(0, 0, 0.8)),
    lion(130, 600, 0.6, "happy", crown=False),
    mehar(470, 600, 1.0, arms="wave", eyes="happy"),
])

# 1. Two crows crying in the nest
pics["01"] = scene(crow_tree("sky-1") + [
    crow(410, 226, 0.7, mood="sad"), crow(490, 226, 0.7, flip=True, mood="sad"),
    mehar(140, 600, 1.15, arms="down", mouth="oh", look=5),
])

# 2. Sarpu steals the eggs
pics["02"] = scene(crow_tree("sky-2", nest_eggs=0) + [
    crow(410, 226, 0.7, mood="sad", wings="up"), crow(490, 226, 0.7, flip=True, mood="sad"),
    snake(300, 520, 1.0, "sly"),
    '<ellipse cx="380" cy="470" rx="11" ry="14" fill="#cfe3f2" stroke="#9fb8c8" stroke-width="1.5"/>',
    word(150, 380, "Zisch!", "#3f8a36", 52),
    mehar(520, 600, 0.95, arms="down", mouth="oh", look=-5),
])

# 3. Mehar asks Uhu
pics["03"] = scene([sky("dusk", "sky-3"), '<circle cx="480" cy="150" r="50" fill="#ffb35c"/>',
    '<rect y="500" width="600" height="100" fill="#5a9a42"/>',
    '<path d="M60,520 C70,400 70,250 80,0 L150,0 C160,250 160,400 170,520 Z" fill="#7a5236"/>',
    '<path d="M150,300 C250,290 330,280 380,270" fill="none" stroke="#7a5236" stroke-width="22" stroke-linecap="round"/>',
    owl(330, 262, 0.9),
    mehar(380, 590, 1.2, arms="down", mouth="open", look=-4),
    '<circle cx="240" cy="160" r="30" fill="#fffbe6"/><text x="240" y="174" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="38" fill="#e0912a">!</text>',
])

# 4. A secret plan with Raja Singh
pics["04"] = scene(jungle("day", "sky-4") + [
    rock(200, 520, 1.0),
    lion(200, 440, 0.95, "happy", crown=False),
    necklace(200, 312, 1.1),
    mehar(430, 590, 1.2, arms="down", mouth="soft", look=-6),
    '<path d="M360,300 q-14,-8 -22,0 M354,286 q-18,-12 -30,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>',
])

# 5. Krah, krah! The chase (just for fun)
pics["05"] = scene(jungle("day", "sky-5") + [
    crow(420, 200, 1.1, wings="up", holding=necklace(0, 0, 0.9)),
    word(430, 90, "Krah, krah!", "#3b3f52", 40),
    lion(250, 590, 0.85, "roar", crown=False),
    '<path d="M110,500 h-40 M120,530 h-50 M110,560 h-40" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>',
    mehar(500, 595, 0.95, arms="wave", eyes="happy", mouth="open"),
])

# 6. Plopp! Into the snake's hole
pics["06"] = scene(crow_tree("sky-6") + [
    crow(330, 330, 0.9, wings="up"),
    necklace(300, 420, 0.8),
    '<path d="M300,400 v-30 M285,405 l-10,-20 M315,405 l10,-20" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
    word(430, 450, "Plopp!", "#e0912a", 50),
    '<circle cx="130" cy="380" r="28" fill="#fffbe6"/><text x="130" y="393" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="36" fill="#3f7be8">?</text>',
    mehar(120, 600, 0.85, arms="up", mouth="open"),
])

# 7. Rums! Rums! Raja Singh digs
sand = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#d9b98a"/>' for x, y, r in ((200, 420, 10), (170, 380, 7), (420, 410, 9), (450, 370, 7), (230, 360, 6), (390, 350, 6)))
pics["07"] = scene(crow_tree("sky-7") + [
    '<path d="M240,520 Q300,470 360,520 Z" fill="#c9a776"/>',
    lion(300, 600, 0.85, "roar", crown=False),
    sand,
    word(300, 330, "Rums! Rums!", "#e0912a", 46),
    crow(450, 226, 0.6, wings="up"),
])

# 8. Sarpu slithers far away
pics["08"] = scene([sky("day", "sky-8"), '<circle cx="520" cy="80" r="44" fill="#ffe38a"/>',
    hill("#86c05a", 420, 60, "#9fd06e"),
    '<path d="M0,520 Q300,480 600,520 V600 H0 Z" fill="#6aa84f"/>',
    g(snake(0, 0, 1, "scared"), 450, 390, 0.6),
    '<path d="M330,400 h-40 M340,380 h-30" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
    word(450, 220, "Hilfe!", "#3f8a36", 44),
    mehar(150, 590, 1.2, arms="wave", mouth="open", look=5),
    lion(330, 600, 0.6, "happy", crown=False),
])

# 9. Three chicks in spring
chicks = "".join(crow(x, 228, 0.32) for x in (420, 450, 480))
pics["09"] = scene(crow_tree("sky-9", hole=False) + [
    chicks,
    crow(360, 230, 0.7), crow(560, 230, 0.7, flip=True),
    flower(100, 560, 1.2, PAINT["pink"]), flower(520, 560, 1.1, PAINT["yellow"]),
    lion(170, 600, 0.65, "happy", crown=False), necklace(170, 515, 0.75),
    mehar(420, 600, 1.0, arms="up", eyes="happy", mouth="open"),
])

# 10. Back home, a crow on the windowsill
pics["10"] = scene([bedroom("#2d2a5a"), window_frame(340, 50, 220, 240, "".join(night("sky-10w")) + moon(450, 140, 50, "sleepy")),
    crow(420, 300, 0.6),
    mehar_in_bed(240, 470, 0.9, eyes="closed"),
    zzz(150, 390),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
