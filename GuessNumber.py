import random

def guessNumber(Guess ,Number):
    if Guess:
        if Guess < Number:
            print("Too low")
        elif Guess > Number:
            print("Too high")
        else:
            print("You got it!")
            return True

def Gaming():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    Number = random.randint(1, 100)
    Guess = int(input("Take a guess: "))
    while 1:
        if guessNumber(Guess, Number):
            break
        Guess = int(input("Take a guess: "))
        
def main():
    Gaming()

if __name__ == "__main__": 
    main()