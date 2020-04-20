import copy

m = [["·" for x in range(6)] for y in range(6)]

matriz = copy.deepcopy(m)

m[0][0] = "a"

for x in m:
    print(*x)

for x in matriz:
    print(*x)

