from art import logo
from replit import clear

print(logo)

another_bidder = True
bid_counter = 0
bid_dict = {}

while another_bidder:
    bid_name = input("What is your name? ")
    bid_price = int(input("Please enter your bid: €"))
    bid_again = input("Are there any other users who want to bid? Yes or No ").lower()

    bid_counter += 1

    if bid_again == "no":
        another_bidder = False
    elif bid_again == "yes":
        clear()

    for i in range(bid_counter):
        bid_dict[bid_name]=bid_price
        max_bid_value = max(bid_dict.values())
        max_bid_name = max(bid_dict)


print(f"The highest bidder is {max_bid_name} with a bid of €{max_bid_value}")


