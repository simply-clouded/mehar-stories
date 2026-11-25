# Publishing tonight's story

One story a night takes four steps.

## 1. Start the story

```sh
python3 tools/new_story.py "Mehar and the Sleepy Snail"
```

This creates `stories/<today>-mehar-and-the-sleepy-snail/` with a `story.json`, a
`make_art.py` and placeholder pictures, and adds it to `stories/index.json`.

## 2. Write it (`story.json`)

| field | what goes in it |
| --- | --- |
| `title` | the title in `en`, `de`, `hi`, plus `hi_roman` (Hindi in Roman letters) |
| `themes` | any of `moon`, `animals`, `painting`, `nature`, `colours`, `stars`, `sea`, `numbers`, `friends`, `weather`, `food`, `music` |
| `learning` | what she learns tonight, in a few words, e.g. "Counting to five" |
| `pages` | 5 to 8 pages. Each has an `image`, one or two short English sentences in `text`, and usually one `word` to learn in all three languages |
| `say` | optional: one short line on a page in German (`"lang": "de"`) or Hindi (`"lang": "hi"`, add `roman`) |
| `question` | one question to ask Mehar before sleep, in all three languages |

Story guide:

- Mehar is always the hero. Fantasy is welcome: talking animals, a moon with a face,
  paint that comes alive.
- Each story teaches one small thing: colours, numbers, animal names, kindness, nature.
- Few words, big pictures: at most two short sentences a page (the checker warns above 25 words).
- Mix the languages gently: English carries the story; German and Hindi come in as one
  word per page and an occasional short line.
- End calm and sleepy, with goodnight in the three languages.

## 3. Draw it (`make_art.py`)

Pictures are SVG drawings built from `tools/storyart.py`, so Mehar looks the same every
night. The kit has:

- `mehar(x, y, s, arms="down|wave|up|brush", eyes="open|closed", mouth="smile|open|oh|yawn", outfit="dress|pyjama", brush=colour)`
- `mehar_in_bed(...)`, `moon(..., mood="happy|sad|sleepy", grey=False)`, `owl`, `bunny`, `tree`, `flower`, `star`
- backgrounds: `sky("night|grey|dusk|day|painted")`, `hill`, `bedroom`, `window_frame`, paint `stroke`s, `zzz`

Run `python3 make_art.py` inside the story folder to redraw. Finished PNG, JPG or WebP
pictures from another tool also work: drop them in the folder and name them in `story.json`.
Never use real photos of Mehar as story pictures.

If her look needs a change (hairstyle, favourite dress), edit `MEHAR` at the top of
`tools/storyart.py`; old stories keep the SVGs they were drawn with.

## 4. Check and publish

```sh
python3 tools/check_stories.py
python3 -m http.server 8000   # look at it on http://localhost:8000
git add stories && git commit -m "Add story: Mehar and the Sleepy Snail" && git push
```

GitHub Pages publishes within a minute or two, and the new story shows up as
*Tonight's story* at the top of the shelf.
