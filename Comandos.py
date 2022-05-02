def linha(tam=35):
    return '-' * tam

def leiastr(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError):
            print('Tente Novamente!')
            continue
        except KeyboardInterrupt:
            print()
            print('Não houve digitação!')
            return 0
        else:
            return n


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mInsira um número valido!\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[32mNão houve digitação!\033[m')
            return 0
        else:
            return n


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabecalho('MENU')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    escolha = leiaint('Opção escolhida: ')
    return escolha


def menu2(lista):
    cabecalho('MENU')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[33m{item}\033[m')
        c += 1
    print(linha())
    escolha = leiaint('\033[32mOpção escolhida: \033[m')
    return escolha
