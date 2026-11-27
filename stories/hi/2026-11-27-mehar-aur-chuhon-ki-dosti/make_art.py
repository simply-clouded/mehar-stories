"""Draws the pictures for "मेहर और चूहों की दोस्ती" (Mehar aur chuhon ki dosti). Run: python3 make_art.py"""
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


def mouse_hole(x, y, s=1, broken=False):
    """A little mouse home: an earth mound with a round door."""
    inner = ('<path d="M-50,0 C-50,-50 50,-50 50,0 Z" fill="#a8774a"/>'
             '<path d="M-16,0 C-16,-24 16,-24 16,0 Z" fill="#3b2a20"/>')
    if broken:
        inner = ('<path d="M-56,0 C-46,-18 -30,-10 -20,-22 C-6,-8 10,-26 24,-12 C36,-20 50,-8 56,0 Z" fill="#a8774a"/>'
                 '<path d="M-30,-4 l10,-6 M10,-6 l12,-4" stroke="#7a5236" stroke-width="3" stroke-linecap="round"/>'
                 '<ellipse cx="-40" cy="-4" rx="8" ry="4" fill="#8a5a3c"/><ellipse cx="40" cy="-2" rx="6" ry="3" fill="#8a5a3c"/>')
    return g(inner, x, y, s)


def footprint(x, y, s=1):
    return g('<ellipse cx="0" cy="0" rx="34" ry="16" fill="#8a6a45" opacity="0.55"/>'
             + "".join(f'<ellipse cx="{dx}" cy="-12" rx="7" ry="5" fill="#8a6a45" opacity="0.55"/>' for dx in (-18, 0, 18)), x, y, s)


def dust(x, y):
    return "".join(f'<circle cx="{x + dx}" cy="{y + dy}" r="{r}" fill="#e8d6b0" opacity="0.8"/>' for dx, dy, r in ((-20, 0, 16), (0, -10, 20), (24, -2, 14)))


def on_trunk(ex, ey, s, m):
    """Chuchu sitting on the curled-up end of Moti's trunk."""
    return mouse(ex + 152 * s, ey - 126 * s, m, crown=True)


pics = {}

pics["cover"] = scene(jungle("day", "sky-c") + [
    elephant(170, 580, 0.95, trunk="up"),
    on_trunk(170, 580, 0.95, 0.5),
    mouse(380, 585, 0.55), mouse(440, 590, 0.5, flip=True),
    mehar(450, 585, 1.1, arms="wave", eyes="happy"),
])

# 1. The book glows again; the ground goes dham-dham
pics["01"] = scene([bedroom("#2d2a5a"), window_frame(380, 60, 180, 210, "".join(night("sky-1w"))),
    magic_book(260, 500, 0.75),
    mouse(250, 425, 0.45, crown=True),
    mehar(110, 575, 1.25, arms="up", mouth="open", look=4),
])

# 2. Dham! Dham! The herd marches to the lake
pics["02"] = scene(jungle("day", "sky-2") + [
    elephant(300, 560, 0.5, blanket="#3f7be8", trunk="down"),
    elephant(410, 580, 0.55, blanket="#ffd23f", trunk="down"),
    elephant(160, 600, 0.85, trunk="up"),
    dust(120, 595), dust(250, 600), dust(420, 590),
    word(300, 140, "धम! धम!", "#d8343f", 56),
    mehar(550, 590, 0.75, arms="up", mouth="oh", look=-4),
])

# 3. The mice homes are broken
pics["03"] = scene(jungle("day", "sky-3") + [
    footprint(150, 540, 1.2), footprint(420, 520, 1.0),
    mouse_hole(160, 560, 1.2, broken=True), mouse_hole(360, 530, 1.0, broken=True), mouse_hole(470, 575, 1.1),
    mouse(250, 575, 1.1, "sad"), mouse(400, 595, 1.0, "sad", flip=True), mouse(90, 600, 0.85, "sad"),
    mehar(520, 560, 1.0, arms="down", mouth="soft", look=-5),
])

# 4. Chuchu on Mehar's palm asks Moti for help
pics["04"] = scene(jungle("day", "sky-4") + [
    elephant(170, 590, 0.95, trunk="down"),
    mehar(470, 590, 1.25, arms="hold", mouth="smile", look=-5),
    mouse(470 - 58 * 1.25 - 4, 590 - 74 * 1.25 + 4, 0.65, crown=True, flip=True),
    '<path d="M330,330 q-14,-10 -28,0 M336,310 q-20,-14 -40,0" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>',
])

