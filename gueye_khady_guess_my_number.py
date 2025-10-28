# Creator: Khady Gueye

"""
This program chooses a random number 1-100 and the user has 10 trys to guess what that number is.
"""

print ("I have generated random number between 1 and 100. You will have 10 attempts to guess that number.")

# Import random for the random number
import random

random_number = random.randint(1, 100)
attempts = 10

# Loop for attempts
for attempt in range(10):
    #print(f"Guess {attempt+1}: ")
    guess = int(input(f"Guess {attempt+1}:"))
    if guess < random_number:
        print("Your guess is less than my random number. Try Again.")
    elif guess > random_number:
        print("Your guess is greater than my random number. Try Again.")
    elif guess == random_number:
        print("Your correctly guessed my random number!")
# Let the user know they are out of attempts    
else:
    print("Out of attempts!")