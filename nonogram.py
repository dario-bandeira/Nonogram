import copy


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


m = [["·" for x in range(16)] for y in range(16)]

# MATRIZ 1 (flor)
"""
m[0][15] = [1, 2, 3]
m[1][15] = [2, 4, 3]
m[2][15] = [2, 8]
m[3][15] = [3, 1, 6]
m[4][15] = [5, 5]
m[5][15] = [4, 4]
m[6][15] = [3, 4]
m[7][15] = [1, 4, 5]
m[8][15] = [1, 8, 1]
m[9][15] = [2, 6, 1]
m[10][15] = [3, 4, 3]
m[11][15] = [4, 2, 4]
m[12][15] = [4, 2, 4]
m[13][15] = [5, 2, 4]
m[14][15] = [11]

m[15][0] = [5]
m[15][1] = [5]
m[15][2] = [5, 5]
m[15][3] = [8, 4]
m[15][4] = [6, 3]
m[15][5] = [6, 2]
m[15][6] = [4, 4, 1]
m[15][7] = [3, 7]
m[15][8] = [4, 8]
m[15][9] = [10, 1]
m[15][10] = [8, 3]
m[15][11] = [8, 4]
m[15][12] = [8, 5]
m[15][13] = [5, 4]
m[15][14] = [1, 4]

matrix_correta = [
    ["x", "x", "x", 0, "x", "x", "x", 0, 0, "x", "x", "x", 0, 0, 0],
    ["x", "x", 0, 0, "x", "x", 0, 0, 0, 0, "x", 0, 0, 0, "x"],
    ["x", "x", 0, 0, "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, "x"],
    ["x", "x", 0, 0, 0, "x", 0, "x", 0, 0, 0, 0, 0, 0, "x"],
    ["x", "x", 0, 0, 0, 0, 0, "x", "x", 0, 0, 0, 0, 0, "x"],

    ["x", "x", 0, 0, 0, 0, "x", "x", "x", 0, 0, 0, 0, "x", "x"],
    ["x", "x", "x", 0, 0, 0, "x", "x", "x", 0, 0, 0, 0, "x", "x"],
    [0, "x", "x", 0, 0, 0, 0, "x", 0, 0, 0, 0, 0, "x", "x"],
    [0, "x", "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, "x", "x", 0],
    [0, 0, "x", "x", "x", 0, 0, 0, 0, 0, 0, "x", "x", "x", 0],

    [0, 0, 0, "x", "x", "x", 0, 0, 0, 0, "x", "x", 0, 0, 0],
    [0, 0, 0, 0, "x", "x", "x", 0, 0, "x", "x", 0, 0, 0, 0],
    ["x", 0, 0, 0, 0, "x", "x", 0, 0, "x", 0, 0, 0, 0, "x"],
    ["x", 0, 0, 0, 0, 0, "x", 0, 0, "x", 0, 0, 0, 0, "x"],
    ["x", "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "x", "x"],
]
"""

# MATRIZ 2 (nota musical)
"""
m[0][15] = [5]
m[1][15] = [4, 1]
m[2][15] = [4, 1, 5]
m[3][15] = [11, 1]
m[4][15] = [9, 1]
m[5][15] = [3, 4, 1]
m[6][15] = [3, 1, 3]
m[7][15] = [1, 1, 3]
m[8][15] = [1, 3, 5]
m[9][15] = [3, 10]
m[10][15] = [15]
m[11][15] = [15]
m[12][15] = [10, 3]
m[13][15] = [5, 3]
m[14][15] = [3]

m[15][0] = [4, 4]
m[15][1] = [6, 6]
m[15][2] = [14]
m[15][3] = [4, 1, 6]
m[15][4] = [2, 2, 4]
m[15][5] = [1, 2, 4]
m[15][6] = [1, 2, 6]
m[15][7] = [14]
m[15][8] = [1, 3, 6]
m[15][9] = [1, 1, 4]
m[15][10] = [2, 2, 4]
m[15][11] = [1, 7]
m[15][12] = [11]
m[15][13] = [1, 6]
m[15][14] = [1, 4]

matrix_correta = [
    ["x","x","x","x",0,0,0,0,0,"x","x","x","x","x","x"],
    ["x",0,0,0,0,"x","x",0,"x","x","x","x","x","x","x"],
    [0,0,0,0,"x","x","x",0,"x","x",0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,"x",0,"x","x"],
    [0,0,0,0,0,0,0,0,0,"x","x","x",0,"x","x"],

    [0,0,0,"x","x","x","x",0,0,0,0,"x",0,"x","x"],
    ["x",0,0,0,"x","x","x",0,"x","x",0,0,0,"x","x"],
    ["x","x",0,"x","x","x","x",0,"x","x","x",0,0,0,"x"],
    ["x","x",0,"x","x","x",0,0,0,"x",0,0,0,0,0],
    ["x",0,0,0,"x",0,0,0,0,0,0,0,0,0,0],

    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,"x",0,0,0,"x"],
    [0,0,0,0,0,"x",0,0,0,"x","x","x","x","x","x"],
    ["x",0,0,0,"x","x","x","x","x","x","x","x","x","x","x"]
]
"""

