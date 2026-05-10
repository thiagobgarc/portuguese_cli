# 🇧🇷 Brazilian Portuguese Learning CLI

A terminal-based language learning application for studying Brazilian Portuguese (Brazilian Portuguese language). The goal of this project is to help users build vocabulary and reinforce learning through active recall techniques like flashcards, quizzes, and a word-of-the-day system.

The project is built in Python using a modular, scalable architecture designed for clarity, extensibility, and long-term learning features.

### ✨ Features
### 📅 Word of the Day — Learn a new Brazilian Portuguese word daily with meaning and example usage
### 🧠 Flashcards System — Active recall-based vocabulary practice
### ❓ Quiz Mode — Multiple-choice questions for reinforcement
### 📊 Progress Tracking — Track accuracy, streaks, and weak words
### 💾 Persistent Storage — Saves vocabulary and user progress locally (JSON / optional SQLite)
### 🧩 Modular Design — Easy to extend with new learning features (verbs, conjugation, audio, etc.)
## 🧱 Project Structure
```text
portuguese_cli/
│
├── main.py
│
├── app/
│   ├── core/
│   │   ├── menu.py
│   │   ├── config.py
│   │
│   ├── features/
│   │   ├── flashcards/
│   │   │   ├── flashcards.py
│   │   │   └── spaced_repetition.py
│   │   │
│   │   ├── quizzes/
│   │   │   └── quiz.py
│   │   │
│   │   ├── word_of_day/
│   │   │   └── word_of_day.py
│   │   │
│   │   └── progress/
│   │       └── tracker.py
│   │
│   ├── models/
│   │   ├── word.py
│   │   ├── flashcard.py
│   │   └── progress.py
│   │
│   ├── services/
│   │   ├── storage_service.py
│   │   └── vocabulary_service.py
│   │
│   ├── ui/
│   │   ├── screens/
│   │   │   ├── main_menu.py
│   │   │   ├── flashcards_screen.py
│   │   │   ├── quiz_screen.py
│   │   │   └── progress_screen.py
│   │
│   └── utils/
│       ├── helpers.py
│       └── validators.py
│
├── data/
│   ├── vocabulary.json
│   └── progress.json
│
├── tests/
│   ├── test_flashcards.py
│   ├── test_quiz.py
│   └── test_progress.py
│
├── requirements.txt
└── README.md
```
## 🧠 Design Philosophy

This project is structured around feature isolation + clean separation of concerns:

Features handle learning logic (flashcards, quizzes, word-of-day)
Models define core data structures
Services handle storage and data management
UI layer handles terminal interaction only
Core layer manages navigation and configuration

This ensures the system is:

scalable
testable
easy to extend
cleanly separated between logic and UI
## 🚀 Future Improvements
Spaced repetition system improvements (SM-2 algorithm style)
Verb conjugation trainer (especially important in Brazilian Portuguese)
Audio pronunciation integration
Difficulty-based learning paths
User profiles + cloud sync
