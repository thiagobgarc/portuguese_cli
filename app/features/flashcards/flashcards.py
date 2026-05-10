import random
from app.services.services import load_words

class Flashcard:
    def __init__(self):
        self.words = load_words()
        self.score = 0
        self.total_questions = 0

    
    def get_random_word(self):
        return random.choice(self.words)
    
    def display_card(self, card):
        print("\n=== FLASH CARD ===")
        print(f"Portuguese: {card['portuguese']}")

        input("\nPress Enter to see answer...")

        print(f"English: {card['english']}")
    
    def start_flashcards(self):
        while True:
            card = self.get_random_word()
            self.display_card(card)
            self.total_questions += 1
            again = input("\nContinue? (y/n): ")
            if again.lower() != 'y':
                break
            else:
                return self.score, self.total_questions