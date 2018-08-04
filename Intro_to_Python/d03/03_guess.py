from random import * 
random_word = ['Water', 'Juice', 'Tiger', 'Lion', 'Years']
x = sample(random_word, 1)
print(x[0][0])


def guess():
    remaining = 10
    while remaining > 0:
        word = input('Guess: ')
        if len(word) < 1:
            print('You wasted a guess =P')
            remaining -= 1
        elif len(x[0]) != len(word):
            print('0,1,2,3,4 thats how we count to five')
            remaining -= 1
        elif word[0] != x[0][0]:
            print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        elif word == x[0]:
            print('Good job! You are one with the source')
            return
        elif word != x[0]:
            remaining -= 1
            print('You have {} guesses left'.format(remaining))
               
guess()
