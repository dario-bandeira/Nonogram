m = [[0, 0, 0, "x", "x", "·", "·", 0, 0, "·", "x", "x", 0, 0, 0]]


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


print(*m[0])
preenche_barra_no_espaco(0, [5, 9], 4)
print(*m[0])
