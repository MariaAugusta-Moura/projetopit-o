# ______________________Banco de Dados______________________#

import mysql.connector

def menucriar_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)



def menufechar_conexao(con):
    return con.close()

