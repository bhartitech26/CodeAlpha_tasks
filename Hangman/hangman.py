import random

# List of predefined words
words = ["python", "apple", "computer", "coding", "school"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("=== Welcome to Hangman ===")

while incorrect_guesses < max_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining guesses:", max_guesses - incorrect_guesses)

if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The word was:", word)