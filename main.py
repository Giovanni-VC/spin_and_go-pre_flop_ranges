from poker.hand import Range, Hand
from poker import Card

# Botao

# 13+ BBs

# TODO 1: Criar as tabelas de range

############## Dicionario botao por BB ###################

ranges_botao_mais13BB = {

    "RAISE/FOLD": Range('A2-A8 '
                     'A9o '
                     'K6s-K9s '
                     'Q7s-Q9s '
                     'J7s-J9s '
                     'T7s-T9s '
                     '97s-98s '
                     '87s '
                     'K9o-KJo '
                     'Q9o-QJo '
                     'J9o- JTo '
                     'T9o').hands,
    "RAISE/CALL 3BET ALL-IN OU IR-ALL IN EM QUALQUER 3BET": Range('77+ '
                   'AQo-AKo '
                   'AJs-AKs').hands,
    "ALL-IN DIRETO": Range('33-66').hands,

    "RAISE/CALL 3BET (FOLD 3BET ALL IN)": Range('A9s-ATs '
                         'ATo-AJo').hands,
    "RAISE/ CALL QUALQUER 3BET": Range('KTs-KQs '
                        'QTs-QJs '
                        'KQo '
                        'JTs').hands
}

ranges_botao_menos13BB = {
    "RAISE/FOLD": Range("98s T8s J8s Q8s K7s").hands,
    "RAISE/CALL 3BET ALL-IN OU IR-ALL IN EM QUALQUER 3BET": Range("99-AA ATs-AKs").hands,
    "ALL-IN DIRETO": Range("22-88 A2s-A9s K8s-KQs Q9s-QJs J9s-JTS T9s A2o-AKo K9o-KQo QTo-QJo JTo").hands

}

###################################################

############## Dicionario botao por BB ###################


botao_ranges = {
    "+13BB": ranges_botao_mais13BB,
    "-13BB": ranges_botao_menos13BB
}

###################################################

############## Dicionario geral ###################

ranges = {
    "BOTAO": botao_ranges,

    "SMALL BLIND VS BIG BLIND": {"+13BB":
        {
        "RAISE/FOLD": Range("K2s-K9s Q2s-Q9s J2s-J9s T5s-T9s 95s-98s 85s-87s 75s-76s 65s A2o-A6o K2o-KTo "
                         "Q7o-QJo J7o-JTo T7o-T9o 97o-98o 87o").hands,
        "RAISE/ALL-IN EM 3BET OU CALL 3BET ALL-IN": Range("77-AA A9o-AKo A8s-AKs KQs").hands,
        "ALL-IN DIRETO": Range('22-66').hands,
        "RAISE/CALL 3BET (FOLD 3BET ALL IN)": Range('A2s-A7s KTs-KJs QTs-QJs JTs KJo-KQo A7o-A8o').hands,
        "LIMP/FOLD": Range('Q2o-Q6o J4o-J6o T4o-T6o 94o-96o 84o-86o 74o-76o 64o-65o 54o '
                           '32s 42s-43s 52s-54s 62s-64s 72s-74s 82s-84s 92s-94s T2s-T4s').hands

    },
                                 "-13BB": {
        "RAISE/FOLD": Range("Q2s-Q5s J2s-J7s T5s-T7s 95s-97s 85s-87s 75s 65s "
                         "K2o-K7o Q7o-Q8o J7o-J9o T7o-T9o 97o-98o 87o").hands,
        "RAISE/ALL-IN EM 3BET OU CALL 3BET ALL-IN": Range("99-AA").hands,
        "ALL-IN DIRETO": Range('22-88 98s T8s-T9s J8s-JTs Q6s-QJs K2s-KQs A8s-AKs '
                               'A2o-AKo K9o-KQo Q9o-QJo JTo').hands,
        "RAISE/CALL 3BET (FOLD 3BET ALL IN)": Range('A2s-A7s').hands,
        "LIMP/FOLD": Range('Q2o-Q6o J5o-J6o T5o-T6o 95o-96o 85o-86o 75o-76o 65o '
                           '32s 42s-43s 52s-54s 62s-64s 72s-74s 82s-84s 92s-94s T2s-T4s').hands

    }
    },
    "BIG BLIND VS SMALL BLIND": {"+13BB": {
        "3BET SHOVE (ALL-IN)": Range('A8o-AKo A7s-AKs 22-99').hands,
        "3BET (3X)/CALL ALL-IN": Range('TT-AA').hands,
        "CALL": Range('A2o-A7o K2o-KQo Q2o-QJo J4o-JTo T5o-T9o 95o-98o 84o-87o 74o-76o 64o-65o 54o '
                      '32s 42s-43s 52s-54s 62s-65s 72s-76s 82s-87s 92s-98s T2s-T9s J2s-JTs Q2s-QJs '
                      'K2s-KQs A2s-A6s').hands
    },
                                 "-13BB": {
        "3BET SHOVE (ALL-IN)": Range('A2o-AKo KTo-KQo QTo-QJo JTo 22-QQ').hands,
        "CALL": Range('K2o-K9o Q2o-Q9o J5o-J9o T5o-T9o 95o-98o 85o-87o 75o-76o 65o '
                      '32s 42s-43s 52s-54s 62s-65s 72s-76s 82s-87s 92s-98s T2s-T9s J2s-J9s Q2s-Q9s '
                      'K2s-K9s KK-AA').hands
    }
    },

    "BIG BLIND VS BOTAO": {"+13BB": {
        "3BET SHOVE (ALL-IN)": Range('A7o-AKo A6s-AKs 22-JJ').hands,
        "3BET (3X)/CALL ALL IN": Range('QQ-AA'),
        "CALL": Range('A2o-A6o K2o-KQo Q2o-QJo J6o-JTo T6o-T9o 96o-98o 86o-87o 76o '
                      '32s 42s-43s 52s-54s 62s-65s 72s-76s 82s-87s 92s-98s T2s-T9s J2s-JTs Q2s-QJs K2s-KQs '
                      'A2s-A5s').hands
    },
                           "-13BB": {
        "3BET SHOVE (ALL-IN)": Range('A7o-AKo KTo-KQo QJs KTs-KQs A2s-AKs 22-JJ').hands,
        "3BET (3X)/CALL ALL IN": Range('QQ-AA'),
        "CALL": Range('A2o-A6o K2o-K9o Q2o-QJo J7o-JTo T7o-T9o 97o-98o 87o 76o '
                      '43s 53s-54s 63s-65s 73s-76s 83s-87s 92s-98s T2s-T9s J2s-JTs Q2s-QTs K2s-K9s').hands
    }},
    "SMALL BLIND VS BOTAO": {"+13BB": {
        "3BET SHOVE (ALL-IN)": Range('A2o-AKo A2s-AKs 22-QQ').hands,
        "3BET (3X)/CALL ALL IN": Range('KK-AA').hands,
        "CALL": Range('KTo-KQo QTo-QJo JTo T9s J9s-JTs Q9s-QJs K9s-KQs').hands
    },
                                 "-13BB": {
        "3BET SHOVE (ALL-IN)": Range('A2o-AKo KTo-KQo 22-QQ QJs K9s-KQs A2s-AKs').hands,
        "3BET (3X)/CALL ALL IN": Range('KK-AA'),
        "CALL": Range('QJo JTs QTs').hands
    }},
}

