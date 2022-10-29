#1
arr = [i for i in range(1, 51)]
print(*arr)

#2
a = [i for i in range(1, 51)]
a.reverse()
print(*a)

#3
n = [i**2 for i in range(1,12)]
print(*n)

#4
b = [i**2 for i in range(1,12)]
b.reverse()
print(*b)

#5
c = [i * 2 for i in range(1,21)]
print(*c)


#6
s = [(-1)** i * i ** 2 for i in range(1,11)]
s = [i*(-1) for i in s]
print(*s)


#7
d = []
k = 0
for i in d:
    d.append(i)
    k += 1
print(d)
