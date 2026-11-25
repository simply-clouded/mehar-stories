"""Reusable SVG pieces for Mehar's bedtime stories.

Every illustration is a plain SVG built from these pieces, so Mehar, the moon and
her animal friends look the same from one night's story to the next.

    from storyart import *
    svg = scene([sky("night"), moon(450, 120, 60, mood="happy"), mehar(300, 520)])
    open("01.svg", "w").write(svg)

Mehar's look lives in MEHAR below (skin, hair, outfit). Change it there once and
every new picture follows.
"""

import math

W, H = 600, 600  # every picture is a square; the page puts the words underneath

# Mehar's look, drawn from her family's reference photos (the photos themselves are
# never stored in this repository): a round face with rosy cheeks and a wide smile,
# big dark eyes, a chin-length dark-brown bob lighter at the tips with a long
# side-swept fringe and a pearl clip, a red pinafore over a white collared blouse.
MEHAR = {
    "skin": "#f1c6a3",
    "skin_shade": "#d9a07c",
    "cheek": "#ff8a8a",
    "hair": "#2a1810",
    "hair_tips": "#5b3a26",   # her bob turns lighter brown at the ends
    "hair_shine": "#7a5238",
    "iris": "#3a2216",
    "lash": "#1d120c",
    "tie": "#ff8fb1",
    "dress": "#d42f3c",       # red pinafore
    "dress_dark": "#9e1f2b",
    "button": "#ffffff",
    "blouse": "#fffdf7",      # white puff-sleeve blouse with a round collar
    "blouse_line": "#e3d9c8",
    "tights": "#fbf7f1",
    "shoes": "#b81f2e",
    "pyjama": "#9fb8ff",
}

PAINT = {
    "blue": "#3f7be8",
    "yellow": "#ffd23f",
    "green": "#4cbf6b",
    "red": "#ef5350",
    "purple": "#9b6ef3",
    "orange": "#ff9a3d",
    "pink": "#ff7fb6",
}


def scene(parts, bg=None):
    body = "\n".join(parts)
    bgrect = f'<rect width="{W}" height="{H}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" role="img">\n{bgrect}\n{body}\n</svg>\n')


def g(inner, x=0, y=0, s=1, extra=""):
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" {extra}>{inner}</g>'


# ---------------------------------------------------------------- skies and ground

SKIES = {
    "night": ("#16194a", "#3b3f8f"),
    "grey": ("#4b4d5c", "#7a7c8a"),
    "dusk": ("#2b2f7a", "#c86fa6"),
    "day": ("#7fc8ff", "#d8f1ff"),
    "painted": ("#1b3fa8", "#4f8cf0"),
}


def sky(kind="night", gid=None):
    top, bottom = SKIES[kind]
    gid = gid or f"sky-{kind}"
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>'
            f'</linearGradient></defs><rect width="{W}" height="{H}" fill="url(#{gid})"/>')


def hill(color="#2f6b4f", y=470, bump=60, back=None):
    out = []
    if back:
        out.append(f'<path d="M0,{y-30} Q150,{y-30-bump} 330,{y-20} T600,{y-40} V600 H0 Z" fill="{back}"/>')
    out.append(f'<path d="M0,{y} Q200,{y-bump} 380,{y+5} T600,{y-10} V600 H0 Z" fill="{color}"/>')
    return "".join(out)


def star_path(cx, cy, r, points=5, inner=0.45):
    pts = []
    for i in range(points * 2):
        a = math.pi / points * i - math.pi / 2
        rr = r if i % 2 == 0 else r * inner
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return "M" + " L".join(pts) + " Z"


def star(cx, cy, r=10, color="#ffe680", face=False):
    out = f'<path d="{star_path(cx, cy, r)}" fill="{color}" stroke="{color}" stroke-width="{r*0.25:.1f}" stroke-linejoin="round"/>'
    if face:
        out += (f'<circle cx="{cx-r*0.22:.1f}" cy="{cy-r*0.05:.1f}" r="{r*0.08:.1f}" fill="#4a3a10"/>'
                f'<circle cx="{cx+r*0.22:.1f}" cy="{cy-r*0.05:.1f}" r="{r*0.08:.1f}" fill="#4a3a10"/>'
                f'<path d="M{cx-r*0.18:.1f},{cy+r*0.15:.1f} Q{cx:.1f},{cy+r*0.32:.1f} {cx+r*0.18:.1f},{cy+r*0.15:.1f}" '
                f'fill="none" stroke="#4a3a10" stroke-width="{r*0.07:.1f}" stroke-linecap="round"/>')
    return out


def sparkles(points, color="#ffffff", r=2.2):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" opacity="0.8"/>' for x, y in points)


def stroke(d, color, width=46, opacity=0.95):
    """A thick, round paint stroke."""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"/>')


