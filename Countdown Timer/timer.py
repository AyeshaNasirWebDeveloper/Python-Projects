import time

def countdown():
    print("Welcome to the Countdown Timer! ⏳")
    
    # Ask the user for minutes and seconds
    while True:
        try:
            mins = int(input("Enter minutes: "))
            secs = int(input("Enter seconds: "))
            if mins >= 0 and secs >= 0:
                break
            else:
                print("Please enter non-negative numbers.")
        except ValueError:
            print("Invalid input! Please enter numbers.")

    total_seconds = mins * 60 + secs  # Convert to total seconds
    print("\nCountdown started!")

    # Countdown logic
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)  # Convert seconds to minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
        print(timer, end="\r")  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        total_seconds -= 1  # Decrease the time by 1 second

    print("\nTime's up! 🎉")

countdown()