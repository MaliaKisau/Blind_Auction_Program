import os

#Function to clear the terminal
def clear_terminal():
    os.system('cls')

#Importing the auction logo
from auction_art import logo
print(logo)

#Dictionary to store bids
bids = {}
bidding_finnished = False

#Function to find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    print(f"The winner is {winner} with a bid of ${highest_bid}")

#Getting bidder's name and bid amount
name = input("What is your name?: ")
price = int(input("What is your bid?: $ "))
bids[name] = price 

#Asking if there are any other bidders
should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

#Checking if bidding is finished
if should_continue == "no":
    bidding_finnished = True
    find_highest_bidder(bids)
elif should_continue == "yes":
    #Clearing the terminal for the next bidder
    clear_terminal()