def zzz(x, y, color="#ffffff"):
    return "".join(
        f'<text x="{x + i*22}" y="{y - i*26}" font-family="Baloo 2, Arial Rounded MT Bold, sans-serif" '
        f'font-weight="700" font-size="{22 + i*8}" fill="{color}" opacity="{0.9 - i*0.2}">z</text>'
        for i in range(3))


# ---------------------------------------------------------------- the moon

def moon(cx, cy, r=70, mood="happy", glow=True, grey=False):
    face = "#c3c5cf" if grey else "#ffe9a8"
    crater = "#a9abb6" if grey else "#f5d27a"
    ink = "#55586a" if grey else "#6b4b16"
    out = []
    if glow and not grey:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r*1.7:.0f}" fill="#fff3c4" opacity="0.12"/>'
                   f'<circle cx="{cx}" cy="{cy}" r="{r*1.3:.0f}" fill="#fff3c4" opacity="0.18"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{face}"/>')
    out.append(f'<circle cx="{cx+r*0.45:.0f}" cy="{cy-r*0.4:.0f}" r="{r*0.14:.0f}" fill="{crater}"/>'
               f'<circle cx="{cx-r*0.5:.0f}" cy="{cy+r*0.45:.0f}" r="{r*0.1:.0f}" fill="{crater}"/>'
               f'<circle cx="{cx+r*0.15:.0f}" cy="{cy+r*0.62:.0f}" r="{r*0.07:.0f}" fill="{crater}"/>')
    ex, ey = r * 0.3, cy - r * 0.08
    if mood == "sleepy":
        for sx in (-1, 1):
            out.append(f'<path d="M{cx+sx*ex-r*0.12:.1f},{ey:.1f} Q{cx+sx*ex:.1f},{ey+r*0.1:.1f} {cx+sx*ex+r*0.12:.1f},{ey:.1f}" '
                       f'fill="none" stroke="{ink}" stroke-width="{r*0.05:.1f}" stroke-linecap="round"/>')
    else:
        for sx in (-1, 1):
            out.append(f'<ellipse cx="{cx+sx*ex:.1f}" cy="{ey:.1f}" rx="{r*0.07:.1f}" ry="{r*0.1:.1f}" fill="{ink}"/>')
    my = cy + r * 0.28
    if mood == "sad":
        out.append(f'<path d="M{cx-r*0.2:.1f},{my+r*0.08:.1f} Q{cx:.1f},{my-r*0.08:.1f} {cx+r*0.2:.1f},{my+r*0.08:.1f}" '
                   f'fill="none" stroke="{ink}" stroke-width="{r*0.05:.1f}" stroke-linecap="round"/>')
    else:
        big = 0.3 if mood == "happy" else 0.18
        out.append(f'<path d="M{cx-r*0.24:.1f},{my-r*0.05:.1f} Q{cx:.1f},{my+r*big:.1f} {cx+r*0.24:.1f},{my-r*0.05:.1f}" '
                   f'fill="none" stroke="{ink}" stroke-width="{r*0.05:.1f}" stroke-linecap="round"/>')
        if not grey:
            out.append(f'<circle cx="{cx-r*0.5:.1f}" cy="{my-r*0.08:.1f}" r="{r*0.1:.1f}" fill="#ffad8a" opacity="0.6"/>'
                       f'<circle cx="{cx+r*0.5:.1f}" cy="{my-r*0.08:.1f}" r="{r*0.1:.1f}" fill="#ffad8a" opacity="0.6"/>')
    return "".join(out)


# ---------------------------------------------------------------- Mehar

def _defs_mehar():
    c = MEHAR
    return (f'<defs><linearGradient id="mehar-hair" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{c["hair"]}"/><stop offset="0.7" stop-color="{c["hair"]}"/>'
            f'<stop offset="1" stop-color="{c["hair_tips"]}"/></linearGradient></defs>')


def _eye(x, kind, c):
    ink = c["lash"]
    if kind == "closed":
        return (f'<path d="M{x-7},-148 Q{x},-141 {x+7},-148" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>'
                f'<path d="M{x+6},-147 l3,1.5 M{x-6},-147 l-3,1.5" stroke="{ink}" stroke-width="1.6" stroke-linecap="round"/>')
    if kind == "happy":
        return (f'<path d="M{x-7.5},-145 Q{x},-155 {x+7.5},-145" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>'
                f'<path d="M{x+7},-147 l3,-2" stroke="{ink}" stroke-width="1.6" stroke-linecap="round"/>')
    side = 1 if x > 0 else -1
    return (f'<ellipse cx="{x}" cy="-148" rx="7.2" ry="8" fill="#ffffff"/>'
            f'<ellipse cx="{x+0.6}" cy="-147.4" rx="5.6" ry="6.6" fill="{c["iris"]}"/>'
            f'<circle cx="{x+0.6}" cy="-147.2" r="3.1" fill="#120a06"/>'
            f'<circle cx="{x+2.6}" cy="-150.2" r="2" fill="#fff"/>'
            f'<circle cx="{x-1.6}" cy="-144.6" r="0.9" fill="#fff" opacity="0.8"/>'
            f'<path d="M{x-8},-148.5 Q{x},-158.5 {x+8},-148.5" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>'
            f'<path d="M{x+side*7.5},-150 l{side*3.2},-2.4" stroke="{ink}" stroke-width="1.6" stroke-linecap="round"/>')


