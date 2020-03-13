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
for i, x in enumerate(m[:15]):
    if max(x[15]) >= 8:
        linhas_que_tem_maior_igual_8.append(i)

colunas_que_tem_maior_igual_8 = []
for coluna in range(15):
    if max(m[15][coluna]) >= 8:
        colunas_que_tem_maior_igual_8.append(coluna)


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
    '''
    Achar na linha um número maior ou igual a 8 e
    preencher a barra a partir do meio da linha.
    Usar os números vizinhos pra preencher ao redor
    da barra, considerando os espaços.
    '''

    # linhas
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

        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_depois):
            m[linha][guia] = 0
            guia -= 1
        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_antes):
            m[linha][guia] = 0
            guia += 1

    # colunas
    for coluna in colunas_que_tem_maior_igual_8:

        quantas_barras_tem_na_linha = len(m[15][coluna])
        indice_do_maior = m[15][coluna].index(max(m[15][coluna]))
        tamanho_da_barra = ((max(m[15][coluna]) - 7) * 2) - 1

        marcar_x_depois = 0
        marcar_x_antes = 0
        espacos_antes = 0
        espacos_depois = 0

        if quantas_barras_tem_na_linha > 1:  # tem mais de 1 número

            if indice_do_maior < quantas_barras_tem_na_linha - 1:  # tem barra depois do maior

                espacos_depois = (quantas_barras_tem_na_linha - (indice_do_maior + 1))

                for n_barra in m[15][coluna][indice_do_maior + 1:]:
                    marcar_x_depois += n_barra
                marcar_x_depois += espacos_depois

            if indice_do_maior != 0:  # tem barra antes do maior

                espacos_antes = indice_do_maior

                for n_barra in m[15][coluna][:indice_do_maior]:
                    #                      [0:-1]
                    marcar_x_antes += n_barra
                marcar_x_antes += espacos_antes

        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_depois):
            m[guia][coluna] = 0
            guia -= 1
        guia = 7
        for y in range((tamanho_da_barra // 2 + 1) + marcar_x_antes):
            m[guia][coluna] = 0
            guia += 1



def passo3():
    '''
    Ver se tem quadrado pintado encostado nas paredes.
    A partir dele, desenhar os adjacentes e marcar o
    fim com um X.
    -ou-
    Se o primeiro quadrado NÃO for pintado, ir contando
    a partir da borda e quando encontrar um
    quadrado pintado, pintar os seguintes até completar o
    número em questão, mas nesse caso não marca o
    fim com X. Lembrar de ignorar os X que aparecem
    desde o começo da linha.
    '''
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


def passo4():
    '''
    A partir da borda, conferir se a primeira barra
    cabe no primeiro espaço vazio. Se não couber,
    preencher o espaço com X.
    '''

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

    # pra baixo
    for coluna in range(15):
        tamanho_do_primeiro_espaco = 0
        for linha in range(15):
            if m[linha][coluna] != "x":
                tamanho_do_primeiro_espaco += 1
            else:
                break

        if tamanho_do_primeiro_espaco < m[15][coluna][0]:
            for voltando in range(linha, -1, -1):
                m[voltando][coluna] = "x"

    # pra cima
    for coluna in range(15):
        tamanho_do_ultimo_espaco = 0
        for linha in range(14, -1, -1):
            if m[linha][coluna] != "x":
                tamanho_do_ultimo_espaco += 1
            else:
                break

        if tamanho_do_ultimo_espaco < m[15][coluna][-1]:
            for voltando in range(linha, 15):
                m[voltando][coluna] = "x"


def passo5():
    '''
    Quebrar as linhas (e colunas) em pedaços usando os X's como divisor.
    Conferir se o número de pedaços é o mesmo número de
    barras da linha. Se for, e se não couberem duas
    barras em um único espaço, sabemos que cada barra está dentro de
    cada pedaço, então é preencher os espaços que são certeza. Assim:

    SE o número em questão é maior que a metade do espaço:
    Conta da esquerda pra direita e marca o último quadrado.
    Depois da direita pra esquerda e pinta todos a partir do pintado
    anteriormente, até completar o número. Depois contar da esquerda
    pra direita a partir do primeiro quadrado pintado o número em
    questão, e marcar X nos que sobrarem. Fazer a mesma coisa da
    direita pra esquerda.
    '''

    # m[0][0] = "x"
    # m[1][0] = "x"
    # m[1][1] = "x"
    # m[2][1] = "x"
    # m[2][2] = "x"
    # m[2][3] = "x"
    for linha in range(15):
        comecar_por_aqui = 0
        tamanho_de_cada_parte = []
        medindo = 0
        for coluna in range(15):
            if m[linha][coluna] == "x":
                comecar_por_aqui += 1
            else:
                break
        for coluna in range(comecar_por_aqui, 15):
            if m[linha][coluna] != "x":
                medindo += 1
            if m[linha][coluna] == "x" and m[linha][coluna + 1] != "x":
                tamanho_de_cada_parte.append(medindo)
                medindo = 0

        tamanho_de_cada_parte.append(medindo)

        if len(tamanho_de_cada_parte) == len(m[linha][15]):
            barras = m[linha][15]
            cabe_mais_de_um = False
            indice_inicio_de_cada_parte = [0]
            for i, x in enumerate(tamanho_de_cada_parte[1:], 1):
                indice_inicio_de_cada_parte.append(
                    tamanho_de_cada_parte[i - 1] + indice_inicio_de_cada_parte[i - 1] + 1)
            indice_inicio_de_cada_parte.append(15)

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

                # if not cabe_mais_de_um:

        '''
        SE o número em questão é maior que a metade do espaço:
        Conta da esquerda pra direita e marca o último quadrado.
        Depois da direita pra esquerda e pinta todos a partir do pintado
        anteriormente, até completar o número. Depois contar da esquerda
        pra direita a partir do primeiro quadrado pintado o número em
        questão, e marcar X nos que sobrarem. Fazer a mesma coisa da
        direita pra esquerda.
        '''


passo1()
# passo3()
# passo4()
# passo5()


def print_matrix():
    for i, x in enumerate(m[:15]):
        print('{: <2} '.format(i), end='')
        print(*x)
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


print_matrix()
