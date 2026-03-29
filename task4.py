import random

# Welcome message
print("===================================")
print("   ROCK - PAPER - SCISSORS GAME   ")
print("===================================")
print("Instructions:")
print("Type 'rock', 'paper', or 'scissors' to play.\n")

# Initialize scores
user_score = 0
computer_score = 0

# Choices list
choices = ["rock", "paper", "scissors"]

# Game loop
while True:
    # User Input
    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("❌ Invalid input! Please enter rock, paper, or scissors.")
        continue

    # Computer Selection
    computer_choice = random.choice(choices)

    # Display Choices
    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game Logic
    if user_choice == computer_choice:
        print("🤝 It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You win!")
        user_score += 1

    else:
        print("🤖 Computer wins!")
        computer_score += 1

    # Display Score
    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Score:")
        print("You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing! 👋")
        break