#tuple
teszt = 1, 2, 3, 1, 3, 1
print(type(teszt))
print(teszt)
teszt = (1, 2, 3, 1, 3, 1)
print(type(teszt))
print(teszt)

#lasza
teszt = [1, 2, 3, 1, 3, 1]
print(type(teszt))
print(teszt)

#halmaz
teszt = {1, 2, 3, 1, 3, 1}
print(type(teszt))
print(teszt)

teszt.add(12)
print(teszt)
print(type(teszt))

teszt.add("alma")
print(teszt)
print(type(teszt))

teszt.add("Alma")
print(teszt)
print(type(teszt))

teszt.add(3-2)
print(teszt)
print(type(teszt))

halmaz = ("ló", 12)
teszt.add(halmaz)
print(teszt)

print(teszt.pop())
print(teszt.pop())
print(teszt)

teszt.remove(3)
print(teszt)

teszt.remove('alma')
print(teszt)

halmaz = ("ló", 12, 6,69)

print(teszt.union(halmaz))
#print(teszt.update(halmaz))
print(teszt)


teszt.clear()
print(teszt)
print(type(teszt))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}
print(set1.intersection(set2))
print(len(set1.intersection(set2)))
