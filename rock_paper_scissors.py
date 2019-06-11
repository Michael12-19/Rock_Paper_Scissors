import random

choices = ['rock', 'paper', 'scissors']

'rock' > 'scissors'
'rock' < 'paper'
'rock' == 'rock'
'paper' > 'rock'
'paper' < 'scissors'
'paper' == 'paper'
'scissors' < 'rock'
'scissors' > 'paper'
'scissors' == 'scissors'

human_choice = input('Pick rock, paper, or scissors:')
computer_choice = random.choice(choices)

if computer_choice > human_choice:
    print('computer picks', computer_choice)
    print('computer wins')

elif computer_choice < human_choice:
    print('computer picks', computer_choice)
    print('human wins')

else:
    print('computer picks', computer_choice)
    print('Its an tie')
