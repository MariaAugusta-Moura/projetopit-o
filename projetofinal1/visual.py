# ______________________VISUAL________________#
def menu4 ():
    print("Visualização final:")
    op = int(input())

    while (op < 1 or op > 4):
        print("Entrada Inválida")
        print("Informe Novamente:")

    while (op == 1):
        print("Parque Euclides Dourado")
        print("AV. Julio Brasileiro, Heliópolis, Garanhuns-PE,55295-475")
        print("Fone: 363-425 ")
        print("Segunda- Feira a Sexta-Feira: 05:00 - 22:00")
        print("Sábado a Domingo: 05:00 - 21:00 ")
        break
    while (op == 2):
        print("Parque Ruber Van Der Linden- Pau Pombo")
        print("R Manoel Clemente, Santo Antonio, Granhuns-PE,5529-000")
        print("Segunda- Feira a Domingo: 08:00 - 18:00")
        break
    while (op == 3):
        print("Relógio das Flores")
        print("Helioplis, Garanhuns-PE,55296-300")
        print("Segunda-Feira a Domingo: 24 horas")
        break
    while (op == 4):
        print("Fonte Luminosa")
        print("Santo Antonio, Garanhuns-PE,55295-430")
        print("Segunda-Feira a Domingo: 24 horas")
        break
