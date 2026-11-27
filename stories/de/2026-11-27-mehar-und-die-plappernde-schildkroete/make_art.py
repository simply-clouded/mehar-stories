"""Draws the pictures for "Mehar und die plappernde Schildkröte". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def summer(gid, sun="#ffd23f", ground="#9cc35a"):
    return [sky("day", gid), f'<circle cx="500" cy="90" r="56" fill="{sun}"/><circle cx="500" cy="90" r="80" fill="{sun}" opacity="0.25"/>',
            hill(ground, 430, 40, "#b5d36e")]


def meadow(gid):
    return [sky("day", gid), '<circle cx="520" cy="80" r="44" fill="#ffe38a"/>',
            '<ellipse cx="120" cy="120" rx="60" ry="22" fill="#ffffff" opacity="0.9"/><ellipse cx="380" cy="60" rx="50" ry="18" fill="#ffffff" opacity="0.9"/>',
            hill("#6aa84f", 480, 40, "#86c05a")]


def carry(x1, x2, y, s=0.8, ts=0.8, mouth="closed", blush=False, eyes="open"):
    """Gisi and Gusti carry the stick between them; Plappi hangs from the middle."""
    xm = (x1 + x2) / 2
    return (goose(x1 + 96 * s, y - 62 * s, s, feet=True) + goose(x2 + 96 * s, y - 62 * s, s, feet=True)
            + tortoise(xm, y, ts, mouth=mouth, pose="hang", blush=blush, eyes=eyes) + stick(x1 - 14, y, x2 + 14, y, 8))


def bubble_text(x, y, text, color="#3f7be8", size=40):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif" font-weight="800" '
            f'font-size="{size}" fill="{color}" stroke="#ffffff" stroke-width="6" paint-order="stroke">{text}</text>')


pics = {}

pics["cover"] = scene(meadow("sky-c") + [
    carry(170, 410, 220, 0.8, 0.85),
    flower(90, 560, 1.2, PAINT["pink"]), flower(520, 570, 1.1, PAINT["purple"]),
    mehar(300, 585, 1.1, arms="wave", eyes="happy"),
])

# 1. The book glows, and it is summer
pics["01"] = scene([bedroom("#2d2a5a"), window_frame(380, 60, 180, 210, "".join(night("sky-1w"))),
    magic_book(260, 500, 0.75),
    tortoise(260, 420, 0.4, "talk"),
    '<circle cx="190" cy="350" r="22" fill="#ffd23f"/>' + "".join(f'<path d="M{190 + 32*c},{350 + 32*d} l{8*c},{8*d}" stroke="#ffd23f" stroke-width="4" stroke-linecap="round"/>' for c, d in ((1, 0), (-1, 0), (0, 1), (0, -1), (0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7))),
    mehar(110, 575, 1.25, arms="up", mouth="open", look=4),
])

# 2. Plappi chatters all day
pics["02"] = scene(summer("sky-2") + [
    pond(300, 500, 230, 60),
    goose(300, 420, 0.8, pose="stand"),
    goose(470, 420, 0.8, pose="stand", flip=True),
    tortoise(380, 500, 0.8, "talk"),
    bubble_text(420, 330, "bla bla bla!", "#5d8f30", 30),
    mehar(90, 590, 1.05, arms="down", mouth="smile", look=4),
])

# 3. The pond dries up
pics["03"] = scene(summer("sky-3", "#ff9a3d", "#c9b45a") + [
    pond(300, 500, 230, 60, dry=True),
    tree(70, 440, 0.8, "#b5a24a"),
    goose(170, 410, 0.75, pose="stand", eyes="closed"),
    goose(250, 450, 0.75, pose="stand", eyes="closed"),
    tortoise(360, 510, 0.9, "closed", eyes="closed"),
    mehar(510, 595, 1.0, arms="down", mouth="oh", look=-5),
])

# 4. Mehar's idea: a long stick
pics["04"] = scene(summer("sky-4") + [
    pond(300, 520, 230, 50, dry=True),
    mehar(300, 560, 1.2, arms="up", mouth="open"),
    stick(160, 380, 440, 380, 10),
    goose(140, 470, 0.75, pose="stand", flip=True),
    goose(560, 470, 0.75, pose="stand"),
    tortoise(150, 572, 0.75, "talk"),
    '<circle cx="300" cy="120" r="30" fill="#fffbe6"/><text x="300" y="134" text-anchor="middle" font-family="&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif" font-weight="800" font-size="38" fill="#e0912a">!</text>',
])

# 5. Psst!
pics["05"] = scene(summer("sky-5") + [
    tortoise(340, 560, 1.6, "talk"),
    mehar(110, 590, 1.2, arms="down", mouth="soft", look=5),
    goose(560, 340, 0.6, pose="stand"),
    bubble_text(300, 180, "Psst!", "#e0912a", 64),
    bubble_text(480, 300, "Psst!", "#3f7be8", 36),
])

# 6. Flatter, flatter!
pics["06"] = scene(meadow("sky-6") + [
    carry(170, 420, 230, 0.85, 0.85),
    '<path d="M60,130 q20,-14 40,0 M70,170 q20,-14 40,0" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
    mehar(470, 580, 0.8, arms="wave", eyes="happy"),
    '<path d="M410,560 h-30 M415,540 h-24" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
])

# 7. Look, a flying tortoise!
pics["07"] = scene(meadow("sky-7") + [
    carry(190, 390, 150, 0.6, 0.65, blush=True),
    bunny(120, 570, 1.0),
    owl(250, 560, 0.85, wings="up"),
    bubble_text(220, 400, "Ha, ha!", "#ef5350", 40),
    mehar(470, 585, 1.0, arms="down", mouth="oh", look=-3),
    '<circle cx="470" cy="300" r="26" fill="#fffbe6"/><text x="470" y="313" text-anchor="middle" font-family="&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif" font-weight="800" font-size="34" fill="#3f7be8">?</text>',
])

# 8. Oh no, she opened her mouth!
pics["08"] = scene(meadow("sky-8") + [
    goose(170 + 77, 110 - 50, 0.8, feet=True), goose(430 + 77, 110 - 50, 0.8, feet=True),
    stick(156, 110, 444, 110, 8),
    tortoise(300, 260, 0.95, mouth="open", pose="hang"),
    '<path d="M230,250 v-50 M370,250 v-50 M260,220 v-40 M340,220 v-40" stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.8"/>',
    bubble_text(300, 520, "Oh nein!", "#ef5350", 48),
])

# 9. PLUMPS! Into the hay
pics["09"] = scene(meadow("sky-9") + [
    haystack(250, 560, 1.4),
    tortoise(250, 395, 0.85, "closed", blush=True),
    '<path d="M190,360 l-20,-12 M210,340 l-6,-20 M300,345 l10,-18 M320,365 l20,-8" stroke="#d9a92a" stroke-width="5" stroke-linecap="round"/>',
    bubble_text(250, 150, "PLUMPS!", "#e0912a", 60),
    mehar(480, 590, 1.1, arms="up", mouth="open", look=-6),
])

# 10. Mmmm all the way to the big lake
pics["10"] = scene([sky("dusk", "sky-10"), '<circle cx="480" cy="160" r="50" fill="#ffb35c"/>',
    '<path d="M0,330 Q300,300 600,330 V600 H0 Z" fill="#3f8fd0"/><path d="M0,330 Q300,300 600,330 V340 Q300,312 0,340 Z" fill="#7fc0ee"/>',
    '<path d="M0,520 Q160,480 300,520 Q200,560 0,600 Z" fill="#6aa84f"/>',
    tortoise(380, 420, 0.95, "closed", eyes="closed"),
    water_over(260, 540, 410),
    bubble_text(420, 300, "Mmmm!", "#e0912a", 44),
    goose(250 + 77, 140, 0.6), goose(520 + 77, 110, 0.6),
    mehar(120, 585, 1.0, arms="wave", eyes="happy"),
])

# 11. Back home, humming
pics["11"] = scene([bedroom("#2d2a5a"), window_frame(40, 50, 220, 240, "".join(night("sky-11w")) + moon(150, 140, 50, "sleepy")),
    mehar_in_bed(300, 470, 0.95, eyes="closed"),
    tortoise(410, 450, 0.35, "closed", eyes="closed"),
    bubble_text(440, 330, "Mmmm ...", "#9b6ef3", 34),
    zzz(200, 380),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
