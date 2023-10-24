import random
import time
def get_random_number(min, max):
    return random.randint(min, max)

def GuessNumber():
    number = get_random_number(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    guess = 0
    while guess != number:
        guess = int(input("What is your guess? "))
        if guess == number:
            print("You got it!")
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
def main ():
    GuessNumber()
    # print("You guessed the number in", guesses, "guesses!")
if __name__ == "__main__": 
    main()