
import random
ra = random.randint(1,10)
lista = []
osszesen = 0
for i in range(1,6):
    ra = random.randint(1,10)
    lista.append(ra)    

for ertekesites in lista:
    if ertekesites % 2 == 0:
        osszesen = osszesen + ertekesites

print('Ezek voltak a listában.',lista)
print('És ennyi volt összesen.',osszesen)

print('---------------------------------------')
elista = [1,4,-5,-1,2]
osszesen = 0
while True:
    intervalum = int(input('Kérek -5 és 5 közti számokat: '))
    if intervalum <= 5 and intervalum >= -5:
        elista.append(intervalum)
    else:
        break

print(elista)
for ertekesites in elista:
    osszesen = osszesen + ertekesites

print(osszesen)
print('---------------------------------------')

lista = [2, 5, 4, 8, 9, 11, 10, 12]
    
talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')

print('---------------------------------------')

lista = ['piros','kék', 'zöld' , 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
      if lista[index] == 'piros':
            talalat = True
      index = index + 1

if talalat:
      print('Van a listában piros szín, az indexe: ', index-1)
else:
      print('Nincs a listában piros szín.')

print('---------------------------------------')

lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while not talalat:
      if lista[index] % 3 == 0:
            talalat = True
      index = index + 1

print('A hárommal osztható szám indexe a listában: ', index-1)

print('---------------------------------------')

lilla = []

for i in range(1,6):
    rag = random.randint(1,7)
    lilla.append(rag)

bekert = int(input('Kérem a kereset számott(1 és 7 közöt): '))
index = 0
megvan = False

while index < len(lilla) and not megvan:
    if lilla[index] % bekert == 0:
        megvan = True
    index = index + 1

if megvan:
    print('Van benne ',bekert)
else:
    print('Nincs benne ',bekert)
print(lilla)

print('---------------------------------------')

szo = 'almafa'
lista = []
talalat = False
index = 0



for betu in szo:
    print(betu)
    lista.append(betu)

print(lista)


