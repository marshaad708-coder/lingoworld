"""Build the single-file LingoWorld page with the Roman Urdu dictionary embedded."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
DICT_FILE = Path.home() / "workspace/roman-urdu-toolkit/roman_urdu_toolkit/data/roman_to_urdu.txt"

mapping = {}
for line in DICT_FILE.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    roman, urdu = line.split("\t")
    mapping[roman.strip()] = urdu.strip()

# Common everyday words people type that the base word list missed.
SUPPLEMENT = {
    "pakistan": "پاکستان", "pakistani": "پاکستانی", "lahore": "لاہور", "karachi": "کراچی",
    "islamabad": "اسلام آباد", "india": "انڈیا", "china": "چین", "urdu": "اردو",
    "hoon": "ہوں", "hun": "ہوں", "mera": "میرا", "meri": "میری", "mere": "میرے",
    "tera": "تیرا", "teri": "تیری", "tere": "تیرے", "uska": "اس کا", "uski": "اس کی",
    "iska": "اس کا", "iski": "اس کی", "naam": "نام", "ja": "جا", "rahe": "رہے",
    "raha": "رہا", "rahi": "رہی", "ho": "ہو", "mausam": "موسم", "kaisa": "کیسا",
    "kaisi": "کیسی", "guzra": "گزرا", "guzri": "گزری", "theek": "ٹھیک", "hum": "ہم",
    "jayenge": "جائیں گے", "jayega": "جائے گا", "seekhni": "سیکھنی", "seekhna": "سیکھنا",
    "seekh": "سیکھ", "tujhe": "تجھے", "usse": "اس سے", "isse": "اس سے", "is": "اس",
    "us": "اس", "in": "ان", "un": "ان", "kitne": "کتنے", "kidhar": "کدھر",
    "duniya": "دنیا", "log": "لوگ", "university": "یونیورسٹی", "college": "کالج",
    "naraz": "ناراض", "pareshan": "پریشان", "bimar": "بیمار", "gaye": "گئے",
    "aaye": "آئے", "khaya": "کھایا", "piya": "پیا", "likha": "لکھا", "parha": "پڑھا",
    "dekha": "دیکھا", "bola": "بولا", "samajh": "سمجھ", "khuda": "خدا",
    "assalamualaikum": "السلام علیکم", "walaikumassalam": "وعلیکم السلام",
    "cheh": "چھ", "saat": "سات", "aath": "آٹھ", "nau": "نو", "das": "دس",
    "sau": "سو", "hazar": "ہزار", "peer": "پیر", "mangal": "منگل", "budh": "بدھ",
    "jumerat": "جمعرات", "jumma": "جمعہ", "hafta": "ہفتہ", "itwaar": "اتوار",
    "parson": "پرسوں", "roz": "روز", "aajkal": "آج کل", "zaroor": "ضرور",
    "shayad": "شاید", "bilkul": "بالکل", "waqai": "واقعی", "matlab": "مطلب",
    "masla": "مسئلہ", "sawal": "سوال", "jawab": "جواب", "khabar": "خبر",
    "ghar": "گھر", "mohalla": "محلہ", "sadak": "سڑک", "pul": "پل",
    "train": "ٹرین", "bus": "بس", "jahaz": "جہاز", "ticket": "ٹکٹ",
    "khareedna": "خریدنا", "bechna": "بیچنا", "qeemat": "قیمت", "sasta": "سستا",
    "mehenga": "مہنگا", "mehnga": "مہنگا", "muft": "مفت", "khaas": "خاص",
    "aam": "عام", "faida": "فائدہ", "nuqsan": "نقصان",
    # Chat-style short spellings people actually type (added after his live test,
    # where "hng kaisy ho jnb" was not recognised at all).
    "hng": "ہاں", "hanji": "ہاں جی", "han": "ہاں", "kaisy": "کیسے", "kaisay": "کیسے",
    "kesay": "کیسے", "kese": "کیسے", "jnb": "جناب", "janab": "جناب", "thk": "ٹھیک",
    "thik": "ٹھیک", "bhi": "بھی", "bht": "بہت", "boht": "بہت", "kia": "کیا",
    "hy": "ہے", "nhi": "نہیں", "kr": "کر", "rha": "رہا", "rhi": "رہی",
    "rhy": "رہے", "gya": "گیا", "gyi": "گئی", "sb": "سب", "mjhe": "مجھے",
    "mujhy": "مجھے", "ap": "آپ", "kb": "کب", "jb": "جب", "tb": "تب",
    "phr": "پھر", "yar": "یار", "yr": "یار", "shukria": "شکریہ", "bohut": "بہت",
}
for roman, urdu in SUPPLEMENT.items():
    mapping.setdefault(roman, urdu)

template = (ROOT / "template.html").read_text(encoding="utf-8")
page = template.replace("__ROMAN_DICT__", json.dumps(mapping, ensure_ascii=False))
(ROOT / "index.html").write_text(page, encoding="utf-8")
print(f"index.html written, {len(mapping)} roman words embedded, {len(page)} bytes")
