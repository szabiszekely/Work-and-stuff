szam=int( input("Kérek egy egész számot: "))
print(type(szam))
'''
sor=input("Kérek egy egész számot: ")
szam=int(sor)
print(type(szam))
'''
if szam <= 0:
    print("A szám negatív")
elif szam == 0:
    print("A szán NULLA")
elif szam % 2 == 0:
    print("páros")
else:
    print("páratlan")

    '''
    if (szam % 2 == 0){
        ....
    }
    '''

    
    print(2 == 2)
    print(2 == 3)
    print(2 < 2)
    print(2 <= 2)
    print(2 == 3)
    print(2 < 2)
    