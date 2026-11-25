# Goodnight, Mehar · शुभ रात्रि, मेहर · Gute Nacht, Mehar

*a new picture story every night*

A bedtime picture book for Mehar, read aloud at night. Every story stars Mehar as an
illustrated character and mixes simple English with a little German and Hindi. Themes
come from what she loves: animals, the moon, painting and nature. Stories are fantasy,
gently teach something, and use very few words per page.

It is built like the Raahi diary: a single page (`index.html`) shows a bookshelf, and
each story opens as a book you turn page by page. A soft music-box lullaby plays in the
browser, and every coloured word can be tapped to hear it in English, Deutsch or हिंदी.

## How it is laid out

- `index.html`: the shelf, the book, the lullaby and the tap-to-hear words.
- `stories/index.json`: the book's name and the list of stories, oldest first.
- `stories/<date>-<slug>/story.json`: one story's words, in English, German and Hindi.
- `stories/<date>-<slug>/*.svg`: its pictures, one square picture per page plus a cover.
- `tools/storyart.py`: the drawing kit (Mehar, the moon, owl, bunny, trees, stars...).
- `tools/new_story.py`: starts tonight's story from `templates/story/`.
- `tools/check_stories.py`: checks every story before it goes live.
- `lib/page-flip.js`: page-turn library ([StPageFlip](https://github.com/Nodlik/StPageFlip), MIT licence).

Each story has its own link, for example `…/#2026-11-26-mehar-paints-the-moon`.

To publish a new story every day, see [PUBLISHING.md](PUBLISHING.md).

## Privacy

This is a public site about a young child, so it is careful by design:

- **No photos of Mehar are stored here or published.** Her family's reference photos
  were used only to decide how the illustrated Mehar looks (her bob and fringe, the hair
  clip, her red kurta-style dress). Only the drawings are public.
- `.gitignore` blocks common photo formats and a `private/` folder, and
  `tools/check_stories.py` fails if a photo file appears in the repository.
- Only her first name appears. No surname, birthday, school, city or other identifying
  detail goes into a story.
- The page asks search engines not to index it (`noindex`), so it is shared by link.
  Anyone with the link can still see it.

## Viewing it locally

The page loads its stories with `fetch`, so open it through a small web server:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

## Going live

In the repository's **Settings → Pages**, choose *Deploy from a branch*, branch `main`,
folder `/ (root)`. The site then lives at `https://simply-clouded.github.io/mehar-stories/`.
