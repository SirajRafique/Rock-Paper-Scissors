import random

user_score = 0
comp_score = 0

"""A loop to play again and again"""

while True:
    user_action = str(input("Enter your choice (rock, paper or scissors): "))

    """Check if user choice is valid or not"""
    while user_action != "rock" and user_action != "paper" \
            and user_action != "scissors":
        user_action = str(input("Invalid choice, please enter again: "))

    """Assign random choice to computer"""
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    """Print computer and user choices"""

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    """Determine who won and calculate score, 1 point for a win."""
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_score = user_score + 1
        else:
            print("Paper covers rock! You lose.")
            comp_score = comp_score + 1

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_score = user_score + 1
        else:
            print("Scissors cuts paper! You lose.")
            comp_score = comp_score + 1

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_score = user_score + 1
        else:
            print("Rock smashes scissors! You lose.")
            comp_score = comp_score + 1

    """Display the score """
    print("User =", user_score)
    print("Computer =", comp_score)

    """Play again or stop"""
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
