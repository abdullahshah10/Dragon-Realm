import random
import time

def displayIntro():
    print("You are in a land full of dragons. In front of you,")
    print("you see two caves. In one cave, the dragon is friendly, ")
    print("and will share his treasure with you. The other dragon is ")
    print("is greedy and hungry and will eat you on sight.")
    print()

def chooseCave():
    cave=""
    while cave !="1" or cave !="2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()
        return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print("Its dark and spooky...")
    time.sleep(2)
    print("A Large dragon jumps our in front of you! He opeans his jaws and...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if chosenCave==str(friendlyCave):
        print("Gives you the treasure")
    else: print("Gobbles you down in one bite!")


displayIntro()
caveNumber = chooseCave()
checkCave(caveNumber)
print("Do you want to play again? (yes or no)")
playAgain=input()
if playAgain=="yes" or playAgain=="y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
elif playAgain == "no" or playAgain == "n":
    print("Game", time.sleep(1), ".", time.sleep(1), ".", time.sleep(1), ".")
    print("Over!")

