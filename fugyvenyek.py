
def koszont():
      print('Üdv a fedélzeten!')

koszont()
print('--------------------------------------------')
def koszont_nevvel(nev):
      print('Szia '+ nev +', üdv a fedélzeten!')

koszont_nevvel('Szabolcs')

print('--------------------------------------------')


def koszont_ket_nevvel(nev1, nev2):
      print('Szia '+ nev1 + ', ' + nev2 +'!\nÜdv a fedélzeten!')

koszont_ket_nevvel('Nóra', 'Ádám')

print('--------------------------------------------')


'''
Az argumentum (aktuális paraméter) lehet érték, kifejezés, változó is!
Az 'x', 'y' és 'eredmeny' nevű változók LOKÁLISAK, csak az eljáráson belül érhetők el! 
'''
def osszead(x, y):
      eredmeny = x + y
      print('A két szám összege: ', eredmeny)


osszead(10, 9)
osszead(5+5, 5+4)

a = 10
b = 9
osszead(a, b) 

print('--------------------------------------------')


def osszegzo(list):
      osszesen = 0
      for szam in list:
            osszesen = osszesen + szam
      print('A listában lévő számok összege: ', osszesen)


szamok = [3, 5, 19, 11, 17, 1]
osszegzo(szamok)

print('--------------------------------------------')


def kepernyore_ir():
    lokalis_valtozo = 'alma'
    print(lokalis_valtozo)
    print(globalis_valtozo)


globalis_valtozo = 'gyümölcs'
kepernyore_ir()

print(globalis_valtozo)
# a lokalis_valtozo az eljáráson KÍVŰL nem elérhető !!!
#print(lokalis_valtozo) # hibát eredményez !!!

print('--------------------------------------------')

def rovidites(szoveg):
    
    print(szoveg[0:3] + '.')

#szoveg = input('Kérek szót: ')
szoveg = 'követekező'
rovidites(szoveg)

print('--------------------------------------------')

def paros_parat_null(x):
    if x == 0:
        print('Nulla')
    elif x % 2 == 0:
        print("Páros")
    else:
        print('Páratlan')

szo = int(input('Kérek egy pozitív egész számot: '))


paros_parat_null(szo)

print('--------------------------------------------')

def hasonlitas(x,y):
    if x == y:
        print('Egyenlő')
    elif x > y:
        print(x,'Nagyobb')
    elif x < y:
        print(y,'Nagyobb')

egy = int(input('Kérem az 1. számot: '))
ketto = int(input('Kérem az 2. számot: '))

hasonlitas(egy,ketto)

print('--------------------------------------------')

def hossz(szo_lista):
    rovid = szo_lista[0]   
    for szo in szo_lista:
        if len(szo) < len(rovid):
            rovid = szo
    print(rovid,'A legrövidebb')
szo_lista = []
szam = 0
while szam != 3:
    szo = input('Kérek egy szót: ')
    szo_lista.append(szo)
    szam += 1

hossz(szo_lista)























































