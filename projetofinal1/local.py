                           #___________________LOCAL____________________#
def boasVindas():
        print("Seja Bem vindo(a) !")
def menu():
        print("Escolha uma Opção: 1 - Parque Euclides, 2 - Pau Pombo, 3 - Relogio das Flores, 4 - Fonte Luminosa")
        op = int(input())

        while (op < 1 or op > 4):
            print("Entrada Inválida")
            print("Informe Novamente:")

        while (op == 1):
            print("Parque Euclides Dourado")
            break
        while (op == 2):
            print("Parque Ruber Van Der Linden- Pau Pombo")
            break
        while (op == 3):
            print("Relógio das Flores")
            break
        while (op == 4):
            print("Fonte Luminosa")
            break