def mehar_head(eyes="open", mouth="smile", look=0, hair="bob"):
    """Mehar's head, centred near (0, -150).

    Drawn from her family's photos: a round face with full rosy cheeks and a wide
    smile, big dark eyes with lashes, and a chin-length bob in dark brown that turns
    lighter at the tips, parted on one side with a long fringe swept across, and a
    pearl-white hair clip. hair="bun" adds the little top bun with a bow she
    sometimes wears; hair="sprout" the tied-up "palm tree" from when she was small.
    """
    c = MEHAR
    hc = "url(#mehar-hair)"
    ex = 14 + look
    p = [_defs_mehar()]
    if hair == "bun":
        p.append(f'<circle cx="2" cy="-196" r="12" fill="{c["hair"]}"/>'
                 f'<path d="M-8,-188 l-9,-6 l1,12 z M10,-188 l9,-6 l-1,12 z" fill="#ffffff" stroke="#e6dccb" stroke-width="1"/>'
                 f'<circle cx="1" cy="-187" r="3.5" fill="#ffffff" stroke="#e6dccb" stroke-width="1"/>')
    elif hair == "sprout":
        p.append(f'<path d="M0,-188 C-3,-198 -10,-203 -16,-208 M0,-188 C-1,-200 -1,-208 2,-216 M0,-188 C3,-199 9,-204 16,-206" '
                 f'fill="none" stroke="{c["hair"]}" stroke-width="4.5" stroke-linecap="round"/>'
                 f'<ellipse cx="0" cy="-189" rx="7" ry="4.5" fill="{c["tie"]}"/>')
    p += [
        # the bob behind the face, ends flicking out at the chin
        f'<path d="M-46,-148 C-50,-198 50,-202 46,-148 C46,-130 48,-118 55,-109 C45,-104 37,-108 33,-114 L-33,-114 '
        f'C-37,-108 -45,-104 -55,-109 C-48,-118 -46,-130 -46,-148 Z" fill="{hc}"/>',
        # face
        f'<path d="M-34,-156 C-34,-188 34,-188 34,-156 C36,-128 22,-111 0,-110 C-22,-111 -36,-128 -34,-156 Z" fill="{c["skin"]}"/>',
        f'<path d="M-30,-130 C-24,-116 -12,-111 0,-110 C12,-111 24,-116 30,-130 C22,-118 12,-114 0,-114 C-12,-114 -22,-118 -30,-130 Z" fill="{c["skin_shade"]}" opacity="0.35"/>',
        # locks falling in front of the cheeks
        f'<path d="M-46,-150 C-45,-130 -44,-117 -55,-109 C-43,-104 -34,-112 -31,-124 C-29,-138 -31,-150 -35,-162 Z" fill="{hc}"/>',
        f'<path d="M46,-150 C45,-130 44,-117 55,-109 C43,-104 34,-112 31,-124 C29,-138 31,-150 35,-162 Z" fill="{hc}"/>',
        # long side-swept fringe from a parting on her left
        f'<path d="M12,-192 C-12,-194 -40,-184 -42,-150 C-36,-158 -26,-163 -14,-162 C0,-163 9,-170 13,-179 '
        f'C18,-170 28,-163 38,-155 C39,-176 29,-191 12,-192 Z" fill="{c["hair"]}"/>',
        # shine on the hair
        f'<path d="M-26,-184 C-36,-176 -42,-162 -43,-146 M28,-186 C38,-176 43,-160 43,-140 M4,-189 C-8,-186 -20,-178 -28,-168" '
        f'fill="none" stroke="{c["hair_shine"]}" stroke-width="2.2" stroke-linecap="round" opacity="0.55"/>',
        # pearl hair clip
        f'<rect x="16" y="-184" width="24" height="7" rx="3.5" fill="#fffaf0" stroke="#e2d6c2" stroke-width="1" transform="rotate(28 28 -180)"/>' if hair == "bob" else "",
        # cheeks, brows, nose
        f'<ellipse cx="-21" cy="-131" rx="8.5" ry="6.5" fill="{c["cheek"]}" opacity="0.45"/>',
        f'<ellipse cx="21" cy="-131" rx="8.5" ry="6.5" fill="{c["cheek"]}" opacity="0.45"/>',
        f'<path d="M{ex-6},-162 Q{ex},-165.5 {ex+6},-162" fill="none" stroke="{c["hair"]}" stroke-width="2" stroke-linecap="round" opacity="0.85"/>',
        f'<path d="M-2.6,-136.5 Q0,-133.8 2.6,-136.5" fill="none" stroke="{c["skin_shade"]}" stroke-width="2.4" stroke-linecap="round"/>',
        _eye(-ex, eyes, c), _eye(ex, eyes, c),
    ]
    if mouth == "smile":   # her wide, toothy smile
        p.append('<path d="M-12.5,-127 Q0,-109 12.5,-127 Q0,-123.5 -12.5,-127 Z" fill="#7a2f2a"/>'
                 '<path d="M-8.5,-125.6 Q0,-123.4 8.5,-125.6 L7.5,-122.6 Q0,-121.2 -7.5,-122.6 Z" fill="#fff"/>'
                 '<path d="M-5.5,-116.8 Q0,-114.6 5.5,-116.8" fill="none" stroke="#ff8d8d" stroke-width="2.6" stroke-linecap="round"/>')
    elif mouth == "soft":
        p.append('<path d="M-8,-126 Q0,-119 8,-126" fill="none" stroke="#6a2f22" stroke-width="2.6" stroke-linecap="round"/>')
    elif mouth == "open":
        p.append('<path d="M-10,-128 Q0,-108 10,-128 Z" fill="#7a2f2a"/><ellipse cx="0" cy="-116" rx="5" ry="3" fill="#ff8d8d"/>')
    elif mouth == "yawn":
        p.append('<ellipse cx="0" cy="-122" rx="5.5" ry="7" fill="#7a2f2a"/>')
    elif mouth == "oh":
        p.append('<circle cx="0" cy="-123" r="4" fill="#7a2f2a"/>')
    return "".join(p)


