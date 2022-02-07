honapok = ['január', 'február','március', 'április']

print(', '.join(honapok))

print(len(honapok))

print(honapok[0])

print(honapok[3])

print(honapok[1:3])

print(honapok[:3])

print(honapok[2:])

print(honapok[-1])
print("-------------------------------------------------")
szo = "almafa"
print(szo[:3])
print("-------------------------------------------------")
gyumolcsok = []

gyumolcs = None
while gyumolcs != '':
    gyumolcs = input('Adj meg egy gyümölcsöt! ')
    if gyumolcs != '':
        gyumolcsok.append(gyumolcs)
print(gyumolcsok)
print("-------------------------------------------------")
keresztnevek = []

megadot = 0
keresztnev = None
while keresztnev != '':
    keresztnev = 'Mihály'
    #keresztnev = input('Megadott keresztnevek: ')
    if keresztnev != '' and megadot <= 2:
        keresztnevek.append(keresztnev)
        megadot = megadot + 1
        print(megadot,'/3')
    else:
        print('Nincs több lehetöséged kereszt neveket beírnod!')
        print('A megadott keresztnevek: ',keresztnevek)
        break        

print('A megadott keresztnevek: ',keresztnevek)
print("-------------------------------------------------")
abetu = []
a = None
while a != '':
    a = str(input("Kérek csak 'a' betüs szavakat"))
    print("minden más szó nem kerül be a listába")
    if a != '' and a[0] == 'a' or a[0] == 'A':
        abetu.append(a)
    
print('Itt az összes "a" betüs szó: ',abetu)
print("-------------------------------------------------")
import random
negy = []
szam = 0
random_szam = random.randint(1,50)
while szam <= 10:
    if random_szam % 4 == 0:
        negy.append(random_szam)
        szam = szam + 1
        random_szam = random.randint(1,50)
    else:
        random_szam = random.randint(0,50)
        szam = szam + 1
print(len(negy))
print(negy)        

print("-------------------------------------------------")
print('Lista bejárása')
tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']

for tantargy in tantargyak:
	print(tantargy)
  
print("-------------------------------------------------")
print('Lista bejárása index-szel I.')
honapok = ['január', 'február','március', 'április', 'május', 'június'] 

index = 0
for honap in honapok:
  print(index, honap)
  index = index + 1

print("-------------------------------------------------")
print('Lista bejárása index-szel II.')
honapok = ['január', 'február','március', 'április', 'május', 'június']

for index in range(len(honapok)):
    print(index, honapok[index])

print("-------------------------------------------------")
print('Lista bejárása index-szel III.')
honapok = ['január', 'február','március', 'április', 'május', 'június']

for index, honap in enumerate(honapok):
  print(index, honap)
print("-------------------------------------------------")
print('magyarázat I')
honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
  # az eredeti listaelem NEM módosul!
  honap = honap.upper()	
print("-------------------------------------------------")
print('magyarázat II')
honapok = ['január', 'február','március', 'április', 'május', 'június']

for index in range(len(honapok)):
  # az eredeti listaelem módosul!
  honapok[index] = honapok[index].upper()
print(index, honapok[index])
print("-------------------------------------------------")

for i in range(1,41):
    if i % 3 == 0:
        print(i)
        
