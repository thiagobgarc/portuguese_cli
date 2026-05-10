from app.features.flashcards.flashcards import Flashcard
from app.features.word_of_the_day.word_of_the_day import WordOfTheDay
from app.services.services import load_words
from app.features.category.category import category_menu

def main_menu():
    while True:
        print("\n=== Brazilian Portuguese CLI ===")
        print("1. Flash Cards")
        print("2. Word of the Day")
        print("3. Categories")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            session = Flashcard()
            session.start_flashcards()

        elif choice == "2":
            session = WordOfTheDay(load_words())
            session.display_word()

        elif choice == "3":
            category_menu()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
