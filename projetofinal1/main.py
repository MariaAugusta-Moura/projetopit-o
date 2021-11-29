from banco import menucriar_conexao, menufechar_conexao
import cadastrar
import local
import endereco
import contato
import horario
import visual
import repositorio as rep
opcao = cadastrar.menucadVisitante()

lD = rep.cadastrarContato(opcao,opcao[0],opcao[1])

def insert_contato(cone,nome,fone):
    cursor = cone.cursor()
    sql = "INSERT INTO cadastro (nome,fone) values (%s,%s)"
    valores = (nome,fone)
    cursor.execute(sql, valores)
    cursor.close()
    cone.commit()





cone = menucriar_conexao("localhost", "root", "","cadastro")

insert_contato(cone,opcao[0],opcao[1])
menufechar_conexao(cone)

opcao = local.menu()

opcao = endereco.menu1()

opcao = contato.menu2()

opcao = horario.menu3()

opcao = visual.menu4()


