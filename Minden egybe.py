import random
print("Hi") #string (egyszerű szöveg)
print(1) #integer (egész szám)
print(1.0) #float (pontos szám)
print(10+12) 
print(6-3)
print(3*5)
print(6/2)
print(15//5)
print(15%7)
print("alma","körte","csirke")
print(1,2,3,1,5,3)
a = [1,2,1,4,3,3,5,6,4] #lista
b = {1,2,1,4,3,3,5,6,4} #halmaz
print(a)
print(b)
print("-----------------------------------------------------------------------------------------------------------------------------")
'''
adat = input('Adj meg egy számot! ')
szam = int(adat)
#rövidebben
szam = int(input('Adj meg egy számot! '))
print("-----------------------------------------------------------------------------------------------------------------------------")

folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n':
        folytatja = False
print('>> Program vége! <<')    
'''
print("-----------------------------------------------------------------------------------------------------------------------------")
szam = 2
'''szam = int(input("Kérek egy páros számot: "))'''
if szam < 0:
   print("negatív") 
elif not szam <= 0:
    print("pozitív")

henrik = "i"
hanna = "i"
'''
henrik = str(input("Henrik jön ma kosarazni? (i/n): "))
hanna = str(input("És Hanna, ő tud jönni kosarazni? (i/n): "))
'''
if henrik == 'i' and hanna == 'i':
    print("mind a ketten jönnek kosarazni")

if henrik == 'n' or hanna == 'n':
    print("csak az egyikük jön kosarazni")

if henrik == 'n' and hanna == 'n':
    print("egyikük sem tud jön kosarazni")

szam = 12
'''
szam = int(input("Kérek egy számot: "))
'''
if szam % 3 == 0:
    print("osztható 3-mal")
else:
    print("nem osztható 3-mal")
if szam % 4 == 0:
    print("osztható 4-gyel")
else:
    print("nem osztható 4-gyel")
if szam % 3 == 0 and szam % 4 == 0:
    print("osztható 3-mal és 4-gyel")
if szam % 3 != 0 and szam % 4 != 0:
    print("nem osztható 3-mal és 4-gyel")

randomszam = random.randint(1,3)
szam = 3
'''
szam = int(input("Adj meg egy számot 1 és 3 közöt: "))
'''
összeadás = randomszam + szam
kivonás =  randomszam - szam
szorzás =  randomszam * szam

print("random szám", randomszam)
print("A megadott szám", szam)
print("Összeadás", összeadás)
print("Kivonás", kivonás)
print("Szorzás", szorzás)

randomszam = random.randint(1,2)

találat = 'i'
'''
találat = str(input("Fej vagy írás?(f/i): "))
'''
if randomszam == 1:
    válasz = "Fej"
    helyes = 'f'
if randomszam == 2:
    válasz = "Írás"
    helyes = 'i'
print(válasz)
if találat == 'f' and helyes == 'f':
    print("Nyertél")
if találat == 'i' and helyes == 'i':
    print("Nyertél")
if találat == 'f' and helyes == 'i':
    print("Vesztettél")
if találat == 'i' and helyes == 'f':
    print("Vesztettél")

szam = 0
while szam <= 10:
    if szam % 2 == 0:
        print(szam)
        szam = szam + 1
    else:
        szam = szam + 1
print("--------------------")

szam = 10
while szam >= 1:
    print(szam)
    szam = szam - 1
print("--------------------")

szam = 10
while szam >= 1:
    if szam % 2 != 0:
        print(szam)
        szam = szam - 1
    else:
        szam = szam - 1
print("--------------------")

szoveg = "a"
alkalom = 1
'''
szoveg = str(input("Adjon meg egy szöveget: "))
alkalom = int(input("Adja meg hányszor legyen ki írva: "))
'''
while alkalom >= 1:
    print(szoveg)
    alkalom = alkalom - 1

igaz = True
szam = 2
'''
szam = int(input("Kérek egy páros számot: "))
'''
while igaz:
    if szam % 2 == 0:
        print("Köszönjük")
        print(szam)
        igaz = False
    else:
        szam = int(input("Kérek egy páros számot: "))
print("--------------------")
randomszam = random.randint(1,12)
szam = 20
darab = 0
while szam >= 1:
    if randomszam % 3 == 0:
        print(randomszam)
        darab = darab + 1
        szam = szam - 1
        randomszam = random.randint(1,12)
    else:
        szam = szam - 1
        randomszam = random.randint(1,12)
print("enyi 3-mal osztható szám volt: ", darab)
print("--------------------")
igaz = True
darab_karakter = 1
sor = 1
szam = int(input("Kérek egy páros számot: "))
while igaz:
    if szam % 2 == 0:
        while sor <= szam:
            oszlop = 1
            while oszlop <= darab_karakter:
                print('O ', end='')
                oszlop = oszlop + 1
            print('')
            darab_karakter = darab_karakter + 1
            sor = sor + 1   
            if sor == szam / 2:
                oszlop = 1
                while oszlop <= darab_karakter:
                    print('O ', end='')
                    oszlop = oszlop + 1
                print('')
                while sor <= szam:
                    oszlop = 1
                    while oszlop <= darab_karakter:
                        print('O ', end='')
                        oszlop = oszlop + 1
                    print('')
                    darab_karakter = darab_karakter - 1
                    sor = sor + 1
        igaz = False
    else:
        szam = int(input("Kérek egy páros számot: "))

