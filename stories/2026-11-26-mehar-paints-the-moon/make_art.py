"""Draws the pictures for "Mehar Paints the Moon". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from storyart import *  # noqa

GREY_STARS = [(80, 70), (190, 140), (300, 60), (120, 230), (380, 180), (540, 250), (250, 260)]
STAR_SPOTS = [(70, 80, 13), (180, 150, 10), (300, 60, 14), (110, 250, 9), (390, 200, 11), (560, 260, 10), (260, 250, 8)]
DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210)]


def grey_night():
    return [sky("grey"), sparkles(GREY_STARS, "#b9bbc4", 2.5)]


def coloured_night(gid="sky-p"):
    return [sky("painted", gid), sparkles(DOTS, "#ffffff", 1.8)]


def yellow_stars(face=False):
    return "".join(star(x, y, r, "#ffd23f", face=face and r > 12) for x, y, r in STAR_SPOTS)


pics = {}

pics["cover"] = scene(
    coloured_night("sky-cover") + [
        yellow_stars(face=True),
        moon(450, 140, 78, "happy"),
        hill("#3fa45e", 470, 70, "#2f8a4c"),
        tree(70, 470, 0.9), tree(560, 450, 0.7),
        flower(200, 520, 1, PAINT["pink"]), flower(470, 545, 0.9, PAINT["purple"]), flower(520, 520, 0.8, PAINT["orange"]),
        owl(150, 330, 0.9, wings="up"),
        mehar(320, 555, 1.35, arms="brush", brush=PAINT["blue"], eyes="happy"),
        bunny(470, 560, 0.9),
    ])

# 1. The moon is grey and sad.
outside = "".join(grey_night()) + moon(140, 140, 62, "sad", grey=True)
pics["01"] = scene([
    bedroom(),
    window_frame(70, 60, 260, 300, outside),
    '<rect x="360" y="300" width="170" height="170" rx="10" fill="#6c4b33"/><rect x="372" y="316" width="146" height="60" rx="6" fill="#7d5a40"/>',
    '<rect x="380" y="270" width="70" height="40" rx="4" fill="#ffffff"/><circle cx="398" cy="290" r="7" fill="#3f7be8"/><circle cx="416" cy="285" r="7" fill="#ffd23f"/><circle cx="433" cy="292" r="7" fill="#4cbf6b"/>',
    mehar(250, 560, 1.45, arms="down", mouth="oh", look=-3, outfit="pyjama"),
])

# 2. An owl brings a paintbrush.
pics["02"] = scene(grey_night() + [
    moon(470, 110, 55, "sad", grey=True),
    hill("#5d6170", 480, 50, "#4e5160"),
    tree(80, 480, 0.8, grey=True), tree(540, 470, 0.7, grey=True),
    owl(380, 300, 1.3, wings="up", holding=PAINT["blue"]),
    mehar(200, 560, 1.4, arms="up", mouth="open"),
])

# 3. Swish! Blue sky.
pics["03"] = scene(grey_night() + [
    stroke("M-20,90 C150,20 300,160 620,60", PAINT["blue"], 110),
    stroke("M-20,220 C180,150 330,280 620,190", PAINT["blue"], 110, 0.9),
    moon(470, 110, 55, "sad", grey=True),
    hill("#5d6170", 480, 50, "#4e5160"),
    tree(80, 480, 0.8, grey=True), tree(540, 470, 0.7, grey=True),
    owl(520, 330, 0.8, wings="down"),
    mehar(260, 560, 1.4, arms="brush", brush=PAINT["blue"], mouth="open"),
])

# 4. Dab, dab! Yellow stars.
pics["04"] = scene(coloured_night("sky-4") + [
    "".join(star(x, y, r, "#ffd23f" if i < 4 else "#c6c8d0") for i, (x, y, r) in enumerate(STAR_SPOTS)),
    star(390, 200, 18, "#ffd23f"),
    moon(480, 100, 55, "sad", grey=True),
    hill("#5d6170", 480, 50, "#4e5160"),
    tree(80, 480, 0.8, grey=True),
    owl(500, 330, 0.8),
    mehar(300, 560, 1.4, arms="brush", brush=PAINT["yellow"]),
])

# 5. Green trees for the bunny.
pics["05"] = scene(coloured_night("sky-5") + [
    yellow_stars(),
    moon(480, 100, 55, "sad", grey=True),
    hill("#3fa45e", 480, 50, "#5d6170"),
    tree(90, 480, 0.95), tree(560, 470, 0.75, grey=True),
    bunny(450, 560, 1.1),
    mehar(250, 560, 1.4, arms="brush", brush=PAINT["green"], look=4),
])

# 6. The moon smiles: thank you!
pics["06"] = scene(coloured_night("sky-6") + [
    yellow_stars(face=True),
    moon(300, 150, 95, "happy"),
    hill("#3fa45e", 480, 50, "#2f8a4c"),
    tree(70, 480, 0.85), tree(550, 470, 0.75),
    flower(160, 540, 1, PAINT["pink"]), flower(420, 555, 0.9, PAINT["orange"]),
    owl(120, 380, 0.75, wings="up"),
    bunny(480, 560, 0.9),
    mehar(300, 565, 1.25, arms="wave", mouth="open", eyes="happy"),
])

# 7. Goodnight.
outside = "".join(coloured_night("sky-7")) + moon(150, 130, 60, "sleepy") + star(70, 70, 10, "#ffd23f") + star(240, 230, 8, "#ffd23f")
pics["07"] = scene([
    bedroom("#2d2a5a"),
    window_frame(60, 50, 240, 260, outside),
    mehar_in_bed(330, 450, 1.0, eyes="closed"),
    owl(500, 300, 0.6, eyes="closed"),
    '<rect x="460" y="300" width="90" height="10" rx="4" fill="#8a5a3c"/>',
    zzz(250, 370),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
