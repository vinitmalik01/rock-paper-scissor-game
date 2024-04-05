import random


# Unbiased game
def game():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Make your choice (rock/paper/scissors): ").lower()
        if user_choice in choices:
            computer_choice = random.choice(choices)
            print("Computer chose:", computer_choice)
            if user_choice == computer_choice:
                print("It's a tie! Try again.")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print("Congratulations! You won!")
                break
            else:
                print("You lost! Try again.")
        else:
            print("Invalid choice. Please choose again.")

# game()


# Biased game
def game2():
    while True:
        input1=input('Enter yoru choice (rock,paper,scissors): ')
        
        if input1 in ["rock","paper","scissors"]:
            if input1=="rock":
                cc='paper'
            elif input1 =="scissors":
                cc='rock'
            elif input1=="paper":
                cc="scissor"
            print('computer chose',cc)
            if input1 == cc:
                print("It's a tie! Try again.")
                
            else:
                print("You lost! Try again.")
        else:
            print('u choose wrong options try again')
choice = input('Enter Choice want to Play Biased or Unbiased game : ')
if choice.lower== 'biased':
    game2()
elif choice.lower== 'unbiased':
    game()
else:
    print('enter valid choice')
# game2()
