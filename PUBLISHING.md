# Publishing tonight's stories

The shelf holds three books, and each gets its own new story every night:

| book | folder | written in |
| --- | --- | --- |
| **Goodnight, Mehar** | `stories/en/` | English |
| **Gute Nacht, Mehar** | `stories/de/` | German |
| **शुभ रात्रि, मेहर** | `stories/hi/` | Hindi (Devanagari), with a Roman-letters line under each page |

The three stories of one night are three *different* fables, so the books don't repeat
each other. Before choosing a tale, look at what each book already has:

```sh
grep -h '"inspired_by"' stories/*/*/story.json
```

## 1. Start each story

```sh
python3 tools/new_story.py --book en "Mehar and the Talkative Tortoise"
python3 tools/new_story.py --book de "Mehar und der kluge Affe"
python3 tools/new_story.py --book hi "Mehar aur kauve ki chaal"   # Hindi title in Roman letters
```

Each creates `stories/<book>/<today>-<slug>/` with a `story.json`, a `make_art.py` and
placeholder pictures, and adds it to that book in `stories/index.json`.

## 2. Write it (`story.json`)

Everything a child hears is in the book's language. Fields:

| field | what goes in it |
| --- | --- |
| `book` | `en`, `de` or `hi` (filled in for you) |
| `title` | the title in the book's language (`hi` also needs `hi_roman`), plus `en` so parents can see it |
| `inspired_by` | the Panchatantra (or other folk) tale it grows from, in the book's language |
| `themes` | any of `moon`, `animals`, `painting`, `nature`, `colours`, `stars`, `sea`, `numbers`, `friends`, `weather`, `food`, `music` |
| `learning` | the lesson in a few words, in the book's language |
| `characters` | who appears: `[{ "name": "...", "who": "..." }]`, in the book's language |
| `pages` | 10 to 12 pages. Each has an `image` and `text` (book language). Hindi pages also have `roman`. Optional: one `word` in en/de/hi to tap and hear, and a short `say` line |
| `moral` | the moral under the book's key (`en`, `de` or `hi`; Hindi also `hi_roman`) |
| `questions` | three questions to talk about before sleep, under the book's key (Hindi also `hi_roman`) |

Story guide (written for a 6-year-old listener):

- **Panchatantra at heart.** Take a classic fable (the clever hare and the lion, the
  monkey and the crocodile, the talkative tortoise, the crows and the snake, the blue
  jackal, the brahmin and the goat, the mice who freed the elephants, the lion brought
  back to life, the heron and the crab...) and retell it with Mehar inside the story.
  Jataka tales, Hitopadesha and Akbar–Birbal-style riddles are fine too. She doesn't just
  watch: she notices things, asks questions and helps decide.
- **Less text, more pictures.** About 20 to 35 words a page (the checker stops at 60).
  Let the picture tell half the story.
- **A moral that is earned.** The lesson comes out of what happens, then is said plainly
  on the moral page. Good themes: cleverness over strength, honesty, not trusting
  flatterers, thinking before acting, sharing, standing up for friends, kindness even to
  someone unkind, listening to good advice, teamwork.
- **Twists and turns.** At least one surprise the listener can guess at ("Can you guess?"
  / "Was glaubst du?" / "बताओ, क्या हुआ होगा?"), and one moment where it could go wrong.
- **Gentle endings.** Old fables can end harshly. Keep the lesson but soften the ending:
  the bully is humbled and changes, nobody gets eaten.
- **Fun to read aloud.** Dialogue, sound words (SPLASH! PLATSCH! छपाक!), a repeated line.
- **Mehar's world:** she loves animals, the moon, painting and nature. Regular friends:
  Hasi the bunny, Moti the elephant, Uhu the owl, Chanda Mama the moon, and Raja Singh the
  lion, now reformed. New characters are welcome.
- **Good German and Hindi.** Simple, natural children's-book language, not word-for-word
  translation. Hindi uses feminine forms for Mehar (मेहर बोली, वह गई).
- Always end with Mehar back home and sleepy.

## 3. Draw it (`make_art.py`)

Pictures are SVG drawings built from `tools/storyart.py`, so Mehar looks the same every
night. The kit has:

- `mehar(x, y, s, arms="down|wave|up|brush|hold", eyes="open|happy|closed", mouth="smile|open|oh|soft|yawn", outfit="dress|pyjama", hair="bob|bun|sprout", legs=True, brush=colour)`
- `mehar_in_bed(...)`, `moon(..., mood="happy|sad|sleepy", grey=False)`, `owl`, `bunny`, `elephant(rider=...)`, `lion(mood=...)`, `cloud(mood, rainbow)`, `firefly`, `paintbox`, `tree`, `flower`, `star`, `well`, `rock`, `magic_book`
- backgrounds: `sky("night|grey|dusk|day|painted")`, `hill`, `forest`, `jungle`, `bedroom`, `window_frame`, `moonbeam`, paint `stroke`s, `zzz`

When a story needs an animal or thing the kit doesn't have yet (a monkey, a crocodile, a
tortoise, a crow...), add a new function for it to `tools/storyart.py` in the same flat,
friendly style, so later stories can use it too. Never change how existing pieces look
by accident: old stories keep their SVGs, but new ones should match.

Run `python3 make_art.py` inside the story folder to redraw. Never use real photos of
Mehar as story pictures. Her look is in `MEHAR` at the top of `tools/storyart.py`.

## 4. Check and publish

```sh
python3 tools/check_stories.py
git add -A stories tools && git commit -m "Tonight's stories: <en title> / <de title> / <hi title>" && git push origin main
```

GitHub Pages publishes within a minute or two, and each book shows its new story as
*Tonight's story*. A scheduled task does all of this every evening at about 7 PM
Berlin time.