def _arm(x1, y1, x2, y2, sleeve):
    c = MEHAR
    mx, my = x1 + (x2 - x1) * 0.38, y1 + (y2 - y1) * 0.38
    return (f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{c["skin"]}" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cx="{x2}" cy="{y2}" r="6.5" fill="{c["skin"]}"/>'
            f'<path d="M{x1},{y1} L{mx:.1f},{my:.1f}" stroke="{c["blouse_line"]}" stroke-width="17" stroke-linecap="round"/>'
            f'<path d="M{x1},{y1} L{mx:.1f},{my:.1f}" stroke="{sleeve}" stroke-width="15" stroke-linecap="round"/>')


def paintbrush(x, y, angle=-35, tip=PAINT["blue"], s=1):
    """A brush held at (x, y), rotated `angle` degrees (0 = bristles straight up)."""
    return (f'<g transform="translate({x} {y}) rotate({angle}) scale({s})">'
            f'<rect x="-4" y="-70" width="8" height="64" rx="4" fill="#c98a4b"/>'
            f'<rect x="-6" y="-80" width="12" height="14" rx="2" fill="#b8bcc8"/>'
            f'<path d="M-6,-80 Q0,-108 6,-80 Z" fill="{tip}"/></g>')


def mehar(x, y, s=1, arms="down", eyes="open", mouth="smile", outfit="dress",
          brush=None, look=0, flip=False, hair="bob", legs=True):
    """Mehar standing, feet at (x, y). About 215*s pixels tall.

    arms: down | wave | up | brush | hold (left hand out, to hold a friend's paw)
    outfit: dress (red pinafore over a white puff-sleeve blouse) | pyjama
    legs=False hides the legs (for riding Moti, sitting behind things).
    """
    c = MEHAR
    pj = outfit == "pyjama"
    sleeve = c["pyjama"] if pj else c["blouse"]
    p = []
    if legs:
        if pj:
            p.append(f'<rect x="-18" y="-46" width="14" height="42" rx="6" fill="{c["pyjama"]}"/>'
                     f'<rect x="4" y="-46" width="14" height="42" rx="6" fill="{c["pyjama"]}"/>'
                     f'<ellipse cx="-11" cy="-3" rx="10" ry="6" fill="{c["skin"]}"/><ellipse cx="11" cy="-3" rx="10" ry="6" fill="{c["skin"]}"/>')
        else:
            p.append(f'<rect x="-16" y="-46" width="10" height="42" rx="5" fill="{c["tights"]}" stroke="{c["blouse_line"]}" stroke-width="1.2"/>'
                     f'<rect x="6" y="-46" width="10" height="42" rx="5" fill="{c["tights"]}" stroke="{c["blouse_line"]}" stroke-width="1.2"/>'
                     f'<path d="M-24,-2 Q-24,-12 -11,-12 Q0,-12 -1,-2 Z" fill="{c["shoes"]}"/>'
                     f'<path d="M24,-2 Q24,-12 11,-12 Q0,-12 1,-2 Z" fill="{c["shoes"]}"/>'
                     f'<path d="M-16,-11 L-6,-11 M6,-11 L16,-11" stroke="{c["shoes"]}" stroke-width="2.4"/>')
    left = {"down": (-34, -62), "wave": (-36, -64), "up": (-46, -148), "brush": (-34, -62), "hold": (-58, -74)}[arms]
    right = {"down": (34, -62), "wave": (46, -146), "up": (46, -148), "brush": (52, -110), "hold": (34, -62)}[arms]
    # body
    if pj:
        p.append(f'<path d="M-21,-108 Q0,-113 21,-108 L34,-42 Q0,-36 -34,-42 Z" fill="{c["pyjama"]}"/>')
        for dx, dy in ((-14, -60), (12, -78), (18, -52), (-6, -92), (-20, -82), (4, -56)):
            p.append(f'<path d="{star_path(dx, dy, 4)}" fill="#ffe680"/>')
    else:
        p.append(f'<path d="M-21,-108 Q0,-113 21,-108 L28,-96 L-28,-96 Z" fill="{c["blouse"]}"/>'
                 f'<path d="M-18,-100 Q0,-104 18,-100 L44,-40 Q0,-30 -44,-40 Z" fill="{c["dress"]}"/>'
                 f'<path d="M-42,-44 Q0,-34 42,-44" fill="none" stroke="{c["dress_dark"]}" stroke-width="3"/>'
                 f'<path d="M-30,-70 Q0,-64 30,-70" fill="none" stroke="{c["dress_dark"]}" stroke-width="1.5" opacity="0.6"/>'
                 # Peter Pan collar and a little bow
                 f'<path d="M0,-108 C-6,-109 -19,-110 -21,-103 C-18,-94 -7,-95 0,-102 Z" fill="{c["blouse"]}" stroke="{c["blouse_line"]}" stroke-width="1.2"/>'
                 f'<path d="M0,-108 C6,-109 19,-110 21,-103 C18,-94 7,-95 0,-102 Z" fill="{c["blouse"]}" stroke="{c["blouse_line"]}" stroke-width="1.2"/>'
                 f'<path d="M0,-98 l-7,-4 v9 z M0,-98 l7,-4 v9 z" fill="{c["dress_dark"]}"/><circle cx="0" cy="-98" r="2.4" fill="{c["dress_dark"]}"/>'
                 f'<circle cx="-12" cy="-84" r="2.2" fill="{c["button"]}"/><circle cx="12" cy="-84" r="2.2" fill="{c["button"]}"/>')
    p.append(_arm(-21, -100, *left, sleeve))
    p.append(_arm(21, -100, *right, sleeve))
    p.append(f'<rect x="-6" y="-116" width="12" height="10" rx="4" fill="{c["skin"]}"/>')
    p.append(mehar_head(eyes, mouth, look, hair))
    if arms == "brush" or brush:
        hx, hy = right
        p.append(paintbrush(hx, hy + 6, angle=30, tip=brush or PAINT["blue"]))
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def mehar_in_bed(x, y, s=1, blanket="#7f8cff", eyes="closed", friend=None):
    """Mehar tucked into bed; (x, y) is the middle of the mattress top.
    friend: extra svg (in bed coordinates) drawn on the blanket, e.g. a sleeping bunny."""
    inner = (
        f'<rect x="-190" y="-10" width="380" height="80" rx="16" fill="#8a5a3c"/>'
        f'<rect x="-200" y="-130" width="26" height="200" rx="10" fill="#8a5a3c"/>'
        f'<rect x="-182" y="-24" width="364" height="34" rx="14" fill="#f3efe6"/>'
        f'<ellipse cx="-110" cy="-30" rx="70" ry="30" fill="#ffffff"/>'
        + g(mehar_head(eyes, "soft"), -110, 92, 0.95)
        + f'<path d="M-150,-14 Q-40,-60 180,-24 L180,30 L-150,30 Z" fill="{blanket}"/>'
        + "".join(f'<path d="{star_path(-60 + i*55, 0 - (i % 2) * 14, 7)}" fill="#ffe680"/>' for i in range(5))
        + (friend or "")
    )
    return g(inner, x, y, s)


