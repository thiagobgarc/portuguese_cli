# portuguese_cli

portuguese-learning-cli/
│
├── app/
│   ├── __init__.py
│   │
│   ├── core/
│   │   ├── menu.py
│   │   ├── config.py
│   │   └── app_state.py
│   │
│   ├── features/
│   │   ├── flashcards/
│   │   │   ├── flashcards.py
│   │   │   ├── spaced_repetition.py
│   │   │   └── flashcard_service.py
│   │   │
│   │   ├── quizzes/
│   │   │   ├── quiz.py
│   │   │   └── quiz_service.py
│   │   │
│   │   ├── word_of_day/
│   │   │   ├── word_of_day.py
│   │   │   └── word_service.py
│   │   │
│   │   └── progress/
│   │       ├── tracker.py
│   │       └── statistics.py
│   │
│   ├── models/
│   │   ├── word.py
│   │   ├── flashcard.py
│   │   └── user_progress.py
│   │
│   ├── services/
│   │   ├── database_service.py
│   │   ├── json_service.py
│   │   └── vocabulary_service.py
│   │
│   ├── ui/
│   │   ├── screens/
│   │   │   ├── main_menu.py
│   │   │   ├── flashcard_screen.py
│   │   │   ├── quiz_screen.py
│   │   │   └── progress_screen.py
│   │   │
│   │   ├── components/
│   │   │   ├── header.py
│   │   │   ├── footer.py
│   │   │   └── cards.py
│   │   │
│   │   └── theme.py
│   │
│   └── utils/
│       ├── helpers.py
│       ├── validators.py
│       └── constants.py
│
├── data/
│   ├── vocabulary/
│   │   ├── beginner.json
│   │   ├── intermediate.json
│   │   └── advanced.json
│   │
│   ├── user/
│   │   └── progress.db
│   │
│   └── config/
│       └── settings.json
│
├── tests/
│   ├── test_flashcards.py
│   ├── test_quizzes.py
│   └── test_services.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py
