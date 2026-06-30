

import random 


choices = ["snake" , "water" , "gun"]

computer = random.choice(choices) 

user = input("Enter your choice :").lower()

if(user not in choices):
    print("Invalid choice ")

else:

    if(user==choices):

        print("Its a DRAW")

    elif((user=="snake" and computer=="water") or 
         (user == "water" and computer=="gun") or
         (user =="gun" and computer == "snake")):
        
        print("You WIN !!")

    else :

        print("you LOSE ")




