def owl(x, y, s=1, wings="down", holding=None, eyes="open"):
    body, belly, wing = "#9a6b47", "#e8c9a0", "#7d5536"
    p = [
        f'<path d="M-30,-58 L-22,-84 L-10,-64 Z" fill="{body}"/>',
        f'<path d="M30,-58 L22,-84 L10,-64 Z" fill="{body}"/>',
        f'<ellipse cx="0" cy="-36" rx="36" ry="42" fill="{body}"/>',
        f'<ellipse cx="0" cy="-22" rx="22" ry="24" fill="{belly}"/>',
    ]
    if wings == "up":
        p.append(f'<path d="M-32,-40 Q-80,-80 -70,-20 Q-50,-30 -32,-20 Z" fill="{wing}"/>'
                 f'<path d="M32,-40 Q80,-80 70,-20 Q50,-30 32,-20 Z" fill="{wing}"/>')
    else:
        p.append(f'<ellipse cx="-33" cy="-30" rx="10" ry="24" fill="{wing}"/>'
                 f'<ellipse cx="33" cy="-30" rx="10" ry="24" fill="{wing}"/>')
    for sx in (-1, 1):
        p.append(f'<circle cx="{sx*14}" cy="-52" r="13" fill="#fff8e6"/>')
        if eyes == "closed":
            p.append(f'<path d="M{sx*14-7},-52 Q{sx*14},-46 {sx*14+7},-52" fill="none" stroke="#2a1b14" stroke-width="2.5" stroke-linecap="round"/>')
        else:
            p.append(f'<circle cx="{sx*14}" cy="-51" r="6.5" fill="#2a1b14"/><circle cx="{sx*14+2}" cy="-53" r="2" fill="#fff"/>')
    p.append('<path d="M-6,-42 L6,-42 L0,-32 Z" fill="#f2a33a"/>')
    p.append('<path d="M-14,4 l-4,6 M-10,4 l0,7 M10,4 l0,7 M14,4 l4,6" stroke="#f2a33a" stroke-width="3" stroke-linecap="round"/>')
    if holding:
        p.append(paintbrush(-8, 4, angle=-70, tip=holding, s=0.8))
    return g("".join(p), x, y, s)


