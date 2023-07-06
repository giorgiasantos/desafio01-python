import random


# FUNÇÃO DO JOGO BASE
def jogobase(pontuacao, erros, acertos):
    # PERGUNTAR DIFICULDADE
    dificuldade = input("SELECIONE A DIFICULDADE: FÁCIL (F) / DIFÍCIL (D)")
    print("----------------------------------------------")

    # ESCOLHA - NÍVEL FÁCIL
    if dificuldade == "F" or dificuldade == "f":
        print("DIFICULDADE SELECIONADA: FÁCIL. VOCÊ TEM 5 CHANCES PARA ACERTAR")
        aleatorio = random.randint(0, 10)
        print(aleatorio)

        for x in range(5):
            chute = int(input("DIGITE UM NÚMERO DE 0 A 10: "))

            if chute == (aleatorio + 1):
                print("SEU NÚMERO FOI UM A MAIS DO QUE EU PENSEI")
                print(aleatorio)
                erros.append(chute)
                pontuacao += 5
                return pontuacao
            elif chute == (aleatorio - 1):
                print("SEU NÚMERO FOI UM A MENOS DO QUE EU PENSEI")
                print(aleatorio)
                erros.append(chute)
                pontuacao += 5
                return pontuacao
            elif chute == aleatorio:
                print("VOCÊ ACERTOU!!")
                acertos.append(chute)
                pontuacao += 10
                return pontuacao
            elif chute != aleatorio:
                print(aleatorio)
                print("Você errou :(")
                erros.append(chute)

    # ESCOLHA - NÍVEL DIFÍCIL
    elif dificuldade == "D" or dificuldade == "d":
        print("DIFICULDADE SELECIONADA: DIFÍCIL. VOCÊ TEM 3 CHANCES PARA ACERTAR")
        aleatorio = random.randint(0, 100)
        print(aleatorio)
        for x in range(3):
            chute = int(input("DIGITE UM NÚMERO DE 0 A 100: "))
            if chute == (aleatorio + 1):
                print("SEU NÚMERO FOI UM A MAIS DO QUE EU PENSEI")
                print(aleatorio)
                erros.append(chute)
                pontuacao += 5
                return pontuacao
            elif chute == (aleatorio - 1):
                print("SEU NÚMERO FOI UM A MENOS DO QUE EU PENSEI")
                print(aleatorio)
                erros.append(chute)
                pontuacao += 5
                return pontuacao
            elif chute == aleatorio:
                print("VOCÊ ACERTOU!!")
                print(aleatorio)
                acertos.append(chute)
                pontuacao += 10
                return pontuacao
            elif chute != aleatorio:
                print("Você errou :(")
                erros.append(chute)

    # ESCOLHA - OPÇÃO INVÁLIDA
    else:
        print("OPÇÃO INVÁLIDA! FIM DE JOGO")
    return pontuacao


# FUNÇÃO DE REINICIAR O JOGO
def reiniciar(pontuacao, erros, acertos):
    while True:

        # PERGUNTAR SE QUER REINICIAR O JOGO
        denovo = input("QUER JOGAR NOVAMENTE? SIM (S) / NÃO (N): ")

        # VALIDAÇÃO PARA JOGAR DE NOVO
        if denovo == "S" or denovo == "s":
            pontuacao = jogobase(pontuacao, erros, acertos)
            printpontuacao(pontuacao)
        elif denovo == "N" or denovo == "n":
            print("TUDO BEM. ATÉ LOGO!")
            printpontuacao(pontuacao)
            break
        else:
            print("COMANDO INVÁLIDO")
            print("FIM DE JOGO")
            print(f"PONTUAÇÃO FINAL = {pontuacao}")
            break


if __name__ == "__main__":
    # DECLARAÇÃO DE VARIÁVEIS
    pontuacao = 0
    erros = []
    acertos = []

    #TELA INICIAL
    print("✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩")
    print("VOCÊ CONSEGUE ADIVINHAR O NÚMERO EM QUE ESTOU PENSANDO?")
    print("✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩")

    #FUNÇÃO PARA EXIBIR ESTATISTICAS DE PONTUAÇÃO
    def printpontuacao(pontuacao):
        print("PONTUAÇÃO TOTAL =", pontuacao)
        print("-----------------------------------------------------------")
        print("SEU HISTORICO DE ACERTOS:", acertos)
        print("SEU HISTORICO DE ERROS:", erros)
        print("-----------------------------------------------------------")

    #CHAMANDO FUNÇÃO DO JOGO
    pontuacao = jogobase(pontuacao, erros, acertos)
    #PRINTANDO A FUNÇÃO DE PONTUAÇÃO
    printpontuacao(pontuacao)
    #CHAMANDO A FUNÇÃO DE REINICIAR JOGO
    reiniciar(pontuacao, erros, acertos)
