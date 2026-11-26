#!/usr/bin/env python3
"""Start tonight's story in one of the three books (en, de, hi).

    python3 tools/new_story.py --book en "Mehar and the Sleepy Snail"
    python3 tools/new_story.py --book de "Mehar und die müde Schnecke"
    python3 tools/new_story.py --book hi "Mehar aur aalsi ghonga" --date 2026-11-27

The title is the story's title in the book's language (for Hindi, give it in Roman
letters: it becomes the folder name; put the Devanagari in story.json afterwards).
Creates stories/<book>/<date>-<slug>/ from templates/story/, fills in the book, number,
date and title, draws placeholder pictures, and adds the story to that book in
stories/index.json (newest last). Then edit story.json and make_art.py, run
make_art.py again, and commit. The website picks the story up by itself.
"""
import argparse, datetime, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "stories", "index.json")


def slugify(text):
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        text = text.lower().replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")[:60]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--book", required=True, choices=["en", "de", "hi"], help="which book: en, de or hi")
    ap.add_argument("title", help="title in the book's language (Hindi: Roman letters)")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="YYYY-MM-DD (default: today)")
    args = ap.parse_args()

    datetime.date.fromisoformat(args.date)
    story_id = f"{args.date}-{slugify(args.title)}"
    folder = os.path.join(ROOT, "stories", args.book, story_id)
    if os.path.exists(folder):
        sys.exit(f"{folder} already exists")

    with open(INDEX, encoding="utf-8") as f:
        index = json.load(f)

    shutil.copytree(os.path.join(ROOT, "templates", "story"), folder)
    path = os.path.join(folder, "story.json")
    with open(path, encoding="utf-8") as f:
        story = json.load(f)
    book = next(b for b in index["books"] if b["id"] == args.book)
    story = {"id": story_id, "book": args.book, **story}
    story["number"] = len(book["stories"]) + 1
    story["date"] = args.date
    story["title"]["hi_roman" if args.book == "hi" else args.book] = args.title
    with open(path, "w", encoding="utf-8") as f:
        json.dump(story, f, ensure_ascii=False, indent=2)
        f.write("\n")

    subprocess.run([sys.executable, os.path.join(folder, "make_art.py")], check=True)

    book["stories"].append(story_id)
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Story No. {story['number']} started in stories/{args.book}/{story_id}/")
    print("Next: write story.json, draw the pictures in make_art.py, run it, then commit and push.")


if __name__ == "__main__":
    main()
