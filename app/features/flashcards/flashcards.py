import random
from app.services.services import load_words
from app.services.services import get_words_by_category

class Flashcard:
    def __init__(self, category=None):
        if category:
            self.words = get_words_by_category(category) 
        else:
            self.words = load_words()

        self.correct_answers = 0
        self.incorrect_answers = 0

    
    def get_random_word(self):
        return random.choice(self.words)
    
    def display_card(self, card):
        print("\n=== FLASH CARD ===")
        print(f"Portuguese: {card['portuguese']}")

        input("\nPress Enter to see answer...")

        print(f"English: {card['english']}")

        answer = input("\nDid you get it right? (y/n): ")
        if answer.lower() == 'y':
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

    def get_score(self):
        total = self.correct_answers + self.incorrect_answers

        if total == 0:
            return 0
        else:
            accuracy = (self.correct_answers / total) * 100

        print("\n=== SCORE ===")
        print(f"Correct: {self.correct_answers}")
        print(f"Incorrect: {self.incorrect_answers}")
        print(f"Accuracy: {accuracy:.2f}%")
    
    def start_flashcards(self):
        while True:
            card = self.get_random_word()
            self.display_card(card)
            again = input("\nContinue? (y/n): ")
            if again.lower() != 'y':
                break
        self.get_score()