def bunny(x, y, s=1, eyes="open", ear_flop=False):
    fur, inner = "#f6f2ee", "#ffb3c7"
    lean = 18 if ear_flop else 0
    p = [
        f'<ellipse cx="-14" cy="-108" rx="10" ry="34" fill="{fur}" transform="rotate({-8 - lean} -14 -80)"/>',
        f'<ellipse cx="-14" cy="-108" rx="5" ry="24" fill="{inner}" transform="rotate({-8 - lean} -14 -80)"/>',
        f'<ellipse cx="14" cy="-108" rx="10" ry="34" fill="{fur}" transform="rotate(8 14 -80)"/>',
        f'<ellipse cx="14" cy="-108" rx="5" ry="24" fill="{inner}" transform="rotate(8 14 -80)"/>',
        f'<ellipse cx="0" cy="-26" rx="32" ry="30" fill="{fur}"/>',
        f'<circle cx="30" cy="-14" r="10" fill="#ffffff"/>',
        f'<circle cx="0" cy="-66" r="27" fill="{fur}"/>',
        f'<ellipse cx="-14" cy="-2" rx="12" ry="7" fill="{fur}"/><ellipse cx="14" cy="-2" rx="12" ry="7" fill="{fur}"/>',
        f'<circle cx="-15" cy="-58" r="5" fill="{inner}" opacity="0.6"/><circle cx="15" cy="-58" r="5" fill="{inner}" opacity="0.6"/>',
        '<path d="M-3,-62 L3,-62 L0,-58 Z" fill="#ff7fa0"/>',
        '<path d="M0,-58 Q-5,-52 -8,-55 M0,-58 Q5,-52 8,-55" fill="none" stroke="#7a5a5a" stroke-width="1.8" stroke-linecap="round"/>',
    ]
    for sx in (-1, 1):
        if eyes == "closed":
            p.append(f'<path d="M{sx*10-5},-70 Q{sx*10},-66 {sx*10+5},-70" fill="none" stroke="#2a1b14" stroke-width="2.2" stroke-linecap="round"/>')
        else:
            p.append(f'<circle cx="{sx*10}" cy="-70" r="4" fill="#2a1b14"/><circle cx="{sx*10+1.4}" cy="-71.5" r="1.3" fill="#fff"/>')
    return g("".join(p), x, y, s)


def tree(x, y, s=1, color="#4cbf6b", trunk="#7a5236", grey=False):
    if grey:
        color, trunk = "#8c8f99", "#6d6f78"
    shade = "#000000"
    inner = (f'<rect x="-9" y="-70" width="18" height="70" rx="6" fill="{trunk}"/>'
             f'<circle cx="0" cy="-118" r="46" fill="{color}"/>'
             f'<circle cx="-34" cy="-90" r="32" fill="{color}"/>'
             f'<circle cx="34" cy="-90" r="32" fill="{color}"/>'
             f'<circle cx="12" cy="-80" r="26" fill="{shade}" opacity="0.08"/>')
    return g(inner, x, y, s)


def flower(x, y, s=1, petal=PAINT["pink"], center="#ffd23f"):
    petals = "".join(f'<circle cx="{10*math.cos(a):.1f}" cy="{-40 + 10*math.sin(a):.1f}" r="8" fill="{petal}"/>'
                     for a in [i * math.pi * 2 / 5 for i in range(5)])
    return g(f'<path d="M0,0 Q4,-20 0,-38" stroke="#3f9a55" stroke-width="4" fill="none"/>'
             f'<ellipse cx="7" cy="-16" rx="8" ry="4" fill="#3f9a55" transform="rotate(-30 7 -16)"/>'
             + petals + f'<circle cx="0" cy="-40" r="6" fill="{center}"/>', x, y, s)