# 5. Moti laughs, then takes a new path
pics["05"] = scene(jungle("day", "sky-5") + [
    '<path d="M600,520 Q450,470 360,420 L330,440 Q420,500 600,560 Z" fill="#c9a76a"/>',
    '<rect x="440" y="330" width="10" height="90" fill="#7a5236"/><path d="M400,330 h90 l20,20 l-20,20 h-90 Z" fill="#f3d9a8"/><path d="M420,350 h50 m-14,-10 l14,10 l-14,10" fill="none" stroke="#7a5236" stroke-width="5" stroke-linecap="round"/>',
    elephant(180, 590, 0.95, trunk="up", eyes="closed"),
    word(140, 330, "हा हा हा!", "#3f7be8", 40),
    mehar(470, 590, 1.0, arms="down", mouth="open", look=-5),
    mouse(400, 595, 0.5, crown=True),
])

# 6. Dhadaam! The net
pics["06"] = scene(jungle("dusk", "sky-6") + [
    elephant(130, 590, 0.75, blanket="#3f7be8", trunk="down"),
    elephant(320, 600, 0.95, trunk="down"),
    net(290, 600, 560, 250, "net6"),
    word(300, 150, "धड़ाम!", "#ffd23f", 60),
])

# 7. Moti calls for help; the rope is too thick for Mehar
pics["07"] = scene(jungle("dusk", "sky-7") + [
    elephant(220, 600, 1.0, trunk="up"),
    net(310, 600, 420, 230, "net7"),
    mehar(500, 590, 1.1, arms="hold", mouth="oh", look=-5),
    '<path d="M430,505 C460,500 440,520 470,510" fill="none" stroke="#c8a46a" stroke-width="6" stroke-linecap="round"/>',
    word(380, 190, "पूँ-पूँ!", "#d8343f", 50),
    '<circle cx="530" cy="300" r="26" fill="#fffbe6"/><text x="530" y="313" text-anchor="middle" font-family="Arial, sans-serif" font-weight="800" font-size="34" fill="#3f7be8">?</text>',
])

# 8. Chuchu whistles, and the mice come running
pics["08"] = scene(jungle("day", "sky-8") + [
    mehar(140, 590, 1.1, arms="wave", mouth="open", look=4),
    mouse(260, 590, 0.95, crown=True),
] + [mouse(340 + i * 55, 600 - (i % 2) * 30, 0.7) for i in range(5)]
  + [mouse(370 + i * 60, 535 - (i % 2) * 20, 0.6) for i in range(4)] + [
    '<path d="M310,570 h-30 M320,550 h-24" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>',
    word(420, 160, "चूँ-चूँ-चूँ!", "#d8343f", 46),
])

# 9. Kutar, kutar! The mice chew the net
pics["09"] = scene(jungle("dusk", "sky-9") + [
    elephant(220, 600, 1.0, trunk="down"),
    net(310, 600, 420, 230, "net9", torn=True),
    mouse(140, 470, 0.5, "chew"), mouse(250, 380, 0.5, "chew"), mouse(380, 400, 0.5, "chew", flip=True),
    mouse(470, 520, 0.5, "chew", flip=True), mouse(320, 520, 0.5, "chew"),
    word(300, 150, "कुतर, कुतर!", "#ffd23f", 48),
    mehar(540, 595, 0.8, arms="up", mouth="open", look=-4),
])

# 10. Free! Chuchu rides on Moti's trunk, and everybody dances
pics["10"] = scene(jungle("day", "sky-10") + [
    rope_heap(300, 595, 1.0),
    elephant(170, 580, 0.95, trunk="up"),
    on_trunk(170, 580, 0.95, 0.5),
    mehar(470, 585, 1.05, arms="up", eyes="happy", mouth="open"),
    mouse(370, 590, 0.5), mouse(560, 595, 0.5, flip=True),
    '<path d="M110,240 q20,-30 40,0 q20,-30 40,0 q-40,40 -40,40 q0,0 -40,-40 Z" fill="#ff7fb6" transform="translate(260 20) scale(0.7)"/>',
])

# 11. Back home, the new picture in the book
picture = (f'<circle cx="460" cy="230" r="90" fill="#ffffff"/><circle cx="440" cy="340" r="10" fill="#ffffff"/><circle cx="430" cy="380" r="6" fill="#ffffff"/>'
           + elephant(420, 290, 0.35, trunk="up") + on_trunk(420, 290, 0.35, 0.22))
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
