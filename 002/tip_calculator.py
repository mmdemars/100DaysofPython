#!/usr/bin/env python
# coding: utf-8

# In[13]:


print("Welcome to the tip calculator. ")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
party = int(input("How many people to split the bill? "))

total_tip = (tip)/100 * total_bill
bill_with_tip = total_bill + total_tip
split_check = bill_with_tip / party

result = (f"Each person should pay: ${(round(split_check, 2))}")

print(result)

