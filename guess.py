import random
def guess():
    print('Take a guess: ')
    number = int(input())
    print('=' * 45)
    return number

def cpuNumber():
    return random.randint(1, 20)


count = 1
cpuN = cpuNumber()
print('I am thinking of a number between 1 and 20')
while True:
    n = guess()
    if n < cpuN:
        print('Your guess is too low!')
    elif n > cpuN:
        print('Your guess is too high!')
    else:
        print('Good job! You guessed my number in ' + str(count) + ' guesses.')
        break
    count += 1
