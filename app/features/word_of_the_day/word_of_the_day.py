import random

class WordOfTheDay:
    def __init__(self, words):
        self.words = words

    def get_word_of_the_day(self):
        return random.choice(self.words)
    
    def display_word(self):
        word = self.get_word_of_the_day()
        print("\n=== WORD OF THE DAY ===")
        print(f"Portuguese: {word['portuguese']}")
        print(f"English: {word['english']}")