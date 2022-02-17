import random
from time import time

elhelyezett_random_oszlop = random.randint(2,9)
elhelyezett_random_sor = random.randint(2,9)

'''
if random_oszlop == 5 and random_sor == 5:
    random_oszlop = random.randint(1,10)
    random_sor = random.randint(1,10)
'''




elhelyezés_oszlop = 5
elhelyezés_sor = 5


#elhelyezés_sor = int(input('Határozd meg a sort amiben az X elhelyezkedjen: '))
#elhelyezés_oszlop = int(input('Határozd meg az oszlopot ahol az X elhelyezkedjen: '))
while True:
    
    #AI irányitás
    random_lepes = random.randint(1,4)
    #elöre
    if random_lepes == 1:
        elhelyezett_random_sor -= random.randint(1,2)

    #hátra
    if random_lepes == 2:
        elhelyezett_random_sor += random.randint(1,2)

    #balra
    if random_lepes == 3:
        elhelyezett_random_oszlop -= random.randint(1,2) 

    #jobbra
    if random_lepes == 4:
        elhelyezett_random_oszlop += random.randint(1,2)

    
    #Hogyha az AI ki megy a map szélére
    if elhelyezett_random_sor >= 10:
        elhelyezett_random_sor -= 4
        print('ki ment alul az elenfél a pályárol')
    
    if elhelyezett_random_sor <= 1:
        elhelyezett_random_sor += 4
        print('ki ment felül az elenfél a pályárol')
    
    if elhelyezett_random_oszlop >= 10:
        elhelyezett_random_oszlop -= 4
        print('ki ment jobb az elenfél a pályárol')
    
    if elhelyezett_random_oszlop <= 1:
        elhelyezett_random_oszlop += 4
        print('ki ment bal az elenfél a pályárol')

    
        

    sor = 1
    while sor <= 10:
        oszlop = 1
        while oszlop <= 10:
            
            if sor == elhelyezés_sor and oszlop == elhelyezés_oszlop:
                print('X ', end='')
                oszlop = oszlop + 1  
                  
            if sor == elhelyezett_random_sor and oszlop == elhelyezett_random_oszlop:
                print('[ ', end='')
                
                oszlop = oszlop + 1
                
            else:
                print('O ', end='')
                oszlop = oszlop + 1
        print('')
        sor = sor + 1  
    
    #Hogyha hozzá érsz
    if elhelyezett_random_oszlop == elhelyezés_oszlop and elhelyezett_random_sor == elhelyezés_sor:
        print('Vesztetél')
        break
    
    
    
    print('AI sor',elhelyezett_random_sor)
    print('AI oszlop',elhelyezett_random_oszlop)

    print('Játékos sor',elhelyezés_sor)
    print('Játékos oszlop',elhelyezés_oszlop)

   
    
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