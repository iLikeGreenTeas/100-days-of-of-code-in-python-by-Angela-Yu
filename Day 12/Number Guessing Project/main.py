import random

def number_guessing_game():
	game_over = False
	attempts_left = 0

	while game_over == False:
		print("Welcome to the Number Guessing Game. The goal is "
        "to guess the correct number. If you select Easy, you get "
        "10 attempts. If you select Hard, you get 5. The number "
        "is between 0 and 100 inclusive.")
		
		play_game = input("Start new game? Type 'y' for Yes, "
						"or 'n' for No.").lower()
		if play_game == 'n':
			game_over = True
			continue
		
		correct_guess = random.randint(0, 100)

		difficulty_level = input("Type 'e' for Easy, "
								"or 'h' for Hard.\n").lower()
		if difficulty_level == 'e':
			attempts_left = 10
		elif difficulty_level == 'h':
			attempts_left = 5
		else:
			print("Please follow instructions.")

		while attempts_left > 0:
			user_guess = int(input("Enter your guess.\n"))

			if user_guess == correct_guess:
				print(f"You guessed the correct number: {correct_guess}! "
					"You Win!")
				break
			elif user_guess > correct_guess:
				print("Guess is too high.")
				attempts_left -= 1
			else:
				print("Guess is too low.")
				attempts_left -= 1
		
			if attempts_left == 0:
				print("You loose.")
				game_over = True      
    
number_guessing_game()