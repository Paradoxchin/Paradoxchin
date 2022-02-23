from random import *

list = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0","ß","?","@","$","%","&"]

ans = "y"

print("Do you want to generate a password? y/n ", end = "")
ans = input()
    
while ans == "y":
    print("How long should your password be? ", end = "")
    y = input()

    y = int(y)

    p = ""

    for i in range(y):
        x = choice(list)
        p = p + x	

    print("")
    print("Your new " + str(y) + " letter password is: " + str(p))
    print("")
    print("Do you want to generate another password? y/n ", end = "")
    ans = input()
    
else: 
    while True:
        print("Eat shit idiot! ", end = ""
