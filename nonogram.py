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


def executar_passos():
    global m
    passos = {
        passo1: '',
        passo2: '',
        passo3: '',
        passo4: '',
        passo5: '',
        passo6: '',
        passo7: '',
    }
    for key, val in passos.items():
        # print(key)
        key()
        m = girar_antihorario(m)
        key()
        girar_horario(m)


def print_matrix(ll, cc):
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


def comparar():
    errado = False
    for linha in range(15):
        for coluna in range(15):
            if m[linha][coluna] != "·" and m[linha][coluna] != matrix_correta[linha][coluna]:
                print("errado linha ", linha, " coluna ", coluna)
                errado = True
    if errado:
        return False
    else:
        print("Tudo certo!")
        return True


# # # PASSOS # # #


def passo1(debug=False):
    '''
    Achar na linha um número maior ou igual a 8 e
    preencher a barra a partir do meio da linha.
    Usar os números vizinhos pra preencher ao redor
    da barra, considerando os espaços.
    '''
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
    '''
    Ver se os números dos extremos são o maior e conferir se
    a barra dele está completa. Se tiver, marcar o espaço restante
    com X e conferir a próxima barra.
    '''
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
    '''
    Ver se tem 'zero' encostado nas paredes.
    A partir dele, desenhar os seguintes e marcar o
    fim com um X.
    -ou-
    Se a primeira casa NÃO for zero, ir contando
    a partir da borda e quando encontrar um
    zero, pintar os seguintes até completar o
    número em questão, mas nesse caso não marca o
    fim com X. Lembrar de ignorar os X que aparecem
    desde o começo da linha.
    '''
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
    questão. Fazer a mesma coisa da direita pra esquerda. Se a
    barra estiver completa, marcar os espaços livres com X.
    '''
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

            if not cabe_mais_de_um:
                for i, espaco in enumerate(inicio_e_fim_de_cada_parte):
                    # a barra tem que ter no mínimo metade do espaço
                    if not barras[i] > (espaco[1] - espaco[0] + 1) // 2:
                        continue
                    # esquerda pra direita
                    # se a primeira é zero:
                    if m[linha][espaco[0]] == 0:
                        # preenche a barra toda e o resto é x
                        barra_aux = barras[i]
                        for coluna in range(espaco[0], espaco[1] + 1):
                            if barra_aux:
                                m[linha][coluna] = 0
                                if debug:
                                    print_matrix(linha, coluna)
                                barra_aux -= 1
                            else:
                                m[linha][coluna] = "x"
                                if debug:
                                    print_matrix(linha, coluna)

                    # senão: se a última é x:
                    elif m[linha][espaco[1]] == 0:
                        # preenche a barra toda e o resto é x
                        barra_aux = barras[i]
                        for coluna in range(espaco[1], espaco[0] - 1, -1):
                            if barra_aux:
                                m[linha][coluna] = 0
                                if debug:
                                    print_matrix(linha, coluna)
                                barra_aux -= 1
                            else:
                                m[linha][coluna] = "x"
                                if debug:
                                    print_matrix(linha, coluna)
                    # senão:
                    else:
                        # esquerda pra direita
                        # pula o tanto de casas que é a barra, se achar 0 vai pondo 0, na última põe 0
                        barra_aux = barras[i]
                        em_aberto = False
                        for coluna in range(espaco[0], espaco[1] + 1):
                            if barra_aux:
                                barra_aux -= 1
                                if m[linha][coluna] == 0:
                                    em_aberto = True
                                if em_aberto:
                                    m[linha][coluna] = 0
                                    if debug:
                                        print_matrix(linha, coluna)
                                if not barra_aux:
                                    m[linha][coluna] = 0
                                    if debug:
                                        print_matrix(linha, coluna)
                                    break

                        # direita pra esquerda
                        # pula o tanto de casas que é a barra, quando achar 0 vai pondo 0
                        barra_aux = barras[i]
                        em_aberto = False
                        for coluna in range(espaco[1], espaco[0] - 1, -1):
                            if barra_aux:
                                if m[linha][coluna] == 0:
                                    em_aberto = True
                                if em_aberto:
                                    m[linha][coluna] = 0
                                    if debug:
                                        print_matrix(linha, coluna)
                                barra_aux -= 1
                            else:
                                break

            # cabe mais de um, mas...
            # conferir se só falta uma barra pra preencher,
            # vendo quais partes tem espaços vazios ainda.
            # else:

        # nº de barras != nº de espaços
        else:
            # se tem mais espaços que barras:
            if len(tamanho_de_cada_parte) > len(m[linha][15]):
                # confere se as barras já estão em seus espaços,
                # mesmo que parcialmente

                espacos_preenchidos = []
                espacos_vazios = []
                for espaco in inicio_e_fim_de_cada_parte:
                    vazio = True
                    for coluna in range(espaco[0], espaco[1] + 1):
                        if m[linha][coluna] == 0:
                            # esse espaço tem preenchimento
                            espacos_preenchidos.append(espaco)
                            vazio = False
                            break
                    if vazio:
                        espacos_vazios.append(espaco)

                # print("linha ", linha, " espacos vazios ", espacos_vazios, end='')
                # if girado: print(", girado")

                # as barras já estão em seus devidos lugares:
                if len(espacos_preenchidos) == len(m[linha][15]):
                    # então ponha "x" nos espaços vazios
                    for espaco in espacos_vazios:
                        for coluna in range(espaco[0], espaco[1] + 1):
                            m[linha][coluna] = "x"
                            if debug:
                                print_matrix(linha, coluna)


def passo6(debug=False):
    '''
    Nas linhas que tiverem uma barra só, se tiver mais de uma,
    emendar.
    '''

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
    '''
    Conferir as linhas que já estão completas e marcar X nos espaços
    em branco.
    '''
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


executar_passos()
executar_passos()
executar_passos()
executar_passos()
print_matrix(0, 0)
comparar()
