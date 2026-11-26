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
| `inspired_by` | the Panchatantra (or other folk) tale it grows from |
| `themes` | any of `moon`, `animals`, `painting`, `nature`, `colours`, `stars`, `sea`, `numbers`, `friends`, `weather`, `food`, `music` |
| `learning` | the lesson in a few words, e.g. "Thinking before you trust a flatterer" |
| `characters` | who appears: `[{ "name": "Raja Singh", "who": "a proud, bossy lion" }]` |
| `pages` | 10 to 12 pages. Each has an `image`, two to four sentences in `text`, and one `word` to learn in all three languages |
| `say` | optional: one short line on a page in German (`"lang": "de"`) or Hindi (`"lang": "hi"`, add `roman`) |
| `moral` | the moral in all three languages; it gets its own page at the end |
| `questions` | two or three questions to talk about before sleep, in all three languages |

Story guide (written for a 6-year-old listener):

- **Panchatantra at heart.** Take a classic fable (the clever hare and the lion, the
  monkey and the crocodile, the talkative tortoise, the crows and the snake, the blue
  jackal, the brahmin and the goat...) and retell it with Mehar inside the story.
  She doesn't just watch: she notices things, asks questions and helps decide.
- **A moral that is earned.** The lesson must come out of what happens, then be said
  plainly on the moral page. Good themes: cleverness over strength, honesty, not
  trusting flatterers, thinking before acting, sharing, standing up for friends,
  kindness even to someone unkind.
- **Twists and turns.** At least one surprise the listener can guess at (ask "Can you
  guess?" in the text), and one moment where it could go wrong.
- **Gentle endings.** Old fables can end harshly. Keep the lesson but soften the
  ending: the bully is humbled and changes, nobody gets eaten.
- **Fun to read aloud.** Dialogue, sound words (SPLASH! ROAAAR!), and a repeated line.
- **Regular friends:** Hasi the bunny, Moti the elephant (greets in Hindi), Uhu the owl
  (speaks German), Chanda Mama the moon, and Raja Singh the lion, now reformed. New
  characters are welcome.
- **Languages:** English carries the story; German and Hindi come in through one word per
  page, a short line now and then, the moral and the questions.
- Keep pages to about 30 to 45 words (the checker stops at 60), and always end with
  Mehar back home and sleepy.

## 3. Draw it (`make_art.py`)

Pictures are SVG drawings built from `tools/storyart.py`, so Mehar looks the same every
night. The kit has:

- `mehar(x, y, s, arms="down|wave|up|brush|hold", eyes="open|happy|closed", mouth="smile|open|oh|soft|yawn", outfit="dress|pyjama", hair="bob|bun|sprout", legs=True, brush=colour)`
- `mehar_in_bed(...)`, `moon(..., mood="happy|sad|sleepy", grey=False)`, `owl`, `bunny`, `elephant(rider=...)`, `cloud(mood, rainbow)`, `firefly`, `paintbox`, `tree`, `flower`, `star`
- backgrounds: `sky("night|grey|dusk|day|painted")`, `hill`, `forest`, `bedroom`, `window_frame`, `moonbeam`, paint `stroke`s, `zzz`

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
