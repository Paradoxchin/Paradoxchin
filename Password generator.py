from random import *
import random  

list = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9","0","ß","?","=","$","%","&"]

print("How long should your password be? ", end = "")
y = input()

y = int(y)

p = ""

for i in range(y):
    x = choice(list)
    p = p + x	

print(p)