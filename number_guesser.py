import random

quit_confirm = False
quit_input = 'placeholder'

blank = ''

while True:
    print(blank)
    print('input "quit" on any input to end program')
    print(blank)
    print('Enter 2 numbers to define a range')
    print(blank)

    number_1 = input('Enter first number:  ')

    if number_1 == 'quit':
        break
    else:
        pass

    try:
        int(number_1)
    except ValueError:
        print(f'"{number_1}" is an invalid entry, must type a number')
        continue
    number_1 = int(number_1)

    number_2 = input('Enter second number:  ')
    
    if number_2 == 'quit':
        break
    else:
        pass
    
    try:
        int(number_2)
    except ValueError:
        print(f'"{number_2}" is an invalid entry, must type a number')
        continue
    number_2 = int(number_2)

    def create_list(placeholder_1, placeholder_2):
        if placeholder_1 == placeholder_2:
            return placeholder_1

        else:

            res = []

            while placeholder_1 < placeholder_2 + 1:
                res.append(placeholder_1)
                placeholder_1 += 1
            return res 

    random_number = random.choice(create_list(number_1, number_2))


    while True:
        guess = input('What number do you want to guess:  ')

        if guess == 'quit':
            break
        else:
            pass

        try:
            int(guess)
        except ValueError:
            print(f'{guess} is an invalid input, must be number')
            continue
        guess = int(guess)
        if guess > random_number:
            print(blank)
            print('your guess is greater than the random number')
            print(blank)
        elif guess < random_number:
            print(blank)
            print('your guess is less than the random number')
            print(blank)
        elif guess == random_number:
            print(blank)
            print('--**you guessed the correct number**--')
            break
        else:
            print('unexpected error')
            break
        