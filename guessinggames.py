import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number: 
            print('Sorry, guess again. Too low')
        if guess == '10':
            print('Wow, you got it!')
        elif guess > random_number:
            print('Sorry, too high. Guess again')
    print('Correct! you have guessed the random number: {random_number}')
            

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    input('Welcome to a guessing game. Guess a number between 1 and 10 and see how long it takes me to get the answer:')

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C): ')
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1


    print(f'Woo! I guessed your number, {guess}, correctly! ')

computer_guess(10)