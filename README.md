# LingoWorld

**By Arshaad**

A free translator for the languages of the whole world — with one special mode nobody else built in.

Live demo: https://marshaad708-coder.github.io/lingoworld/

Video: *(paste your video link here)*

## What it does

- Translate between **121 languages** — any language to any language. English to Chinese, Arabic to Urdu, French to German, Urdu to English, and thousands of other pairs.
- **Roman Urdu (Special)** — type Urdu the way everyone actually types it on their phone, in English letters: `mujhe kal ghar jana hai` becomes proper Urdu script **مجھے کل گھر جانا ہے**, and from there it can go into any other language. It also works in reverse.
- **Auto-detect** — you do not have to know which language the text is in. Roman Urdu is detected on its own too.
- **Listen** — hear the translation spoken aloud.
- **Copy and WhatsApp share** — send a translation to anyone in one tap.
- No login, no install, no cost. Open the page and use it.

The Roman Urdu mode works from a hand-built word list of about 500 everyday words and runs fully on the page. The other languages use a free translation service, so they need an internet connection.

## Run it yourself

Easiest way: open `index.html` in any browser.

Or with Python:

```
pip install flask
python app.py
```

Then open http://127.0.0.1:5000

## Build the page

The page is generated so the Roman Urdu word list stays in one place:

```
python build_page.py
```

It reads the word list from the Roman Urdu Toolkit project and writes a fresh `index.html`.

## Tests

```
python -m pytest tests/ -q
```

## License

MIT — see LICENSE. Free to use and share; please keep the credit line.
