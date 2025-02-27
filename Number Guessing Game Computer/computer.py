import random

def guessing_game():
    print("Welcome to the Number Guessing Game! 🎮")
    print("\n Choose your difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (3 attempts)")
    
    # Ask user to choose difficulty
    while True:
        try:
            level = int(input("\n Enter your choice (1, 2, or 3): "))
            if level in [1, 2, 3]:
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Set attempts based on difficulty
    if level == 1:
        max_attempts = 10
    elif level == 2:
        max_attempts = 5
    else:
        max_attempts = 3

    print(f"\nI'm thinking of a number between 1 and 10. Can you guess it in {max_attempts} attempts?")

    # Generate a random number
    secret_number = random.randint(1, 10)
    attempts = 0

    while attempts < max_attempts:
        print(f"\nYou have {max_attempts - attempts} attempts left.")
        
        # Ask the user to guess the number
        try:
            guess = int(input("Enter your guess (between 1 and 10): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Check if the guess is correct
        if guess == secret_number:
            print(f"\n 🎉 Congratulations! You guessed the number in {attempts + 1} attempts!")
            break
        elif guess < secret_number:
            print("\n Too low! Try a higher number.")
        else:
            print("\n Too high! Try a lower number.")

        attempts += 1

    else:
        print(f"\n Game over! 😢 The number was {secret_number}.")

guessing_game()