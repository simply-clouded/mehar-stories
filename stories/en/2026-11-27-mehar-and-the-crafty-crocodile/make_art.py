"""Draws the pictures for "Mehar and the Crafty Crocodile". Run: python3 make_art.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
from storyart import *  # noqa

DOTS = [(40, 40), (150, 100), (240, 30), (350, 120), (430, 40), (520, 180), (60, 180), (330, 260), (210, 210), (560, 60)]
JAMUNS = [(40, 120), (110, 60), (170, 130), (250, 90), (300, 40), (330, 140), (80, 30), (220, 30)]


def night(gid):
    return [sky("night", gid), sparkles(DOTS, "#ffffff", 1.8)] + [star(x, y, 8, "#ffe680") for x, y in ((70, 80), (300, 50), (540, 240))]


def bank(y=470, x2=260):
    """The grassy river bank on the left."""
    return f'<path d="M0,{y - 20} Q{x2 * 0.6:.0f},{y - 30} {x2},{y} Q{x2 + 20},{y + 20} {x2 - 10},{y + 40} L0,{y + 40} Z" fill="#6aa84f"/>'


def big_tree(x=80, branch_y=300, x2=380, top=True):
    """Chiku's jamun tree: a thick trunk on the left and one long branch to stand on."""
    out = [f'<path d="M{x - 40},520 C{x - 30},400 {x - 26},200 {x - 20},0 L{x + 30},0 C{x + 36},200 {x + 40},400 {x + 50},520 Z" fill="#7a5236"/>',
           f'<path d="M{x + 20},{branch_y + 24} C{x + 120},{branch_y + 6} {x2 - 80},{branch_y} {x2},{branch_y - 6}" fill="none" stroke="#7a5236" stroke-width="28" stroke-linecap="round"/>',
           f'<circle cx="{x2 + 10}" cy="{branch_y - 26}" r="34" fill="#3f9a55"/><circle cx="{x2 - 30}" cy="{branch_y - 36}" r="26" fill="#4cbf6b"/>']
    if top:
        out.append('<circle cx="40" cy="40" r="120" fill="#2f8a4c"/><circle cx="200" cy="10" r="110" fill="#3f9a55"/><circle cx="350" cy="-10" r="90" fill="#2f8a4c"/>'
                   + "".join(jamun(jx, jy, 1.2) for jx, jy in JAMUNS))
    return "".join(out)


def day_river(gid, water=470):
    return [sky("day", gid), '<circle cx="520" cy="80" r="44" fill="#ffe38a"/>', river(water)]


def bubble(x, y, r, inner, tail=(0, 0)):
    tx, ty = tail
    return (f'<circle cx="{tx}" cy="{ty}" r="6" fill="#ffffff"/><circle cx="{(tx + x) / 2:.0f}" cy="{(ty + y) / 2:.0f}" r="10" fill="#ffffff"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff"/>' + inner)


def heart(x, y, s=1, color="#ef5350"):
    return g('<path d="M0,12 C-30,-8 -22,-30 -10,-30 C-4,-30 0,-24 0,-20 C0,-24 4,-30 10,-30 C22,-30 30,-8 0,12 Z" fill="' + color + '"/>', x, y, s)


def riders(mehar_kw=None, monkey_kw=None):
    m = dict(arms="down", mouth="smile")
    m.update(mehar_kw or {})
    k = dict(mood="happy", arms="down")
    k.update(monkey_kw or {})
    return mehar(-30, -14, 0.75, legs=False, **m) + monkey(50, -44, 0.6, **k)


pics = {}

pics["cover"] = scene(day_river("sky-c", 430) + [
    fruit_tree(90, 450, 1.0),
    bank(450, 200),
    crocodile(330, 500, 1.0, "happy", "smile", rider=riders({"arms": "wave", "eyes": "happy"}, {"mood": "laugh", "arms": "up"})),
    water_over(120, 560, 512),
])

# 1. The book glows again
pics["01"] = scene([bedroom("#2d2a5a"), window_frame(380, 60, 180, 210, "".join(night("sky-1w"))),
    magic_book(250, 500, 0.75),
    monkey(250, 410, 0.45, "laugh", "up"),
    jamun(170, 340, 1.4), jamun(330, 320, 1.4),
    mehar(110, 575, 1.25, arms="up", mouth="open", look=4),
])

# 2. Chiku shares the sweetest jamuns
pics["02"] = scene(day_river("sky-2", 520) + [
    big_tree(80, 380, 560),
    monkey(230, 366, 0.85, "happy", "hold"),
    mehar(400, 368, 0.95, arms="hold", mouth="open", look=-4),
    jamun(345, 290, 1.3),
])

# 3. Plop, plop, PLOP!
arc = "".join(jamun(x, y, 1.1) for x, y in ((290, 230), (340, 260), (380, 320), (410, 390)))
pics["03"] = scene(day_river("sky-3", 470) + [
    big_tree(70, 230, 300),
    monkey(230, 216, 0.75, "laugh", "up"),
    mehar(130, 218, 0.75, arms="wave", eyes="happy"),
    '<path d="M260,170 Q360,160 420,400" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="4 10" stroke-linecap="round"/>',
    arc,
    crocodile(330, 500, 0.95, "happy", "open"),
    water_over(100, 600, 505),
    '<text x="470" y="250" text-anchor="middle" font-family="&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif" font-weight="800" font-size="40" fill="#5b2a86">PLOP!</text>',
])

