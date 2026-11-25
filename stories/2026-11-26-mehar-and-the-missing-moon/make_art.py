"""Draws the pictures for "Mehar and the Missing Moon". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60), (110, 300)]
STARS = [(70, 80, 10), (190, 150, 8), (300, 50, 11), (400, 190, 8), (540, 240, 9), (250, 260, 7)]


def night(gid, moonless=False):
    out = [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)]
    out += [star(x, y, r, "#ffe680") for x, y, r in STARS]
    return out


def bedroom_window(inside, wall="#2d2a5a"):
    return [bedroom(wall), window_frame(70, 60, 260, 290, inside)]


pics = {}

# Cover: the whole gang under a rainbow cloud and a peeking moon
pics["cover"] = scene(night("sky-cover") + [
    moon(460, 150, 72, "happy"),
    cloud(400, 210, 0.75, "happy", rainbow=True, cid="cl-cover"),
    hill("#2f6b4f", 480, 60, "#24563f"),
    firefly(90, 300), firefly(150, 250, 0.8), firefly(520, 340, 0.9),
    owl(120, 200, 0.75, wings="up"),
    elephant(250, 560, 1.1, rider=mehar(-10, -118, 0.78, arms="wave", eyes="happy", outfit="pyjama", legs=False)),
    bunny(510, 565, 0.85),
])

# 1. No moon tonight
inside = "".join(night("sky-1"))
pics["01"] = scene(bedroom_window(inside) + [
    '<rect x="380" y="300" width="160" height="170" rx="10" fill="#6c4b33"/><rect x="392" y="316" width="136" height="60" rx="6" fill="#7d5a40"/>',
    paintbox(460, 300, 0.7, open_=False),
    mehar(270, 565, 1.45, arms="down", mouth="oh", look=-3, outfit="pyjama"),
])

# 2. Uhu taps on the window
inside = "".join(night("sky-2")) + owl(200, 250, 1.0, wings="up")
pics["02"] = scene(bedroom_window(inside) + [
    mehar(430, 565, 1.45, arms="up", mouth="open", look=-4, outfit="pyjama"),
])

# 3. Moti waits in the garden
pics["03"] = scene(night("sky-3") + [
    hill("#2f6b4f", 470, 40, "#24563f"),
    flower(60, 560, 1, PAINT["pink"]), flower(110, 575, 0.8, PAINT["purple"]),
    owl(470, 180, 0.8, wings="up"),
    elephant(270, 555, 1.15, trunk="up", rider=mehar(-10, -118, 0.8, arms="brush", brush=PAINT["red"], outfit="pyjama", legs=False)),
    paintbox(80, 470, 0.55),
])

# 4. Hasi is scared of the dark
pics["04"] = scene([sky("night", "sky-4"), sparkles(DOTS, "#ffffff", 1.4), forest(True),
    eyes_in_dark([(120, 330), (500, 300), (300, 360)]),
    bunny(400, 560, 1.15, ear_flop=True),
    '<path d="M362,470 l-14,-6 M440,470 l14,-6 M360,500 l-14,2 M442,500 l14,2" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.7"/>',
    mehar(250, 565, 1.4, arms="hold", outfit="pyjama", mouth="soft"),
])

# 5. One, two, three fireflies
pics["05"] = scene([sky("night", "sky-5"), sparkles(DOTS, "#ffffff", 1.4), forest(True),
    firefly(170, 200, 1.3), number_tag(170, 160, "1"),
    firefly(300, 150, 1.3), number_tag(300, 110, "2"),
    firefly(430, 200, 1.3), number_tag(430, 160, "3"),
    owl(520, 330, 0.7),
    bunny(420, 565, 0.85),
    mehar(250, 565, 1.35, arms="up", eyes="happy", mouth="open", outfit="pyjama"),
])

# 6. The grey cloud sitting on the moon
pics["06"] = scene([sky("grey", "sky-6"), sparkles(DOTS, "#d0d2dc", 1.6),
    moon(340, 170, 70, "sleepy"),
    cloud(320, 210, 1.0, "sad", cid="cl-6"),
    hill("#3d5a4a", 500, 40, "#34503f"),
    bunny(520, 575, 0.75),
    mehar(140, 580, 1.25, arms="down", mouth="oh", look=4, outfit="pyjama"),
])

# 7. Painting Badal
stripes = ('<defs><clipPath id="cl-7b"><rect x="160" y="120" width="330" height="200"/></clipPath></defs>'
           '<g clip-path="url(#cl-7b)">'
           + stroke("M190,170 C260,140 330,190 420,160", PAINT["red"], 34)
           + stroke("M180,215 C270,190 340,240 440,205", PAINT["yellow"], 34)
           + stroke("M190,260 C280,235 350,285 430,250", PAINT["blue"], 34) + '</g>')
pics["07"] = scene([sky("grey", "sky-7"), sparkles(DOTS, "#d0d2dc", 1.6),
    moon(340, 170, 70, "sleepy"),
    cloud(320, 210, 1.0, "happy", cid="cl-7"),
    stripes,
    hill("#3d5a4a", 500, 40, "#34503f"),
    paintbox(470, 560, 0.7),
    mehar(150, 580, 1.3, arms="brush", brush=PAINT["blue"], eyes="happy", outfit="pyjama"),
])

# 8. Badal floats up, the moon peeks out
pics["08"] = scene(night("sky-8") + [
    moon(300, 250, 85, "happy"),
    cloud(300, 90, 0.8, "happy", rainbow=True, cid="cl-8"),
    hill("#2f6b4f", 500, 40, "#24563f"),
    firefly(80, 320, 0.8), firefly(520, 300, 0.8), firefly(560, 380, 0.6),
    owl(90, 420, 0.65, wings="up"),
    bunny(470, 575, 0.8),
    mehar(300, 585, 1.15, arms="up", eyes="happy", mouth="open", outfit="pyjama"),
])

# 9. Thank you, Mehar
pics["09"] = scene(night("sky-9") + [
    moon(300, 200, 120, "happy"),
    cloud(110, 110, 0.45, "happy", rainbow=True, cid="cl-9"),
    hill("#2f6b4f", 520, 30, "#24563f"),
    elephant(120, 600, 0.65, trunk="up"),
    mehar(330, 590, 1.05, arms="wave", eyes="happy", outfit="pyjama"),
    bunny(440, 595, 0.65),
    owl(520, 470, 0.6),
])

# 10. Home along a moonbeam, and goodnight
inside = "".join(night("sky-10")) + moon(160, 140, 55, "sleepy") + cloud(250, 250, 0.3, "happy", rainbow=True, cid="cl-10")
pics["10"] = scene([bedroom("#2d2a5a"), moonbeam(200, 60, 330, 470, 40, 260), window_frame(60, 50, 240, 260, inside),
    mehar_in_bed(330, 450, 1.0, eyes="closed", friend=g(bunny(0, 0, 0.5, eyes="closed").replace("", ""), 80, -14)),
    owl(500, 300, 0.6, eyes="closed"),
    '<rect x="460" y="300" width="90" height="10" rx="4" fill="#8a5a3c"/>',
    zzz(250, 370),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
