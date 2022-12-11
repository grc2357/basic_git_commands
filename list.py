lst = []

lst = [(i, i**2 -1) if i%2 == 0 else (i, i**2 +1) for i in range(10)]

print(lst)