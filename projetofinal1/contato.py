# ______________________CONTATO________________#
import horario


def menu2():
    print("Informe o numero novamente para o Contato: ")
    op = int(input())

    while (op < 1 ):
        print("Entrada Inválida")
        print(horario.menu3())


    while (op == 1):
        print(" Fone: 363-425 ")
        break
