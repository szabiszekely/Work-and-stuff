i=1
while i <= 5:
    print(i)
    i +=1
print("---------------------------------------------------------------------------------------------------------")
i=0
while 10 > i or i > 100:
#    i = int(input("Kérek egy számot 10 és 100 között:"))
    i = 50

print(i)
print("---------------------------------------------------------------------------------------------------------")

'''
ciklus
    i = int(input("Kérek egy számot 10 és 100 között:"))
ismételd amig  (10 > i or i > 100)
'''
'''
for (i=1 ; i<=5 ; i ++){

}
'''

sor={1,2,3,4,5,2,7,3,"UwU",6.9}
for i in sor:
    print(i)
print("---------------------------------------------------------------------------------------------------------")
#java foreach
#print(type(sor))

sor=["márton","éva","jocsik",["s","b"],{1,2,3,2}]
for i in sor:
    print(i)
print("---------------------------------------------------------------------------------------------------------")
print(range(10,20))
for i in range(6):
    print(i)
print("---------------------------------------------------------------------------------------------------------")
for i in range(1,6):
    print(i)
print("----------------------------------------------------------------------------------------------------")

for i in range(10,20,2):
    print(i)

for i in range(10,20,-2):
    print(i,end='')
print()
print("---------------------------------------------------------------------------------------------------------")
x=1/7
y=0
while y < 1:
    y = y + x
    print(y)

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
import random
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

szam1 = int(input("Írja meg hogy mi a minimum szám: "))
szam2 = int(input("Írja meg hogy mi a maximum szám: "))
szam = 0
osztas = int(input("Hányal legyen elosztva: "))
számláló = 0
alkalom = int(input("Hány alkalommal legyen ki írva: "))
ismetles = True
while ismetles:
    if szam2 < szam1:
        print("!!!A maximum nem lehet kisebb a minimumnál!!!")
        szam1 = int(input("Írja meg hogy mi a minimum szám: "))
        szam2 = int(input("Írja meg hogy mi a maximum szám: "))
    elif szam1 < szam2:
        while szam <= alkalom:
            randomszam = random.randint(szam1,szam2)
            if randomszam % osztas == 0:
                print(randomszam)
                szam = szam + 1
                számláló = számláló + 1        
            else:
                szam = szam + 1
    ismetles = False
print("Enyiszer fordult elö a 4-mal osztható számok: ",számláló)