#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# input for user
choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n")
kirk = int(choice)

if kirk >= 3 or kirk < 0:
    print("You choose an invalid number.")
else:    
    if kirk == 0:
        print(f"You choose rock: \n{rock}")
    elif kirk == 1:
        print(f"You choose paper: \n{paper}")
    elif kirk == 2:
        print(f"You choose scissors: \n{scissors}")


    # random number generator for computer
    spock = random.randint(0, 2)
    if spock == 0:
        print(f"Computer chose rock: \n{rock}")
    elif spock == 1:
        print(f"Computer chose paper: \n{paper}")
    elif spock == 2:
        print(f"Computer chose scissors: \n{scissors}")

    if kirk == 0 and spock == 1:
        print("Computer wins.")
    elif kirk == 0 and spock == 2:
        print("You win.")
    elif kirk == 1 and spock == 0:
        print("You win.")
    elif kirk == 1 and spock == 2:
        print("Computer wins.")    
    elif kirk == 2 and spock ==0:
        print("Computer wins.")
    elif kirk == 2 and spock == 1:
        print("You win.")
    else:
        print("Lizard, Spock")


# computer wins - 0,1; 1, 2; 2, 0
# user wins - 0, 2; 1, 0; 2, 1
 


# In[ ]:




