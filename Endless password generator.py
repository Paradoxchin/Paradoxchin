from random import *                                                                            #imports random

list = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0","ß","?","@","$","%","&"]            #creats a list with all necessery letters and signs

ans = "y"                                                                                       #creats the varible ans to make an endless-loop

print("Do you want to generate a password? y/n ", end = "")
ans = input()                                                                                   #makes an input
    
while ans == "y":                                                                               #creates the endless-loop
    print("How long should your password be? ", end = "")
    y = input()

    y = int(y)                                                                                  #string to int

    p = ""                                                                                      #creating a varible     

    for i in range(y):                                                                          #for loop to get the length of the password right
        x = choice(list)                                                                        #chooses a random symbol out of the list
        p = p + x	                                                                            #creats a varible that contains the whole password

    print("")
    print("Your new " + str(y) + " letter password is: " + str(p))
    print("")
    print("Do you want to generate another password? y/n ", end = "")                           #asks you if you want to generate another password
    ans = input()                                                                               
    
else: 
    while True:                                                                                 #endless-loop that can not be stopped
        print("Eat shit idiot! ", end = "")                                                     #tells you to eat shit in an endless-loop
