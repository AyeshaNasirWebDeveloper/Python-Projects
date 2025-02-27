import random

def game():
    print("Welcome to Rock, Paper, Scissors! 🎮")
    print("Rules:")
    print("1. Rock beats Scissors")
    print("2. Scissors beats Paper")
    print("3. Paper beats Rock")

    # Define the choices
    choices = ["rock", "paper", "scissors"]

    # Ask the user for their choice
    while True:
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie! 😐")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")

game()