'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random
print("Welcome to Roshambo")
win=0
loss=0
ties=0
done= False
user_choice = input("Would you like to stop? y or n?")
if user_choice.lower() == "y":
    print("Hope you had fun!")
    done = True
else:
    print("Alright")
    print()
while not done:
    user_choice=int(input("What is your choice?\nEnter 1 for rock\nEnter 2 for paper\nEnter 3 for scissors\n"))
    if user_choice==1:
        print("You selected rock")
    elif user_choice==2:
        print("You selected paper")
    elif user_choice==3:
        print("You selected scissors")
    print()
    my_number= random.randrange(1,4)
    if my_number==1:
        print("The computer selected rock")
    elif my_number==2:
        print("The computer selected paper")
    else:
        print("The computer selected scissors")
    print()
    if user_choice==my_number:
        print("It's a tie!")
        ties+=1
    elif user_choice==1 and my_number==3:
        print("You win")
        win+=1
    elif user_choice==3 and my_number==1:
        print("You lose")
        loss+=1
    elif user_choice>my_number:
        print("You win")
        win+=1
    else:
        print("You lose")
        loss+=1
    user_choice = input("Would you like to stop? y or n?")
    print()
    if user_choice.lower() == "y":
        print("Hope you had fun!")
        done = True
    else:
        print("Alright down for another go")
        print()
print()
if done== True:
    print("Your win/loss was",win,"/",loss,"With",ties,"ties")








