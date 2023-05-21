#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("024/mail_merge/Input/Names/invited_names.txt") as names:
    guests = names.read()
    guest_list = guests.replace('\n', ',').split(',')

    for person in guest_list:
        with open("024/mail_merge/Input/Letters/starting_letter.txt") as blank:
            words = blank.read()
            new_letter = words.replace("[name]", person)
            with open(f"024/mail_merge/Output/ReadyToSend/letter_for_{person}.txt", mode = "w") as completed_letter:
                completed_letter.write(new_letter)

