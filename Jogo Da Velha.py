listateste = [[0,0,0],
              [0,0,0],
              [0,0,0]]

#primeiro campo é a linha [Linha] e o segundo é a coluna [Linha][Coluna]!
#a linha e o Campo Y e a coluna é o Campo X, como se fosse um grafico de reta 

def verificando_X():
    #verificação diagonal
    if listateste[0][0] == 'X' and listateste[1][1] == 'X' and listateste[2][2] == 'X':
        return 1
    elif listateste[0][2] == 'X' and listateste[1][1] == 'X' and listateste[2][0] == 'X':
        return 1
    #verificação diagonal
        
    #verificação horizontal
    elif listateste[0][0] == 'X' and listateste[0][1] == 'X' and listateste[0][2] == 'X':
        return 1
    elif listateste[1][0] == 'X' and listateste[1][1] == 'X' and listateste[1][2] == 'X':
        return 1
    elif listateste[2][0] == 'X' and listateste[2][1] == 'X' and listateste[2][2] == 'X':
        return 1
    #verificação horizontal
        
    #verificação Vertical
    elif listateste[0][0] == 'X' and listateste[1][0] == 'X' and listateste[2][0] == 'X':
        return 1
    elif listateste[0][1] == 'X' and listateste[1][1] == 'X' and listateste[2][1] == 'X':
        return 1
    elif listateste[0][2] == 'X' and listateste[1][2] == 'X' and listateste[2][2] == 'X':
        return 1
    #verificação Vertical
        
def verificando_O():
    #verificação diagonal
    if listateste[0][0] == 'O' and listateste[1][1] == 'O' and listateste[2][2] == 'O':
        return 2
    elif listateste[0][2] == 'O' and listateste[1][1] == 'O' and listateste[2][0] == 'O':
        return 2
    #verificação diagonal
        
    #verificação horizontal
    elif listateste[0][0] == 'O' and listateste[0][1] == 'O' and listateste[0][2] == 'O':
        return 2
    elif listateste[1][0] == 'O' and listateste[1][1] == 'O' and listateste[1][2] == 'O':
        return 2
    elif listateste[2][0] == 'O' and listateste[2][1] == 'O' and listateste[2][2] == 'O':
        return 2
    #verificação horizontal
        
    #verificação Vertical
    elif listateste[0][0] == 'O' and listateste[1][0] == 'O' and listateste[2][0] == 'O':
        return 2
    elif listateste[0][1] == 'O' and listateste[1][1] == 'O' and listateste[2][1] == 'O':
        return 2
    elif listateste[0][2] == 'O' and listateste[1][2] == 'O' and listateste[2][2] == 'O':
        return 2
    #verificação Vertical

def exibir():
    for linha in range(len(listateste)):
        for coluna in range(len(listateste)):
            if listateste[linha][coluna] == 0:
                listateste[linha][coluna] = '_'
            print(f'{listateste[linha][coluna]}',end=' ')
        print()


def jogo():
    jogar = 1
    alt = 1
    count = 1
    while jogar:
        print()
        match alt:
            case 1:
                jogador1 = 1
                while jogador1:
                    exibir()
                    try:
                        print(f'{alt} jogador (_X_) Jogada:{count}',end='\n')
                        Linha = int(input('Linha:'))
                        Coluna = int(input('Coluna:'))
                        if listateste[Linha-1][Coluna-1] == '_':
                            listateste[Linha-1][Coluna-1] = 'X'
                            jogador1 -= 1
                            count += 1
                            alt = 2
                        else:print('posição já preenchida')
                        verificando_X()
                        if verificando_X() == 1:
                            print(f'O jogador 1 ganhou como X, depois de {count} rounds'.center(100,'$'))
                            jogar -=1
                        elif count == 9:
                            print('sem movimentos validos\n Portando Empate'.center(100,'#'))
                            jogar -= 1
                    except ValueError as err:
                        print(f'valor informado não corresponde a um Inteiro\n{err}')
                    except IndexError as er:
                        print(f'\nvalor informado fora do escopo da lista \n{er}')
            case 2:
                jogador2 = 1
                while jogador2:
                    exibir()
                    try:
                        print(f'{alt} jogador (_O_) Jogada:{count}',end='\n')
                        Linha = int(input('Linha:'))
                        Coluna = int(input('Coluna:'))
                        if listateste[Linha-1][Coluna-1] == '_':
                            listateste[Linha-1][Coluna-1] = 'O'
                            jogador2 -= 1
                            count += 1
                            alt = 1
                        else:print('posição já preenchida')
                        verificando_O()
                        if verificando_O() == 2:
                            print(f'O jogador 2 ganhou como O, depois de {count} rounds'.center(100,'$'))
                            jogar -=1
                        
                        elif count == 9:
                            print('sem movimentos validos\n Portando Empate'.center(100,'#'))
                            jogar -= 1
                    except ValueError as err:
                        print(f'valor informado não corresponde a um Inteiro\n{err}')
                    except IndexError as er:
                        print(f'\nvalor informado fora do escopo da lista \n{er}')

        print()

def menu():
    print(verificando_X())
    continuar =1 
    while continuar:
        try:
            continuar = int(input("""\n0-Sair\n1-Jogar\nAlternativa:"""))
            if continuar == 0:
                print('saindo...')

            elif continuar ==1:
                for linha in range(len(listateste)):
                    for coluna in range(len(listateste)):
                        listateste[linha][coluna] = 0
                jogo()
            else:
                print('\nessa opção não existe\n'.center(100,'#'))
        except ValueError as err:
            print(f'\n o Valor informado não existe\n {err}')

menu()

