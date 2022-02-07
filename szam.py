import random
tip = random.randint(1,100)
#print(tip)
tipeltszam = int(input("Gondoltam egy számot 1 és 100 közöt találd ki \nA szám6: "))
folytat = True
talált = 0
while folytat:
    talált = talált + 1
    if tip == tipeltszam:
        print("Talált")
        folytat = False
    elif tip > tipeltszam:
        print("Nagyobb")
        tipeltszam = int(input("Akkor a szám: "))
    elif tip < tipeltszam:
        print("Kisebb")
        tipeltszam = int(input("Akkor a szám: "))
print("Enyi találatbol sikerült",talált)