# MATRIZ 3 (comedouro de pássaro)
"""
m[0][15] = [1]
m[1][15] = [1, 1]
m[2][15] = [3]
m[3][15] = [1]
m[4][15] = [3]

m[5][15] = [5]
m[6][15] = [3, 1]
m[7][15] = [3, 1]
m[8][15] = [3, 1, 2]
m[9][15] = [4, 1, 2, 2]

m[10][15] = [3, 1, 6]
m[11][15] = [4, 3, 3]
m[12][15] = [4, 3, 4]
m[13][15] = [2, 1, 3, 4]
m[14][15] = [1, 9]

m[15][0] = [2]
m[15][1] = [3]
m[15][2] = [3]
m[15][3] = [6]
m[15][4] = [5, 1]

m[15][5] = [1, 2, 1]
m[15][6] = [2, 11]
m[15][7] = [6, 4]
m[15][8] = [3, 11]
m[15][9] = [1, 1, 1]

m[15][10] = [2, 1]
m[15][11] = [6]
m[15][12] = [4]
m[15][13] = [6]
m[15][14] = [4, 2]

matrix_correta = [
    ["x", "x", "x", "x", "x", "x", "x", "x", 0, "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", 0, "x", 0, "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", 0, 0, 0, "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", "x", 0, "x", "x", "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", 0, 0, 0, "x", "x", "x", "x", "x", "x"],

    ["x", "x", "x", "x", "x", 0, 0, 0, 0, 0, "x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", 0, 0, 0, "x", "x", "x", "x", "x", 0],
    ["x", "x", "x", "x", "x", "x", 0, 0, 0, "x", "x", "x", "x", "x", 0],
    ["x", "x", "x", "x", 0, 0, 0, "x", 0, "x", "x", "x", "x", 0, 0],
    ["x", "x", "x", 0, 0, 0, 0, "x", 0, "x", 0, 0, "x", 0, 0],

    ["x", "x", 0, 0, 0, "x", 0, "x", 0, 0, 0, 0, 0, 0, "x"],
    ["x", 0, 0, 0, 0, "x", 0, 0, 0, "x", "x", 0, 0, 0, "x"],
    ["x", 0, 0, 0, 0, "x", 0, 0, 0, "x", "x", 0, 0, 0, 0],
    [0, 0, "x", 0, "x", "x", 0, 0, 0, "x", "x", 0, 0, 0, 0],
    [0, "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, "x", "x", "x"]
]
"""

