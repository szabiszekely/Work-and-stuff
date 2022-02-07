
'''
A print függvény a megadott szöveg kiírása után sort emel, 
vagyis a következő print függvény már egy újabb sorba ír.
Az alapértelmezett viselkedés azonban felülírható a "t" paraméterrel.
'''
'''
# a kiírást követően a kurzor egy tabulátornyit ugrik
print('Teszt', end='\t')

# a kiírást követően a kurzor a kiírás végén marad
print('Teszt', end='')       


sor = 1
while sor <= 3:
    oszlop = 1
    while oszlop <= 5:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1       
'''  
'''  
szam = int(input("Kérek egy páros számot: "))
'''
szam = 2
darab_karakter = 1
sor = 1
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

darab_karakter = 5
sor = 1
while sor <= 5:
    oszlop = 1
    nulla = 1
    hely = 1
    while hely == darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    while oszlop <= darab_karakter:
        print('. ', end='')
        oszlop = oszlop + 1
    print('')
    hely = hely + 1
    sor = sor + 1 
print("----------")
for i in range(5):
    for j in range(5):
        if i != j:
            print('. ',end="")
        else:
            print('o ',end="")
    print()
