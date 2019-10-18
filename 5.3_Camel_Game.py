'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
done=False
thirst=0
miles_traveled=0
duck_tiredness=0
hydro_flask=6
goose_distance=-20
print("Welcome to Duck Leader")
instructions=input("Would you like instructions? Y or N?")
if instructions.lower()== "y":
    print("The goal of this game is to lead your duck friend 200 miles to get grapes.")
    print("You will be chased by a group of geese so take your time and hurry up.")
    print("Every so often you will be asked to make a choice, your choices will determine how well you do")
    print("Your commands include:")
    print("1. Drink some water from your hydro flask\n2. Walk towards the store\n3. Run towards the store")
    print("4. Stop for the night\n5. Check your status\n6. Quit")
    print("You'll start with 6 drinks in your hydro flask and the geese will be behind you by 40 miles.")
    print("Make sure to answer with the # of the command.")
    print()
else:
    print("Alrighty then")
    print("Make sure to answer with the # of the command.")
print()
input("Would you like to play hard mode?")
print()

while not done:
    if goose_distance<miles_traveled:
        if thirst<6:
            print()
        if duck_tiredness<8:
            oasis=random.randint(1,20)
            if oasis==7:
                print("You have found a bird fountain\nYou refilled your hydro flask")
                hydro_flask=6
            if goose_distance>miles_traveled-15 and goose_distance<miles_traveled:
                print("The geese are hot on your tail. Only",miles_traveled-goose_distance,"miles away.")
            if thirst>=4 and thirst<=6:
                print("Your duck friend is thirsty")
            if duck_tiredness>=5 and duck_tiredness<=8:
                print("Your duck friend is tired")
            if miles_traveled < 200:
                print()
                print("What is your command?")
                user_choice=int(input("1. Drink some water from your hydro flask\n2. Walk towards the store\n3. Run towards the store\n4. Stop for the night\n5. Check your status\n6. Quit\n" ))
                if user_choice==6:
                    done=True
                elif user_choice==1:
                    if hydro_flask>=1:
                        print("You take a drink from your hydro flask. You have",hydro_flask-1,"drinks left.")
                        thirst=0
                        hydro_flask-=1
                    else:
                        print("You're out of water!")
                elif user_choice == 2:
                    moderate_speed=random.randint(5,12)
                    miles_traveled+=moderate_speed
                    print("You traveled", moderate_speed,"miles.")
                    thirst+=1
                    duck_tiredness+=1
                    goose_distance+= random.randint(7,14)
                elif user_choice == 3:
                    full_speed=random.randint(10,20)
                    miles_traveled+= full_speed
                    print("You moved forward", full_speed,"miles.")
                    thirst+=1
                    duck_tiredness+= random.randint(1,3)
                    goose_distance+= random.randint(7,14)
                elif user_choice == 4:
                    duck_tiredness=0
                    print("Your duck buddy is happy")
                    goose_distance+= random.randint(7,14)
                elif user_choice == 5:
                    print("You have traveled: ",miles_traveled,"miles.")
                    print("You have",hydro_flask,"drinks left in your hydro flask.")
                    print("The geese are",miles_traveled-goose_distance,"miles behind you.")
                else:
                    print("Please select a number 1 through 6")
            else:
                print("Congratulations you've won.")
                user_choice = input("Would you like to play again? Y or N?")
                if user_choice.lower() == "y":
                    print("WOOOHOOO")
                    miles_traveled=0
                    thirst=0
                    duck_tiredness=0
                    hydro_flask=6
                    goose_distance=-20
                    print("Welcome Back")
                    print()
                else:
                    print("Maybe some other time")
                    done = True
        else:
            print("Your duck friend died.\nYou made it",miles_traveled,"Miles")
            user_choice = input("Would you like to play again? Y or N?")
            if user_choice.lower() == "y":
                print("WOOOHOOO")
                miles_traveled = 0
                thirst = 0
                duck_tiredness = 0
                hydro_flask = 6
                goose_distance = -20
                print("Welcome Back")
                print()
            else:
                print("Maybe some other time")
                done = True
    else:
        print("The jig is up, the geese have caught you.\nYou made it",miles_traveled,"miles.")
        user_choice = input("Would you like to play again? Y or N?")
        if user_choice.lower() == "y":
            print("WOOOHOOO")
            miles_traveled = 0
            thirst = 0
            duck_tiredness = 0
            hydro_flask = 6
            goose_distance = -20
            print("Welcome Back")
            print()
        else:
            print("Maybe some other time")
            done = True

print("Thanks for playing.")
