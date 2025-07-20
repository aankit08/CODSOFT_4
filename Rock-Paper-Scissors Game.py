import random


def get_user_choice():
##Ask the user to choose rock, paper, or scissors.   
    while True:
        user_input = input("Choose your weapon (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
##Generates a random choice for the computer
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
##Determines the winner of that round. 
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
##Manages the Rock-Paper-Scissors game loop.
    user_score = 0
    computer_score = 0
    round_count = 0

    print("--- Welcome to Rock-Paper-Scissors! ---")
    print("---------------------------------------")

    while True:
        round_count += 1
        print(f"\n--- Round {round_count} ---")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == 'no':
            break

    print("\n--- Game Over! ---")
    print(f"Final Score: You {user_score} - Computer {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Better luck next time! The computer won the overall game.")
    else:
        print("It's an overall tie!")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
