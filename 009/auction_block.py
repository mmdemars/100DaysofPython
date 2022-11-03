#!/usr/bin/env python
# coding: utf-8

# In[1]:


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


# In[6]:


import os
#HINT: You can call clear() to clear the output in the console.


# In[24]:


print(logo)
people_money = {}
close_auction = False

def find_winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while close_auction == False:
    bidder = input("Who is bidding? ")
    bid = input("What is your bid? $")
    people_money[bidder] = int(bid)
    keep_going = input("Are there any other bidders? y or n ")
    if keep_going == "n":
        close_auction = True
        print("\033[2J\033[1;1H")
        find_winner(people_money)
    else:
        close_auction = False
        print("\033[2J\033[1;1H")


# 
