import random
import include

def play_game():
	"""Set up the game. Create lists to represent each player's
	hand and draw 2 cards at random in turns."""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	hand_computer = []
	hand_player = []
	play_score = 0
	comp_score = 0

	for _ in range(2):
		hand_computer.append(random.choice(cards))
		hand_player.append(random.choice(cards))


	print(f"Computer Hand: {hand_computer[0]}")	
	print(f"Player Hand: {hand_player}")
	if check_winner(hand_computer) == 21:
		print("Computer Wins!")
		
	if check_winner(hand_player) == 21:
		print("Player Wins!")

def check_winner(hands):
	sum_score = sum(hands)
			
 #   if sum_score > 21 & 11 in hands:
	return sum_score	
	
	


def start_game():
### Prompt user and call play_game() if user input == 'y'

	player_prompt = input("Do you want to play Back Jack against " \
    	"the computer? Type 'y' for Yes, or 'n' for No.\n").lower()
	if player_prompt != "y":
		return
	play_game()


start_game()
