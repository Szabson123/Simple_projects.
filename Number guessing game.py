import random
import math

print("Enter the range in which you want to guess: ")
userlower = int(input("Lower Bound: "))
userupper = int(input("Upper Bound: "))

randomnumber = random.randint(userlower, userupper)
k = 0
c = round(math.log(userupper-userlower+1, 2))
print(f"You have a maximum of {c+1} tries")

while True:
    guess = int(input("Guess: "))
    if guess > userupper or guess < userlower:
        print("Out of range")
        continue
    if guess > randomnumber:
        print("Too high")
    elif guess < randomnumber:
        print("Too low")
    else:
        print(f"Congratulations, you've won in {k+1} guesses")
        break
    c -= 1
    if c == -1:
        print(f"You did not succeed :( correct number was {randomnumber}")
        break
    print(f"You have {c+1} tries left")
    k += 1
