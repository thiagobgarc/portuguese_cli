import json

def load_words():
    with open('data/vocabulary/vocabulary.json', 'r', encoding='utf-8') as file:
        words = json.load(file)
    return words