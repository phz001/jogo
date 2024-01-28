import random

fichas = 0

def adicao_de_fichas(fichas):
    while True:
        adicionar_ficha = input(f'\n🎰 Você possui {fichas} fichas. Deseja adicionar mais fichas? (S/N): ').upper()

        if adicionar_ficha == 'S':
            while True:
                try:
                    fichas_num = int(input('Quantas fichas deseja adicionar? '))
                    break  
                except ValueError:
                    print('Entrada inválida. Digite um número inteiro.')

            fichas += fichas_num
            print(f'\n✨ Agora você possui {fichas} fichas. Boa sorte!')
            return fichas
        elif adicionar_ficha == 'N':
            return fichas
        else:
            print('Opção inválida. Por favor, escolha S ou N.')

fichas = adicao_de_fichas(fichas)

def tutorial():
    print("\n🌴 Bem-vindo à emocionante jornada do tesouro perdido! 🏴‍☠️")
    print("Na remota ilha de Eldoria, rumores de um tesouro lendário têm atraído corajosos caçadores de fortuna de todos os cantos do mundo.")
    print("Você é um destemido aventureiro que chegou a Eldoria, ansioso para participar da caça ao tesouro.")
    print("\n🔍 ** Tutorial ** 🔍")
    print("Você possui fichas que podem ser usadas para fazer apostas.")
    print("O jogo tem três modos: Fácil, Normal e Difícil.")
    print("Cada modo possui uma forma diferente de apostar e ganhar fichas.")
    print("No final, você pode decidir se deseja jogar novamente ou sair.")
    print("Boa sorte na busca pelo tesouro perdido!\n")

tutorial()

def jogo():
    global fichas
    rep_ex = 0

    while True:
        print(f'\n💰 Você possui {fichas} fichas disponíveis.')

        try:
            aposta_ficha = int(input('Quantas fichas deseja apostar? '))
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')
            continue

        if aposta_ficha > fichas:
            print('Você não possui fichas suficientes para esta aposta.')

            op_ficha_jogo = input('Escolha 1 ou 2:\n1. Adicionar mais fichas\n2. Mudar a aposta de ficha\n')
            if op_ficha_jogo == '1':
                fichas = adicao_de_fichas(fichas)
                continue
            elif op_ficha_jogo == '2':
                continue
            else:
                print('Opção inválida. Escolha 1 ou 2.')
                continue

        print('\nEscolha o modo de jogo:')
        print('1. Fácil (aposta em 3 números, fichas apostadas multiplicadas por 2x para cada acerto)')
        print('2. Normal (aposta em 2 números, fichas apostadas multiplicadas por 5x para cada acerto)')
        print('3. Difícil (aposta em 2 números, fichas apostadas multiplicadas por 15.0x)')
        if rep_ex == 0:
            print('\033[91m', 'Exemplo', '\033[0m','\nEscolhi o modo fácil, acertei 2 números\naposta x 2(modo fácil) x 2(número de acertos)\n')
            rep_ex += 1

        try:
            modo_jogo = int(input('Digite o número do modo desejado (1, 2 ou 3): '))
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')
            continue

        if modo_jogo not in [1, 2, 3]:
            print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
            continue

        print('\nEsta é a tabela de jogo:')
        tabela_jogo = (
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15,
            16, 17, 18, 19, 20,
            21, 22, 23, 24, 25
        )

        for i, num in enumerate(tabela_jogo, 1):
            print(num, end=', ' if i % 5 != 0 else '\n')

        ne1, ne2, ne3 = 0, 0, 0  

        def obter_numero_entrada(mensagem):
            while True:
                try:
                    numero = int(input(mensagem))
                    if 1 <= numero <= 25:
                        return numero
                    else:
                        print('Número inválido. Digite um número entre 1 e 25.')
                except ValueError:
                    print('Entrada inválida. Digite um número inteiro.')

        def escolha_num():
            nonlocal ne1, ne2, ne3  
            if modo_jogo == 1:
                ne1 = obter_numero_entrada('Digite o primeiro número para apostar (entre 1 e 25): ')
                ne2 = obter_numero_entrada('Digite o segundo número para apostar (entre 1 e 25): ')
                ne3 = obter_numero_entrada('Digite o terceiro número para apostar (entre 1 e 25): ')
                print(f'\nApostando nos números: {ne1}, {ne2}, {ne3}')
                return ne1, ne2, ne3
            elif modo_jogo == 2:
                ne1 = obter_numero_entrada('Digite o primeiro número para apostar (entre 1 e 25): ')
                ne2 = obter_numero_entrada('Digite o segundo número para apostar (entre 1 e 25): ')
                print(f'\nApostando nos números: {ne1}, {ne2}')
                return ne1, ne2
            elif modo_jogo == 3:
                ne1 = obter_numero_entrada('Digite o primeiro número para apostar (entre 1 e 25): ')
                print(f'\nApostando no número: {ne1}')
                return ne1

        escolha_num()

        num_apostado = [ne1, ne2, ne3] if modo_jogo == 1 else [ne1, ne2] if modo_jogo == 2 else [ne1]
        ns = 3 if modo_jogo == 1 else 2 if modo_jogo == 2 else 1
        sorteio = random.sample(tabela_jogo, ns)

        def imprimir_numero_colorido(numero):
            cor_vermelha = '\033[91m'
            cor_reset = '\033[0m'
            print(f'{cor_vermelha}{numero}{cor_reset}', end=', ')

        print('\nOs números em que estavam a recompensa são:')
        for i, num in enumerate(tabela_jogo, 1):
            if num in sorteio:
                imprimir_numero_colorido(num)
            else:
                print(num, end=', ' if i % 5 != 0 else '\n')

        num_acertado = sum(1 for elemento in sorteio if elemento in num_apostado)

        print(f'\nOs números apostados foram: {num_apostado}')
        print(f'Você acertou {num_acertado} número(s)!')

        fichas_ganhas = 0
        fichas = fichas - aposta_ficha

        if modo_jogo == 1:
            if num_acertado == 1:
                fichas_ganhas = aposta_ficha * 2
            elif num_acertado == 2:
                fichas_ganhas = aposta_ficha * 2 * 2
            elif num_acertado == 3:
                fichas_ganhas = aposta_ficha * 2 * 3
            else:
                print('Você perdeu as fichas apostadas pois não acertou nenhum número')

        elif modo_jogo == 2:
            if num_acertado == 1:
                fichas_ganhas = aposta_ficha * 5
            elif num_acertado == 2:
                fichas_ganhas = aposta_ficha * 5 * 2
            else:
                print('Você perdeu as fichas apostadas pois não acertou nenhum número')

        elif modo_jogo == 3:
            if num_acertado == 1:
                fichas_ganhas = aposta_ficha * 15
            else:
                print('Você perdeu as fichas apostadas pois não acertou nenhum número')

        fichas += fichas_ganhas
        print(f'\n🎉 Agora você possui {fichas} fichas!')

        jogar_novamente = input('Deseja jogar novamente? (S/N): ').upper()
        if jogar_novamente != 'S':
            print('Obrigado por jogar! Até a próxima. 🌟')
            break
  
jogo()