# MATRIZ 4 (mãe terra)
"""
m[0][15] = [5]
m[1][15] = [8]
m[2][15] = [4, 4]
m[3][15] = [4, 4]
m[4][15] = [3, 4, 3]

m[5][15] = [3, 1, 2, 3]
m[6][15] = [3, 2, 2]
m[7][15] = [3, 4, 1]
m[8][15] = [4, 6]
m[9][15] = [5, 5]

m[10][15] = [10]
m[11][15] = [3, 6]
m[12][15] = [2, 4]
m[13][15] = [8]
m[14][15] = [8]

m[15][0] = [2]
m[15][1] = [1, 4]
m[15][2] = [4, 6]
m[15][3] = [10, 2]
m[15][4] = [11, 2]

m[15][5] = [3, 9]
m[15][6] = [2, 1, 5]
m[15][7] = [2, 2, 5]
m[15][8] = [3, 1, 8]
m[15][9] = [12, 2]

m[15][10] = [3, 5, 1]
m[15][11] = [3, 3]
m[15][12] = [3, 2]
m[15][13] = [5]
m[15][14] = [2]

matrix_correta = [
    ["x", "x", "x", "x", "x", 0, 0, 0, 0, 0, "x", "x", "x", "x", "x"],
    ["x", "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, "x", "x", "x", "x"],
    ["x", "x", 0, 0, 0, 0, "x", "x", 0, 0, 0, 0, "x", "x", "x"],
    ["x", 0, 0, 0, 0, "x", "x", "x", "x", 0, 0, 0, 0, "x", "x"],
    ["x", "x", 0, 0, 0, "x", 0, 0, 0, 0, "x", 0, 0, 0, "x"],

    ["x", "x", 0, 0, 0, "x", "x", 0, "x", 0, 0, "x", 0, 0, 0],
    ["x", "x", "x", 0, 0, 0, "x", "x", "x", 0, 0, "x", "x", 0, 0],
    ["x", "x", "x", 0, 0, 0, "x", "x", 0, 0, 0, 0, "x", 0, "x"],
    ["x", "x", 0, 0, 0, 0, "x", "x", 0, 0, 0, 0, 0, 0, "x"],
    ["x", 0, 0, 0, 0, 0, "x", "x", 0, 0, 0, 0, 0, "x", "x"],

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "x", "x", "x", "x", "x"],
    [0, 0, 0, "x", 0, 0, 0, 0, 0, 0, "x", "x", "x", "x", "x"],
    ["x", 0, 0, "x", "x", 0, 0, 0, 0, "x", "x", "x", "x", "x", "x"],
    ["x", "x", 0, 0, 0, 0, 0, 0, 0, 0, "x", "x", "x", "x", "x"],
    ["x", "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, "x", "x", "x", "x"]
]
"""

# MATRIZ 5

m[0][15] = [2]
m[1][15] = [4, 9]
m[2][15] = [4, 10]
m[3][15] = [2, 10]
m[4][15] = [10]

m[5][15] = [9]
m[6][15] = [6]
m[7][15] = [2, 1, 6]
m[8][15] = [6, 2, 2]
m[9][15] = [2, 4]

m[10][15] = [1, 3, 2]
m[11][15] = [1, 9, 3]
m[12][15] = [15]
m[13][15] = [9]
m[14][15] = [2]

m[15][0] = [2, 1, 2]
m[15][1] = [4, 2, 1]
m[15][2] = [4, 2, 2]
m[15][3] = [2, 2, 1, 3]
m[15][4] = [3, 2, 2]

m[15][5] = [4, 1, 2]
m[15][6] = [7, 3]
m[15][7] = [7, 4]
m[15][8] = [13]
m[15][9] = [13]

m[15][10] = [7, 3]
m[15][11] = [7, 1, 2]
m[15][12] = [4, 1, 3]
m[15][13] = [3, 7]
m[15][14] = [2, 7]