def window_frame(x, y, w, h, inside, frame="#f3d9a8"):
    """A bedroom window at (x, y) showing `inside` (svg drawn in 600x600 space, clipped)."""
    cid = f"win{x}{y}"
    return (f'<defs><clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14"/></clipPath></defs>'
            f'<g clip-path="url(#{cid})">{inside}</g>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="none" stroke="{frame}" stroke-width="14"/>'
            f'<line x1="{x + w/2}" y1="{y}" x2="{x + w/2}" y2="{y+h}" stroke="{frame}" stroke-width="10"/>'
            f'<line x1="{x}" y1="{y + h/2}" x2="{x+w}" y2="{y + h/2}" stroke="{frame}" stroke-width="10"/>'
            f'<rect x="{x-20}" y="{y+h}" width="{w+40}" height="16" rx="6" fill="{frame}"/>')


def bedroom(wall="#3b3770", floor="#5a4636"):
    return (f'<rect width="{W}" height="{H}" fill="{wall}"/>'
            f'<rect y="470" width="{W}" height="130" fill="{floor}"/>'
            f'<rect y="462" width="{W}" height="12" fill="#00000022"/>')


# ---------------------------------------------------------------- more friends

def elephant(x, y, s=1, rider=None, trunk="up", eyes="open", blanket="#d42f3c"):
    """Moti the elephant, facing right, feet at (x, y). About 230*s wide.
    rider: an svg drawn on his back (place it at about (-10, -150) in his space,
    e.g. mehar(-10, -118, 0.8, legs=False)); the saddle cloth covers its lower half."""
    skin, dark, inner = "#9fabc8", "#8592b2", "#f3b6c6"
    p = [
        f'<path d="M-92,-80 q-16,10 -12,30" fill="none" stroke="{dark}" stroke-width="5" stroke-linecap="round"/>',
        f'<rect x="-70" y="-60" width="30" height="60" rx="12" fill="{dark}"/><rect x="30" y="-60" width="30" height="60" rx="12" fill="{dark}"/>',
        f'<ellipse cx="0" cy="-90" rx="95" ry="62" fill="{skin}"/>',
        f'<rect x="-48" y="-56" width="30" height="56" rx="12" fill="{skin}"/><rect x="50" y="-56" width="30" height="56" rx="12" fill="{skin}"/>',
        f'<path d="M-48,-8 h30 M50,-8 h30" stroke="#ffffff" stroke-width="3" stroke-dasharray="4 5" opacity="0.7"/>',
    ]
    if rider:
        p.append(rider)
    p += [
        f'<path d="M-60,-148 Q-10,-160 40,-148 L46,-108 Q-10,-96 -66,-108 Z" fill="{blanket}"/>',
        f'<path d="M-66,-108 Q-10,-96 46,-108" fill="none" stroke="#ffd36b" stroke-width="5" stroke-dasharray="3 6" stroke-linecap="round"/>',
        f'<circle cx="-10" cy="-130" r="6" fill="#ffd36b"/>',
        # head, ear, trunk
        f'<circle cx="92" cy="-122" r="52" fill="{skin}"/>',
        f'<ellipse cx="62" cy="-118" rx="34" ry="44" fill="{dark}"/><ellipse cx="64" cy="-116" rx="22" ry="31" fill="{inner}" opacity="0.8"/>',
    ]
    if trunk == "up":
        p.append(f'<path d="M128,-104 C150,-80 160,-60 170,-90 C176,-110 168,-124 156,-128" fill="none" stroke="{skin}" stroke-width="24" stroke-linecap="round"/>')
    else:
        p.append(f'<path d="M128,-104 C146,-80 150,-50 142,-26" fill="none" stroke="{skin}" stroke-width="24" stroke-linecap="round"/>')
    p.append(f'<path d="M120,-92 q12,6 16,18" fill="none" stroke="#fffdf4" stroke-width="7" stroke-linecap="round"/>')
    if eyes == "closed":
        p.append('<path d="M100,-134 q7,6 14,0" fill="none" stroke="#2a2440" stroke-width="3" stroke-linecap="round"/>')
    else:
        p.append('<ellipse cx="106" cy="-134" rx="5.5" ry="7" fill="#2a2440"/><circle cx="108" cy="-136.5" r="2" fill="#fff"/>')
    p.append('<ellipse cx="114" cy="-112" rx="8" ry="5" fill="#ff9aa8" opacity="0.5"/>')
    p.append('<path d="M70,-170 q4,-14 12,-4 q6,-12 10,2" fill="none" stroke="#8592b2" stroke-width="3" stroke-linecap="round"/>')
    return g("".join(p), x, y, s)


