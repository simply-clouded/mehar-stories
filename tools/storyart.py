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
# never stored in this repository): a dark chin-length bob with a soft fringe and a
# tiny top sprout, a hair clip, big dark eyes, round cheeks, a red kurta-style dress.
MEHAR = {
    "skin": "#e8b994",
    "skin_shade": "#d39f7a",
    "hair": "#23160f",
    "tie": "#ff8fb1",       # hair clip
    "dress": "#d8343f",     # red kurta-style dress
    "dress_dots": "#ffd36b", # gold trim dots
    "pyjama": "#9fb8ff",
    "shoes": "#e2546b",
    "cheek": "#ff8b8b",
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

def mehar_head(eyes="open", mouth="smile", look=0):
    c = MEHAR
    ex = 13 + look
    parts = [
        # chin-length bob behind the face
        f'<path d="M-44,-150 Q-46,-196 0,-196 Q46,-196 44,-150 L46,-116 Q36,-108 26,-114 L-26,-114 Q-36,-108 -46,-116 Z" fill="{c["hair"]}"/>',
        # ears and face
        f'<circle cx="-35" cy="-142" r="6" fill="{c["skin_shade"]}"/>',
        f'<circle cx="35" cy="-142" r="6" fill="{c["skin_shade"]}"/>',
        f'<ellipse cx="0" cy="-146" rx="35" ry="36" fill="{c["skin"]}"/>',
        # side locks over the ears and a soft straight fringe
        f'<path d="M-44,-154 Q-40,-128 -42,-114 Q-34,-112 -30,-118 Q-34,-134 -30,-156 Z" fill="{c["hair"]}"/>',
        f'<path d="M44,-154 Q40,-128 42,-114 Q34,-112 30,-118 Q34,-134 30,-156 Z" fill="{c["hair"]}"/>',
        f'<path d="M-38,-150 Q-38,-190 0,-190 Q38,-190 38,-150 Q30,-158 20,-157 Q12,-162 4,-158 Q-6,-163 -14,-157 Q-26,-160 -38,-150 Z" fill="{c["hair"]}"/>',
        # little top sprout and a hair clip, like hers
        f'<path d="M-2,-190 Q-10,-212 -4,-220 M2,-190 Q8,-210 14,-214" fill="none" stroke="{c["hair"]}" stroke-width="4" stroke-linecap="round"/>',
        f'<rect x="-30" y="-180" width="20" height="8" rx="4" fill="{c["tie"]}" transform="rotate(-20 -20 -176)"/>',
        f'<circle cx="-20" cy="-132" r="7" fill="{c["cheek"]}" opacity="0.45"/>',
        f'<circle cx="20" cy="-132" r="7" fill="{c["cheek"]}" opacity="0.45"/>',
    ]
    if eyes == "closed":
        for sx in (-1, 1):
            parts.append(f'<path d="M{sx*ex-6},-147 Q{sx*ex},-141 {sx*ex+6},-147" fill="none" stroke="{c["hair"]}" stroke-width="2.6" stroke-linecap="round"/>')
    else:
        for sx in (-1, 1):
            parts.append(f'<ellipse cx="{sx*ex}" cy="-148" rx="5" ry="6.5" fill="{c["hair"]}"/>'
                         f'<circle cx="{sx*ex+1.6}" cy="-150.5" r="1.8" fill="#fff"/>')
    if mouth == "smile":
        parts.append('<path d="M-8,-130 Q0,-121 8,-130" fill="none" stroke="#5a2a1c" stroke-width="2.6" stroke-linecap="round"/>')
    elif mouth == "open":
        parts.append('<path d="M-8,-131 Q0,-118 8,-131 Z" fill="#7a2f2a"/>')
    elif mouth == "yawn":
        parts.append('<ellipse cx="0" cy="-127" rx="5" ry="6.5" fill="#7a2f2a"/>')
    elif mouth == "oh":
        parts.append('<circle cx="0" cy="-128" r="3.6" fill="#7a2f2a"/>')
    return "".join(parts)


def _arm(x1, y1, x2, y2, color):
    return (f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="11" stroke-linecap="round"/>'
            f'<circle cx="{x2}" cy="{y2}" r="7" fill="{MEHAR["skin"]}"/>')


def paintbrush(x, y, angle=-35, tip=PAINT["blue"], s=1):
    """A brush held at (x, y), rotated `angle` degrees (0 = bristles straight up)."""
    return (f'<g transform="translate({x} {y}) rotate({angle}) scale({s})">'
            f'<rect x="-4" y="-70" width="8" height="64" rx="4" fill="#c98a4b"/>'
            f'<rect x="-6" y="-80" width="12" height="14" rx="2" fill="#b8bcc8"/>'
            f'<path d="M-6,-80 Q0,-108 6,-80 Z" fill="{tip}"/></g>')


def mehar(x, y, s=1, arms="down", eyes="open", mouth="smile", outfit="dress",
          brush=None, look=0, flip=False):
    """Mehar standing, feet at (x, y). About 200*s pixels tall.

    arms: down | wave | up | brush (right hand holds a brush; pass brush=colour)
    """
    c = MEHAR
    cloth = c["dress"] if outfit == "dress" else c["pyjama"]
    p = []
    # legs and shoes
    p.append(f'<rect x="-17" y="-46" width="11" height="44" rx="5" fill="{c["skin"]}"/>'
             f'<rect x="6" y="-46" width="11" height="44" rx="5" fill="{c["skin"]}"/>'
             f'<ellipse cx="-12" cy="-2" rx="12" ry="7" fill="{c["shoes"]}"/>'
             f'<ellipse cx="12" cy="-2" rx="12" ry="7" fill="{c["shoes"]}"/>')
    # arms behind/at sides
    left = {"down": (-38, -66), "wave": (-40, -70), "up": (-48, -150), "brush": (-38, -66)}[arms]
    right = {"down": (38, -66), "wave": (50, -150), "up": (48, -150), "brush": (54, -112)}[arms]
    p.append(_arm(-20, -104, *left, c["skin"]))
    p.append(_arm(20, -104, *right, c["skin"]))
    # dress
    p.append(f'<path d="M-22,-114 Q0,-120 22,-114 L46,-40 Q0,-30 -46,-40 Z" fill="{cloth}"/>')
    p.append(f'<path d="M-44,-46 Q0,-36 44,-46" fill="none" stroke="{c["dress_dots"]}" stroke-width="4" stroke-dasharray="2 5" stroke-linecap="round"/>')
    for dx, dy in ((-18, -60), (12, -78), (24, -58), (-6, -94), (-26, -70), (2, -64)):
        p.append(f'<circle cx="{dx}" cy="{dy}" r="3" fill="{c["dress_dots"]}" opacity="0.8"/>')
    p.append(f'<rect x="-7" y="-122" width="14" height="12" rx="4" fill="{c["skin"]}"/>')
    p.append(mehar_head(eyes, mouth, look))
    if arms == "brush" or brush:
        hx, hy = right
        p.append(paintbrush(hx, hy + 6, angle=30, tip=brush or PAINT["blue"]))
    inner = "".join(p)
    if flip:
        inner = f'<g transform="scale(-1 1)">{inner}</g>'
    return g(inner, x, y, s)


def mehar_in_bed(x, y, s=1, blanket="#7f8cff", eyes="closed"):
    """Mehar tucked into bed; (x, y) is the middle of the mattress top."""
    c = MEHAR
    inner = (
        f'<rect x="-190" y="-10" width="380" height="80" rx="16" fill="#8a5a3c"/>'
        f'<rect x="-200" y="-130" width="26" height="200" rx="10" fill="#8a5a3c"/>'
        f'<rect x="-182" y="-24" width="364" height="34" rx="14" fill="#f3efe6"/>'
        f'<ellipse cx="-110" cy="-30" rx="70" ry="30" fill="#ffffff"/>'
        + g(mehar_head(eyes, "smile"), -110, 92, 0.95)
        + f'<path d="M-150,-14 Q-40,-60 180,-24 L180,30 L-150,30 Z" fill="{blanket}"/>'
        + "".join(f'<path d="{star_path(-60 + i*55, 0 - (i % 2) * 14, 7)}" fill="#ffe680"/>' for i in range(5))
    )
    return g(inner, x, y, s)


# ---------------------------------------------------------------- friends

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
