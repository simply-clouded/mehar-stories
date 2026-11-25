#!/usr/bin/env python3
"""Start tonight's story.

    python3 tools/new_story.py "Mehar and the Sleepy Snail"
    python3 tools/new_story.py "Mehar and the Sleepy Snail" --date 2026-11-27

Creates stories/<date>-<slug>/ from templates/story/, fills in the number, date and
English title, draws placeholder pictures, and adds the story to stories/index.json
(newest last). Then edit story.json and make_art.py, run make_art.py again, and
commit. The website picks the story up by itself.
"""
import argparse, datetime, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "stories", "index.json")


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title", help="English title of the story")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="YYYY-MM-DD (default: today)")
    args = ap.parse_args()

    datetime.date.fromisoformat(args.date)
    story_id = f"{args.date}-{slugify(args.title)}"
    folder = os.path.join(ROOT, "stories", story_id)
    if os.path.exists(folder):
        sys.exit(f"{folder} already exists")

    with open(INDEX, encoding="utf-8") as f:
        index = json.load(f)

    shutil.copytree(os.path.join(ROOT, "templates", "story"), folder)
    path = os.path.join(folder, "story.json")
    with open(path, encoding="utf-8") as f:
        story = json.load(f)
    story = {"id": story_id, **story}
    story["number"] = len(index["stories"]) + 1
    story["date"] = args.date
    story["title"]["en"] = args.title
    with open(path, "w", encoding="utf-8") as f:
        json.dump(story, f, ensure_ascii=False, indent=2)
        f.write("\n")

    subprocess.run([sys.executable, os.path.join(folder, "make_art.py")], check=True)

    index["stories"].append(story_id)
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Story No. {story['number']} started in stories/{story_id}/")
    print("Next: write story.json, draw the pictures in make_art.py, run it, then commit and push.")


if __name__ == "__main__":
    main()
