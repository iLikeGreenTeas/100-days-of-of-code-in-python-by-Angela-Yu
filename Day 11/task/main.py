import random
import time

def calculate_score(hands):
	if sum(hands) == 21 and len(hands) == 2:
		return 0  
	elif 11 in hands and sum(hands) > 21:
		hands.remove(11)
		hands.append(1)
	elif not(11 in hands) and sum(hands) > 21:
		return 1
	return sum(hands)


def player_hit_or_stay():
	while True: 
		choice = str(input("Type 'h' to HIT, or 's' to STAY.\n")).lower()
		if choice == 'h' or choice == 's':
			return choice
		else:
			print("Please follow the instructions.\n")

def check_winner(player_score, comp_score): 
	if player_score > 21:
		print("Player busts! Dealer wins!")
	elif comp_score > 21:
		print("Dealer busts! Player wins!")
	elif player_score == comp_score:
		print("It's a draw!")
	elif player_score > comp_score:
		print("Player wins!")
	else:
		print("Dealer wins!") 
	return True   

def play_game():
	"""Set up the game. Create lists to represent each player's
	hand and draw 2 cards at random in turns."""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	hand_computer = []
	hand_player = []
	player_score = 0
	comp_score = 0
	game_over = False

	for _ in range(2):
		hand_computer.append(random.choice(cards))
		hand_player.append(random.choice(cards))

	hit_or_stay_choice = ""
	while game_over == False:

		calculate_score_computer = calculate_score(hand_computer)
		calculate_score_player = calculate_score(hand_player)
		if calculate_score_computer == 0:
			game_over = True
			print("GAME OVER!")
			print(f"Computer Hand: {hand_computer}")	
			print(f"Player Hand: {hand_player}")
			continue
		elif calculate_score_computer == 1:
			game_over = True
			print("GAME OVER!")
			print(f"Computer Hand: {hand_computer}")	
			print(f"Player Hand: {hand_player}")
			continue
		if calculate_score_player == 0:
			game_over = True
			print("GAME OVER!")
			print(f"Computer Hand: {hand_computer}")	
			print(f"Player Hand: {hand_player}")
			continue
		elif calculate_score_player == 1:
			game_over = True
			print("GAME OVER!")
			print(f"Computer Hand: {hand_computer}")	
			print(f"Player Hand: {hand_player}")
			continue

		print(f"Computer Hand: {hand_computer[0]}")	
		print(f"Player Hand: {hand_player}")
		hit_or_stay_choice = player_hit_or_stay()
		if hit_or_stay_choice == 'h':
			hand_player.append(random.choice(cards))
			continue
		elif hit_or_stay_choice == 's':

			while calculate_score(hand_computer) < 17 and calculate_score(hand_computer) > 1:
				hand_computer.append(random.choice(cards))
				calculate_score_computer = calculate_score(hand_computer)
				print(f"Computer Hand: {hand_computer}")
				time.sleep(2)

			if calculate_score_computer	> 16 and calculate_score_computer != 1:
				game_over = True
				print("GAME OVER!")
				print(f"Computer Hand: {hand_computer}")	
				print(f"Player Hand: {hand_player}")

	player_score = sum(hand_player)
	comp_score = sum(hand_computer)
	check_winner(player_score, comp_score)

def start_game():
### Prompt user and call play_game() if user input == 'y'

	player_prompt = input("Do you want to play Back Jack against " \
		"the computer? Type 'y' for Yes, or 'n' for No.\n").lower()
	if player_prompt != "y":
		return
	play_game()

start_game()
