#!/usr/bin/env python3
"""Check every story before publishing: valid JSON, all fields there, every picture exists,
and no photo files slipped into the repository."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("en", "de", "hi")
problems = []

index = json.load(open(os.path.join(ROOT, "stories", "index.json"), encoding="utf-8"))
numbers = []
for sid in index["stories"]:
    folder = os.path.join(ROOT, "stories", sid)
    try:
        st = json.load(open(os.path.join(folder, "story.json"), encoding="utf-8"))
    except Exception as e:
        problems.append(f"{sid}: story.json unreadable ({e})"); continue
    numbers.append(st.get("number"))
    for lang in LANGS:
        if not st.get("title", {}).get(lang):
            problems.append(f"{sid}: title.{lang} missing")
    images = [st.get("cover")] + [p.get("image") for p in st.get("pages", [])]
    for img in images:
        if not img or not os.path.exists(os.path.join(folder, img)):
            problems.append(f"{sid}: picture {img!r} not found")
    for i, p in enumerate(st.get("pages", []), 1):
        if not p.get("text"):
            problems.append(f"{sid}: page {i} has no text")
        if len(p.get("text", "").split()) > 25:
            problems.append(f"{sid}: page {i} has more than 25 words; keep it short")
        w = p.get("word")
        if w and not all(w.get(l) for l in LANGS):
            problems.append(f"{sid}: page {i} word needs en, de and hi")
        if p.get("say", {}).get("lang") not in (None, *LANGS):
            problems.append(f"{sid}: page {i} say.lang must be en, de or hi")

if numbers != list(range(1, len(numbers) + 1)):
    problems.append(f"story numbers should run 1, 2, 3... in index order, found {numbers}")

for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in (".git", "private", "node_modules")]
    for f in files:
        if f.lower().endswith((".heic", ".jpeg", ".jpg", ".dng", ".mov", ".mp4")):
            problems.append(f"{os.path.relpath(os.path.join(dirpath, f), ROOT)}: photo/video file in the repo; is this a private photo?")

if problems:
    print("\n".join(problems)); sys.exit(1)
print(f"All {len(index['stories'])} stories look good.")
