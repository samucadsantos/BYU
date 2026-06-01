import random

def start_game() -> tuple[int, int, int]:
    print("--- Welcome to the Guessing Game! ---")
    
    secret_number = random.randint(1, 100)
    user_guess = int(input("Guess a number between 1 and 100: "))
    guesses = 1
    
    return secret_number, user_guess, guesses

def validate_guess(user_guess, secret_number) -> bool:
    if user_guess < 1 or user_guess > 100:
        print("Please enter a number between 1 and 100.")
        return False
    elif user_guess < secret_number:
        print("Higher")
        return False
    elif user_guess > secret_number:
        print("Lower")
        return False
    else:        
        print("You guessed it!")
        return True
    
def ask_new_guess(current_guesses) -> tuple[int, int]:
    new_guess = int(input("Guess a number between 1 and 100: "))
    updated_guesses = current_guesses + 1
    
    return new_guess, updated_guesses

def end_game(total_guesses):
    print("\n===============================")
    print("Thank you for playing. Goodbye.")
    print("===============================\n")

keep_playing = "yes"
secret_number, user_guess, guesses = start_game()
        
while keep_playing.lower() == "yes":
    while not validate_guess(user_guess, secret_number):
        user_guess, guesses = ask_new_guess(guesses)
        
    print(f"It took you {guesses} guesses.")
        
    keep_playing = input("Do you want to play again? (yes/no): ")
    
    if keep_playing.lower() == "yes":
        secret_number, user_guess, guesses = start_game()
        
end_game(guesses)