from random import *                                                                            
import random                                                                                  
import time                                                                                     

monster_tür = 0                                                                                 #creats a varible which contains the door where tho monster is hiding
player = 0                                                                                      #creats a verible which contains the door that the player is choosing
i = "y"                                                                                         #creats a verible that is needed for the while-loop
stage = 0                                                                                       #creats a verible that contains the stage you'r on
list = ["Ghost", "Phantom", "Butcher", "Doom Slayer"]                                           #creats a list that contains the monsters
print("AI: Do you want to play a game? y/n: ", end = "")                                        #the computer asks if you wanna play
x = input()                                                                                     #the player says if he wants to play or not

if x == "y":                                                                                    #if-function if the player wants to play a game
    Monster = random.choice(list)                                                               #a monster is randomly chosen from the list
    print(".")                                                                                  #imitates a loading sequenz
    time.sleep(0.5)                                                                             #the program freezes for a certain time
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("AI: You have to pick one of three doors by typing 1, 2 or 3 in the terminal.")       #explains the rules to the player
    time.sleep(3)
    print("AI: Good Luck!")
    time.sleep(1)
    
    while i == "y":                                                                             #the while-loop makes it possible to have more levels
        monster_tür = int(randint(1,3))                                                         #the door behind which the monster is hiding is selected
        stage = int(stage + 1)                                                                  #the current level is calculated
        print("AI: Stage " + str(stage))                                                        #tells the player in which level he is
        print("")                                                                               #space
        print("AI: Pick one of three doors. ", end = "")                                        #the player is asked to choose one of 3 doors
        player = int(input())                                                                   #the player enters the door of his choice                                                 
        
        if player == monster_tür:                                                               #a if-function that detects if the chosen door contains the monster
            time.sleep(0.5)                                                                     #imitates a loading sequenz
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("AI: Sorry mate; but the " + Monster + " has found you.")                     #the game tells the player which monster has found him
            print("AI: You lost.")
            print("AI: Your score was " + str(stage))                                           #tells the player his score
            break                                                                               #ends the loop
        
        if player >= 4 or player <= 0:                                                          #if the player is choosing a door that not exists 
            time.sleep(0.5)
            print("")
            while True:                                                                         #creats a while-loop to spam the cheater
                print("AI: Eat shit idiot. ", end="")                                           #tells the Player to eat shit for trying to cheat
            break                                                                               #ends the loop
       
        else:
            time.sleep(0.5)                                                                     #imitates a loading sequenz
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)

else:
    print(".")                                                                                  #imitates a loading sequenz
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("AI: Goodbye lad.")
