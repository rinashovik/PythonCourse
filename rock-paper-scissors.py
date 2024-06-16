
import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])

#computer_choice = 'scissors'
user_choice = input("Do you want rock paper or scissors?\n")
print("Computer Choice: " + computer_choice)

if computer_choice == user_choice:
        print("TIE")
elif computer_choice == 'rock' and user_choice == 'scissors':
        print("WIN")
elif computer_choice == 'rock' and user_choice == 'paper':
        print("WIN")
elif computer_choice == 'paper' and user_choice == 'paper':
        print("WIN")
elif user_choice == 'paper' and computer_choice == 'scissors':
        print(" You Loose Computer Win")
