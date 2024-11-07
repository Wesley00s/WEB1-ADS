# Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo
# que o usuário foi multado. Nesse caso, exiba o valor da multa
# cobrando R$ 5,00 por km/h acima de 80.


def calc_velocity(velocity):
    if velocity > 80:
        fine = (velocity - 80) * 5
        print(f"Você foi multado, no valor de R$ {fine}.")
    else:
        print("Nenhuma multa aplicada.")

try:
    vel = float(input("Informe a velocidade em km/h: "))
    calc_velocity(vel)
except ValueError:
    print("Entrada inválida!")