#!/usr/bin/env python3
"""Check every story before publishing: valid JSON, all fields there, every picture exists,
and no photo files slipped into the repository.

The shelf holds three books (stories/index.json "books"): English (en), German (de) and
Hindi (hi). Each story lives in stories/<book>/<id>/ and is written in its book's language."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("en", "de", "hi")
MAX_WORDS = 60
problems = []

index = json.load(open(os.path.join(ROOT, "stories", "index.json"), encoding="utf-8"))
books = index.get("books", [])
if sorted(b.get("id") for b in books) != sorted(LANGS):
    problems.append("stories/index.json should have exactly three books: en, de and hi")

total = 0
for book in books:
    L = book.get("id")
    numbers = []
    for sid in book.get("stories", []):
        total += 1
        folder = os.path.join(ROOT, "stories", L, sid)
        where = f"{L}/{sid}"
        try:
            st = json.load(open(os.path.join(folder, "story.json"), encoding="utf-8"))
        except Exception as e:
            problems.append(f"{where}: story.json unreadable ({e})"); continue
        numbers.append(st.get("number"))
        if st.get("book") != L:
            problems.append(f"{where}: \"book\" should be {L!r}, found {st.get('book')!r}")
        if st.get("id") not in (None, sid):
            problems.append(f"{where}: \"id\" should match the folder name")
        title = st.get("title", {})
        if not title.get(L):
            problems.append(f"{where}: title.{L} missing")
        if L == "hi" and not title.get("hi_roman"):
            problems.append(f"{where}: title.hi_roman missing")
        images = [st.get("cover")] + [p.get("image") for p in st.get("pages", [])]
        for img in images:
            if not img or not os.path.exists(os.path.join(folder, img)):
                problems.append(f"{where}: picture {img!r} not found")
        pages = st.get("pages", [])
        if not 8 <= len(pages) <= 14:
            problems.append(f"{where}: has {len(pages)} pages; aim for 10 to 12")
        if not st.get("moral", {}).get(L):
            problems.append(f"{where}: moral.{L} missing")
        if L == "hi" and not st.get("moral", {}).get("hi_roman"):
            problems.append(f"{where}: moral.hi_roman missing")
        for i, q in enumerate(st.get("questions", []), 1):
            if not q.get(L):
                problems.append(f"{where}: question {i} needs {L}")
        for i, p in enumerate(pages, 1):
            if not p.get("text"):
                problems.append(f"{where}: page {i} has no text")
            if len(p.get("text", "").split()) > MAX_WORDS:
                problems.append(f"{where}: page {i} has more than {MAX_WORDS} words; keep it short")
            if L == "hi" and not p.get("roman"):
                problems.append(f"{where}: page {i} needs \"roman\" (the Hindi in Roman letters)")
            w = p.get("word")
            if w and not all(w.get(l) for l in LANGS):
                problems.append(f"{where}: page {i} word needs en, de and hi")
            if p.get("say", {}).get("lang") not in (None, *LANGS):
                problems.append(f"{where}: page {i} say.lang must be en, de or hi")
    if numbers != list(range(1, len(numbers) + 1)):
        problems.append(f"book {L}: story numbers should run 1, 2, 3... in index order, found {numbers}")
    for name in os.listdir(os.path.join(ROOT, "stories", L)) if os.path.isdir(os.path.join(ROOT, "stories", L)) else []:
        if os.path.isdir(os.path.join(ROOT, "stories", L, name)) and name not in book.get("stories", []):
            problems.append(f"{L}/{name}: folder is not listed in stories/index.json")

for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in (".git", "private", "node_modules")]
    for f in files:
        if f.lower().endswith((".heic", ".jpeg", ".jpg", ".dng", ".mov", ".mp4")):
            problems.append(f"{os.path.relpath(os.path.join(dirpath, f), ROOT)}: photo/video file in the repo; is this a private photo?")

if problems:
    print("\n".join(problems)); sys.exit(1)
print(f"All {total} stories in {len(books)} books look good.")
