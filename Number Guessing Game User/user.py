def user_guessing():
    print("Welcome to the Number Guessing Game! 🎮")
    print("\n This time, YOU choose the number, and I'll guess it!")
    
    # Ask the user to choose a number between 1 and 10
    while True:
        try:
            secret_number = int(input("\n Enter a number between 1 and 10 (don't tell me!): "))
            if 1 <= secret_number <= 10:
                break
            else:
                print("\n Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\n Great! Now I'll try to guess your number. Let's begin!")

    # Initialize variables for binary search
    low = 1
    high = 10
    attempts = 0
    max_attempts = 5 # Set the maximum number of attempts

    while low <= high:
        attempts += 1
        guess = (low + high) // 2  # Computer guesses the middle number
        print(f"\nAttempt {attempts}: Is your number {guess}?")

        # Ask the user if the guess is correct
        response = input("\n Enter 'H' if my guess is too high, 'L' if too low, or 'C' if correct: ").upper()

        if response == 'C':
            print(f"\n 🎉 Yay! I guessed your number in {attempts} attempts!")
            break
        elif response == 'L':
            low = guess + 1  # Adjust the lower bound
        elif response == 'H':
            high = guess - 1  # Adjust the upper bound
        else:
            print("\n Invalid input! Please enter 'H', 'L', or 'C'.")

    else:
        if attempts >= max_attempts:
            print(f"\n😢 I couldn't guess your number in {max_attempts} attempts. You win!")
        else:
          print("\nHmm, something went wrong. Did you change your number? 😢")


user_guessing()