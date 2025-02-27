import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_numbers else ""
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?" if use_special_chars else ""

    # Combine all character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        print("Error: At least one character set must be selected.")
        return None

    # Generate the password
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator! 🔐")
    
    # Ask the user for password length
    while True:
        try:
            length = int(input("Enter the length of the password (default is 12): ") or 12)
            if length > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Ask the user for character set preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

    if password:
        print("\nYour generated password is:")
        print(password)

main()