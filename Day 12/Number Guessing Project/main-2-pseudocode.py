import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5



def check_user_guess(correct_number, attempts_remaining, user_guess):
    '''Compares user guess with correct number and return attempts remaining.''' 
    if user_guess == correct_number:
        print(f"You win! You guessed the corrected number: {correct_number}.")
        return -1
    elif user_guess > correct_number:
        print("Your guess is too high!")
        attempts_remaining -= 1
    else:
        print("Your guess is too low!")
        attempts_remaining -= 1
    
    return attempts_remaining
    
        



def gameplay():
    '''The actual game.'''
    game_over = False
    start_game = input("Welcome to The Number Guessing Game. Do you want to play? "
                        "Press 'y' for yes, or 'n' for no.\n").lower()
    if start_game == 'n':
        return
    elif start_game != 'y':
        print("Please follow instructions!")
    else:
        while game_over == False:
            correct_number = random.randint(0,100)
            total_attempts = set_difficulty()
            user_guess = int(input("Enter your guess:\n"))
            if attempts_remaining == 0:
                game_over = True
                print(f"You lose! You are out of attempts. The corrected number was: {correct_number}.")
                continue
            attempts_remaining = check_user_guess(correct_number, total_attempts, user_guess)
            if attempts_remaining == -1:
                game_over = True
            




def set_difficulty():
    '''Function to set gameplay difficulty. Returns total attempts remaining'''
    while True:
        difficulty = input("Select difficulty: 'e' for easy, or 'h' for hard.\n").lower()
        if difficulty == 'e':
            return EASY_ATTEMPTS
        elif difficulty == 'h':
            return HARD_ATTEMPTS
        else:
            print("Please follow instructions!")