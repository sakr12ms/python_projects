#
import time

print("Now , you are lost in a forest and you have to ways to escape \n(1)from the river \n(2) from the forest  ")
way=input("From where will you go:")
if way =="1":
    print("you chose to go from the river")
elif way=="2":
    print("you chose to go from the forest")
else:
    print("invalid input please try again")


#
if way =="1":
    print("Now, you are thirsty and hungry you can drink from the river ")
    print("You are drinking from the river but there is no food you \n (1)you will try to catch fish \n (2)you will "
      "return back to forest to get fruits ")
food=input("what will you do:")

if food =="1":

    print("Successfully , you catch a fish")
elif food =="2":
    print("There is a bear in front of you  ")
    print("you find abig stone \n (1)you will through it on the bear \n (2)you will return back and try to catch afish")
else:
    print("invalid input please try again ")

if food=="2":
    bear=input("what will you do?:")

if bear =="1":
    print("the stone does not affect the bear and it notice you and killed you")
elif bear =="2":
    print("Successfully , you catch a fish")
else:
    print("invalid input please try again ")







