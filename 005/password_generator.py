#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

char_sum = int(nr_letters) + int(nr_symbols) + int(nr_numbers)

char_set = []
# how to choose a random charcter to match the total number of charters choosen

for number in range(1, nr_letters+1):
    char = random.choice(letters)
    char_set.append(char)
for number in range(1, nr_symbols+1):
    char = random.choice(symbols)
    char_set.append(char)
for number in range(1, nr_numbers+1):
    char = random.choice(numbers)
    char_set.append(char)
    
random.shuffle(char_set)

password = " "
for alpha in char_set:
    password += str(alpha)

print(f"Your password is: {password}")


# In[ ]:




