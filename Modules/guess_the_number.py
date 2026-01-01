import random
import time

print("""
=================================
***** GUESS THE NUMBER *****
==================================
Please enter a number between 1 to 100""")

num = random.randint(1, 100)
guess = None
num_guess = 0

name = input("Enter your name: ")
print(f"Welcome {name}! Let's start the game. I am hoping a number between 1 to 100.")

while num_guess < 8:
    try:
        guess = int(input("Enter your guess: "))
        

        num_guess += 1
        guess_left = 8 - num_guess
        print("Checking...")
        time.sleep(1)

        if guess < num:
            print(f"Your guess {guess} is too low. You have {guess_left} guesses left.")
        elif( guess > num):
            print(f"Your guess {guess} is too high. You have {guess_left} guesses left.")
        elif( guess == num):
            print(f"Congratulations {name}! You guessed the number {num} in {num_guess} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number between 1 to 100.")
    else:
        if( guess <1 or guess >100):
            print("Out of bounds! Please enter a number between 1 to 100.")

if(guess == num):
    print("You won the game!")
else:
    print(f"Sorry {name}, you've used all your attempts. The number was {num}. Better luck next time!")
        
