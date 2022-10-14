#!/usr/bin/env python
# coding: utf-8

# In[17]:


print("Welcome to treasure Island. Your mission is to find the treasure.")

direction1 = input("You enter a cave that branches in two directions. Will you go left or right? \n")

if direction1.lower() == "right":
    swim = input("You reach a cavern filled with water. It's high tide. Do you swim across or wait? \n")
    if swim.lower() == "swim":
        door = input("You reach a chamber with two doors, one red, one blue and one gold. Which do you choose? \n")
        if door.lower() == "blue":
            print("You found the treasure, you win!")
        elif door.lower() == "gold":
            print("You find a large chest. When you open it, it is filled with not treasure but teeth and a giant wet tongue. The mimic consumes you in a single bite.")
        else:
            print("You burst through the door and find a chamber filled with bears. Game over.")
    else:
        print("You fall asleep waiting and get eaten by a bear.")
else:
    if direction1.lower() == "left":
        print("You burst through the opening and fall into a lava pit. Game over.")

    else:
        print("You run into the wall, knock yourself unconscious and get eaten by a bear.")

