def category_menu(self, category):
        print("\n=== Categories ===")
        print("1. Animals")
        print("2. Verbs")
        print("3. Food")

        choice = input("\nChoose a category: ")

        category_map = {
            "1": "animals",
            "2": "verbs",
            "3": "food"
        }

        category = category_map.get(random.choice(list(category_map.keys())))

        if category:
            session = FlashcardSession(category)
            session.start()

        else:
            print("Invalid category.")