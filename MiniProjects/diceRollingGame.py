#Python Beginner Project 1)

# Dice Rolling Game Logic

#loop
 #Ask:Roll the dice?
 #if user enter y?
    #Generate two random numbwers
    #print them
 #elif print thanks of playing | terminate
 #else invalid choice

import random # for random number generate

# choice = input("enter your choice: ") input gives string in All case
# if(choice=='Y' and choice=='y'):# to minimize logic use (.lower())method
while True:
   choice = input("enter your choice (Y|N): ").lower()

   if choice=='y':
      dice1 = random.randint(1,6)#range(1,6)
      dice2 = random.randint(1,6)
      print(f"({dice1},{dice2})")
   elif choice =='n':
      print("thanks for playing!")
      break
   else:
     print("Invalid Choice")


