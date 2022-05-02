import Comandos


def existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo')
    else:
        print(f'Arquivo {nome} criado! ')


def lerArquivo(nome):
    a = ''
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        Comandos.cabecalho('PESSOAS CADASTRADAS!')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<10}{dado[1]:>3} anos, função {dado[2]}')
    finally:
        a.close()


def cadastrar(a1, nome='desconhecido', idade=0):
    try:
        a = open(a1, 'at')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao inserir os dados!')
        else:
            print(f'Registro de {nome} concluído!')
            a.close()



def cadastrar2(a1, nome='desconhecido', idade=0, funcao='desconhecido', hora=0):
    try:
        a = open(a1, 'at')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{nome};{idade};{funcao}; {hora}\n')
        except:
            print('Erro ao inserir os dados!')
        else:
            print(f'Registro de {nome} concluído!')
            a.close()



def cadastrar3(a1, nome='desconhecido'):
    try:
        a = open(a1, 'at')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{nome};\n')
        except:
            print('Erro ao inserir os dados!')
        else:
            print(f'Registro de {nome} concluído!')
            a.close()
