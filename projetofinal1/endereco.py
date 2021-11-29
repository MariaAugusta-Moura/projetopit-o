# ______________________ENDEREÇO______________________#

def menu1():
    print("Informe o numero novamente para o endereço: ")
    op = int(input())

    while (op < 1 or op > 4):
        print("Entrada Inválida")
        print("Informe Novamente:")


    while (op == 1):
        print(" AV. Julio Brasileiro, Heliópolis, Garanhuns-PE,55295-475")
        break
    while (op == 2):
        print(" R Manoel Clemente, Santo Antonio, Granhuns-PE,5529-000")
        break
    while (op == 3):
        print("Helioplis, Garanhuns-PE,55296-300")
        break
    while (op == 4):
        print("Santo Antonio, Garanhuns-PE,55295-430")
        break