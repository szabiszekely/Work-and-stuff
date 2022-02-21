import random
# a szavak:
szavak =  ["alma","fa","ablak","asztal","szék","körte","golyó","papucs","váza","szekrény","labda","szönyeg","pohár","üveg","lámpa","könvy","zokni","cipő","sál","nadrág","sapka","kesztyű","kabát","doboz","ceruza","hegyező","radir","táska"]
# változok / variables, listák
rajzol = 0
elet = 10
kivalaszt = random.choice(szavak)
eltalalt = []
szeletelo = []
rossz = []
tarolo = ""
segitseg_szamlalo = 2
figy = 0
for betu in kivalaszt:
    szeletelo.append(betu)
meddig = len(szeletelo)
#________________________________________________________
# játék beállitások
print("Gondoltam egy szóra találd ki melyik az!")
print("10 szer probálkozhatsz alapból!")
print("Kettő segítséged van ha akarod használni ird be hogy: \"segitseg\"")
rajzol_e = input("Akarod-e, hogy rajzoljuk az akasztófát? (i/n)\t")
if rajzol_e == "i":
    import turtle
    egyszer_1 = 0
    egyszer_2 = 0
    egyszer_3 = 0
    egyszer_4 = 0
    egyszer_5 = 0
    egyszer_6 = 0
    egyszer_7 = 0
    egyszer_8 = 0
    egyszer_9 = 0
    egyszer_10 = 0
    egyszer_11 = 0
    egyszer_12 = 0
    egyszer_13 = 0
    wn = turtle.Screen()
    defi = turtle.Turtle()
    #defi.speed(0)              #!!!!!!!!!!!!!!!!!
    wn.bgcolor("darkgreen")
    defi.color("white")            
    defi.pensize(3)
    defi.shape("turtle")
    defi.penup()
    defi.goto(-160,-300)
    defi.pendown()
    wn.title("Akasztófa")
    print("Annyi probálozásod van míg meg nem rajzolom az akasztófát!")
    print(f"A szó hosszúsága: {meddig}")
else:
    kerdes = input("Akarod e megváltoztatni az életed számát? (i/n)\t")
    if kerdes == "i":
        try:
            elet  = int(input("Mennyi életed lenne?\t"))
        except:
            print("Számot kértem töki!")
            print("Ha már ilyen vicces hangulatban vagy akkor kevesebb életed lesz! :)")
            elet = 3
    elif kerdes == "n":
        elet = 10
    elif kerdes != "i" or kerdes != "n":
        print("Nincs ilyen opció, akkor ennyi életed lesz: 10")
        elet = 10
    print(f"Ennyi probálkozásod van akkor alapból: {elet}")
    print("________________________________________\n")
    print(f"A szó hosszúsága: {meddig}")
    if 0 > elet:
        print(f"Sajnálom {elet} életed nem lehet,\n 0-nál nagyobb értéket kellet volna megadnod!")
        elet = 10
#________________________________________________________
# maga a program ciklusban
while True:
    if elet == 0 and rajzol_e != "i":
        print(f"Sajnálom elfogytak az életeid Vége a játéknak! A szó amire gondoltam: {kivalaszt}")
        print("<<< GAME OVER >>>")
        break
    if len(szeletelo) == 0:
        print(f"Gratulálok, eltaláltad! A szó amire gondoltam: {kivalaszt}")
        break
    bekeres = input("kérek egy betüt!\t")
    print("")
    if len(bekeres) > 1 and bekeres != "Lócaj_77" and bekeres != "segitseg":
      print(f"Egy karaktert kértem! Nem {len(bekeres)}!")
    if bekeres == "Lócaj_77":
        print("<<< Cheat code activated >>>")
        print(f"Gratulálok, eltaláltad! A szó amire gondoltam: {kivalaszt}")
        break
    if bekeres == "segitseg" and segitseg_szamlalo > 0:
        segitseg_szamlalo = segitseg_szamlalo - 1
        segi = random.choice(szeletelo)
        eltalalt.append(segi)
        szeletelo.remove(segi)
        print(f"Segítség aktiválva, a betű: \"{segi}\"\n")
        print(f"Az eltalált betük eddig: {', '.join(eltalalt)}\n")
        print(f"A rosz betük: {', '.join(rossz)}\n")
    if bekeres == "segitseg" and segitseg_szamlalo == 0:
        print(f"Figy{figy} Segítséget csak kétszer használhatod! :)")
        figy = figy + 1
        if figy == 4:
            print("Szándékos csalási folyamatért büntetés jár!!!\n -3 élet")
            elet = elet - 3
        elif figy == 8:
            print("Túlságosan sokszor szerettél volna segítséget haszálni!\n Ezért a kitartó probálkozásaidnak hála a játékod véget ért!\n")
            elet = 0
    # a program kulcs sora:
    kereso = [szo for szo in szeletelo if bekeres == szo and bekeres != "segitseg"]
    if len(kereso) > 0:
        szeletelo.remove(bekeres)
        eltalalt.append(bekeres)
        print(f"Helyes! Ez a betü: \"{bekeres}\" szerepel a szóban\n")
        print(f"Az eltalált betük eddig: {', '.join(eltalalt)}\n")
        print(f"A rosz betük: {', '.join(rossz)}\n")
    elif len(kereso) == 0 and bekeres != "segitseg" and len(bekeres) == 1:
        elet = elet - 1
        rossz.append(bekeres)
        if rajzol_e == "i":
            rajzol = rajzol + 1
        print(f"Nem, Ez a betű: \"{bekeres}\" NEM szerepel a szóban!\n")
        print(f"A jo betük eddig: {', '.join(eltalalt)}\n")
        print(f"A rosz betük: {', '.join(rossz)}\n")
