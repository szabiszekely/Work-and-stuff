import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().date())
print(datetime.datetime.now().year)
print(datetime.datetime.now().hour)

szoveg=12
print(type(szoveg))

szoveg="12"
print(type(szoveg))

b=szoveg*6
print(b)
print("*"*20)

# c=szoveg+12 - hibás
c=szoveg+"12"
print(c)

d= int(szoveg)
print(type(d))

d= int(szoveg)+12
print(d)

print(szoveg+str(d))

#szoveg="11 alma"
#print(int(szoveg))

szoveg="11.56"
#print(int(szoveg))
#print(type(12.4))
print(float(szoveg)*2)
tizedes=float(szoveg)*2
egesz=int(tizedes)
print(egesz)

gyumolcsok=["alma","körte","barack","alma"]
print(type(gyumolcsok))
print(gyumolcsok)

gyumolcsok={"alma","körte","barack","alma"}
print(type(gyumolcsok))
print(gyumolcsok)