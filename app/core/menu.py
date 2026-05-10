from app.features.flashcards.flashcards import Flashcard


def main_menu():
    while True:
        print("\n=== Brazilian Portuguese CLI ===")
        print("1. Flash Cards")
        print("2. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            session = Flashcard()
            session.start_flashcards()

        elif choice == "2":
            break