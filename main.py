import art

print(art.logo)

bid_dict = {}

more_bid_true = True

def highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for i in bidding_record:
        bid_amount = bidding_record[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")



while more_bid_true:

    name = input("What is your name?")
    bid_price = int(input("What is your bid? $"))
    
    bid_dict[name] = bid_price
    
    more_bid = input("Are there other users who want to bid? Type 'yes' or 'no'").lower()
    if more_bid == 'yes':
        more_bid_true = True
        print("\n" * 100)
    else:
        more_bid_true = False
        highest_bid(bid_dict)