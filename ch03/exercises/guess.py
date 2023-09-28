import random

x = random.randrange(1,11)

for i in range(3):
    guess =  int(input("Try to Guess the random number"))
    if x < guess:
        print("TOO LOW")
    else : 
        if x > guess:
            print("TOO HIGH")
        else :
            print("Your Guess Was Correct!")

