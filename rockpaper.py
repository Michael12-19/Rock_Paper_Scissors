import random

choices = ['rock', 'paper', 'scissors']

human_score = 0
computer_score = 0

while human_score or computer_score < 2:
    if human_score == 3:
        print('You Won', human_score)
        break

    if computer_score == 3:
        print('Computer Won', computer_score)
        break

    computer_choice = random.choice(choices)
    human_choice = input('Pick rock, paper, or scissors:')

    while human_choice != 'rock' and human_choice != 'paper' and human_choice != 'scissors':
        human_choice = input(
            'You did not choose rock, paper or scisscors. Choose again.:')

    if human_choice == 'rock' and computer_choice == 'scissors' or human_choice == 'paper' and computer_choice == 'rock' or human_choice == 'scissors' and computer_choice == 'paper':
        print('computer picked', computer_choice)
        print('you win')
        human_score = human_score + 1
        print(human_score)
        print(computer_score)

    elif computer_choice == 'rock' and human_choice == 'scisscors' or computer_choice == 'paper' and human_choice == 'rock' or computer_choice == 'scissors' and human_choice == 'paper':
        print('computer picked', computer_choice)
        print('computer won')
        computer_score = computer_score + 1
        print(human_score)
        print(computer_score)

    else:
        print('computer picked', computer_choice)
        print('Its a tie')
        print(human_score)
        print(computer_score)
