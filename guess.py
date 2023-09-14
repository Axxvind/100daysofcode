import random
n=random.randint(0,9)
i=1

while i<=3:
    guess=int(input("Guess: "))

    if guess==n:
        print("You win")
        break
    else :
        print("You loose")
        i+=1
print("correct ans:",n)        