l = [
    [11, 1, 1, 1, 1, 1],
    [11, 1, 1, 1, 1, 1],
    [11, 1, 2, 1, 1, 1],
    [11, 1, 1, 1, 1, 1]
]

for linha in l:
    for coluna in linha:
        if coluna == 2:
            linha[coluna] = 3
    print(linha)

