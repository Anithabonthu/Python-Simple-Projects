import os
def findWinner(bidder_details):
    high=0
    winner=""
    for bidder in bidder_details:
        if(bidder_details[bidder]>high):
            high=bidder_details[bidder]
            winner=bidder
    print(f"The Winner is {winner} with bid price of  {high}")
bid_data={}
end_of_bid=False
while not end_of_bid:
    name=input("enter your name:")
    bid_price=int(input("enter your bid price:"))
    bid_data[name]=bid_price
    more_bidders=input("if there are more bidders type yes otherwise no").lower()
    if(more_bidders=='no'):
        end_of_bid=True
        findWinner(bid_data)
    else:
        end_of_bid=False
        os.system("cls")      #to clear the screen