# 4. An invitation, and eyes that slide away
pics["04"] = scene(day_river("sky-4", 450) + [
    bank(450, 280),
    fruit_tree(60, 440, 0.8),
    monkey(160, 452, 0.8, "laugh", "up"),
    mehar(250, 460, 1.0, arms="down", mouth="soft", look=5),
    crocodile(420, 520, 0.85, "sly", "smile"),
    water_over(250, 600, 525),
    '<circle cx="300" cy="180" r="30" fill="#fffbe6"/><text x="300" y="194" text-anchor="middle" font-family="&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif" font-weight="800" font-size="38" fill="#3f7be8">?</text>',
])

# 5. In the middle of the river
pics["05"] = scene([sky("day", "sky-5"), '<circle cx="90" cy="90" r="40" fill="#ffe38a"/>',
    '<path d="M0,250 Q150,230 300,250 T600,245 V270 H0 Z" fill="#6aa84f"/>', tree(70, 255, 0.4, "#2f8a4c"), tree(520, 252, 0.35, "#3f9a55"),
    river(265),
    crocodile(300, 470, 1.25, "sorry", "closed", rider=riders({"mouth": "oh", "look": 4}, {"mood": "scared", "arms": "up"})),
    water_over(40, 600, 482),
])

# 6. A deep breath, and a plan
think = bubble(450, 130, 80, fruit_tree(450, 200, 0.42) + heart(470, 120, 0.8) + '<text x="420" y="110" font-family="&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif" font-weight="800" font-size="34" fill="#3f7be8">?</text>', (330, 250))
pics["06"] = scene([sky("day", "sky-6"), river(300),
    crocodile(250, 575, 1.7, "sorry", rider=mehar(-40, 0, 0.95, legs=False, eyes="closed", mouth="soft")
              + monkey(70, -40, 0.6, "scared", "up")),
    water_over(0, 600, 588),
    think,
])

# 7. Monkeys never take their hearts swimming!
say = bubble(150, 120, 75, fruit_tree(150, 190, 0.4) + '<path d="M150,140 v20" stroke="#7a5236" stroke-width="3"/>' + heart(150, 175, 0.6), (280, 230))
pics["07"] = scene([sky("day", "sky-7"), river(330),
    crocodile(320, 500, 1.25, "happy", "closed", flip=True, rider=riders({"arms": "up", "mouth": "open"}, {"mood": "scared"})),
    water_over(0, 600, 512),
    say,
])

# 8. Up, up, UP!
pics["08"] = scene(day_river("sky-8", 470) + [
    big_tree(80, 200, 360),
    bank(470, 220),
    monkey(300, 186, 0.75, "laugh", "up"),
    mehar(190, 300, 0.85, arms="up", mouth="open", look=3),
    '<path d="M150,330 v40 M175,340 v40 M225,340 v40 M250,330 v40" stroke="#ffffff" stroke-width="4" stroke-linecap="round" opacity="0.8"/>',
    crocodile(430, 520, 0.9, "sly", "closed", flip=True),
    water_over(250, 600, 525),
    '<text x="440" y="230" text-anchor="middle" font-family="&apos;Baloo 2&apos;, &apos;Arial Rounded MT Bold&apos;, Arial, sans-serif" font-weight="800" font-size="44" fill="#ffffff">UP!</text>',
])

# 9. My heart is right here!
pics["09"] = scene(day_river("sky-9", 470) + [
    big_tree(70, 250, 360),
    monkey(270, 236, 0.85, "laugh", "down"),
    heart(270, 175, 0.7),
    mehar(160, 238, 0.85, arms="wave", eyes="happy"),
    crocodile(430, 520, 0.9, "sly", "open", flip=True),
    water_over(250, 600, 525),
])

# 10. A basket of jamuns to share
basket = ('<path d="M-40,0 L-32,-34 L32,-34 L40,0 Z" fill="#c98a4b"/><path d="M-36,-16 H36" stroke="#a06d3b" stroke-width="3"/>'
          + "".join(jamun(dx, -40, 1.0) for dx in (-20, -4, 12, 26)))
pics["10"] = scene(day_river("sky-10", 470) + [
    big_tree(70, 230, 380),
    mehar(300, 218, 0.85, arms="down", mouth="smile", look=4),
    monkey(180, 216, 0.75, "happy", "down"),
    '<path d="M335,165 C380,180 400,260 400,380" fill="none" stroke="#c8b48a" stroke-width="3"/>',
    g(basket, 400, 420, 1.1),
    crocodile(420, 540, 0.85, "sorry", "closed", flip=True),
    water_over(250, 600, 545),
])

# 11. Back home, a new picture in the book
picture = bubble(470, 230, 80, monkey(440, 280, 0.42, "laugh", "up") + crocodile(500, 290, 0.22, "happy", "smile", flip=True)
                 + '<rect x="455" y="160" width="26" height="30" rx="5" fill="#5b2a86"/><rect x="455" y="156" width="26" height="8" rx="3" fill="#ffd23f"/>', (440, 400))
pics["11"] = scene([bedroom("#2d2a5a"), window_frame(40, 50, 220, 240, "".join(night("sky-11w")) + moon(150, 140, 50, "sleepy")),
    mehar_in_bed(300, 470, 0.95, eyes="closed"),
    magic_book(420, 450, 0.5, glow=True, title=""),
    picture,
    zzz(200, 380),
])

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
