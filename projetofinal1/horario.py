# ______________________HORARIO________________#

def menu3():
    print("Informe o numero novamente para os Horarios:")
    op= int(input())

    while (op < 1 or op > 4):
        print("Entrada Inválida")
        print("Informe Novamente:")

    while (op == 1):
        print("Segunda- Feira a Sexta-Feira: 05:00 - 22:00")
        print("Sábado a Domingo: 05:00 - 21:00 ")
        break
    while (op == 2):
        print("Segunda- Feira a Domingo: 08:00 - 18:00")
        break
    while (op == 3):
        print("Segunda-Feira a Domingo: 24 horas")
        break
    while (op == 4):
        print("Segunda-Feira a Domingo: 24 horas")
        break