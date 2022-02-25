x = [1,4,3,6,2,1]
def osszegzes(x):
    a = 0
    for i in x:
        a += i
    return a
print(osszegzes(x))

x = [3,2,9,5,6,12]

def paros_e(x):
    for szam in x:
        if szam % 2 == 0:
            e = True
            break
        else:
            e = False
    return e
   
    
print(paros_e(x))


x = []

bevitel = int(input('Kérek számokat(adj meg egy negatívat ha már nem akarsz többer meg adni): '))
while bevitel >= 0:    
    bevitel = int(input('Kérek számokat(adj meg egy negatívat ha már nem akarsz többer meg adni): '))
    x.append(bevitel)
def haromal_oszthatok(x):
    max = 0
    for szam in x:
        if szam % 3 == 0:
              max += 1
    return max

print(haromal_oszthatok(x))




























































































