import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = 0
    while feedback != 'c':
        if low != high :
            guess = random.randint(low , high)
        else:
            guess = low
        feedback = input(f"Is {guess} is Too high(H), Too Low(L), or corrdctly(c) ?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay, Computer Guessed the number {guess} Correctly !")

computer_guess(10)