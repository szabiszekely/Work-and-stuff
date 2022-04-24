
#https://infojegyzet.hu/vizsgafeladatok/okj-programozas/rendszeruzemelteto-191008/

#Ausztria;1995.01.01
#Belgium;1958.01.01

class Eutagallamok:
  def __init__(self,sor):
    orszag, datum = sor.strip().split(";")
    self.orszag = orszag
    self.datum = datum
    self.ev = int(datum[0:4])
    self.honap = datum[5:7]
    self.nap = datum[8:10]

with open("EUcsatlakozas.txt","r",encoding="latin2") as f:
  lista = [Eutagallamok(sor) for sor in f]


"""
 2. Olvassa be az EUcsatlakozas.txt állomány sorait és tárolja az adatokat egy olyan
összetett adatszerkezetben (pl. vektor, lista stb.), amely használatával a további
feladatok megoldhatók!
3. Határozza meg és írja ki a képernyöre a minta szerint, hogy hány tagállama volt
2018-ban az Európai Uniónak!
4. Határozza meg és írja ki a képemyőre a minta szerint a 2007-ben csatlakozott
országok számát!
5. Határozza meg és írja ki a képernyöre a minta szerint Magyarország csatlakozásának
dátumát!
"""

#3. Határozza meg és írja ki a képernyöre a minta szerint, #hogy hány tagállama volt
#2018-ban az Európai Uniónak!

print(f"3.feladat: EU tagállamainak száma: {len(lista)}")

#4. Határozza meg és írja ki a képemyőre a minta szerint a #2007-ben csatlakozott
#országok számát!

darab = 0
for sor in lista:
  if sor.ev == 2007:
    darab += 1

hany = [sor for sor in lista if sor.ev == 2007]

print(f"4. feladat: 2007-ben {darab} ország csatlakozott")

#5. Határozza meg és írja ki a képernyöre a minta szerint #Magyarország csatlakozásának
#dátumát!

magyar = [sor.datum for sor in lista if sor.orszag in {"Magyarország"}]
magyar2 = [sor.datum for sor in lista if sor.orszag == "Magyarország"]

for sor in lista:
  if sor.orszag == "Magyarország":
    print(f"5.feladat: Magyarország csatlakozásának dátuma {sor.datum}")

#print(f"5.feladat: Magyarország csatlakozásának dátuma {magyar[0]}")

# 6. Határozza meg, hogy májusban történt-e csatlakozás az EU-hoz!

maju = [sor for sor in lista if sor.honap in {"05"}]

"""
if len(maju) > 0:
  print("volt")
else:
  print("nem volt")
"""

if maju:
  print(f"6. feladat: Májusban volt csatlakozás")
else:
  print("nem volt")

# 7. Keresse meg az utoljára csatlakozott tagállamot! Az eredményt #a minta szerint
#jelenítse meg a képernyőn! Feltételezheti, hogy nem alakult ki #„holtverseny".


utso = 0
orszag = ""
for sor in lista:
  if sor.ev > utso:
    utso = sor.ev
    orszag = sor.orszag
    
print(orszag)

stat = dict()

for sor in lista:
  ev = sor.ev
  stat[ev] = stat.get(ev,0) + 1
print("8. feladat: statisztika ")
for ev,darab in stat.items():
  print(f"{ev} - {darab} -orszag ")
  


    
    


