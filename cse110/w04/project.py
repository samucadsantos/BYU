"""
    Author: Samuel dos Santos
    Purpose: A word guessing game where the user has to guess a secret word chosen randomly from a list of options. 
        The user receives hints after each guess, indicating which letters are correct and in the correct position (uppercase), which letters are correct but in the wrong position (lowercase), 
        and which letters are not in the secret word at all (underscore).
        The game continues until the user guesses the secret word correctly, at which point the total number of guesses is displayed.
    Additional: The secret words are all names of biblical figures, adding an educational element to the game.
        I also used the _ to avoid an unused variable in the initial hint. I've seen that in the other programas I work with and thought it would be a good opportunity to practice it.
"""

import random

secret_options = ["Adam", "Eve", "Noah", "Abraham", "Moses", "David", "Solomon", "Elijah", "Isaiah", "Jeremiah", "Daniel", "Jonah", "Peter", "Paul", "Mary", "Joseph"]
current_secret = random.choice(secret_options)

guess = ""
total_guesses = 0

print("---- Welcome to the Biblical names guessing game! ----")

def create_initial_hint(secret_word):
    initial_hint = "Your hint is: "
    
    for _ in secret_word:
        initial_hint += "_ "        
        
    print(initial_hint)

create_initial_hint(current_secret)

while guess.lower() != current_secret.lower():
    guess = input("What is your guess? ")
    total_guesses += 1
    
    # check if the length of the guess is the same as the secret word
    if len(guess) != len(current_secret):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue
    
    if guess.lower() == current_secret.lower():
        break
    
    # check current guess word by word against the secret word and update the hint
    hint = "Your hint is: "
    for i in range(len(current_secret)):
        if guess[i].lower() == current_secret[i].lower():
            hint += guess[i].upper() + " "
        elif guess[i].lower() in current_secret.lower():
            hint += guess[i].lower() + " "
        else:
            hint += "_ "
    
    print(hint)
    print()

print("Congratulations! You guessed it!")
print(f"It took you {total_guesses} guesses.")
