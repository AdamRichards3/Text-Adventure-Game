# Setup
yes_no = ['yes', 'no']
movement = ['Forward', 'Back', 'Left', 'Right']

#Intro
name = input("What is your name adventureur?\n")
print("Greetings " + name + " Lets start this quest!")
print("You find you self at the edge of a forrest")

#Start of game 
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\n")
    if response == "yes":
        print("You have entered into the forest. You hear crows barking in the distance.")
    elif response == "no":
        print("You are not ready for this adventrure.")

    response = input("There are three paths in front of you, Which one od you take? (Forward, Back, Left, Right)\n")
    if response == "Forward":
        input("You step further into the forest and see a figure on the horizen, Would you like to continue?")
    elif response == "Back":
        print("You are not ready for the this adventure, come back when you are!")
    elif response == "Left":
        print("You follow the path and fall into a pit of spikes")
    elif response == "Right":
        print("You walk down the path and hearing branches crackling, suddenly a wolf pounces on you!")
    else:
        print("Please put a correct input! (Forward, Back, Left, Right)")
