import random

# Armazena as multiplicações
multiplicacao = {
    (2, 2): 4,
    (2, 3): 6,
    (2, 4): 8,
    (2, 5): 10,
    (2, 6): 12,
    (2, 7): 14,
    (2, 8): 16,
    (2, 9): 18,
    (3, 3): 9,
    (3, 4): 12,
    (3, 5): 15,
    (3, 6): 18,
    (3, 7): 21,
    (3, 8): 24,
    (3, 9): 27,
    (4, 4): 16,
    (4, 5): 20,
    (4, 6): 24,
    (4, 7): 28,
    (4, 8): 32,
    (4, 9): 36,
    (5, 5): 25,
    (5, 6): 30,
    (5, 7): 35,
    (5, 8): 40,
    (5, 9): 45,
    (6, 6): 36,
    (6, 7): 42,
    (6, 8): 48,
    (6, 9): 54,
    (7, 7): 49,
    (7, 8): 56,
    (7, 9): 63,
    (8, 8): 64,
    (8, 9): 72,
    (9, 9): 81,
}

# Inicia o jogo
def iniciar_jogo():
    # Armazena as multiplicações não respondidas
    multiplicacoes_nao_respondidas = multiplicacao.copy()

    # Enquanto houver multiplicações não respondidas, continue o jogo
    while multiplicacoes_nao_respondidas:
        # Gera um número aleatório entre 0 e o número de multiplicações não respondidas
        numero_aleatorio = random.randint(0, len( multiplicacoes_nao_respondidas) - 1)

        # Obtém a multiplicação correspondente ao número aleatório
        multiplicacao_aleatoria = list( multiplicacoes_nao_respondidas.keys())[numero_aleatorio]

        # Exibe a multiplicação
        print("Qual é o resultado de {} x {}?".format(*multiplicacao_aleatoria))

        # Obtém a resposta do usuário
        resposta = input()

        # Compara a resposta do usuário com o resultado correto
        if resposta == str(multiplicacao[multiplicacao_aleatoria]):
            # Resposta correta
            multiplicacoes_nao_respondidas.pop(list(multiplicacoes_nao_respondidas.keys())[numero_aleatorio])
            print("correto")

        else:
            # Resposta incorreta
            print("Resposta incorreta. O resultado correto é {}.".format(multiplicacao[multiplicacao_aleatoria]))

    # Se não houver multiplicações não respondidas, o jogo acabou
    if not multiplicacoes_nao_respondidas:
        print("Parabéns! Você acertou todas as multiplicações!")

# Chama a função para iniciar o jogo
iniciar_jogo()
