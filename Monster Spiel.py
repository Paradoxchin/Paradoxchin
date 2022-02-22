from random import *                                                                            #importiert alles aus random
import random                                                                                   #importiert random 
import time                                                                                     #importiert die Zeit

monster_tür = 0                                                                                 #erstellt die Variable die anbibt hinter welcher tür sich das Monster versteckt
player = 0                                                                                      #erstellt die Variable die vom Spieler veränder wird um die Tür auszuwählen
i = "y"                                                                                         #erstellt die Variable die für die while-Schleife benötigt wird
stage = 0                                                                                       #erstellt die Variable die das Level angibt
list = ["Herr Jäger", "Frau Irobalieva", "Frau Lukasser", "Herr Bucher"]                        #erstellt eine Liste die vier verschiedene Monster enthält
print("AI: Do you want to play a game? y/n: ", end = "")                                        #der Computer fragt ab ob du ein Spiel spielen möchtest
x = input()                                                                                     #der Spielerinput ob er ein spiel spielen will oder nicht

if x == "y":                                                                                    #if-Abfrage ob der Spieler ein Spiel spielen will
    Monster = random.choice(list)                                                               #es wird ein Monster aus der Liste zufällig gewählt
    print(".")                                                                                  #immitiert eine Ladesequenz
    time.sleep(0.5)                                                                             #der Ablauf des programmes wird für eine bestimmte Zeit pausiert
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("AI: You have to pick one of three doors by typing 1, 2 or 3 in the terminal.")       #dieser Print erklärt die Regeln des Spieles
    time.sleep(3)
    print("AI: Good Luck!")
    time.sleep(1)
    
    while i == "y":                                                                             #die while-Schleife ermöglicht es mehrere Level zu haben
        monster_tür = int(randint(1,3))                                                         #die Tür hinter der sich das Monster versteckt wird ausgewählt
        stage = int(stage + 1)                                                                  #das aktuelle Level wird berechnet  
        print("AI: Stage " + str(stage))                                                        #sagt dem Spieler in welchem Level er sich befindet
        print("")                                                                               #Leerzeile
        print("AI: Pick one of three doors. ", end = "")                                        #der Spieler wird aufgefordert eine von 3 Türen auszuwählen
        player = int(input())                                                                   #der Spieler gibt die Tür seiner Wahl ein                                                 
        
        if player == monster_tür:                                                               #eine if-Abfrage die erkennt ob das Monster hinter der ausgewählten Tür befindet
            time.sleep(0.5)                                                                     #immitiert eine Ladesequenz
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("AI: Sorry mate; but the monster " + Monster + " has found you.")             #dem Spieler wird mitgeteilt welches Monster ihn gefunden hat
            print("AI: You lost.")
            print("AI: Your score was " + str(stage))                                           #teilt dem Spieler seine Punkteanzahl mit
            break                                                                               #beendet die Schleife
        
        if player >= 4 or player <= 0:                                                          #wenn der Spieler eine Tür wählt die es nicht gibt 
            time.sleep(0.5)
            print("")
            while True:                                                                         #erstellt while-Schleife um den Cheater vollzuspammen
                print("AI: Eat shit idiot. ", end="")                                           #tells the Player to eat shit for trying to cheat
            break                                                                               #beendet die Schleife
       
        else:
            time.sleep(0.5)                                                                     #immitiert eine Ladesequenz
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)

else:
    print(".")                                                                                  #immitiert eine Ladesequenz
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("AI: Goodbye lad.")