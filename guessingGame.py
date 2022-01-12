import random

num = random.randint(0, 10)
num_guess = 5

print("Number Guessing Game")
print("Guess a Number between 1 and 10")

while(num_guess > 0):
    guess1 = int(input("Enter your guess "))

    if guess1 == num:
        print("Congradulations, you win ")
    elif guess1 > num:
        print("You have guessed too high, guess lower than ", guess1)
    elif guess1 < num:
        print("You have guessed too low, guess higher than ", guess1)
    else:
        print("Nope guess again")
    num_guess -= 1

if num_guess == 0:
    print("You Lose")
    print("The number was ", num)

