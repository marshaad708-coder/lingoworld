import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


def _dict():
    m = re.search(r"const ROMAN_DICT = (\{.*?\});\nconst LANGS", HTML, re.S)
    return json.loads(m.group(1))


def _to_urdu(text, mapping):
    return " ".join(mapping.get(w, w) for w in text.split())


def test_language_count():
    m = re.search(r"const LANGS = \[(.*?)\n\];", HTML, re.S)
    codes = re.findall(r'\["([a-zA-Z\-]+)",', m.group(1))
    assert len(codes) >= 100
    assert len(codes) == len(set(codes))


def test_roman_dict_embedded():
    assert len(_dict()) >= 400


def test_roman_phrases():
    d = _dict()
    assert _to_urdu("mujhe kal ghar jana hai", d) == "مجھے کل گھر جانا ہے"
    assert _to_urdu("aap ka din kaisa guzra", d) == "آپ کا دن کیسا گزرا"
    assert _to_urdu("mein pakistan se hoon", d) == "میں پاکستان سے ہوں"
    assert _to_urdu("aaj mausam bohat acha hai", d) == "آج موسم بہت اچھا ہے"


def test_page_features():
    for marker in ["wa.me", "speechSynthesis", "translate.googleapis.com",
                   "api.mymemory.translated.net", "Roman Urdu (Special)"]:
        assert marker in HTML, marker
