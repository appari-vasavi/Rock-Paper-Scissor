import random  # Importing random module for computer's move

# Function to get user input
def get_user_choice():
    # Ask user for their choice
    choice = input("Enter Rock, Paper or Scissors: ").lower()
    
    # Validate input
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input!")
        choice = input("Please enter Rock, Paper or Scissors: ").lower()
        
    return choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user, computer):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if user == computer:
        return "It's a tie!"
    
    
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"


def play():
    while True:
        
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()
        
        
        result = determine_winner(user_choice, comp_choice)
        print(result)

        
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break


play()
