#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from word_list import word_list
from stages import stages

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
print("WELCOME TO HANGMAN - try not to die")

# randomly select word
word = random.choice(word_list)

display = []
x = len(word)

# create display blanks for word length
for _ in range(x):
    display += "_"

#print(f"the word is {word}")

# create loop for mulitple guesses, etc...

game_over = False
lives = 6
wrong = []

while not game_over:
    # Ask user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
    guess = input("Guess a letter: ").lower()
    # Check if the letter the user guessed is one of the letters in the choosen word
    for position in range(x):
        letter = word[position]
        if letter == guess:
            display[position] = letter
    if guess not in word:
        lives -=1
        wrong.append(guess)
        if lives == 0:
            game_over = True
            print("Hangman. You die")
    print(f"{' '.join(display)}")
    print("----------------------------------")
    print("Wrong Guesses:")
    print(f"{' '.join(wrong)}")
    print("----------------------------------")

    
    
    if "_" not in display:
        game_over = True
        print("You win.")
        
    print(stages[lives])


# In[ ]:




