import csv

def carregaBanco(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as f:
        conteudo = csv.DictReader(f, delimiter=';')
        dados = list(conteudo)
    return dados


def mediaRenda(file_name):
    dados = carregaBanco(file_name)
    soma = 0
    count = 0
    for i in dados:
        soma += float(i["Renda"])
        count += 1
    if count > 0:
        print(f'A média das rendas é: {soma / count}')
    else:
        print('Não há dados válidos de renda.')


def mediaIdade(file_name):
    dados = carregaBanco(file_name)
    soma = 0
    count = 0
    for i in dados:
        soma += float(i["Idade"])
        count += 1
    if count > 0:
        print(f'A média das idades é: {soma / count}')
    else:
        print('Não há dados válidos de idade.')


mediaRenda("dados.csv")
mediaIdade("dados.csv")