# innentöl már csak rajzolás van ez már nem lényeges
    if rajzol == 1 and egyszer_1 == 0:
        defi.forward(500)
        egyszer_1 = egyszer_1 + 1
    if rajzol == 2 and egyszer_2 == 0:
        defi.left(180)
        defi.forward(350)
        defi.right(90)
        defi.forward(600)
        egyszer_2 = egyszer_2 + 1
    if rajzol == 3 and egyszer_3 == 0:
        defi.left(180)
        defi.forward(500)
        defi.left(45)
        defi.forward(138)
        defi.left(180)
        defi.forward(138)
        egyszer_3 = egyszer_3 + 1
    if rajzol == 4 and egyszer_4 == 0:
        defi.right(45)
        defi.forward(500)
        defi.right(90)
        defi.forward(250)
        egyszer_4 = egyszer_4 + 1
    if rajzol == 5 and egyszer_5 == 0:
        defi.left(180)
        defi.forward(160)
        defi.left(45)
        defi.forward(128)
        egyszer_5 = egyszer_5 + 1
    if rajzol == 6 and egyszer_6 == 0:
        defi.left(180)
        defi.forward(128)
        defi.right(45)
        defi.forward(145)
        defi.right(90)
        defi.forward(100)
        egyszer_6 = egyszer_6 + 1
    if rajzol == 7 and egyszer_7 == 0:
        defi.penup()
        defi.goto(180,150)
        defi.pendown()
        defi.circle(50)
        egyszer_7 = egyszer_7 + 1
    if rajzol == 8 and egyszer_8 == 0:
        defi.penup()
        defi.goto(225,100)
        defi.pendown()
        defi.forward(200)
        egyszer_8 = egyszer_8 + 1
    if rajzol == 9 and egyszer_9 == 0:
        defi.right(45)
        defi.forward(150)
        defi.left(180)
        defi.forward(150)
        egyszer_9 = egyszer_9 + 1
    if rajzol == 10 and egyszer_10 == 0:
        defi.right(85)
        defi.forward(150)
        defi.left(180)
        defi.forward(150)
        defi.right(410)
        egyszer_10 = egyszer_10 + 1
    if rajzol == 11 and egyszer_11 == 0:
        defi.forward(150)
        defi.left(135)
        defi.forward(150)
        defi.left(180)
        defi.forward(150)
        egyszer_11 = egyszer_11 + 1
    if rajzol == 12 and egyszer_12 == 0:
        defi.right(90)
        defi.forward(150)
        defi.right(140)
        defi.penup()
        defi.forward(700)
        defi.pendown()
        defi.left(180)
        defi.write("<<< Játék Vége >>>", font=("Verdana",
                                    15, "normal"))
        egyszer_12 = egyszer_12 + 1
        print(f"Sajnálom elfogytak a próbálkozásaid, Vége a játéknak! A szó amire gondoltam: {kivalaszt}")
        print("<<< GAME OVER >>>")
        break
        