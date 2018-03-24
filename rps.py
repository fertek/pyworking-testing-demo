# rps.py

import random


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']


def random_play():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_game_result(human, computer):
    """Returns str with human, computer or tie"""
    if human == computer:
        return 'tie'
    elif (human == 'rock' and computer == 'scissors') or (human == 'paper' and computer == 'rock') or (human == 'scissors' and computer == 'paper'):
        return 'human'
    else:
        return 'computer'


def main(input_func=input): # tohle není pořádná funkce, ale procedura!
    human = ''
    while not is_valid_play(human):
        human = input_func('rock, paper or scissors? ')

    computer = random_play()

    print(computer)

    result = determine_game_result(human, computer)

    if result == 'tie':
        print('it\'s a tie!')
    else:
        print(result, 'wins!')


if __name__ == '__main__': # tj. spustili jsme soubor my
    main()