print ("2+2=",end='')
print (2+2)
print ("Quick Math")

szam=12 #szám
print(szam) #kinyomtatja a számot aka. 12
print(type(szam)) 
print(szam.bit_length()) #ki írja hogy hány bit böl ál a szám
szam=256
print(szam.bit_length())

szam=12.5
print(szam)
print(type(szam))

szam="hello" #kerülendő!!! félrevezető!!!
print(szam)
print(type(szam))

a=9
b=11
print(a+b)

#print(szam+a+b) hibás
print(szam,a+b)
print(szam,a,b)
print(szam,"",a,b,sep="")

print("Vezeték név:",end='')
vezetekNev = input()
keresztNev =("Keresz név:")
print("Üdvözlöm:",vezetekNev, keresztNev)