###################################################

# print(ranges["SMALL BLIND BOTAO"]['+13BB']['3BET (3X)/CALL ALL IN'])

# TODO 2: Pedir para o usuario digitar a posicao a quantidade de BB e a mao

# TODO 2.1: Pedir para o usuario digitar a posicao

print("Bem-vindo ao verificador de maos para Sit and Go siga as intrucoes")

while True:

    while True:

        posicao_input = input('''
1 - BOTAO
2 - SMALL BLIND VS BIG BLIND
3 - SMALL BLIND VS BOTAO
4 - BIG BLIND VS SMALL BLIND
5 - BIG BLIND VS BOTAO  
    
Digite o numero correspondente a sua posicao: ''')

        if posicao_input == "1":
            posicao = "BOTAO"
            print(f"Sua posicao: {posicao}")
            break
        elif posicao_input == "2":
            posicao = "SMALL BLIND VS BIG BLIND"
            print(f"Sua posicao: {posicao}")
            break
        elif posicao_input == "3":
            posicao = "SMALL BLIND VS BOTAO"
            print(f"Sua posicao: {posicao}")
            break
        elif posicao_input == "4":
            posicao = "BIG BLIND VS SMALL BLIND"
            print(f"Sua posicao: {posicao}")
            break
        elif posicao_input == "5":
            posicao = "BIG BLIND VS BOTAO"
            print(f"Sua posicao: {posicao}")
            break
        else:
            print(" Entrada invalida! Escolha o numero correspondente")

    # TODO 2.2: Pedir para o usuario digitar a quantidade de blinds

    while (True):


        blinds_input = input('''
Voce possui mais ou menos do que 13BB?
Digite + ou - : ''')

        if blinds_input == "+":
            blinds= "+13BB"
            break
        elif blinds_input == "-":
            blinds= "-13BB"
            break
        else:
            print("Entrada invalida! Digite '+' ou '-' ")


    # TODO 2.3 Pedir para o usuario digitar a mao

    while True:

        mao_input = input('Digite sua mao: ')

        # TODO 2.1: Validar o formato de entrada da mao do usuario

        #Transfoma a string digitada num objeto da biblioteca poker

        try:

            mao = Hand(mao_input)

            print(f"Sua mao eh: {mao}")

            break

        except:

            print("Entrada invalida! Digite suas cartas congorme o exemplo: 77 87s 65s A8o 32s")


    # TODO 3: Verificar onde a mao se enquadra nas tabelas e imprimir a acao

    # if mao_objeto in ranges_botao_mais13BB['amarelo']:
    #     print("RAISE/FOLD")
    # elif mao_objeto in ranges_botao_mais13BB['verde']:
    #     print("RAISE/CALL 3BET ALL-IN OU IR-ALL IN EM QUALQUER 3BET")
    # elif mao_objeto in ranges_botao_mais13BB['vermelho']:
    #     print("ALL-IN DIRETO")
    # elif mao_objeto in ranges_botao_mais13BB['azul_claro']:
    #     print("RAISE/CALL 3BET (FOLD 3BET ALL IN)")
    # elif mao_objeto in ranges_botao_mais13BB['azul_escuro']:
    #     print("RAISE/ CALL QUALQUER 3BET")
    # else:
    #     print("Neutro")

    ranges_posiveis = ranges[posicao][blinds]

    melhor_jogada = "neutro"

    for jogada in ranges_posiveis:

        if mao in ranges_posiveis[jogada]:

            melhor_jogada = jogada

    print(f"A melhor jogada eh {melhor_jogada}")


    # TODO 4: Repetir o programa ate o usuario interromper

    continuar = input("Pressione qualquer tecla para repetir ou '0' para sair: ")

    print("===========================================================================================================")

    if continuar == '0':
        "Obrigado!"
        "Fim do programa"
        break

