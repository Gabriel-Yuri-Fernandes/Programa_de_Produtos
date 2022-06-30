import os
import mysql.connector

host = 'localhost'
database = 'para_teste'
user = 'root'
password = 'admin'

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password)


def Excluir(idproduto, endimg):
    end = endimg
    idproduto = idproduto
    dados = "DELETE FROM produto WHERE idproduto = %d" % idproduto
    curso = conexao.cursor(dados)
    curso.execute(dados)
    conexao.commit()
    os.remove(end)

    curso.close()


