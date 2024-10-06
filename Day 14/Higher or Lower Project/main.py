def gameplay():
    import art
    print(art.logo)
    score = 0
    itemA = select_item()
    game_over = False
    
    while game_over == False:
        print(format_comparisons(itemA, "A"))
        print(art.vs)
        itemB = select_item()
        print(format_comparisons(itemB, "B"))
        user_selection = user_response()
        user_outcome = check_winner(itemA, itemB, user_selection)
        print("\n" * 20)
        if user_outcome == 0:
            print(f"Sorry, that's wonrg. Final score: {score}")
            game_over = True
        elif user_outcome == 1:
            print(art.logo)
            score += 1
            print(f"You're right! Current score: {score}")
            itemA = itemB
        else:
            print(art.logo)
            print(f"Oops, computer' mistake for the same elements! Current score: {score}")
            itemA = itemB
        
def user_response():
    #gets user reply and ensures it meets criteria options: ["a", "A", "b", "B"] 
    user_acceptable_responses = ['A', 'B']
    while True:
        user_selection = input("Who has more follower? Item 'A' or 'B': ").upper()
        if user_selection in user_acceptable_responses:
            return user_selection
        else:
            print("Invalid response. Try again.")

        
def check_winner(itemA, itemB, user_selection):
    #compares subscriber count between itemA and itemB. return 1 is uer_selection is correct and 0 if incorrect
    if itemA[1] > itemB[1]:
        winner = "A"
    elif itemA[1] < itemB[1]:
        winner = "B"
    if user_selection == winner:
        return 1
    elif user_selection != winner:
        return 0
    else:
        return 2
    

def format_comparisons(item, A_or_B):
    # formats the list element item and returns a formatted string
    name = item[0]
    description = item[2]
    country = item[3]
    return f"Compare {A_or_B}: {name}, a {description}, from {country}."
        
def select_item():
    # randomly select element from list of dictionaries "game_data" and return it in a list variable
    import game_data
    import random
    
    game_dic = random.choice(game_data.data)
    item = []
    for key in game_dic:
        item.append(game_dic[key])
    return item
    
gameplay()