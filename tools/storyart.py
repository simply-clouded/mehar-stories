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


# ---------------------------------------------------------------- Panchatantra jungle

def lion(x, y, s=1, mood="proud", crown=True, wet=False, mouth=None, eyes="open"):
    """Raja Singh the lion, sitting and facing us, base at (x, y). About 230*s tall.
    mood: proud | roar | angry | sorry | happy"""
    fur, mane, mane2, belly = "#f2b24c", "#c9651f", "#a94f15", "#fbd79a"
    if wet:
        mane, mane2, fur = "#a5622a", "#8a4c1b", "#d9a14a"
    p = [
        f'<path d="M60,-20 C110,-20 110,-80 90,-90" fill="none" stroke="{fur}" stroke-width="10" stroke-linecap="round"/>'
        f'<circle cx="90" cy="-92" r="10" fill="{mane2}"/>',
        f'<ellipse cx="0" cy="-60" rx="62" ry="64" fill="{fur}"/>',
        f'<ellipse cx="0" cy="-48" rx="36" ry="46" fill="{belly}"/>',
        f'<ellipse cx="-34" cy="-6" rx="22" ry="12" fill="{fur}"/><ellipse cx="34" cy="-6" rx="22" ry="12" fill="{fur}"/>',
        f'<path d="M-42,-4 v-6 M-34,-2 v-7 M-26,-4 v-6 M26,-4 v-6 M34,-2 v-7 M42,-4 v-6" stroke="{mane2}" stroke-width="2" stroke-linecap="round"/>',
    ]
    # mane: a ring of soft spikes
    import math as _m
    spikes = []
    for i in range(18):
        a = i / 18 * 2 * _m.pi
        r1 = 62 if not wet else 52
        spikes.append(f'<ellipse cx="{r1*_m.cos(a):.1f}" cy="{-150 + r1*_m.sin(a):.1f}" rx="{24 if not wet else 16}" ry="{16 if not wet else 22}" '
                      f'transform="rotate({a*180/_m.pi:.0f} {r1*_m.cos(a):.1f} {-150 + r1*_m.sin(a):.1f})" fill="{mane if i % 2 else mane2}"/>')
    p.append("".join(spikes))
    p.append(f'<circle cx="0" cy="-150" r="56" fill="{mane}"/>')
    p.append(f'<circle cx="-34" cy="-186" r="12" fill="{fur}"/><circle cx="34" cy="-186" r="12" fill="{fur}"/>'
             f'<circle cx="-34" cy="-186" r="6" fill="#e58a6a"/><circle cx="34" cy="-186" r="6" fill="#e58a6a"/>')
    p.append(f'<ellipse cx="0" cy="-146" rx="42" ry="40" fill="{fur}"/>')
    p.append(f'<ellipse cx="0" cy="-128" rx="22" ry="15" fill="{belly}"/>')
    ink = "#3a2410"
    # brows & eyes
    if mood in ("angry", "roar"):
        p.append(f'<path d="M-26,-168 L-8,-160 M26,-168 L8,-160" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>')
    elif mood == "sorry":
        p.append(f'<path d="M-24,-162 L-8,-168 M24,-162 L8,-168" stroke="{ink}" stroke-width="3.5" stroke-linecap="round"/>')
    if eyes == "closed" or mood == "happy":
        p.append(f'<path d="M-24,-152 q8,-8 16,0 M8,-152 q8,-8 16,0" fill="none" stroke="{ink}" stroke-width="3.5" stroke-linecap="round"/>')
    else:
        p.append(f'<ellipse cx="-16" cy="-152" rx="6" ry="7.5" fill="{ink}"/><ellipse cx="16" cy="-152" rx="6" ry="7.5" fill="{ink}"/>'
                 f'<circle cx="-14" cy="-155" r="2" fill="#fff"/><circle cx="18" cy="-155" r="2" fill="#fff"/>')
    p.append(f'<path d="M-9,-138 Q0,-130 9,-138 Q0,-142 -9,-138 Z" fill="#5a2f1c"/>')
    m = mouth or {"roar": "roar", "angry": "frown", "sorry": "frown", "happy": "smile", "proud": "smirk"}[mood]
    if m == "roar":
        p.append(f'<path d="M-20,-126 Q0,-88 20,-126 Q0,-120 -20,-126 Z" fill="#6a1f1a"/>'
                 f'<path d="M-15,-124 l4,9 l4,-8 M15,-124 l-4,9 l-4,-8" fill="#fff"/>'
                 f'<ellipse cx="0" cy="-104" rx="8" ry="5" fill="#ff8d8d"/>')
    elif m == "frown":
        p.append(f'<path d="M-12,-118 Q0,-126 12,-118" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
    elif m == "smile":
        p.append(f'<path d="M-14,-124 Q0,-108 14,-124" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
    else:
        p.append(f'<path d="M-12,-122 Q0,-116 14,-126" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
    p.append(f'<path d="M-30,-128 l-18,-4 M-30,-122 l-18,2 M30,-128 l18,-4 M30,-122 l18,2" stroke="{ink}" stroke-width="1.5" opacity="0.5"/>')
    if crown:
        p.append('<path d="M-26,-196 L-26,-222 L-13,-208 L0,-228 L13,-208 L26,-222 L26,-196 Z" fill="#ffd23f" stroke="#d49a12" stroke-width="2"/>'
                 '<circle cx="0" cy="-206" r="4" fill="#ef5350"/>')
    if wet:
        p.append("".join(f'<path d="M{dx},{dy} q-5,8 0,11 q5,-3 0,-11 Z" fill="#7fb3ff"/>' for dx, dy in ((-50, -170), (52, -150), (-40, -110), (44, -96), (0, -88))))
    return g("".join(p), x, y, s)


def well(x, y, s=1, inside=None, roof=True):
    """An old stone well, base centre at (x, y). About 240*s wide.
    inside: svg drawn in the water opening, in well space centred on (0, -150)."""
    stone, dark, rim = "#9c8f84", "#7c6f65", "#b8aca1"
    p = [f'<rect x="-110" y="-150" width="220" height="150" fill="{stone}"/>']
    for row in range(5):
        off = 0 if row % 2 else 27
        for col in range(-5, 5):
            p.append(f'<rect x="{-110 + off + col*55 + 55}" y="{-148 + row*30}" width="51" height="26" rx="5" fill="{dark if (row+col) % 3 == 0 else stone}" stroke="{dark}" stroke-width="2"/>')
    p.append(f'<defs><clipPath id="wellclip"><rect x="-110" y="-160" width="220" height="160"/></clipPath></defs>')
    p = [f'<g clip-path="url(#wellclip)">' + "".join(p) + '</g>']
    p.append(f'<ellipse cx="0" cy="-150" rx="122" ry="34" fill="{rim}"/>')
    p.append(f'<ellipse cx="0" cy="-150" rx="100" ry="24" fill="#1c2a4a"/>')
    if inside:
        p.append(f'<defs><clipPath id="wellwater"><ellipse cx="0" cy="-150" rx="100" ry="24"/></clipPath></defs><g clip-path="url(#wellwater)">{inside}</g>')
    if roof:
        p.append('<path d="M-120,-150 V-290 M120,-150 V-290" stroke="#7a5236" stroke-width="12" stroke-linecap="round"/>'
             '<path d="M-130,-290 L0,-330 L130,-290 Z" fill="#a0522d"/>'
             '<path d="M-110,-270 H110" stroke="#7a5236" stroke-width="8"/>'
             '<path d="M0,-270 V-200" stroke="#c8b48a" stroke-width="3"/><rect x="-14" y="-200" width="28" height="22" rx="4" fill="#8a5a3c"/>')
    return g("".join(p), x, y, s)


def magic_book(x, y, s=1, glow=True, title="पंचतंत्र"):
    p = []
    if glow:
        p.append('<circle cx="0" cy="-40" r="120" fill="#ffe680" opacity="0.15"/><circle cx="0" cy="-40" r="70" fill="#ffe680" opacity="0.25"/>')
        p.append("".join(f'<path d="{star_path(dx, dy, r)}" fill="#ffe680"/>' for dx, dy, r in ((-70, -120, 9), (60, -140, 11), (0, -170, 8), (-100, -60, 6), (100, -80, 7))))
        p.append('<path d="M-40,-40 C-60,-90 -20,-120 -30,-160 M40,-40 C70,-80 30,-120 50,-170" fill="none" stroke="#ffe680" stroke-width="5" stroke-linecap="round" opacity="0.6"/>')
    p.append('<path d="M0,-30 C-30,-44 -70,-44 -100,-34 L-100,20 C-70,10 -30,10 0,24 Z" fill="#fff8e6" stroke="#c9b48a" stroke-width="2"/>'
             '<path d="M0,-30 C30,-44 70,-44 100,-34 L100,20 C70,10 30,10 0,24 Z" fill="#fff3d6" stroke="#c9b48a" stroke-width="2"/>'
             '<path d="M-100,20 C-70,10 -30,10 0,24 C30,10 70,10 100,20 L100,28 C70,18 30,18 0,32 C-30,18 -70,18 -100,28 Z" fill="#8b2c2c"/>')
    p.append('<path d="M-80,-20 h60 M-80,-8 h55 M-80,4 h60 M20,-20 h60 M25,-8 h55 M20,4 h50" stroke="#c9b48a" stroke-width="3" stroke-linecap="round"/>')
    if title:
        p.append(f'<text x="-50" y="-22" text-anchor="middle" font-family="Baloo 2, sans-serif" font-weight="800" font-size="18" fill="#8b2c2c">{title}</text>')
    return g("".join(p), x, y, s)


def jungle(time="dusk", gid="jg"):
    """A Panchatantra jungle: banana leaves, a rock, warm sky."""
    out = [sky(time, gid)]
    out.append({"dusk": '<circle cx="480" cy="150" r="55" fill="#ffb35c"/>', "day": '<circle cx="480" cy="120" r="50" fill="#ffe38a"/>'}.get(time, ""))
    out.append(tree(60, 470, 1.25, "#2f8a4c") + tree(560, 470, 1.15, "#3f9a55"))
    for bx, flip_ in ((120, 1), (500, -1)):
        out.append(f'<g transform="translate({bx} 470) scale({flip_} 1)"><path d="M0,0 C-10,-80 -30,-140 -80,-180 C-30,-170 10,-120 10,0 Z" fill="#4cbf6b"/>'
                   f'<path d="M0,0 C20,-90 60,-130 110,-150 C60,-120 30,-70 14,0 Z" fill="#3fa45e"/></g>')
    out.append('<rect y="460" width="600" height="140" fill="#6aa84f"/><path d="M0,470 Q300,440 600,470 V480 H0 Z" fill="#5a9a42"/>')
    return out


def rock(x, y, s=1):
    return g('<path d="M-120,0 C-120,-80 -60,-120 0,-120 C70,-120 120,-70 120,0 Z" fill="#8d8b9a"/>'
             '<path d="M-90,-20 C-80,-70 -40,-95 10,-95" fill="none" stroke="#a9a7b6" stroke-width="10" stroke-linecap="round"/>', x, y, s)


# ---------------------------------------------------------------- river, pond and field friends

def river(y=420, color="#3f8fd0", light="#7fc0ee"):
    """A wide river from the waterline y down to the bottom of the picture."""
    waves = "".join(f'<path d="M{x},{yy} q15,-6 30,0 q15,6 30,0" fill="none" stroke="{light}" stroke-width="3" '
                    f'stroke-linecap="round" opacity="0.7"/>' for x, yy in ((60, y + 50), (360, y + 40), (220, y + 100), (480, y + 120), (100, y + 150)))
    return (f'<rect y="{y}" width="{W}" height="{H - y}" fill="{color}"/>'
            f'<path d="M0,{y} Q75,{y - 8} 150,{y} T300,{y} T450,{y} T600,{y} V{y + 10} H0 Z" fill="{light}"/>' + waves)


def water_over(x1, x2, y, color="#3f8fd0", light="#7fc0ee"):
    """A strip of river water drawn in front of a swimmer, from y down to the bottom, between x1 and x2."""
    return (f'<path d="M{x1},{y} Q{(x1 + x2) / 2:.0f},{y - 10} {x2},{y} V600 H{x1} Z" fill="{color}"/>'
            f'<path d="M{x1 + 10},{y + 2} Q{(x1 + x2) / 2:.0f},{y - 8} {x2 - 10},{y + 2}" fill="none" stroke="{light}" stroke-width="5" stroke-linecap="round"/>')


def fruit_tree(x, y, s=1, color="#3f9a55", trunk="#7a5236", fruit="#5b2a86"):
    """A big jamun tree with purple fruit, trunk base at (x, y). About 300*s tall."""
    dots = ((-60, -230), (-20, -270), (30, -250), (70, -215), (-80, -180), (10, -200), (50, -170), (-40, -150), (90, -260), (-100, -230))
    inner = (f'<path d="M-18,0 C-16,-60 -14,-120 -10,-160 L10,-160 C14,-120 16,-60 18,0 Z" fill="{trunk}"/>'
             f'<circle cx="0" cy="-230" r="80" fill="{color}"/><circle cx="-80" cy="-190" r="60" fill="{color}"/>'
             f'<circle cx="80" cy="-195" r="62" fill="{color}"/>'
             + "".join(f'<circle cx="{dx}" cy="{dy}" r="8" fill="{fruit}"/><circle cx="{dx - 2}" cy="{dy - 3}" r="2.4" fill="#fff" opacity="0.5"/>' for dx, dy in dots))
    return g(inner, x, y, s)


def jamun(x, y, s=1, fruit="#5b2a86"):
    return g(f'<ellipse cx="0" cy="0" rx="8" ry="10" fill="{fruit}"/><circle cx="-2" cy="-4" r="2.6" fill="#fff" opacity="0.5"/>'
             f'<path d="M0,-10 l3,-6" stroke="#3f7a3a" stroke-width="2" stroke-linecap="round"/>', x, y, s)


def monkey(x, y, s=1, mood="happy", arms="down", eyes="open", flip=False):
    """Chiku the monkey, standing, feet at (x, y). About 170*s tall.
    mood: happy | scared | laugh;  arms: down | up | hold (right hand out, holding a jamun)."""
    fur, dark, face = "#8a5a36", "#6e4426", "#f3d3a8"
    ink = "#2a1b14"
    p = [f'<path d="M22,-34 C80,-30 80,-100 44,-100 C24,-100 26,-76 42,-78" fill="none" stroke="{fur}" stroke-width="9" stroke-linecap="round"/>',
         f'<path d="M-12,-40 Q-22,-20 -18,-6 M12,-40 Q22,-20 18,-6" stroke="{fur}" stroke-width="13" stroke-linecap="round" fill="none"/>',
         f'<ellipse cx="-22" cy="-4" rx="12" ry="6" fill="{face}"/><ellipse cx="22" cy="-4" rx="12" ry="6" fill="{face}"/>',
         f'<ellipse cx="0" cy="-58" rx="30" ry="34" fill="{fur}"/>',
         f'<ellipse cx="0" cy="-52" rx="18" ry="22" fill="{face}"/>']
    hands = {"down": ((-36, -40), (36, -40)), "up": ((-44, -132), (44, -132)), "hold": ((-36, -40), (54, -76))}[arms]
    for sx, (hx, hy) in zip((-1, 1), hands):
        p.append(f'<path d="M{sx*22},-80 Q{sx*34 + (hx - sx*22)*0.3:.0f},{(hy - 80)/2:.0f} {hx},{hy}" stroke="{fur}" stroke-width="11" stroke-linecap="round" fill="none"/>'
                 f'<circle cx="{hx}" cy="{hy}" r="7" fill="{face}"/>')
    if arms == "hold":
        p.append(jamun(hands[1][0] + 4, hands[1][1] - 10, 1.1))
    # head
    p.append(f'<circle cx="-38" cy="-122" r="14" fill="{fur}"/><circle cx="-38" cy="-122" r="8" fill="{face}"/>'
             f'<circle cx="38" cy="-122" r="14" fill="{fur}"/><circle cx="38" cy="-122" r="8" fill="{face}"/>'
             f'<circle cx="0" cy="-120" r="35" fill="{fur}"/>'
             f'<path d="M-6,-154 q4,-12 10,-4 q4,-10 10,0" fill="none" stroke="{fur}" stroke-width="5" stroke-linecap="round"/>'
             f'<circle cx="-12" cy="-124" r="14" fill="{face}"/><circle cx="12" cy="-124" r="14" fill="{face}"/>'
             f'<ellipse cx="0" cy="-104" rx="22" ry="16" fill="{face}"/>')
    for sx in (-1, 1):
        ex = sx * 12
        if eyes == "closed" or mood == "laugh":
            p.append(f'<path d="M{ex - 6},-124 Q{ex},-131 {ex + 6},-124" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
        elif mood == "scared":
            p.append(f'<circle cx="{ex}" cy="-125" r="7" fill="#fff"/><circle cx="{ex}" cy="-124" r="3" fill="{ink}"/>')
        else:
            p.append(f'<ellipse cx="{ex}" cy="-125" rx="4.5" ry="5.5" fill="{ink}"/><circle cx="{ex + 1.6}" cy="-127" r="1.6" fill="#fff"/>')
    if mood == "scared":
        p.append(f'<path d="M-20,-140 L-6,-136 M20,-140 L6,-136" stroke="{dark}" stroke-width="3" stroke-linecap="round"/>')
    p.append(f'<circle cx="-3" cy="-110" r="1.8" fill="{ink}"/><circle cx="3" cy="-110" r="1.8" fill="{ink}"/>')
    if mood == "scared":
        p.append(f'<ellipse cx="0" cy="-99" rx="5" ry="6" fill="#6a2a1a"/>')
    elif mood == "laugh":
        p.append(f'<path d="M-11,-103 Q0,-86 11,-103 Z" fill="#6a2a1a"/><ellipse cx="0" cy="-95" rx="5" ry="3" fill="#ff8d8d"/>')
    else:
        p.append(f'<path d="M-10,-102 Q0,-92 10,-102" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="-22" cy="-108" rx="5" ry="3.5" fill="#ff9a8a" opacity="0.6"/><ellipse cx="22" cy="-108" rx="5" ry="3.5" fill="#ff9a8a" opacity="0.6"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def crocodile(x, y, s=1, mood="sly", mouth="closed", rider=None, flip=False):
    """Magar the crocodile, facing right; (x, y) is the middle of his belly line (put the
    waterline here when he swims). About 330*s long.
    mood: sly | sorry | happy;  mouth: closed | open | smile.
    rider: svg drawn on his back (stand riders at about (-20, -40) in his space)."""
    skin, dark, belly = "#4f9a4a", "#3b7c3a", "#cde59a"
    ink = "#1f3a1c"
    p = [f'<path d="M-90,-26 C-140,-30 -170,-20 -205,-44 C-180,-4 -130,8 -90,6 Z" fill="{skin}"/>',
         f'<ellipse cx="-50" cy="8" rx="16" ry="10" fill="{dark}"/><ellipse cx="50" cy="8" rx="16" ry="10" fill="{dark}"/>',
         f'<ellipse cx="0" cy="-16" rx="104" ry="32" fill="{skin}"/>',
         f'<path d="M-92,-2 Q0,22 92,-2 Q0,10 -92,-2 Z" fill="{belly}"/>']
    for i in range(8):
        bx = -84 + i * 22
        by = -16 - 32 * math.sqrt(max(0, 1 - (bx / 104) ** 2))
        p.append(f'<path d="M{bx - 8},{by + 4:.1f} L{bx},{by - 8:.1f} L{bx + 8},{by + 4:.1f} Z" fill="{dark}"/>')
    for bx in (-150, -125):
        p.append(f'<path d="M{bx - 6},{-28 + (bx + 150) * 0.1:.1f} l6,-9 l6,9 Z" fill="{dark}"/>')
    if rider:
        p.append(rider)
    # head and snout
    p.append(f'<ellipse cx="110" cy="-22" rx="38" ry="26" fill="{skin}"/>')
    if mouth == "open":
        p.append(f'<g transform="rotate(-18 112 -20)"><rect x="112" y="-44" width="104" height="26" rx="13" fill="{skin}"/>'
                 + "".join(f'<path d="M{130 + i*14},-18 l5,8 l5,-8 Z" fill="#fff"/>' for i in range(6))
                 + f'<circle cx="204" cy="-38" r="2.5" fill="{ink}"/></g>'
                 f'<path d="M112,-14 L214,-6 Q220,8 206,10 L112,6 Z" fill="#c94a4a"/>'
                 f'<rect x="112" y="-2" width="104" height="18" rx="9" fill="{skin}"/>'
                 + "".join(f'<path d="M{132 + i*14},-2 l5,-8 l5,8 Z" fill="#fff"/>' for i in range(6)))
    else:
        p.append(f'<rect x="112" y="-38" width="104" height="30" rx="15" fill="{skin}"/>'
                 f'<path d="M120,-12 L210,-12" stroke="{ink}" stroke-width="2.5" stroke-linecap="round"/>'
                 + "".join(f'<path d="M{132 + i*15},-12 l5,7 l5,-7 Z" fill="#fff"/>' for i in range(5))
                 + f'<circle cx="204" cy="-30" r="2.5" fill="{ink}"/><circle cx="196" cy="-31" r="2.5" fill="{ink}"/>')
        if mouth == "smile":
            p.append(f'<path d="M180,-12 Q200,-12 212,-24" fill="none" stroke="{ink}" stroke-width="2.5" stroke-linecap="round"/>')
    # eye bump
    p.append(f'<circle cx="104" cy="-46" r="17" fill="{skin}"/><circle cx="105" cy="-48" r="11" fill="#fffbe6"/>')
    if mood == "happy":
        p.append(f'<path d="M97,-48 Q105,-56 113,-48" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
    else:
        p.append(f'<ellipse cx="107" cy="-47" rx="3.2" ry="7" fill="{ink}"/>')
    if mood == "sly":
        p.append(f'<path d="M93,-52 Q105,-62 117,-52 L117,-49 Q105,-57 93,-49 Z" fill="{dark}"/>')
    if mood == "sorry":
        p.append(f'<path d="M94,-62 L114,-58" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>'
                 f'<path d="M100,-34 q-5,9 0,12 q5,-3 0,-12 Z" fill="#7fb3ff"/>')
    p.append(f'<ellipse cx="136" cy="-18" rx="9" ry="5" fill="#ff9aa8" opacity="0.45"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def _hexes(cx, cy, rx, ry, color):
    out = []
    for hx, hy in ((0, 0), (-0.5, 0.25), (0.5, 0.25), (-0.28, -0.45), (0.28, -0.45)):
        px, py, r = cx + hx * rx, cy + hy * ry, min(rx, ry) * 0.24
        pts = " ".join(f"{px + r*math.cos(a*math.pi/3):.1f},{py + r*math.sin(a*math.pi/3):.1f}" for a in range(6))
        out.append(f'<polygon points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round"/>')
    return "".join(out)


def tortoise(x, y, s=1, mouth="closed", pose="walk", eyes="open", blush=False):
    """Plappi the tortoise, a chatterbox.
    pose="walk": side view facing right, feet at (x, y). About 160*s long.
    pose="hang": hanging from a stick by her mouth; (x, y) is where her mouth holds
    the stick (draw the stick after her). mouth: closed | open | talk."""
    shell, shell2, rim, skin, ink = "#7cb342", "#5d8f30", "#c9a64a", "#b9d68a", "#2a3a1a"
    p = []
    if pose == "hang":
        p.append(f'<path d="M-30,96 l-16,22 M30,96 l16,22 M-36,52 l-22,8 M36,52 l22,8" stroke="{skin}" stroke-width="15" stroke-linecap="round"/>')
        p.append(f'<path d="M0,110 l-6,14 l12,0 Z" fill="{skin}"/>')
        p.append(f'<rect x="-9" y="8" width="18" height="34" rx="8" fill="{skin}"/>')
        p.append(f'<ellipse cx="0" cy="76" rx="48" ry="44" fill="{shell}"/>' + _hexes(0, 76, 48, 44, shell2)
                 + f'<ellipse cx="0" cy="76" rx="48" ry="44" fill="none" stroke="{rim}" stroke-width="6"/>')
        p.append(f'<circle cx="0" cy="14" r="18" fill="{skin}"/>')
        for sx in (-1, 1):
            if eyes == "closed":
                p.append(f'<path d="M{sx*7 - 4},14 q4,4 8,0" fill="none" stroke="{ink}" stroke-width="2.2" stroke-linecap="round"/>')
            else:
                p.append(f'<circle cx="{sx*7}" cy="13" r="3.4" fill="{ink}"/><circle cx="{sx*7 + 1}" cy="12" r="1.1" fill="#fff"/>')
        if mouth == "open":
            p.append(f'<ellipse cx="0" cy="26" rx="7" ry="6" fill="#7a2a2a"/>')
        else:
            p.append(f'<path d="M-6,3 Q0,7 6,3" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>')
        if blush:
            p.append(f'<ellipse cx="-12" cy="20" rx="4" ry="2.6" fill="#ff8a8a" opacity="0.7"/><ellipse cx="12" cy="20" rx="4" ry="2.6" fill="#ff8a8a" opacity="0.7"/>')
        return g("".join(p), x, y, s)
    p.append(f'<path d="M-62,-14 l-16,6 l14,6 Z" fill="{skin}"/>')
    for lx in (-44, -20, 20, 44):
        p.append(f'<rect x="{lx - 9}" y="-26" width="18" height="26" rx="8" fill="{skin}"/>')
    p.append(f'<path d="M46,-30 C58,-44 66,-50 78,-50" fill="none" stroke="{skin}" stroke-width="18" stroke-linecap="round"/>')
    p.append(f'<circle cx="84" cy="-52" r="18" fill="{skin}"/>')
    if eyes == "closed":
        p.append(f'<path d="M84,-58 q5,4 10,0" fill="none" stroke="{ink}" stroke-width="2.2" stroke-linecap="round"/>')
    else:
        p.append(f'<circle cx="89" cy="-58" r="3.6" fill="{ink}"/><circle cx="90.4" cy="-59.4" r="1.2" fill="#fff"/>')
    if mouth in ("open", "talk"):
        p.append(f'<path d="M88,-44 Q96,-46 102,-50 Q98,-38 88,-40 Z" fill="#7a2a2a"/>')
    else:
        p.append(f'<path d="M88,-44 Q96,-44 101,-49" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="80" cy="-46" rx="4" ry="2.6" fill="#ff8a8a" opacity="{0.8 if blush else 0.4}"/>')
    p.append(f'<path d="M-64,-20 C-64,-96 64,-96 64,-20 Z" fill="{shell}"/>' + _hexes(0, -50, 56, 36, shell2)
             + f'<rect x="-68" y="-26" width="136" height="12" rx="6" fill="{rim}"/>')
    if mouth == "talk":
        p.append(''.join(f'<path d="M{110 + i*8},{-64 - i*6} q6,4 0,10" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>' for i in range(2)))
    return g("".join(p), x, y, s)


def goose(x, y, s=1, pose="fly", flip=False, eyes="open", feet=False):
    """A wild goose (Gisi or Gusti), facing right. (x, y) is the tip of her beak.
    pose: fly | stand (standing feet at about (-90, 80) from the beak).
    feet=True (flying): her feet hang down and grip at (-96, 62) from the beak, so two
    geese can carry the two ends of a stick between them."""
    white, grey, beak, ink = "#fbfaf6", "#d9d6cc", "#ff9a3d", "#2a2440"
    p = []
    if pose == "fly" and feet:
        p.append(f'<path d="M-100,44 L-98,60 M-90,44 L-94,60" stroke="{beak}" stroke-width="5" stroke-linecap="round"/>'
                 f'<path d="M-106,58 q10,10 20,0" fill="none" stroke="{beak}" stroke-width="5" stroke-linecap="round"/>')
    if pose == "fly":
        p.append(f'<path d="M-100,18 C-120,-30 -150,-60 -196,-70 C-168,-34 -146,-4 -116,24 Z" fill="{grey}"/>')
    else:
        p.append(f'<path d="M-96,44 v34 M-84,44 v34" stroke="{beak}" stroke-width="5" stroke-linecap="round"/>'
                 f'<path d="M-104,80 h14 M-92,80 h14" stroke="{beak}" stroke-width="6" stroke-linecap="round"/>')
    p.append(f'<path d="M-24,-2 C-40,4 -54,10 -66,24" fill="none" stroke="{white}" stroke-width="18" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="-96" cy="30" rx="44" ry="22" fill="{white}"/>'
             f'<path d="M-136,26 l-18,-6 l6,14 Z" fill="{white}"/>')
    if pose == "fly":
        p.append(f'<path d="M-70,24 C-80,-24 -100,-70 -150,-96 C-130,-50 -116,-6 -112,28 Z" fill="{white}" stroke="{grey}" stroke-width="2"/>')
    else:
        p.append(f'<path d="M-120,28 Q-96,6 -70,26 Q-96,44 -120,28 Z" fill="{grey}"/>')
    p.append(f'<circle cx="-24" cy="-6" r="15" fill="{white}"/>')
    p.append(f'<path d="M-12,-12 L0,0 L-12,4 Z" fill="{beak}"/>')
    if eyes == "closed":
        p.append(f'<path d="M-30,-10 q4,3 8,0" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>')
    else:
        p.append(f'<circle cx="-25" cy="-10" r="3" fill="{ink}"/><circle cx="-24" cy="-11" r="1" fill="#fff"/>')
    p.append(f'<ellipse cx="-30" cy="-1" rx="4" ry="2.4" fill="#ff9aa8" opacity="0.6"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def stick(x1, y1, x2, y2, w=8):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#8a5a2c" stroke-width="{w}" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y1 - w*0.2:.1f}" x2="{x2}" y2="{y2 - w*0.2:.1f}" stroke="#b07a42" stroke-width="{w*0.3:.1f}" stroke-linecap="round"/>')


def pond(x, y, rx=160, ry=40, dry=False):
    """A pond centred at (x, y). dry=True draws cracked, dried-up mud."""
    if dry:
        cracks = "".join(f'<path d="M{x + dx},{y + dy} l{a},{b} l{c},{d}" fill="none" stroke="#7a5a3a" stroke-width="3" stroke-linecap="round"/>'
                         for dx, dy, a, b, c, d in ((-90, -10, 20, 8, 14, -6), (-20, -20, 10, 14, 18, 4), (40, -6, 22, 10, 10, 12), (-60, 14, 16, -8, 20, 6), (90, 10, -14, -10, -10, 8)))
        return (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#b98a5a"/>'
                f'<ellipse cx="{x}" cy="{y + 2}" rx="{rx * 0.82:.0f}" ry="{ry * 0.7:.0f}" fill="#a87a4a"/>'
                f'<ellipse cx="{x + 20}" cy="{y + 4}" rx="{rx * 0.18:.0f}" ry="{ry * 0.16:.0f}" fill="#6fa0c8"/>' + cracks)
    return (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#3f8fd0"/>'
            f'<ellipse cx="{x - rx*0.2:.0f}" cy="{y - ry*0.25:.0f}" rx="{rx * 0.5:.0f}" ry="{ry * 0.25:.0f}" fill="#7fc0ee" opacity="0.6"/>'
            f'<ellipse cx="{x + rx*0.5:.0f}" cy="{y + ry*0.2:.0f}" rx="22" ry="8" fill="#4cbf6b"/>'
            f'<circle cx="{x + rx*0.5 + 6:.0f}" cy="{y + ry*0.2 - 6:.0f}" r="6" fill="#ff8fb1"/>')


def haystack(x, y, s=1):
    """A soft golden haystack, base centre at (x, y). About 200*s wide."""
    return g('<path d="M-100,0 C-100,-90 -50,-130 0,-130 C50,-130 100,-90 100,0 Z" fill="#f2c94c"/>'
             '<path d="M-70,-20 q10,-50 30,-80 M-30,-10 q4,-60 14,-100 M20,-10 q-2,-60 -6,-104 M60,-16 q-8,-50 -24,-86" fill="none" stroke="#d9a92a" stroke-width="5" stroke-linecap="round"/>'
             '<path d="M-100,0 l-10,-10 M-80,0 l-6,-16 M90,0 l12,-12 M100,0 l8,-6" stroke="#d9a92a" stroke-width="4" stroke-linecap="round"/>', x, y, s)


def mouse(x, y, s=1, mood="happy", flip=False, crown=False, eyes="open"):
    """A little mouse, facing right, feet at (x, y). About 110*s long (draw them big
    enough to see). mood: happy | sad | chew (teeth out).  crown=True for Chuchu, the mouse king."""
    fur, belly, pink, ink = "#a9a4b8", "#d8d4e2", "#ffb3c7", "#2a2440"
    p = [f'<path d="M-30,-14 C-60,-10 -64,-40 -86,-34" fill="none" stroke="{pink}" stroke-width="4" stroke-linecap="round"/>',
         f'<ellipse cx="-14" cy="-2" rx="9" ry="5" fill="{pink}"/><ellipse cx="14" cy="-2" rx="9" ry="5" fill="{pink}"/>',
         f'<ellipse cx="-2" cy="-24" rx="34" ry="24" fill="{fur}"/><ellipse cx="2" cy="-18" rx="20" ry="13" fill="{belly}"/>',
         f'<circle cx="16" cy="-62" r="16" fill="{fur}"/><circle cx="16" cy="-62" r="9" fill="{pink}"/>',
         f'<path d="M14,-50 C30,-58 46,-46 56,-38 C44,-28 26,-24 14,-28 Z" fill="{fur}"/>',
         f'<circle cx="26" cy="-40" r="20" fill="{fur}"/>',
         f'<circle cx="57" cy="-38" r="4.5" fill="#ff7fa0"/>',
         f'<path d="M48,-34 l16,-4 M48,-32 l16,4 M46,-30 l12,8" stroke="{ink}" stroke-width="1.2" opacity="0.6"/>']
    if eyes == "closed" or mood == "happy" and eyes == "happy":
        p.append(f'<path d="M30,-46 q4,-4 8,0" fill="none" stroke="{ink}" stroke-width="2.2" stroke-linecap="round"/>')
    else:
        p.append(f'<circle cx="34" cy="-46" r="4" fill="{ink}"/><circle cx="35.4" cy="-47.4" r="1.4" fill="#fff"/>')
    if mood == "sad":
        p.append(f'<path d="M28,-54 l10,3" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>'
                 f'<path d="M36,-38 q-4,7 0,9 q4,-2 0,-9 Z" fill="#7fb3ff"/>'
                 f'<path d="M40,-28 Q46,-31 50,-28" fill="none" stroke="{ink}" stroke-width="1.8" stroke-linecap="round"/>')
    elif mood == "chew":
        p.append(f'<rect x="46" y="-31" width="5" height="8" rx="1.5" fill="#fff" stroke="{ink}" stroke-width="0.8"/>'
                 f'<rect x="51" y="-31" width="5" height="8" rx="1.5" fill="#fff" stroke="{ink}" stroke-width="0.8"/>')
    else:
        p.append(f'<path d="M40,-30 Q46,-25 52,-30" fill="none" stroke="{ink}" stroke-width="1.8" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="30" cy="-34" rx="4" ry="2.6" fill="#ff8a8a" opacity="0.6"/>')
    p.append(f'<path d="M4,-26 q8,10 18,8" fill="none" stroke="{fur}" stroke-width="7" stroke-linecap="round"/>')
    if crown:
        p.append('<path d="M14,-58 L14,-72 L21,-65 L28,-76 L35,-65 L42,-72 L42,-58 Z" fill="#ffd23f" stroke="#d49a12" stroke-width="1.5"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def net(x, y, w, h, pid="net", torn=False, color="#c8a46a"):
    """A hunter's rope net thrown over something: a dome, base centre at (x, y),
    w wide and h tall. torn=True cuts holes in it (the mice have been chewing)."""
    pat = (f'<defs><pattern id="{pid}" width="26" height="26" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           f'<path d="M0,0 H26 M0,0 V26" stroke="{color}" stroke-width="4" fill="none"/></pattern></defs>')
    dome = f'M{x - w/2},{y} C{x - w/2},{y - h*1.3:.0f} {x + w/2},{y - h*1.3:.0f} {x + w/2},{y} Z'
    holes = ""
    if torn:
        holes = "".join(f' M{x + dx - r},{y + dy} a{r},{r*0.8:.0f} 0 1,0 {2*r},0 a{r},{r*0.8:.0f} 0 1,0 {-2*r},0 Z'
                        for dx, dy, r in ((-w*0.2, -h*0.5, 34), (w*0.22, -h*0.35, 30), (0, -h*0.8, 26)))
    knots = "".join(f'<circle cx="{x - w/2 + i * w/8:.0f}" cy="{y}" r="5" fill="{color}"/>' for i in range(9))
    return (pat + f'<path d="{dome}{holes}" fill="url(#{pid})" fill-rule="evenodd"/>'
            f'<path d="{dome}" fill="none" stroke="{color}" stroke-width="6"/>' + knots)


def rope_heap(x, y, s=1, color="#c8a46a"):
    """Bits of chewed-up net lying on the ground, centred at (x, y)."""
    return g("".join(f'<path d="M{dx},0 q14,-18 28,-4 q10,10 22,-8" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round"/>' for dx in (-90, -40, 10, 50))
             + '<path d="M-70,-10 l12,-14 M30,-16 l10,10" stroke="#c8a46a" stroke-width="5" stroke-linecap="round"/>', x, y, s)


# ---------------------------------------------------------------- more Panchatantra friends

def jackal(x, y, s=1, fur="#c98a4b", mood="happy", crown=False, flip=False, drips=False):
    """Neelu the jackal, sitting and facing right-ish, feet at (x, y). About 190*s tall.
    fur: "#c98a4b" (his own colour) or "#3a4fc8" (dyed blue). mood: happy | proud | scared | sorry."""
    light = "#f3dcb8" if fur == "#c98a4b" else "#8fa0ef"
    ink = "#2a1b14"
    p = [f'<path d="M-30,-20 C-80,-20 -90,-60 -70,-80 C-66,-50 -50,-36 -26,-36 Z" fill="{fur}"/>'
         f'<path d="M-74,-74 C-70,-60 -66,-56 -58,-52" stroke="{light}" stroke-width="8" stroke-linecap="round" fill="none"/>',
         f'<ellipse cx="0" cy="-50" rx="34" ry="46" fill="{fur}"/><ellipse cx="10" cy="-46" rx="16" ry="30" fill="{light}"/>',
         f'<rect x="-14" y="-40" width="12" height="40" rx="6" fill="{fur}"/><rect x="14" y="-40" width="12" height="40" rx="6" fill="{fur}"/>',
         f'<ellipse cx="-6" cy="-2" rx="11" ry="5" fill="{fur}"/><ellipse cx="22" cy="-2" rx="11" ry="5" fill="{fur}"/>',
         # head
         f'<path d="M-14,-150 L-6,-196 L12,-160 Z" fill="{fur}"/><path d="M-8,-156 L-5,-182 L6,-160 Z" fill="{light}"/>',
         f'<path d="M14,-152 L30,-194 L38,-150 Z" fill="{fur}"/><path d="M20,-154 L29,-180 L33,-154 Z" fill="{light}"/>',
         f'<ellipse cx="12" cy="-124" rx="34" ry="30" fill="{fur}"/>',
         f'<path d="M30,-132 C50,-128 66,-118 70,-110 C60,-100 40,-100 26,-104 Z" fill="{fur}"/>',
         f'<path d="M28,-110 C44,-104 58,-104 68,-108 C60,-96 40,-94 26,-100 Z" fill="{light}"/>',
         f'<circle cx="70" cy="-112" r="5" fill="{ink}"/>',
         f'<ellipse cx="0" cy="-110" rx="16" ry="12" fill="{light}"/>']
    if mood == "scared":
        p.append(f'<circle cx="22" cy="-132" r="6" fill="#fff"/><circle cx="23" cy="-131" r="2.6" fill="{ink}"/>'
                 f'<ellipse cx="52" cy="-100" rx="4" ry="4" fill="#6a2a1a"/>')
    elif mood in ("happy", "proud"):
        if mood == "proud":
            p.append(f'<path d="M15,-134 Q22,-138 29,-134" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
        else:
            p.append(f'<ellipse cx="22" cy="-133" rx="4" ry="5" fill="{ink}"/><circle cx="23.5" cy="-135" r="1.4" fill="#fff"/>')
        p.append(f'<path d="M40,-102 Q52,-96 62,-104" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    else:  # sorry
        p.append(f'<path d="M16,-132 q6,5 12,0" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>'
                 f'<path d="M14,-144 L28,-140" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>'
                 f'<path d="M44,-100 Q52,-104 60,-100" fill="none" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="10" cy="-116" rx="5" ry="3" fill="#ff8a8a" opacity="0.5"/>')
    if crown:
        p.append('<path d="M-6,-150 L-6,-174 L5,-162 L14,-180 L23,-162 L34,-174 L34,-150 Z" fill="#ffd23f" stroke="#d49a12" stroke-width="2"/>')
    if drips:
        p.append("".join(f'<path d="M{dx},{dy} q-5,8 0,11 q5,-3 0,-11 Z" fill="#6f84ff"/>' for dx, dy in ((-30, -70), (36, -60), (-10, -20), (60, -90), (0, -170))))
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def dye_vat(x, y, s=1, color="#3a4fc8", splash=False):
    """A big clay tub of indigo dye, base centre at (x, y). About 200*s wide."""
    p = [f'<path d="M-90,-110 L90,-110 L76,0 L-76,0 Z" fill="#b8643a"/>',
         f'<path d="M-80,-70 H80 M-78,-40 H78" stroke="#9a4f2c" stroke-width="4"/>',
         f'<ellipse cx="0" cy="-110" rx="96" ry="20" fill="#d07a4a"/><ellipse cx="0" cy="-110" rx="80" ry="13" fill="{color}"/>']
    if splash:
        p.append("".join(f'<path d="M{dx},{dy} q-8,14 0,18 q8,-4 0,-18 Z" fill="{color}"/>' for dx, dy in ((-60, -150), (-20, -180), (30, -175), (70, -145), (0, -200))))
    return g("".join(p), x, y, s)


def crow(x, y, s=1, flip=False, holding=None, wings="down", mood="happy"):
    """Kalu the crow, facing right, feet at (x, y). About 110*s tall.
    holding: svg drawn at the beak tip (about (58, -78)). wings: down | up."""
    body, dark, beak, ink = "#3b3f52", "#272a38", "#f2b13a", "#ffffff"
    p = [f'<path d="M-34,-40 L-66,-30 L-60,-46 Z" fill="{dark}"/>',
         f'<path d="M-4,-6 v6 M8,-6 v6" stroke="{beak}" stroke-width="4" stroke-linecap="round"/>',
         f'<path d="M-10,0 h10 M2,0 h12" stroke="{beak}" stroke-width="4" stroke-linecap="round"/>',
         f'<ellipse cx="0" cy="-38" rx="38" ry="30" fill="{body}"/>',
         f'<circle cx="26" cy="-72" r="24" fill="{body}"/>',
         f'<path d="M44,-80 L64,-74 L44,-66 Z" fill="{beak}"/>']
    if wings == "up":
        p.append(f'<path d="M-6,-50 C-30,-110 -70,-110 -90,-96 C-60,-80 -40,-60 -14,-30 Z" fill="{dark}"/>')
    else:
        p.append(f'<path d="M-30,-48 C-10,-60 20,-50 22,-30 C0,-20 -24,-24 -30,-48 Z" fill="{dark}"/>')
    if mood == "sad":
        p.append(f'<circle cx="32" cy="-78" r="7" fill="{ink}"/><circle cx="33" cy="-76" r="3.4" fill="#111"/>'
                 f'<path d="M24,-90 L38,-86" stroke="#111" stroke-width="2.4" stroke-linecap="round"/>'
                 f'<path d="M30,-66 q-4,8 0,10 q4,-2 0,-10 Z" fill="#7fb3ff"/>')
    else:
        p.append(f'<circle cx="32" cy="-78" r="7" fill="{ink}"/><circle cx="34" cy="-78" r="3.4" fill="#111"/><circle cx="35" cy="-80" r="1.2" fill="#fff"/>')
    p.append(f'<ellipse cx="30" cy="-62" rx="5" ry="3" fill="#ff8fb1" opacity="0.6"/>')
    if holding:
        p.append(g(holding, 60, -74))
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def snake(x, y, s=1, mood="sly", flip=False):
    """Sarpu the snake, coiled, base at (x, y), head up and facing right. About 140*s tall.
    mood: sly | scared | sorry."""
    skin, belly, spot, ink = "#5aa84a", "#d6e99a", "#3f8a36", "#1f3a1c"
    p = [f'<ellipse cx="0" cy="-14" rx="70" ry="18" fill="{skin}"/>',
         f'<ellipse cx="0" cy="-40" rx="54" ry="16" fill="{skin}"/><ellipse cx="0" cy="-40" rx="54" ry="6" fill="{belly}" opacity="0.5"/>',
         f'<path d="M30,-44 C50,-70 40,-100 30,-112" fill="none" stroke="{skin}" stroke-width="26" stroke-linecap="round"/>',
         f'<ellipse cx="34" cy="-124" rx="26" ry="20" fill="{skin}"/>',
         f'<path d="M-70,-14 q-20,-4 -24,-14" fill="none" stroke="{skin}" stroke-width="10" stroke-linecap="round"/>']
    p += [f'<circle cx="{dx}" cy="{dy}" r="5" fill="{spot}"/>' for dx, dy in ((-40, -14), (0, -10), (40, -16), (-24, -40), (16, -42), (40, -80))]
    if mood == "scared":
        p.append(f'<circle cx="40" cy="-130" r="6.5" fill="#fff"/><circle cx="41" cy="-129" r="2.6" fill="{ink}"/>'
                 f'<ellipse cx="54" cy="-114" rx="4" ry="5" fill="#7a2a2a"/>')
    elif mood == "sorry":
        p.append(f'<path d="M34,-130 q6,5 12,0" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>'
                 f'<path d="M48,-114 q6,-4 10,0" fill="none" stroke="{ink}" stroke-width="2.2" stroke-linecap="round"/>')
    else:
        p.append(f'<ellipse cx="42" cy="-130" rx="5" ry="6" fill="#fff8c4"/><ellipse cx="43" cy="-130" rx="1.8" ry="5" fill="{ink}"/>'
                 f'<path d="M35,-138 Q42,-142 50,-136" stroke="{spot}" stroke-width="5" stroke-linecap="round" fill="none"/>'
                 f'<path d="M46,-114 Q54,-110 60,-118" fill="none" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>'
                 f'<path d="M60,-118 l10,2 m-10,-2 l8,6" stroke="#e5484d" stroke-width="2" stroke-linecap="round"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def necklace(x, y, s=1):
    """A sparkly pearl necklace with a red jewel, hanging from (x, y)."""
    pearls = "".join(f'<circle cx="{28*math.sin(a):.1f}" cy="{30 - 30*math.cos(a):.1f}" r="4.5" fill="#fffdf2" stroke="#d8cfae" stroke-width="1"/>'
                     for a in [i * math.pi / 7 - math.pi / 2 for i in range(8)])
    return g(pearls + '<path d="M0,54 l-9,10 l9,12 l9,-12 Z" fill="#e5484d"/><path d="M-12,40 l-6,-4 M12,40 l6,-4 M0,82 v6" stroke="#ffe680" stroke-width="2" stroke-linecap="round"/>', x, y, s)


def heron(x, y, s=1, mood="sly", flip=False, eyes="open", holding=None):
    """Bagla the heron, a tall white bird standing on one leg, facing right, foot at (x, y).
    About 260*s tall. mood: sly | sorry | happy.  holding: svg drawn at the beak tip."""
    white, grey, beak, leg, ink = "#fbfaf6", "#cfd4dc", "#f2b13a", "#e0912a", "#2a2440"
    p = [f'<path d="M0,0 V-90 M0,-60 L-16,-76 L-6,-90" fill="none" stroke="{leg}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
         f'<path d="M-6,0 h16" stroke="{leg}" stroke-width="5" stroke-linecap="round"/>',
         f'<ellipse cx="-10" cy="-120" rx="48" ry="32" fill="{white}"/>',
         f'<path d="M-50,-126 C-70,-120 -80,-108 -84,-96 C-66,-102 -50,-104 -40,-110 Z" fill="{grey}"/>',
         f'<path d="M-40,-126 C-10,-140 20,-132 30,-112 C0,-104 -24,-108 -40,-126 Z" fill="{grey}"/>',
         f'<path d="M24,-136 C34,-170 14,-190 22,-214" fill="none" stroke="{white}" stroke-width="16" stroke-linecap="round"/>',
         f'<circle cx="28" cy="-222" r="18" fill="{white}"/>',
         f'<path d="M14,-232 C4,-240 -8,-238 -16,-242" stroke="{grey}" stroke-width="4" stroke-linecap="round" fill="none"/>',
         f'<path d="M42,-228 L96,-218 L42,-212 Z" fill="{beak}"/>']
    if eyes == "closed" or mood == "happy":
        p.append(f'<path d="M26,-226 q5,-5 10,0" fill="none" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>')
    else:
        p.append(f'<circle cx="32" cy="-226" r="4" fill="{ink}"/><circle cx="33.4" cy="-227.4" r="1.3" fill="#fff"/>')
    if mood == "sly":
        p.append(f'<path d="M24,-234 L40,-230" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    elif mood == "sorry":
        p.append(f'<path d="M24,-230 L38,-236" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>'
                 f'<path d="M28,-212 q-4,8 0,10 q4,-2 0,-10 Z" fill="#7fb3ff"/>')
    p.append(f'<ellipse cx="22" cy="-216" rx="5" ry="3" fill="#ff9aa8" opacity="0.5"/>')
    if holding:
        p.append(g(holding, 96, -218))
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def crab(x, y, s=1, mood="happy", claws="down", flip=False):
    """Kekdu the crab, facing us, feet at (x, y). About 150*s wide. claws: down | up | pinch."""
    shell, dark, ink = "#ef6a4a", "#c94a30", "#2a1b14"
    p = [''.join(f'<path d="M{sx*30},-20 l{sx*26},{-6 + i*10} l{sx*8},{14}" fill="none" stroke="{dark}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
                 for sx in (-1, 1) for i in range(3))]
    cl = {"down": ((-62, -40), (62, -40)), "up": ((-56, -100), (56, -100)), "pinch": ((-62, -40), (40, -110))}[claws]
    for sx, (cx, cy) in zip((-1, 1), cl):
        p.append(f'<path d="M{sx*34},-34 Q{(sx*34 + cx)/2 + sx*10:.0f},{(cy - 34)/2 - 10:.0f} {cx},{cy + 10}" fill="none" stroke="{shell}" stroke-width="9" stroke-linecap="round"/>'
                 f'<path d="M{cx - 14},{cy + 8} C{cx - 20},{cy - 16} {cx + 20},{cy - 16} {cx + 14},{cy + 8} L{cx},{cy - 2} Z" fill="{shell}"/>')
    p.append(f'<ellipse cx="0" cy="-30" rx="46" ry="30" fill="{shell}"/><ellipse cx="0" cy="-22" rx="30" ry="12" fill="#ff9a7a" opacity="0.6"/>')
    p.append(f'<path d="M-12,-56 v-16 M12,-56 v-16" stroke="{shell}" stroke-width="5"/>')
    p.append(f'<circle cx="-12" cy="-76" r="9" fill="#fff"/><circle cx="12" cy="-76" r="9" fill="#fff"/>'
             f'<circle cx="-11" cy="-75" r="4" fill="{ink}"/><circle cx="13" cy="-75" r="4" fill="{ink}"/>')
    if mood == "angry":
        p.append(f'<path d="M-22,-88 L-4,-82 M22,-88 L4,-82" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>'
                 f'<path d="M-10,-24 Q0,-30 10,-24" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    else:
        p.append(f'<path d="M-12,-30 Q0,-18 12,-30" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    p.append('<ellipse cx="-26" cy="-32" rx="6" ry="3.5" fill="#ffc4b0" opacity="0.7"/><ellipse cx="26" cy="-32" rx="6" ry="3.5" fill="#ffc4b0" opacity="0.7"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def fish(x, y, s=1, color="#ff9a3d", mood="happy", flip=False):
    """A little fish facing right, centred at (x, y). About 70*s long. mood: happy | scared."""
    ink = "#2a2440"
    p = [f'<path d="M-24,0 L-44,-16 L-40,0 L-44,16 Z" fill="{color}"/>',
         f'<ellipse cx="0" cy="0" rx="28" ry="18" fill="{color}"/>',
         f'<path d="M-6,-16 Q4,-28 14,-14" fill="{color}"/>',
         f'<path d="M-4,-14 Q-10,0 -4,14" fill="none" stroke="#ffffff" stroke-width="2.4" opacity="0.6"/>']
    if mood == "scared":
        p.append(f'<circle cx="12" cy="-4" r="6" fill="#fff"/><circle cx="13" cy="-4" r="2.4" fill="{ink}"/><ellipse cx="24" cy="6" rx="3" ry="3.5" fill="{ink}"/>')
    else:
        p.append(f'<circle cx="12" cy="-4" r="4" fill="{ink}"/><circle cx="13.4" cy="-5.4" r="1.3" fill="#fff"/>'
                 f'<path d="M18,6 Q22,9 26,5" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


# ---------------------------------------------------------------- small friends of the lake and the forest (2026-11-28)

def sparrow(x, y, s=1, flip=False, wings="down", mood="happy"):
    """Chiri the sparrow, a little brown bird facing right, feet at (x, y). About 80*s tall.
    wings: down | up.  mood: happy | sad | cross."""
    body, belly, cap, wing, beak, ink = "#b07a4a", "#f2dcc0", "#7a4a2a", "#8a5a34", "#4a3a2a", "#2a1b14"
    p = [f'<path d="M-26,-30 L-54,-40 L-50,-24 Z" fill="{wing}"/>',
         f'<path d="M-4,-6 v6 M6,-6 v6" stroke="{beak}" stroke-width="3" stroke-linecap="round"/>',
         f'<ellipse cx="0" cy="-28" rx="28" ry="22" fill="{body}"/><ellipse cx="6" cy="-22" rx="18" ry="14" fill="{belly}"/>',
         f'<circle cx="20" cy="-54" r="18" fill="{body}"/>',
         f'<path d="M4,-62 C10,-76 30,-76 36,-62 C26,-66 14,-66 4,-62 Z" fill="{cap}"/>',
         f'<ellipse cx="24" cy="-46" rx="10" ry="6" fill="{belly}"/>',
         f'<path d="M36,-58 L48,-53 L36,-48 Z" fill="{beak}"/>']
    if wings == "up":
        p.append(f'<path d="M-6,-38 C-20,-80 -50,-86 -64,-74 C-44,-62 -30,-48 -12,-24 Z" fill="{wing}"/>')
    else:
        p.append(f'<path d="M-24,-34 C-8,-44 14,-38 14,-22 C-2,-14 -20,-18 -24,-34 Z" fill="{wing}"/>')
    p.append(f'<circle cx="25" cy="-58" r="3.4" fill="{ink}"/><circle cx="26" cy="-59" r="1.1" fill="#fff"/>')
    if mood == "sad":
        p.append(f'<path d="M19,-66 L30,-63" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>'
                 f'<path d="M25,-50 q-3,6 0,8 q3,-2 0,-8 Z" fill="#7fb3ff"/>')
    elif mood == "cross":
        p.append(f'<path d="M18,-63 L31,-66" stroke="{ink}" stroke-width="2.4" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="18" cy="-48" rx="4" ry="2.4" fill="#ff8fb1" opacity="0.6"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def woodpecker(x, y, s=1, flip=False, pecking=False):
    """Tok-Tok the woodpecker, clinging to a tree trunk on its left, facing right; feet at (x, y).
    About 120*s tall. pecking=True leans the head forward with little 'tok' lines."""
    body, belly, red, beak, ink = "#2f3142", "#f4f1ea", "#e5484d", "#9a9aa8", "#2a1b14"
    lean = 12 if pecking else 0
    p = [f'<path d="M-10,0 L-22,24 L-2,8 Z" fill="{body}"/>',
         f'<ellipse cx="0" cy="-40" rx="20" ry="38" fill="{body}"/><ellipse cx="8" cy="-36" rx="10" ry="26" fill="{belly}"/>',
         f'<path d="M-14,-56 l6,4 M-14,-44 l6,4 M-14,-32 l6,4" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>',
         f'<path d="M-2,0 l-6,6 M4,0 l-2,8" stroke="{beak}" stroke-width="3" stroke-linecap="round"/>',
         f'<g transform="rotate({lean} 0 -76)"><circle cx="6" cy="-84" r="16" fill="{body}"/>'
         f'<path d="M-8,-92 C-6,-110 14,-112 20,-96 C10,-100 0,-98 -8,-92 Z" fill="{red}"/>'
         f'<ellipse cx="10" cy="-80" rx="8" ry="5" fill="{belly}"/>'
         f'<path d="M20,-88 L46,-84 L20,-80 Z" fill="{beak}"/>'
         f'<circle cx="12" cy="-88" r="3.2" fill="#ffffff"/><circle cx="13" cy="-88" r="1.8" fill="{ink}"/></g>']
    if pecking:
        p.append(''.join(f'<path d="M{52 + i*6},{-96 + i*12} l10,-4" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>' for i in range(3)))
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def frog(x, y, s=1, mood="happy", croak=False):
    """Dadu the frog, sitting and facing us, feet at (x, y). About 110*s wide.
    croak=True puffs up his throat."""
    skin, dark, belly, ink = "#5cb85c", "#3f9a45", "#d7f0a8", "#1f3a1a"
    p = [f'<ellipse cx="-36" cy="-8" rx="24" ry="12" fill="{dark}"/><ellipse cx="36" cy="-8" rx="24" ry="12" fill="{dark}"/>',
         f'<path d="M-54,0 l-10,0 M-50,0 l-6,6 M54,0 l10,0 M50,0 l6,6" stroke="{dark}" stroke-width="5" stroke-linecap="round"/>',
         f'<ellipse cx="0" cy="-30" rx="44" ry="30" fill="{skin}"/><ellipse cx="0" cy="-20" rx="28" ry="18" fill="{belly}"/>',
         f'<path d="M-16,-6 l-8,6 M16,-6 l8,6" stroke="{skin}" stroke-width="8" stroke-linecap="round"/>',
         f'<circle cx="-20" cy="-58" r="14" fill="{skin}"/><circle cx="20" cy="-58" r="14" fill="{skin}"/>',
         f'<circle cx="-20" cy="-60" r="8" fill="#ffffff"/><circle cx="20" cy="-60" r="8" fill="#ffffff"/>',
         f'<circle cx="-19" cy="-60" r="4.2" fill="{ink}"/><circle cx="21" cy="-60" r="4.2" fill="{ink}"/>',
         f'<circle cx="-18" cy="-62" r="1.4" fill="#fff"/><circle cx="22" cy="-62" r="1.4" fill="#fff"/>']
    if croak:
        p.append(f'<ellipse cx="0" cy="-26" rx="20" ry="16" fill="#ffe680" opacity="0.9"/>'
                 f'<ellipse cx="0" cy="-42" rx="10" ry="6" fill="#7a2a2a"/>')
    elif mood == "sad":
        p.append(f'<path d="M-12,-36 Q0,-44 12,-36" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    else:
        p.append(f'<path d="M-18,-42 Q0,-28 18,-42" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
    p.append(f'<ellipse cx="-30" cy="-38" rx="6" ry="3.5" fill="#ff8fb1" opacity="0.6"/><ellipse cx="30" cy="-38" rx="6" ry="3.5" fill="#ff8fb1" opacity="0.6"/>')
    return g("".join(p), x, y, s)


def bee(x, y, s=1, flip=False):
    """Bunbun the bee, centred at (x, y), facing right. About 50*s long."""
    ink = "#2a2440"
    inner = (f'<ellipse cx="-6" cy="-16" rx="12" ry="9" fill="#ffffff" opacity="0.8" transform="rotate(-25 -6 -16)"/>'
             f'<ellipse cx="6" cy="-18" rx="12" ry="9" fill="#ffffff" opacity="0.8" transform="rotate(20 6 -18)"/>'
             f'<ellipse cx="0" cy="0" rx="20" ry="14" fill="#ffd23f"/>'
             f'<path d="M-8,-13 v26 M4,-14 v28" stroke="{ink}" stroke-width="5"/>'
             f'<path d="M-20,0 l-8,0" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>'
             f'<circle cx="15" cy="-3" r="2.6" fill="{ink}"/><path d="M12,4 q4,3 7,0" fill="none" stroke="{ink}" stroke-width="1.6" stroke-linecap="round"/>'
             f'<path d="M14,-12 q4,-10 10,-10 M10,-13 q0,-10 4,-14" fill="none" stroke="{ink}" stroke-width="1.6" stroke-linecap="round"/>')
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def nest(x, y, s=1, eggs=3, egg="#cfe8ff"):
    """A twiggy nest, base centre at (x, y), with `eggs` speckled eggs peeping out. About 110*s wide."""
    eg = "".join(f'<ellipse cx="{(i - (eggs - 1) / 2) * 22:.0f}" cy="-26" rx="11" ry="14" fill="{egg}" stroke="#a9c4dc" stroke-width="1.2"/>'
                 f'<circle cx="{(i - (eggs - 1) / 2) * 22 - 3:.0f}" cy="-30" r="1.6" fill="#8aa6c0"/>' for i in range(eggs))
    twigs = "".join(f'<path d="M{a},{b} q30,{c} 60,0" fill="none" stroke="#7a5236" stroke-width="3" stroke-linecap="round"/>'
                    for a, b, c in ((-56, -16, 8), (-30, -8, 6), (-10, -18, 8), (-50, -4, 6)))
    return g(eg + '<path d="M-56,-20 Q-50,6 0,6 Q50,6 56,-20 Q0,-6 -56,-20 Z" fill="#a8774a"/>' + twigs, x, y, s)


def mud_pit(x, y, rx=150, ry=36):
    """A gloopy mud hole centred at (x, y), with bubbles."""
    bubbles = "".join(f'<circle cx="{x + dx}" cy="{y + dy}" r="{r}" fill="none" stroke="#a07a52" stroke-width="2.5"/>'
                      for dx, dy, r in ((-rx*0.5, -4, 7), (rx*0.2, 6, 5), (rx*0.6, -8, 6), (-rx*0.1, -12, 4)))
    return (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#7a5236"/>'
            f'<ellipse cx="{x - rx*0.15:.0f}" cy="{y - ry*0.2:.0f}" rx="{rx*0.6:.0f}" ry="{ry*0.4:.0f}" fill="#8f6640"/>' + bubbles)


def moon_in_water(x, y, r=40, wobble=False):
    """The moon's reflection floating in a lake, centred at (x, y).
    wobble=True breaks it into shaky strips, as when the water is stirred."""
    if not wobble:
        return (f'<ellipse cx="{x}" cy="{y}" rx="{r * 1.4:.0f}" ry="{r * 0.6:.0f}" fill="#fff3c4" opacity="0.25"/>'
                f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * 0.42:.0f}" fill="#ffe9a8"/>'
                f'<path d="M{x - r*0.7:.0f},{y + r*0.12:.0f} q{r*0.35:.0f},-6 {r*0.7:.0f},0" fill="none" stroke="#f5d27a" stroke-width="3" stroke-linecap="round"/>')
    out = []
    for i, (dx, w) in enumerate(((-18, 0.9), (14, 1.0), (-10, 0.8), (20, 0.7), (-4, 0.55))):
        out.append(f'<rect x="{x + dx - r*w:.0f}" y="{y - r*0.45 + i*r*0.2:.0f}" width="{2*r*w:.0f}" height="{r*0.12:.0f}" rx="{r*0.06:.0f}" fill="#ffe9a8" opacity="{0.95 - i*0.12:.2f}"/>')
    out.append("".join(f'<ellipse cx="{x}" cy="{y}" rx="{r*k:.0f}" ry="{r*k*0.3:.0f}" fill="none" stroke="#bfe0ff" stroke-width="2.5" opacity="{0.8 - k*0.2:.2f}"/>' for k in (1.4, 2.0, 2.6)))
    return "".join(out)


def deer(x, y, s=1, pose="stand", eyes="open", mood="happy", flip=False):
    """Chitru the spotted deer, facing right, feet at (x, y). About 210*s tall standing.
    pose: stand | lie (lying flat on her side, 'playing dead': use eyes="closed")."""
    fur, dark, belly, spot, ink = "#d9944e", "#b9773a", "#f7e2c4", "#fff6e6", "#2a1b14"
    p = []
    if pose == "lie":
        p.append(f'<path d="M-40,-8 l-30,8 M-20,-6 l-26,14 M40,-8 l34,6 M56,-10 l30,12" stroke="{dark}" stroke-width="9" stroke-linecap="round"/>')
        p.append(f'<ellipse cx="0" cy="-30" rx="80" ry="34" fill="{fur}"/><ellipse cx="0" cy="-16" rx="60" ry="14" fill="{belly}"/>')
        p.append("".join(f'<circle cx="{dx}" cy="{dy}" r="5" fill="{spot}"/>' for dx, dy in ((-40, -44), (-14, -52), (14, -46), (40, -50), (-26, -32), (24, -34))))
        p.append(f'<path d="M-80,-36 l-14,-10 l4,14 Z" fill="{belly}"/>')
        hx, hy = 98, -18
        p.append(f'<path d="M70,-36 C84,-30 90,-24 {hx - 10},{hy}" fill="none" stroke="{fur}" stroke-width="22" stroke-linecap="round"/>')
        p.append(f'<ellipse cx="{hx}" cy="{hy}" rx="30" ry="18" fill="{fur}"/><ellipse cx="{hx + 26}" cy="{hy + 4}" rx="7" ry="5" fill="{ink}"/>')
        p.append(f'<ellipse cx="{hx - 18}" cy="{hy - 20}" rx="7" ry="16" fill="{fur}" transform="rotate(-60 {hx - 18} {hy - 20})"/>')
        p.append(f'<path d="M{hx - 6},{hy - 14} l-16,-20 l-10,4 M{hx - 16},{hy - 26} l-4,-12" fill="none" stroke="#8a5a2c" stroke-width="4" stroke-linecap="round"/>')
        p.append(f'<path d="M{hx},{hy - 6} q6,4 12,0" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>' if eyes == "closed"
                 else f'<circle cx="{hx + 4}" cy="{hy - 6}" r="4" fill="{ink}"/>')
    else:
        for lx, c in ((-50, dark), (-30, fur), (36, dark), (56, fur)):
            p.append(f'<path d="M{lx},-70 L{lx - 2},-6" stroke="{c}" stroke-width="10" stroke-linecap="round"/>'
                     f'<path d="M{lx - 8},-2 h12" stroke="#4a3020" stroke-width="6" stroke-linecap="round"/>')
        p.append(f'<path d="M-70,-104 l-12,-14 l2,18 Z" fill="{belly}"/>')
        p.append(f'<ellipse cx="0" cy="-92" rx="76" ry="34" fill="{fur}"/><ellipse cx="4" cy="-74" rx="54" ry="12" fill="{belly}"/>')
        p.append("".join(f'<circle cx="{dx}" cy="{dy}" r="5" fill="{spot}"/>' for dx, dy in ((-40, -104), (-14, -112), (14, -106), (40, -110), (-26, -90), (24, -92), (0, -96))))
        p.append(f'<path d="M50,-110 C62,-140 70,-156 78,-170" fill="none" stroke="{fur}" stroke-width="26" stroke-linecap="round"/>')
        hx, hy = 92, -176
        p.append(f'<path d="M{hx - 14},{hy - 20} l-10,-30 l-12,-6 M{hx - 18},{hy - 38} l8,-14 M{hx + 2},{hy - 22} l4,-30 l12,-8 M{hx + 4},{hy - 40} l-10,-12" fill="none" stroke="#8a5a2c" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>')
        p.append(f'<ellipse cx="{hx - 26}" cy="{hy - 10}" rx="8" ry="18" fill="{fur}" transform="rotate(-55 {hx - 26} {hy - 10})"/>'
                 f'<ellipse cx="{hx - 26}" cy="{hy - 10}" rx="4" ry="11" fill="#ffb3c7" transform="rotate(-55 {hx - 26} {hy - 10})"/>')
        p.append(f'<ellipse cx="{hx}" cy="{hy}" rx="22" ry="20" fill="{fur}"/><ellipse cx="{hx + 20}" cy="{hy + 8}" rx="16" ry="12" fill="{fur}"/>'
                 f'<ellipse cx="{hx + 22}" cy="{hy + 12}" rx="10" ry="7" fill="{belly}"/><ellipse cx="{hx + 33}" cy="{hy + 6}" rx="5" ry="4" fill="{ink}"/>')
        if eyes == "closed":
            p.append(f'<path d="M{hx},{hy - 4} q6,5 12,0" fill="none" stroke="{ink}" stroke-width="2.6" stroke-linecap="round"/>')
        else:
            p.append(f'<circle cx="{hx + 6}" cy="{hy - 4}" r="5" fill="{ink}"/><circle cx="{hx + 8}" cy="{hy - 6}" r="1.6" fill="#fff"/>'
                     f'<path d="M{hx},{hy - 12} l3,-3 M{hx + 6},{hy - 13} l1,-4 M{hx + 12},{hy - 11} l3,-3" stroke="{ink}" stroke-width="1.6" stroke-linecap="round"/>')
        if mood == "sad":
            p.append(f'<path d="M{hx + 6},{hy + 4} q-4,8 0,10 q4,-2 0,-10 Z" fill="#7fb3ff"/>')
        p.append(f'<ellipse cx="{hx + 6}" cy="{hy + 8}" rx="5" ry="3" fill="#ff8fb1" opacity="0.6"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def hunter_shadow(x, y, s=1, bag=False, flip=False, color="#2b2440"):
    """A hunter drawn only as a dark, faceless shadow (so he stays mysterious, not scary),
    walking right, feet at (x, y). About 300*s tall. bag=True: a sack hangs from a pole on his shoulder."""
    p = [f'<path d="M-24,-130 L-40,0 L-24,0 L-6,-90 L10,0 L26,0 L18,-130 Z" fill="{color}"/>',
         f'<path d="M-34,-230 Q0,-240 30,-226 L34,-120 Q0,-110 -36,-120 Z" fill="{color}"/>',
         f'<path d="M-30,-216 L-56,-150 M30,-216 L50,-160" stroke="{color}" stroke-width="18" stroke-linecap="round"/>',
         f'<circle cx="0" cy="-262" r="28" fill="{color}"/>',
         f'<path d="M-50,-270 Q0,-282 50,-270 L36,-280 Q30,-312 0,-312 Q-30,-312 -36,-280 Z" fill="{color}"/>']
    if bag:
        p.append(f'<path d="M-90,-250 L60,-206" stroke="#6b4a2e" stroke-width="8" stroke-linecap="round"/>'
                 f'<path d="M-82,-246 C-110,-220 -110,-170 -78,-160 C-50,-170 -52,-220 -74,-244 Z" fill="#a8774a"/>'
                 f'<path d="M-88,-236 q10,8 20,0" fill="none" stroke="#6b4a2e" stroke-width="4" stroke-linecap="round"/>')
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)
