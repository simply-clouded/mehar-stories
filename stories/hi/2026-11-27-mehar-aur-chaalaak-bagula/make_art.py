"""Draws the pictures for "मेहर और चालाक बगुला" (Mehar aur chaalaak bagula). Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
FONT = "&apos;Baloo 2&apos;, &apos;Noto Sans Devanagari&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif"
FISH = ["#ff9a3d", "#3f7be8", "#ffd23f", "#ff7fb6", "#9b6ef3"]


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def word(x, y, text, color="#d8343f", size=48):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{FONT}" font-weight="800" '
            f'font-size="{size}" fill="{color}" stroke="#ffffff" stroke-width="6" paint-order="stroke">{text}</text>')


def lake(gid, time="day", water=430, right_bank=False):
    out = [sky(time, gid)]
    out.append('<circle cx="520" cy="80" r="44" fill="#ffe38a"/>' if time == "day" else '<circle cx="480" cy="150" r="50" fill="#ffb35c"/>')
    out.append(hill("#86c05a", 360, 40, "#9fd06e"))
    out.append(f'<rect y="{water - 20}" width="600" height="40" fill="#6aa84f"/>')
    out.append(river(water, "#3f8fd0", "#7fc0ee"))
    out.append('<path d="M0,520 Q150,500 260,530 Q200,580 0,600 Z" fill="#6aa84f"/>')
    if right_bank:
        out.append('<path d="M600,530 Q480,520 390,560 Q440,590 600,600 Z" fill="#6aa84f"/>')
    return out


def fishes(points, mood="happy"):
    return "".join(fish(x, y, 0.8, FISH[i % len(FISH)], mood, flip=i % 2 == 1) for i, (x, y) in enumerate(points))


def neck_crab(hx, hy, hs, mood="happy", claws="down"):
    """Kekdu riding on Bagla's neck (heron foot at (hx, hy), scale hs)."""
    return crab(hx + 18 * hs, hy - 150 * hs, 0.42 * hs / 0.8, mood, claws)


def rocks():
    return ('<path d="M60,520 C60,430 140,400 200,430 C220,380 300,380 320,440 L320,520 Z" fill="#8d8b9a"/>'
            '<path d="M380,520 C380,450 460,420 540,460 L560,520 Z" fill="#8d8b9a"/>'
            '<path d="M90,470 C110,440 140,430 170,440" fill="none" stroke="#a9a7b6" stroke-width="8" stroke-linecap="round"/>')


pics = {}

pics["cover"] = scene(lake("sky-c") + [
    heron(410, 470, 0.95, "happy"),
    neck_crab(410, 470, 0.95),
    fishes(((120, 490), (220, 470), (320, 520))),
    mehar(130, 590, 1.0, arms="wave", eyes="happy"),
])

# 1. A little lake, fish and a crab
pics["01"] = scene(lake("sky-1") + [
    fishes(((300, 480), (380, 520), (460, 470), (520, 540), (250, 560))),
    crab(200, 585, 0.6),
    mehar(80, 595, 0.95, arms="up", mouth="open", look=4),
])

# 2. Bagla's sad story
pics["02"] = scene(lake("sky-2", right_bank=True) + [
    heron(140, 560, 1.15, "sorry"),
    fishes(((320, 470), (400, 500), (480, 460), (300, 530))),
    mehar(470, 600, 0.95, arms="down", mouth="soft", look=-5),
])

# 3. One fish a day, and Bagla grows fatter
fat = f'<g transform="translate(220 560) scale(1.35 1)">{heron(0, 0, 0.9, "sly", holding=fish(10, 0, 0.6, "#3f7be8", "scared"))}</g>'
pics["03"] = scene(lake("sky-3", right_bank=True) + [
    fat,
    fishes(((420, 480), (330, 520))),
    mehar(510, 600, 0.95, arms="down", mouth="oh", look=-5),
    '<circle cx="520" cy="350" r="26" fill="#fffbe6"/><text x="520" y="363" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="34" fill="#3f7be8">?</text>',
])

# 4. Kekdu rides on Bagla's neck
pics["04"] = scene(lake("sky-4", right_bank=True) + [
    heron(200, 560, 1.15, "sly"),
    neck_crab(200, 560, 1.15),
    mehar(470, 595, 1.0, arms="wave", mouth="open", look=-4),
    '<path d="M560,560 h30 M555,540 h24" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
])

# 5. No big lake, only a little rock pool
pool = '<ellipse cx="300" cy="530" rx="140" ry="34" fill="#2f6fb0"/>' + fishes(((240, 530), (300, 520), (360, 535)), "scared")
pics["05"] = scene([sky("dusk", "sky-5"), '<circle cx="480" cy="150" r="50" fill="#ffb35c"/>',
    '<rect y="480" width="600" height="120" fill="#9c8f84"/>', pool, rocks(),
    heron(460, 480, 0.9, "sly"), neck_crab(460, 480, 0.9, "angry"),
    '<circle cx="120" cy="250" r="28" fill="#fffbe6"/><text x="120" y="263" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="36" fill="#3f7be8">?</text>',
])

# 6. Kat! Kekdu pinches
pics["06"] = scene([sky("dusk", "sky-6"), '<circle cx="480" cy="150" r="50" fill="#ffb35c"/>',
    '<rect y="480" width="600" height="120" fill="#9c8f84"/>', rocks(),
    heron(300, 600, 1.5, "sorry"),
    crab(327, 375, 0.75, "angry", "pinch"),
    word(160, 200, "कट!", "#d8343f", 70),
    word(470, 120, "आँ-आँ!", "#3f7be8", 40),
])

# 7. Mehar asks for a promise
pics["07"] = scene([sky("dusk", "sky-7"), '<circle cx="480" cy="150" r="50" fill="#ffb35c"/>',
    '<rect y="480" width="600" height="120" fill="#9c8f84"/>', pool, rocks(),
    heron(170, 590, 1.0, "sorry", eyes="closed"), neck_crab(170, 590, 1.0, "angry", "up"),
    mehar(450, 595, 1.15, arms="down", mouth="open", look=-5),
])

# 8. Chhapaak! Back home to the lake
pics["08"] = scene(lake("sky-8") + [
    heron(150, 560, 1.0, "happy", holding=fish(10, 0, 0.6, "#ff7fb6")),
    neck_crab(150, 560, 1.0),
    "".join(f'<path d="M{x},{y} q-7,12 0,16 q7,-4 0,-16 Z" fill="#9cc7ff"/>' for x, y in ((380, 430), (420, 410), (460, 425))),
    fishes(((420, 480), (500, 520), (360, 540))),
    word(430, 360, "छपाक!", "#3f7be8", 52),
])

# 9. Thank you! Bagla becomes the lake's guard
circle = '<ellipse cx="380" cy="510" rx="120" ry="40" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="6 10" opacity="0.7"/>'
pics["09"] = scene(lake("sky-9") + [
    circle,
    fishes(((280, 500), (360, 470), (460, 490), (480, 540), (380, 550), (290, 545))),
    heron(490, 470, 0.75, "happy"),
    crab(190, 585, 0.6, claws="up"),
    mehar(80, 595, 0.95, arms="up", eyes="happy", mouth="open"),
])

# 10. Back home
pics["10"] = scene([bedroom("#2d2a5a"), window_frame(40, 50, 220, 240, "".join(night("sky-10w")) + moon(150, 140, 50, "happy")),
    mehar_in_bed(300, 470, 0.95, eyes="closed"),
    fish(470, 340, 0.6, "#ff9a3d"), fish(520, 300, 0.5, "#3f7be8", flip=True),
    zzz(200, 380),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
