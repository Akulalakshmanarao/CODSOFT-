# Rock-Paper-Scissors Game
import random

print("1 Welcome to Rock, Paper, Scissors!")
print("Instructions:")
print("1. Type rock, paper, or scissors")
print("2. Rock beats Scissor")
print("3. Scissor beats Paper")
print("4. Paper beats Rock")
print("-" * 35)

user_score = 0
computer_score = 0

while True:
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print(" Inalid input! Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(" It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print(" You win this round!")
        user_score += 1
    else:
        print(" You lose this round!")
        computer_score += 1

    print("Current Score:\n")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("hanks for playing!\n")
        print(f"Final Score → You: {user_score} | Computer: {computer_score}")
        break