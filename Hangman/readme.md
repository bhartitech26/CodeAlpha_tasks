# Hangman Game 🎮

## Project Description

This is a simple text-based Hangman Game developed in Python. The player has to guess a randomly selected word one letter at a time. The game ends when the player successfully guesses the word or uses all available attempts.

## Features

* Random word selection from a predefined list.
* User-friendly console interface.
* Tracks correct and incorrect guesses.
* Maximum of 6 incorrect attempts allowed.
* Displays the current progress of the guessed word.
* Prevents duplicate letter entries.

## Technologies Used

* Python 3
* Random Module

## Concepts Used

* Variables
* Lists
* Strings
* Conditional Statements (`if-else`)
* Loops (`while`)
* Functions (optional enhancement)
* Random Module

## How to Run

1. Install Python 3 on your system.
2. Save the source code as `hangman.py`.
3. Open Terminal or Command Prompt.
4. Navigate to the project folder.
5. Run the following command:

```bash
python hangman.py
```

## Game Rules

1. The computer selects a random word.
2. The player guesses one letter at a time.
3. If the guessed letter is correct, it is revealed in the word.
4. If the guessed letter is incorrect, one attempt is deducted.
5. The player gets a maximum of 6 wrong attempts.
6. The game ends when the word is guessed or attempts run out.

## Sample Output

```
=== Welcome to Hangman ===

Word: _ _ _ _ _ _

Enter a letter: p
Correct guess!

Word: p _ _ _ _ _

Enter a letter: y
Correct guess!

Word: p y _ _ _ _

...
```

## Project Structure

```
Hangman-Game/
│
├── hangman.py
└── README.md
```

## Future Improvements

* Add difficulty levels.
* Load words from a file.
* Add score tracking.
* Create a graphical user interface (GUI).

## Author

Internship Project Submission

Developed using Python.
