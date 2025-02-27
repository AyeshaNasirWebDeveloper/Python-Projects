import random

def hangman():
    print("Welcome to Hangman! 🎮")
    print("Guess the word before the hangman is complete.")

    # List of words for the game
    words = ["python", "programming", "hangman", "challenge", "developer", "algorithm"]
    word = random.choice(words)  # Randomly select a word
    guessed_word = ["_"] * len(word)  # Display blanks for the word
    attempts = 5  # Number of attempts
    guessed_letters = []  # Store guessed letters

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Ask the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

        # Check if the word has been fully guessed
        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word: " + word)
            break

    else:
        print("\nGame over! 😢 The word was: " + word)

hangman()