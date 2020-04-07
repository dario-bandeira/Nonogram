a = 1
b = 2


def c():
    global a, b
    a = 9
    b = 9


c()
print(a, b)
