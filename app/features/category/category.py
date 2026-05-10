# import necessary modules and functions
import random
import app.features.flashcards.flashcards as Flashcard

# Function to display category menu
# User selects a category to pratice specific categories
def category_menu():
    print("\n=== Categories ===")
    print("1. Object")
    print("2. Education")
    print("3. Place")
    print("4. Greetings")
    print("5. Relationships")
    print("6. Liberty")
    print("7. Back to Main Menu")

    # Get user input for category choice
    choice = input("\nChoose category: ")

    # map user choice to category names
    category_map = {
        "1": "object",
        "2": "education",
        "3": "place",
        "4": "greeting",
        "5": "relationship",
        "6": "liberty"
    }

    # Easy exit option to return to main menu
    if choice == "7":
        return

    # Get category name from map based on user choice
    category = category_map.get(choice)

    # If valid category is selected, start flashcard session for that category
    if category:
        from app.features.flashcards.flashcards import Flashcard
        session = Flashcard(category)
        session.start()