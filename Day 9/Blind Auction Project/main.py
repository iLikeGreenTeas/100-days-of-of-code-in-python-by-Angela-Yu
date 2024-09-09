# TODO-1: Ask the user for input
def highest_bidder():
    user_data = {}
    while True:
        user_name = input("What is your name?\n")
        user_bid = int(input("How much do you bid?\n"))
        # TODO-2: Save data into dictionary {name: price}

        user_data[user_name] = user_bid
        # TODO-3: Whether if new bids need to be added
        any_remaining_bids = input("Are there any more bidders? "
                                   "Type 'y' for yes and 'n' for no. \n").lower()
        if any_remaining_bids.startswith('n'):
            break
        elif any_remaining_bids.startswith('y'):
            print("\n" * 20)
# TODO-4: Compare bids in dictionary
    highest_bidder = max(user_data, key=user_data.get)
    highest_bid = user_data[highest_bidder]

    print(f"The highest bidder is {highest_bidder}, with a bid of {highest_bid}.")

highest_bidder()


