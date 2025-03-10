# Dragon Realm game created by Al Sweigart - reworked by me
#In this game, the player is in a land full of dragons. The dragons all live in caves with their large
# piles of collected treasure. Some dragons are friendly and share their treasure with you. Other
# dragons are hungry and eat anyone who enters their cave. The player is in front of two caves, one
# with a friendly dragon and the other with a hungry dragon. The player must choose between the
# two.

import random
import sys

# Introduction
def introduction():
    print("Greetings, brave adventurer!")
    print("You are in a land full of dragons.") 
    print("In front of you, you see two caves.") 
    print("In one cave, the dragon is friendly and will share his treasure with you.") 
    print("The other dragon is greedy and hungry, and will eat you on sight.") 


# Choosing a cave
def cave_choice():
    print("Make your choice adventurer. What do the fates have in store for you?")
    print("Enter 1 to choose the first cave, or 2 to choose the second cave. Or you enter 3 to run away.")
    
    while True:
        try:
            cave = int(input())
            if cave != 1 and cave != 2 and cave != 3:
                print("You must choose 1, 2, or 3! Perhaps fear has clouded your judgement. Try again.")
                continue
            if cave == 1 or cave == 2:
                return cave
            if cave == 3:
                print("You have chosen to flee! Coward!")
                break
            
        except ValueError:
            print("You must choose 1, 2, or 3! Perhaps fear has clouded your judgement. Try again.")
        
        
introduction()

# Check the cave outcome
choice = cave_choice()
if choice is None:
    print("Game Over")
    sys.exit()
    
    
    



# Ask the player if they want to play again