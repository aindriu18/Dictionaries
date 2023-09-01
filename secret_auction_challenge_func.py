from art import logo
#from replit import clear

print(logo)

# control variable for while loop
another_bidder = True
#bid counter variable for for loop with range.
bid_counter = 0
#empty dictionary to store key value pairs from user input.
bid_dict = {}

def highest_bidder(bid_record):

    for i in range(bid_counter):
        # .get required, otherwise the max function will output the max name alphabetically.
        max_bid_name = max(bid_dict, key=bid_dict.get)
        max_bid_value = max(bid_dict.values())
    print(f"The highest bidder is {max_bid_name} with a bid of €{max_bid_value}")

while another_bidder:
    bid_name = input("What is your name? ")
    bid_price = int(input("Please enter your bid: €"))
    bid_dict[bid_name] = bid_price
    bid_again = input("Are there any other users who want to bid? Yes or No ").lower()

    if bid_again == "no":
        another_bidder = False
        highest_bidder(bid_dict)
    elif bid_again == "yes":
       bid_counter += 1





