# Escreva um programa que calcule o preço a pagar pelo consumo
# de internet. Pergunte ao usuário qual a quantidade consumida em
# GB e o tipo de plano: R para residencial ou E para empresarial. A
# tabela de preços é a seguinte:
from exceptiongroup import catch


# Tipo de Plano     Faixa de consumo (em GB)     Preço por GB (em R$)
# Residencial       Até 10                      8,00
#                   Acima de 10                 12,00
# Empresarial       Até 100                     10,00
#                   Acima de 100                15,00

def calc_consume(plan, consume):
    amount = 0
    if plan == 'R':
        if consume <= 10:
            amount = 8 * consume
        else:
            amount = 12 * consume
    elif plan == 'E':
        if consume <= 100:
            amount = 10 * consume
        else:
            amount = 15 * consume
    else:
        print('Opção inválida!')
        amount = False

    return amount


plan_to_calc = input('Qual o plano que deseja calcular?\nR - Residencial\nE - Empresarial\n')
try:
    consume_gb = float(input('Qual o consumo (em GB)? '))
    result = calc_consume(plan_to_calc, consume_gb)
    if result:
        print(f'Total a pagar: R$ {result}')
except ValueError:
    print("Operação inválida!")


