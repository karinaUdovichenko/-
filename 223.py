print(1)
arr = [i for i in range (1, 51)]
print (*arr)

print(2)
a = [i for i in range (1, 51)]
a.reverse()
print(*a)

print(3)
n = [i**2 for i in range (1,12)]
print(*n)

print(4)
b = [i**2 for i in range (1,12)]
b.reverse()
print(*b)

print(5)
c = [i * 2 for i in range (1,21)]
print(*c)


print(6)
s = [(-1)** i * i ** 2 for i in range (1,11)]
s = [i*(-1) for i in s]
print(*s)


print(7)

print(8)
k = [i if i%2!=0 else i*3 for i in range(1,12)]
print(*k)
