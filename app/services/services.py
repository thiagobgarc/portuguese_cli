import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "vocabulary" / "vocabulary.json"


def load_words():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_words_by_category(category):
    words = load_words()

    return [
        word for word in words
        if word.get("category", "").lower() == category.lower()
    ]