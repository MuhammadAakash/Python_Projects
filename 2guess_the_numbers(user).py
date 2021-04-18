import random

def guess(x):

    random_number = random.randint(1 , x)
    guess = 0
    while guess != random_number :
        guess = int(input(f"Guess the number between 1 and {x} :"))
        if guess < random_number :
            print(f"Sorry, guess Again. Too Low !")
        elif guess > random_number :
            print(f"Sorry, guess Again. Too High !")
    
    print(f"Yay, Congrats You guessed the number {random_number} correctly !")

guess(10) 