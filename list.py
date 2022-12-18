lst = []

lst = [(i, i**2 -1) if i%2 == 0 else (i, i**2 +1) for i in range(10)]

for tup in lst:
    print(f"f({tup[0]}) = {tup[1]}")