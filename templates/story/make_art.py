"""Draws the pictures for this story. Run: python3 make_art.py

Each picture is a 600x600 scene built from the pieces in tools/storyart.py, so
Mehar and her friends look the same every night. Save one SVG per page, named
as in story.json (cover.svg, 01.svg, 02.svg, ...). You can also drop in finished
PNG/JPG/WebP pictures instead: just point "image" in story.json at them.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from storyart import *  # noqa

pics = {
    "cover": scene([sky("night"), moon(450, 130, 70), hill("#3fa45e", 480, 60), mehar(300, 560, 1.3, arms="wave")]),
    "01": scene([sky("night"), moon(470, 110, 55), hill("#3fa45e", 480, 50), mehar(250, 560, 1.4)]),
    "02": scene([sky("dusk"), hill("#3fa45e", 480, 50), owl(420, 330, 1), mehar(220, 560, 1.4, arms="up")]),
    "03": scene([bedroom(), mehar_in_bed(320, 450)]),
}

for name, svg in pics.items():
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write(svg)
print("drew", ", ".join(pics))
