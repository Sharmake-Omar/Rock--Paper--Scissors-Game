import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📄'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        # Ask the user to make a choice
        user_choice = input('ROCK, Paper, or Scissors? (r/p/s):').lower()
        if user_choice in choices:  # If choice is not valid
            return user_choice
        else:
            print('invalid choice!')  # print an error


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')  # Print choices (emojis)
    print(f'Computer choice {emojis[computer_choice]}')


def determin_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (  # Determine the winner
            (user_choice == 'ROCK' and computer_choice == 'SICCORS') or
            (user_choice == 'SICCORS' and computer_choice == 'PAPER') or
            (user_choice == 'PAPER' and computer_choice == 'ROCK')):
        print('You win')
    else:
        print('You win')


def play_game():
    while True:
        user_choice = get_user_choice()

        # Let the computer make a choice
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)  # If not
        determin_winner(user_choice, computer_choice)

        # Ask the user if they want to continue
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break  # Terminate


play_game()
