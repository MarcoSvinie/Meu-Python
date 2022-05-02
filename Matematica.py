def dobro(n = 0, format = False):
    res = n * 2
    return res if format is False else moeda(res)

def triplo(n, format = False):
    res = n * 3
    return res if format is False else moeda(res)

def metade(n, format = False):
    res = n / 2
    return res if format is False else moeda(res)

def aumento(n, m = 0, format=False):
    res = n + (n * m / 100)
    return res if format is False else moeda(res)

def reduzir(n, m = 0, format = False):
    res = n - (n * m / 100)
    return res if format is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def multi(*num):
    multi1 = int(input('Primeiro número: '))
    multi2 = int(input('Segundo número: '))
    multi = multi1 * multi2
    return print(f'A resposta foi {multi}')


def soma(*num):
    n = int(input('Primeiro número: '))
    m = int(input('Segundo número: '))
    soma = n + m
    return print(f'O resultado foi {soma}')


def subtracao(*num):
    n = int(input('Primeiro número: '))
    m = int(input('Segundo número: '))
    sub = n - m
    return print(f'O resultado foi {sub}')

def divisao(*num):
    n = int(input('Divisor: '))
    m = int(input('Dividendo: '))
    divi = n / m
    return print(f'O resultado foi {divi}')