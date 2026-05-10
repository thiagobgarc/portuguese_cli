import random
import app.features.flashcards.flashcards as Flashcard

def category_menu():
    print("\n=== Categories ===")
    print("1. Object")
    print("2. Education")
    print("3. Place")
    print("4. Greetings")
    print("5. Relationships")
    print("6. Liberty")
    print("7. Back to Main Menu")

    choice = input("\nChoose category: ")

    category_map = {
        "1": "object",
        "2": "education",
        "3": "place",
        "4": "greeting",
        "5": "relationship",
        "6": "liberty"
    }

    if choice == "7":
        return

    category = category_map.get(choice)

    if category:
        from app.features.flashcards.flashcards import Flashcard
        session = Flashcard(category)
        session.start()