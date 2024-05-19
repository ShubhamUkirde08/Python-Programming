import random

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'paper') or \
         (user_choice == 'scissors' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
print('*'*30)

def play():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        print('*'*30)
        while user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)

        result =winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
            
        elif result == "You lose!":
            computer_score += 1
            
        print('*'*30)
        print("Your score:", user_score)
        
        print("Computer's score:", computer_score)
        print('*'*30)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

play()