matrix_correta = [
    ["x", 0, 0, "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    [0, 0, 0, 0, "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["x", 0, 0, "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "x"],
    ["x", "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "x", "x"],

    ["x", "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, "x", "x", "x"],
    ["x", "x", "x", "x", "x", "x", 0, 0, 0, 0, 0, 0, "x", "x", "x"],
    ["x", 0, 0, "x", 0, "x", 0, 0, 0, 0, 0, 0, "x", "x", "x"],
    [0, 0, 0, 0, 0, 0, "x", "x", 0, 0, "x", "x", "x", 0, 0],
    ["x", "x", "x", "x", "x", "x", "x", "x", 0, 0, "x", 0, 0, 0, 0],

    ["x", "x", "x", 0, "x", "x", "x", 0, 0, 0, "x", "x", "x", 0, 0],
    [0, "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, "x", 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["x", "x", "x", "x", "x", "x", 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", 0, 0]
]

girado = False


def girar_horario(a):
    global girado
    a.reverse()
    N = len(a[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = a[i][j]
            a[i][j] = a[N - 1 - j][i]
            a[N - 1 - j][i] = a[N - 1 - i][N - 1 - j]
            a[N - 1 - i][N - 1 - j] = a[j][N - 1 - i]
            a[j][N - 1 - i] = temp
    girado = False


def girar_antihorario(m):
    global girado
    m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]
    m.reverse()
    girado = True
    return m


def executar_passos(debug=False):
    global m
    passos = {
        passo1: '',
        passo2: '',
        passo3: '',
        passo4: '',
        passo5: '',
        passo6: '',
        passo7: '',
        passo8: '',
    }
    for key, val in passos.items():
        if debug:
            print("###########")
            print("###########")
            print(key)
            print("###########")
            print("###########")
            key(True)
            m = girar_antihorario(m)
            key(True)
            girar_horario(m)
        else:
            key()
            m = girar_antihorario(m)
            key()
            girar_horario(m)


def print_matrix(ll=0, cc=0):
    print('{: <2} '.format("   0 1 2 3 4 5 6 7 8 9 10  12  14"))
    for i_x, x in enumerate(m[:15]):
        print('{: <2} '.format(i_x), end='')
        for i_y, y in enumerate(x):
            if i_x == ll and i_y == cc:
                print(bcolors.WARNING + str(y) + bcolors.ENDC, "", end='')
            else:
                if y == 0:
                    print(bcolors.OKBLUE + str(y) + bcolors.ENDC, "", end='')
                elif y == "x":
                    print(bcolors.FAIL + y + bcolors.ENDC, "", end='')
                else:
                    print(y, "", end='')
        print()
    print("   ", end='')

    for x in m[15]:
        print('{: <2}'.format(x[0]), end='')
    print()
    print("   ", end='')

    for x in m[15]:
        if len(x) >= 2:
            print('{: <2}'.format(x[1]), end='')
        else:
            print('{: <2}'.format(" "), end='')
    print()
    print("   ", end='')
    for x in m[15]:
        if len(x) >= 3:
            print('{: <2}'.format(x[2]), end='')
        else:
            print('{: <2}'.format(" "), end='')
    print()


def print_matrix_final():
    print("- - - - - - - - - - - - - - - - - - -")
    for i_x, x in enumerate(m[:15]):
        for i_y, y in enumerate(x[:15]):
            if i_y % 5 == 0:
                print("| ", end='')
            if y == 0:
                print(bcolors.OKBLUE + str(y) + bcolors.ENDC, "", end='')
            elif y == "x":
                print(bcolors.FAIL + y + bcolors.ENDC, "", end='')
            else:
                print(y, "", end='')
        print("|")
        if (i_x + 1) % 5 == 0:
            print("- - - - - - - - - - - - - - - - - - -")


def comparar():
    errado = False
    for linha in range(15):
        for coluna in range(15):
            if m[linha][coluna] != "·" and m[linha][coluna] != matrix_correta[linha][coluna]:
                print("errado linha", linha, "coluna", coluna)
                errado = True

    if errado:
        return False
    else:
        print(bcolors.OKGREEN + "Nenhum erro encontrado." + bcolors.ENDC)
        return True


def preenche_barra_no_espaco(linha, espaco, tamanho_da_barra, debug=False):
    global m
    tamanho_do_espaco = espaco[1] - espaco[0] + 1
    vazio = True
    for coluna in m[linha][espaco[0]:espaco[1] + 1]:
        if coluna == 0:
            vazio = False
            break
    # se o espaço tá vazio, e a barra é maior que a metade dele:
    if vazio and tamanho_da_barra > (espaco[1] - espaco[0] + 1) // 2:
        # aquele calculo massa lá
        for coluna in range(espaco[1] - tamanho_da_barra + 1, espaco[0] + tamanho_da_barra):
            m[linha][coluna] = 0
            if debug:
                print_matrix(linha, coluna)

    # se não tá vazio:
    if not vazio:
        # esquerda pra direita
        # quando encontrar um 0, "pular" a barra, o resto é "x"
        em_aberto = False
        barra_aux = tamanho_da_barra
        novo_fim = ""
        for coluna in range(espaco[0], espaco[1] + 1):
            if m[linha][coluna] == 0:
                em_aberto = True
            if em_aberto:
                if barra_aux:
                    barra_aux -= 1
                    if not barra_aux:
                        novo_fim = coluna
                else:
                    m[linha][coluna] = "x"
                    if debug:
                        print_matrix(linha, coluna)

        # mesma coisa da direita pra esquerda.
        em_aberto = False
        barra_aux = tamanho_da_barra
        novo_inicio = ""
        for coluna in range(espaco[1], espaco[0] - 1, -1):
            if m[linha][coluna] == 0:
                em_aberto = True
            if em_aberto:
                if barra_aux:
                    barra_aux -= 1
                    if not barra_aux:
                        novo_inicio = coluna
                else:
                    m[linha][coluna] = "x"
                    if debug:
                        print_matrix(linha, coluna)

        if novo_inicio == "":
            novo_inicio = espaco[0]
        if novo_fim == "":
            novo_fim = espaco[1]
        espaco = [novo_inicio, novo_fim]
        for coluna in range(espaco[1] - tamanho_da_barra + 1, espaco[0] + tamanho_da_barra):
            m[linha][coluna] = 0
            if debug:
                print_matrix(linha, coluna)


def matriz_completa():
    for linha in range(15):
        for coluna in range(15):
            if m[linha][coluna] == "·":
                return False
    return True


def resolve(debug=False):
    global m
    matriz_de_comparacao = copy.deepcopy(m)
    quantos_passos_foi_preciso = 0

    while True:
        executar_passos(True if debug else False)
        quantos_passos_foi_preciso += 1

        if m == matriz_de_comparacao:
            print_matrix()
            print("O algoritmo não evoluiu mais depois de", quantos_passos_foi_preciso, "repetições.")
            comparar()
            break

        matriz_de_comparacao = copy.deepcopy(m)

        if matriz_completa():
            print_matrix()
            print("Resolvido depois de", quantos_passos_foi_preciso, "repetições.")
            comparar()
            break


# # # PASSOS # # #


def passo1(debug=False):
    """Achar na linha um número maior ou igual a 8 e
    preencher a barra a partir do meio da linha.
    Usar os números vizinhos pra preencher ao redor
    da barra, considerando os espaços.
    """
    linhas_que_tem_maior_igual_8 = []
    for i, x in enumerate(m[:15]):
        if max(x[15]) >= 8:
            linhas_que_tem_maior_igual_8.append(i)

    for linha in linhas_que_tem_maior_igual_8:

        quantas_barras_tem_na_linha = len(m[linha][15])
        indice_do_maior = m[linha][15].index(max(m[linha][15]))
        tamanho_da_barra = ((max(m[linha][15]) - 7) * 2) - 1

        marcar_x_depois = 0
        marcar_x_antes = 0
        espacos_antes = 0
        espacos_depois = 0

        if quantas_barras_tem_na_linha > 1:  # tem mais de 1 número
            if indice_do_maior < quantas_barras_tem_na_linha - 1:  # tem barra depois do maior
                espacos_depois = (quantas_barras_tem_na_linha - (indice_do_maior + 1))
                for n_barra in m[linha][15][indice_do_maior + 1:]:
                    marcar_x_depois += n_barra
                marcar_x_depois += espacos_depois

            if indice_do_maior != 0:  # tem barra antes do maior
                espacos_antes = indice_do_maior
                for n_barra in m[linha][15][:indice_do_maior]:
                    marcar_x_antes += n_barra
                marcar_x_antes += espacos_antes

        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_depois):
            if debug:
                print_matrix(linha, guia)
            m[linha][guia] = 0
            guia -= 1

        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_antes):
            if debug:
                print_matrix(linha, guia)
            m[linha][guia] = 0
            guia += 1


def passo2(debug=False):
    """Ver se os números dos extremos são o maior e conferir se
    a barra dele está completa. Se tiver, marcar o espaço restante
    com X e conferir a próxima barra.
    """
    for linha in range(15):
        # se a última barra da linha é a maior:
        if m[linha][15][-1] == max(m[linha][15]):
            em_aberto = False
            tamanho_da_ultima_barra = 0
            # definindo início e fim da barra
            for coluna in range(14, -1, -1):
                if m[linha][coluna] == 0 and not em_aberto:
                    t = coluna
                    em_aberto = True
                if m[linha][coluna] != 0 and em_aberto:
                    c = coluna
                    tamanho_da_ultima_barra = t - c
                    break
            # se essa é realmente a última barra
            if m[linha][15][-1] == tamanho_da_ultima_barra:
                # se a última casa da linha não é zero:
                if m[linha][14] != 0:
                    for coluna in range(14, -1, -1):
                        if m[linha][coluna] != 0:
                            m[linha][coluna] = "x"
                            if debug:
                                print_matrix(linha, coluna)
                        else:
                            break
                m[linha][c] = "x"
                if debug:
                    print_matrix(linha, c)


def passo3(debug=False):
    """Ver se tem 'zero' encostado nas paredes.
    A partir dele, desenhar os seguintes e marcar o
    fim com um X.
    -ou-
    Se a primeira casa NÃO for zero, ir contando
    a partir da borda e quando encontrar um
    zero, pintar os seguintes até completar o
    número em questão, mas nesse caso não marca o
    fim com X. Lembrar de ignorar os X que aparecem
    desde o começo da linha.
    """
    # pra direita
    for linha in range(15):
        comecar_por_aqui = 0
        barra_cheia = False
        tamanho_da_barra = m[linha][15][0]
        em_aberto = False

        # ignorando sequencia de x inicial, se houver
        for coluna in range(15):
            if m[linha][coluna] != "x":
                comecar_por_aqui = coluna
                break

        if m[linha][comecar_por_aqui] == 0:
            barra_cheia = True

        for coluna in range(comecar_por_aqui, comecar_por_aqui + tamanho_da_barra):
            if m[linha][coluna] == 0 and not em_aberto:
                em_aberto = True
            if m[linha][coluna] != 0 and em_aberto:
                m[linha][coluna] = 0
                if debug:
                    print_matrix(linha, coluna)

        if barra_cheia and comecar_por_aqui + tamanho_da_barra + 1 < 15:
            m[linha][comecar_por_aqui + tamanho_da_barra] = "x"
            if debug:
                print_matrix(linha, comecar_por_aqui + tamanho_da_barra)

    # pra esquerda
    for linha in range(15):
        comecar_por_aqui = 0
        barra_cheia = False
        tamanho_da_barra = m[linha][15][-1]
        em_aberto = False
        # ignorando sequencia de x inicial, se houver
        for coluna in range(14, -1, -1):
            if m[linha][coluna] != "x":
                comecar_por_aqui = coluna
                break

        if m[linha][comecar_por_aqui] == 0:
            barra_cheia = True

        for coluna in range(comecar_por_aqui, comecar_por_aqui - tamanho_da_barra, -1):
            if m[linha][coluna] == 0 and not em_aberto:
                em_aberto = True
            if m[linha][coluna] != 0 and em_aberto:
                m[linha][coluna] = 0
                if debug:
                    print_matrix(linha, coluna)

        if barra_cheia and comecar_por_aqui - tamanho_da_barra > 0:
            m[linha][comecar_por_aqui - tamanho_da_barra] = "x"
            if debug:
                print_matrix(linha, comecar_por_aqui - tamanho_da_barra)


def passo4(debug=False):
    """A partir da borda, conferir se a primeira barra
    cabe no primeiro espaço vazio. Se não couber,
    preencher o espaço com X.
    """
    # pra direita
    for linha in range(15):
        tamanho_do_primeiro_espaco = 0
        for coluna in range(15):
            if m[linha][coluna] != "x":
                tamanho_do_primeiro_espaco += 1
            else:
                break
        if tamanho_do_primeiro_espaco < m[linha][15][0]:
            for voltando in range(coluna, -1, -1):
                m[linha][voltando] = "x"
                if debug:
                    print_matrix(linha, voltando)

    # pra esquerda
    for linha in range(15):
        tamanho_do_ultimo_espaco = 0
        for coluna in range(14, -1, -1):
            if m[linha][coluna] != "x":
                tamanho_do_ultimo_espaco += 1
            else:
                break

        if tamanho_do_ultimo_espaco < m[linha][15][-1]:
            for voltando in range(coluna, 15):
                m[linha][voltando] = "x"
                if debug:
                    print_matrix(linha, voltando)


def passo5(debug=False):
    """Quebrar as linhas (e colunas) em pedaços usando os X's como divisor.
    Conferir se o número de pedaços é o mesmo número de
    barras da linha. Se for, e se não couberem duas
    barras em um único espaço, sabemos que cada barra está dentro de
    cada pedaço, então é preencher os espaços que são certeza. Assim:

    SE o número em questão é maior que a metade do espaço:
    Conta da esquerda pra direita e marca o último quadrado.
    Depois da direita pra esquerda e pinta todos a partir do pintado
    anteriormente, até completar o número. Depois contar da esquerda
    pra direita a partir do primeiro quadrado pintado o número em
    questão. Fazer a mesma coisa da direita pra esquerda. Se a
    barra estiver completa, marcar os espaços livres com X.
    """
    for linha in range(15):
        comecar_por_aqui = 0
        tamanho_de_cada_parte = []
        medindo = 0
        for coluna in range(15):
            if m[linha][coluna] == "x":
                comecar_por_aqui += 1
            else:
                break

        inicio_e_fim_de_cada_parte = [[comecar_por_aqui]]

        # definindo a coluna inicial e final de cada espaço na linha
        for coluna in range(comecar_por_aqui, 15):
            if m[linha][coluna] != "x":
                medindo += 1
            if m[linha][coluna] == "x" and coluna != 14:
                inicio_e_fim_de_cada_parte[-1].append(coluna - 1)
                if m[linha][coluna + 1] == "x":
                    continue
                if m[linha][coluna + 1] != "x":
                    tamanho_de_cada_parte.append(medindo)
                    medindo = 0
                    inicio_e_fim_de_cada_parte.append([coluna + 1])

        if len(inicio_e_fim_de_cada_parte[-1]) == 1:
            inicio_e_fim_de_cada_parte[-1].append(14)
        tamanho_de_cada_parte.append(medindo)

        # nº de espaços = nº de barras
        if len(tamanho_de_cada_parte) == len(m[linha][15]):
            barras = m[linha][15]
            cabe_mais_de_um = False

            # conferindo se cabe mais de uma barra no mesmo espaço
            for i, tamanho in enumerate(tamanho_de_cada_parte):
                if len(tamanho_de_cada_parte) > 1:  # se tem mais de uma parte
                    if i == 0:  # primeira casa
                        if tamanho >= barras[i] + barras[i + 1] + 1:
                            cabe_mais_de_um = True
                    elif i == len(tamanho_de_cada_parte) - 1:  # última casa
                        if tamanho >= barras[i - 1] + barras[i] + 1:
                            cabe_mais_de_um = True
                    else:  # do meio
                        if (tamanho >= barras[i - 1] + barras[i] + 1 or
                                tamanho >= barras[i] + barras[i + 1] + 1):
                            cabe_mais_de_um = True

            # conferindo se todos os espaços já tem preenchimento
            tem_espaco_vazio = False
            for espaco in inicio_e_fim_de_cada_parte:
                este_espaco_vazio = True
                for coluna in range(espaco[0], espaco[1] + 1):
                    if m[linha][coluna] != "·":
                        este_espaco_vazio = False
                        break
                if este_espaco_vazio:
                    tem_espaco_vazio = True
                    break

            if not cabe_mais_de_um or not tem_espaco_vazio:
                for i, espaco in enumerate(inicio_e_fim_de_cada_parte):
                    preenche_barra_no_espaco(linha, espaco, barras[i], True if debug else False)

        """Se o menor espaço da linha for menor que a menor barra,
        preencher ele com 'x' """
        barras = m[linha][15]
        if min(tamanho_de_cada_parte) < min(barras):
            indice = tamanho_de_cada_parte.index(min(tamanho_de_cada_parte))
            for coluna in range(inicio_e_fim_de_cada_parte[indice][0], inicio_e_fim_de_cada_parte[indice][1] + 1):
                m[linha][coluna] = "x"
                if debug:
                    print_matrix(linha, coluna)


def passo6(debug=False):
    """Nas linhas que tiverem uma barra só, se tiver mais de uma,
    emendar.
    """

    for linha in range(15):
        comecar_por_aqui = 0
        ir_ate_aqui = 0
        if len(m[linha][15]) == 1:
            for coluna in range(15):
                if m[linha][coluna] == 0:
                    comecar_por_aqui = coluna
                    break

            for coluna in range(14, -1, -1):
                if m[linha][coluna] == 0:
                    ir_ate_aqui = coluna
                    break

            for coluna in range(comecar_por_aqui, ir_ate_aqui):
                m[linha][coluna] = 0
                if debug:
                    print_matrix(linha, coluna)


def passo7(debug=False):
    """Conferir as linhas que já estão completas e marcar X nos espaços
    em branco.
    """
    for linha in range(15):
        barras = []
        em_aberto = False
        for coluna in range(15):
            if m[linha][coluna] == 0 and not em_aberto:
                c = coluna
                em_aberto = True
            if m[linha][coluna] != 0 and em_aberto:
                t = coluna
                barras.append(t - c)
                em_aberto = False
        if em_aberto:
            barras.append(15 - c)

        if barras == m[linha][15]:
            for coluna in range(15):
                if m[linha][coluna] != 0:
                    m[linha][coluna] = "x"
                    if debug:
                        print_matrix(linha, coluna)


def passo8(debug=False):
    """Percorrer a linha em ambas as direções. Se a primeira posição
     de cada espaço já está preenchida, significa que isso é o início
     da barra. Complete ela e quantas mais tiverem o início determinado.
     Ao completar uma barra, colocar um 'x' no final e continuar o processo
     se a primeira casa já está preenchida e enquanto não houver um espaço vazio.
     Esse passo se parece com o passo 3, com a diferença que ignora em
     quantas partes a linha já esteja dividida. Isso torna o preenchimento
     mais preciso em alguns casos específicos.
     """

    for linha in range(15):
        def esquerda_pra_direita():
            """usando função pra poder usar 'return' e sair da
            função a qualquer momento"""
            coluna = 0
            barras = m[linha][15]
            for i, barra in enumerate(barras):
                # pula os primeiros "x"
                while m[linha][coluna] == "x":
                    coluna += 1

                # se a primeira casa é 0:
                if m[linha][coluna] == 0:
                    # preenche zeros conforme o tamanho da barra.
                    for c_aux in range(barra):
                        if coluna > 14:
                            return
                        m[linha][coluna] = 0
                        if debug:
                            print_matrix(linha, coluna)
                        coluna += 1

                    # coloca "x" no final se não for a última casa
                    if coluna > 14:
                        return
                    else:
                        m[linha][coluna] = "x"
                        if debug:
                            print_matrix(linha, coluna)

                    # enquanto for x, pula.
                    while m[linha][coluna] == "x":
                        coluna += 1
                        if coluna > 14:
                            return

                    # se preencheu até a última barra, o resto da linha é x
                    if i + 1 == len(barras):  # se é a última barra:
                        while coluna < 15:
                            m[linha][coluna] = "x"
                            if debug:
                                print_matrix(linha, coluna)
                            coluna += 1

        esquerda_pra_direita()

    for linha in range(15):
        def direita_pra_esquerda():
            """usando função pra poder usar 'return' e sair da
            função a qualquer momento"""
            coluna = 14
            barras = copy.deepcopy(m[linha][15])
            barras.reverse()
            for i, barra in enumerate(barras):
                # pula os primeiros "x"
                while m[linha][coluna] == "x":
                    coluna -= 1

                # se a primeira casa é 0:
                if m[linha][coluna] == 0:
                    # preenche zeros conforme o tamanho da barra.
                    for c_aux in range(barra):
                        if coluna < 0:
                            return
                        m[linha][coluna] = 0
                        if debug:
                            print_matrix(linha, coluna)
                        coluna -= 1

                    # coloca "x" no final se não for a última casa
                    if coluna < 0:
                        return
                    else:
                        m[linha][coluna] = "x"
                        if debug:
                            print_matrix(linha, coluna)

                    # enquanto for x, pula.
                    while m[linha][coluna] == "x":
                        coluna -= 1
                        if coluna < 0:
                            return

                    # se preencheu até a última barra, o resto da linha é x
                    if i + 1 == len(barras):  # se é a última barra:
                        while coluna >= 0:
                            m[linha][coluna] = "x"
                            if debug:
                                print_matrix(linha, coluna)
                            coluna -= 1

        direita_pra_esquerda()


resolve()
print_matrix_final()