def cloud(x, y, s=1, mood="sad", rainbow=False, cid="cl"):
    """Badal the cloud, centred at (x, y). About 260*s wide."""
    blobs = [(-80, 0, 50), (-30, -30, 62), (40, -26, 58), (90, 4, 46), (0, 18, 60), (-50, 26, 44), (60, 28, 44)]
    shape = "".join(f'<circle cx="{bx}" cy="{by}" r="{r}"/>' for bx, by, r in blobs)
    p = [f'<defs><clipPath id="{cid}">{shape}</clipPath></defs>']
    if rainbow:
        bands = ["#ef5350", "#ff9a3d", "#ffd23f", "#4cbf6b", "#3f7be8", "#9b6ef3"]
        p.append(f'<g clip-path="url(#{cid})">' + "".join(
            f'<rect x="-140" y="{-95 + i*33}" width="280" height="34" fill="{b}"/>' for i, b in enumerate(bands)) + '</g>')
        p.append(f'<g clip-path="url(#{cid})"><ellipse cx="-30" cy="-60" rx="90" ry="30" fill="#ffffff" opacity="0.25"/></g>')
    else:
        p.append(f'<g fill="#9a9db0">{shape}</g><g clip-path="url(#{cid})"><ellipse cx="0" cy="70" rx="160" ry="40" fill="#7f8297"/></g>')
    ink = "#2c2250"
    if mood == "sad":
        p.append(f'<path d="M-38,-6 q8,-6 16,0 M22,-6 q8,-6 16,0" fill="none" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>'
                 f'<path d="M-14,26 q14,-12 28,0" fill="none" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>'
                 + "".join(f'<path d="M{dx},{dy} q-6,10 0,14 q6,-4 0,-14 Z" fill="#7fb3ff"/>' for dx, dy in ((-30, 10), (30, 12), (-60, 70), (-10, 90), (40, 80), (80, 64), (10, 120))))
    else:
        p.append(f'<path d="M-38,-6 q8,-8 16,0 M22,-6 q8,-8 16,0" fill="none" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>'
                 f'<path d="M-18,14 Q0,40 18,14 Z" fill="{ink}"/><ellipse cx="0" cy="26" rx="6" ry="4" fill="#ff8d8d"/>'
                 f'<ellipse cx="-50" cy="12" rx="10" ry="6" fill="#ff8fb1" opacity="0.7"/><ellipse cx="50" cy="12" rx="10" ry="6" fill="#ff8fb1" opacity="0.7"/>')
    return g("".join(p), x, y, s)


def firefly(x, y, s=1):
    return g('<circle r="22" fill="#e8ff7a" opacity="0.18"/><circle r="12" fill="#e8ff7a" opacity="0.35"/>'
             '<ellipse cx="-5" cy="-7" rx="6" ry="4" fill="#ffffff" opacity="0.7" transform="rotate(-30 -5 -7)"/>'
             '<ellipse cx="5" cy="-7" rx="6" ry="4" fill="#ffffff" opacity="0.7" transform="rotate(30 5 -7)"/>'
             '<ellipse cx="0" cy="0" rx="5" ry="7" fill="#f6ff9e"/><circle cx="0" cy="-7" r="3.5" fill="#3a3550"/>',
             x, y, s)


def number_tag(x, y, n, color="#ffffff"):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Baloo 2, Arial Rounded MT Bold, sans-serif" '
            f'font-weight="800" font-size="28" fill="{color}">{n}</text>')


def paintbox(x, y, s=1, open_=True):
    pans = ["#ef5350", "#ff9a3d", "#ffd23f", "#4cbf6b", "#3f7be8", "#9b6ef3"]
    lid = '<rect x="-60" y="-70" width="120" height="44" rx="8" fill="#2f6fd0"/><text x="0" y="-41" text-anchor="middle" font-family="Baloo 2, sans-serif" font-weight="800" font-size="18" fill="#fff">PAINTS</text>' if open_ else ""
    return g(lid + '<rect x="-62" y="-26" width="124" height="34" rx="8" fill="#ffffff" stroke="#d8d2c4" stroke-width="2"/>'
             + "".join(f'<ellipse cx="{-50 + i*20}" cy="-9" rx="8" ry="6" fill="{c}"/>' for i, c in enumerate(pans)), x, y, s)


def moonbeam(x1, y1, x2, y2, w1=30, w2=140):
    return (f'<defs><linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3c4" stop-opacity="0.75"/>'
            f'<stop offset="1" stop-color="#fff3c4" stop-opacity="0.15"/></linearGradient></defs>'
            f'<path d="M{x1-w1/2},{y1} L{x1+w1/2},{y1} L{x2+w2/2},{y2} L{x2-w2/2},{y2} Z" fill="url(#beam)"/>')


def forest(dark=True):
    trunk = "#2b2440" if dark else "#7a5236"
    leaf = "#24305a" if dark else "#3f9a55"
    leaf2 = "#1c2549" if dark else "#2f8a4c"
    return (tree(40, 470, 1.2, leaf2, trunk) + tree(170, 440, 0.9, leaf, trunk) + tree(450, 450, 1.0, leaf, trunk)
            + tree(575, 480, 1.25, leaf2, trunk) + f'<rect y="460" width="600" height="140" fill="{"#1b2140" if dark else "#3fa45e"}"/>')


def eyes_in_dark(points):
    return "".join(f'<ellipse cx="{x-6}" cy="{y}" rx="3.5" ry="5" fill="#ffe680"/><ellipse cx="{x+6}" cy="{y}" rx="3.5" ry="5" fill="#ffe680"/>' for x, y in points)
