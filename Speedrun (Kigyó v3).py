import random
from time import time

for j in range(1):
    elhelyezett_random_oszlop = [0, 0, 0, 0, 0]
    for i in range(5):
        huzott_oszlop = random.randint(2,9)
        k = 0
        while k < 5:
            if elhelyezett_random_oszlop[k] == huzott_oszlop or huzott_oszlop == 5:
                huzott_oszlop = random.randint(2,9)
                k = 0
            else:
                k += 1
                
               
        elhelyezett_random_oszlop[i] = huzott_oszlop
        


for j in range(1):
    elhelyezett_random_sor = [0, 0, 0, 0, 0]
    for i in range(5):
        huzott_sor = random.randint(2,9)
        k = 0
        while k < 5:
            if elhelyezett_random_sor[k] == huzott_sor or huzott_sor == 5:
                huzott_sor = random.randint(2,9)
                k = 0
            else:
                k += 1
                
              
        elhelyezett_random_sor[i] = huzott_sor
        


elhelyezett_coin_random_oszlop = random.randint(1,10)
elhelyezett_coin_random_sor = random.randint(1,10)


'''
if random_oszlop == 5 and random_sor == 5:
    random_oszlop = random.randint(1,10)
    random_sor = random.randint(1,10)
'''
pont = 0
veszt = 0


darab_össz = 1

elhelyezés_oszlop = 5
elhelyezés_sor = 5

kor = 0
darab = 1

#elhelyezés_sor = int(input('Határozd meg a sort amiben az X elhelyezkedjen: '))
#elhelyezés_oszlop = int(input('Határozd meg az oszlopot ahol az X elhelyezkedjen: '))
while True:
    
    if veszt == 1:
        break



    #AI irányitás
    random_lepes = random.randint(1,4)
    #elöre
    if random_lepes == 1:
        for lep1 in elhelyezett_random_sor:
            lep1 -= 1
        

    #hátra
    if random_lepes == 2:
        for lep2 in elhelyezett_random_sor:
            lep2 += 1

    #balra
    if random_lepes == 3:
        for lep3 in elhelyezett_random_oszlop:
            lep3 -= 1

    #jobbra
    if random_lepes == 4:
        for lep4 in elhelyezett_random_oszlop:
            lep4 += 1
    

    for i in elhelyezett_random_sor:
        #Hogyha az AI ki megy a map szélére
        if i >= 14:
            for nop1 in elhelyezett_random_sor:
                nop1 -= 1
            print('ki ment alul az elenfél a pályárol')
    for i in elhelyezett_random_sor:    
        if i <= -3:
            for nop2 in elhelyezett_random_sor:
                nop2 += 1
            print('ki ment felül az elenfél a pályárol')
    for i in elhelyezett_random_oszlop:    
        if i >= 14:
            for nop3 in elhelyezett_random_oszlop:
                nop3 -= 1
            print('ki ment jobb az elenfél a pályárol')
    for i in elhelyezett_random_oszlop:    
        if i <= -3:
            for nop4 in elhelyezett_random_oszlop:
                nop4 += 1
            print('ki ment bal az elenfél a pályárol')

    
        

    sor = 1
    while sor <= 10:
        oszlop = 1
        while oszlop <= 10:
            
            for i in elhelyezett_random_sor:
                for j in elhelyezett_random_oszlop:
                    if sor == i and oszlop == j and darab_össz != 10:
                        print('Q ', end='')
                        oszlop = oszlop + 1
                    elif darab == darab_össz or darab_össz == 10:
                        break
                darab += 1

            
            
            
            if sor == elhelyezés_sor and oszlop == elhelyezés_oszlop:
                print('P ', end='')
                oszlop = oszlop + 1
                  

            if sor == elhelyezett_coin_random_sor and oszlop == elhelyezett_coin_random_oszlop:
                print('O ', end='')

                oszlop = oszlop + 1
            else:
                print('X ', end='')
                oszlop = oszlop + 1
        print('')
        sor = sor + 1  
    
    #Hogyha hozzá érsz
    for i in elhelyezett_random_oszlop:
        for j in elhelyezett_random_sor:
            if i == elhelyezés_oszlop and j == elhelyezés_sor:
                print('Vesztetél')
                veszt += 1

    for i in elhelyezett_random_oszlop:
        for j in elhelyezett_random_sor:
            if elhelyezett_coin_random_oszlop == i and elhelyezett_coin_random_sor == j:
                elhelyezett_coin_random_oszlop = random.randint(1,10)
                elhelyezett_coin_random_sor = random.randint(1,10)

    if elhelyezett_coin_random_oszlop == elhelyezés_oszlop and elhelyezett_coin_random_sor == elhelyezés_sor:
        pont += 1
        elhelyezett_coin_random_oszlop = random.randint(1,10)
        elhelyezett_coin_random_sor = random.randint(1,10)
    
    
    
   
    
    #Hogyha a Játékos kimegy a pálya szélére
    if elhelyezés_sor >= 11 or elhelyezés_sor <= 0:
        print('Ki mentél a pályárol >:D')
        break
    if elhelyezés_oszlop >= 11 or elhelyezés_oszlop <= 0:
        print('Ki mentél a pályárol >:D')
        break  
    
    #Játékos irányitás
    köv_move = input('Mere mennyen az X következönek("w" = fel,"s" = lefele,"a" = balra,"d" = jobbra): ')
    #elöre
    if köv_move == 'w':
        elhelyezés_sor -= 1
    
    #hátra
    if köv_move == 's':
        elhelyezés_sor += 1
    
    #balra
    if köv_move == 'a':
        elhelyezés_oszlop -= 1
    
    #jobbra
    if köv_move == 'd':
        elhelyezés_oszlop += 1
    
    #ne csináljon semmit
    else:
        elhelyezés_oszlop += 0
        elhelyezés_sor += 0

    if kor == 3 and darab_össz != 10:
        darab_össz += 1
        kor -= 3
    else:
        kor = -1

    if kor >= 0:
        kor += 1

print('Enyi coin-t tudtál szerezni: ', pont)


'''
for j in range(1):
    oszlop_halmaz = [0]
    for i in range(1):
        random_oszlop = random.randint(1,10)
        k = 0
        while k < 1:
            if oszlop_halmaz[k] == random_oszlop or random_oszlop == 5:
                random_oszlop = random.randint(1,10)
                k = 0
            else:
                k += 1
                
               
        oszlop_halmaz[i] = random_oszlop

for j in range(1):
    sor_halmaz = [0]
    for i in range(1):
        random_sor = random.randint(1,10)
        k = 0
        while k < 1:
            if sor_halmaz[k] == random_sor or random_sor == 5:
                random_sor = random.randint(1,10)
                k = 0
            else:
                k += 1
                
               
        sor_halmaz[i] = random_oszlop
'''

'''
print('AI sor',elhelyezett_random_sor)
print('AI oszlop',elhelyezett_random_oszlop)

print('Játékos sor',elhelyezés_sor)
print('Játékos oszlop',elhelyezés_oszlop)
'''




