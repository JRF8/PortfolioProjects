#random number guesser
import random


def main():
    num = generate_the_number()
    auto = check_auto()
    if auto == True:
        auto_guess(1,1000,num)
    else:
        manual_guess(num)


def check_auto():
    a = input('use auto guess?')
    while True:
        if a.upper()=="YES":
            auto = True
            break
        elif a.upper()=="NO":
            auto = False
            break
        else:
            print('invalid response')
            a = input('use auto guess?')
    return auto

def generate_the_number():
    num = random.randint(1,1000)
    return num

def auto_guess(lowest,highest,num):
    #guess = random.randint(lowest, highest)
    guess = int((highest+lowest)/2)
    if guess < num:
        print('computer guessed ' + str(guess) +' which is too low')
        auto_guess(guess+1,highest,num)
    elif guess > num:
        print('computer guessed ' + str(guess) +' which is too high')
        auto_guess(lowest,guess-1,num)
    else:
        print('computer guessed ' + str(guess) +' which is correct!!')

def manual_guess(num):
    while True:
        user_input = input("guess a number:")
        try:
            guess = int(user_input)
            if guess < num:
                print('your guess is too low')
            elif guess > num:
                print('your guess is too high')
            else:
                print('you guessed correctly!!')
                break
        except ValueError:
            if user_input.upper() == "EXIT":
                break
            else:
                print('your guess is not an integer')


#----------
main()
