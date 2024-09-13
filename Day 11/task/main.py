import random

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

	print(f"Computer Hand: {hand_computer[0]}")	
	print(f"Player Hand: {hand_player}")
 
	while game_over == False:
		

	
def calculate_score(hands):
    
	sum_score = sum(hands)
	return sum_score	
	
	


def start_game():
### Prompt user and call play_game() if user input == 'y'

	player_prompt = input("Do you want to play Back Jack against " \
    	"the computer? Type 'y' for Yes, or 'n' for No.\n").lower()
	if player_prompt != "y":
		return
	play_game()


start_game()
