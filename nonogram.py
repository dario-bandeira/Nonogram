m = [["·" for x in range(16)] for y in range(16)]

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

linhas_que_tem_maior_igual_8 = []
for ind, x in enumerate(m[:15]):
    for y in x[15]:
        if y >= 8:
            linhas_que_tem_maior_igual_8.append(ind)


# def girar90horario(A):
#     N = len(A[0])
#     for i in range(N // 2):
#         for j in range(i, N - i - 1):
#             temp = A[i][j]
#             A[i][j] = A[N - 1 - j][i]
#             A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
#             A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
#             A[j][N - 1 - i] = temp


def passo1():
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
                    #                      [0:-1]
                    marcar_x_antes += n_barra
                marcar_x_antes += espacos_antes

            # print("x_depois: ", marcar_x_depois)
            # print("x_antes: ", marcar_x_antes)
            # print("linha: ", linha)
            # print("---")

        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_depois):
            m[linha][guia] = 0
            guia -= 1
        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_antes):
            m[linha][guia] = 0
            guia += 1


def passo3():
    # pra direita
    for linha in m[:15]:
        barra_cheia = False
        if linha[0] == 0:
            barra_cheia = True

        preencher_com = "·"
        ultima_casa_da_linha = 0
        tamanho_da_barra = linha[15][0]
        for y in range(tamanho_da_barra):
            if linha[y] == 0:
                preencher_com = 0
            linha[y] = preencher_com
            ultima_casa_da_linha = y

        if barra_cheia: linha[ultima_casa_da_linha + 1] = "x"

    # pra esquerda
    for linha in m[:15]:
        barra_cheia = False
        if linha[14] == 0:
            barra_cheia = True

        preencher_com = "·"
        ultima_casa_da_linha = 0
        tamanho_da_barra = linha[15][-1]
        for y in range(14, 15 - tamanho_da_barra - 1, -1):
            if linha[y] == 0:
                preencher_com = 0
            linha[y] = preencher_com
            ultima_casa_da_linha = y

        if barra_cheia:
            linha[ultima_casa_da_linha - 1] = "x"

    # pra baixo
    for coluna in range(15):
        for linha in range(15):
            barra_cheia = False
            if m[0][coluna] == 0:
                barra_cheia = True

            preencher_com = "·"
            ultima_casa_da_linha = 0
            tamanho_da_barra = m[15][coluna][0]
            for y in range(tamanho_da_barra):
                if m[y][coluna] == 0:
                    preencher_com = 0
                m[y][coluna] = preencher_com
                ultima_casa_da_linha = y

            if barra_cheia:
                m[ultima_casa_da_linha + 1][coluna] = "x"

    # pra cima
    for coluna in range(15):
        for linha in range(15):
            barra_cheia = False
            if m[14][coluna] == 0:
                barra_cheia = True

            preencher_com = "·"
            ultima_casa_da_linha = 0
            tamanho_da_barra = m[15][coluna][-1]
            for y in range(14, 15 - tamanho_da_barra - 1, -1):
                if m[y][coluna] == 0:
                    preencher_com = 0
                m[y][coluna] = preencher_com
                ultima_casa_da_linha = y

            if barra_cheia:
                m[ultima_casa_da_linha - 1][coluna] = "x"


passo1()
passo3()


def print_matrix():
    for x in m[:15]:
        print(*x)

    for x in m[15]:
        print('{: <2}'.format(x[0]), end='')
    print()
    for x in m[15]:
        if len(x) >= 2:
            print('{: <2}'.format(x[1]), end='')
        else:
            print('{: <2}'.format(" "), end='')
    print()
    for x in m[15]:
        if len(x) >= 3:
            print('{: <2}'.format(x[2]), end='')
        else:
            print('{: <2}'.format(" "), end='')





print_matrix()
