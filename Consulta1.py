import mysql.connector

host = 'localhost'
database = 'para_teste'
user = 'root'
password = 'admin'

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password)


def consulta(idproduto):
    idproduto = idproduto
    sqlconsultar = "SELECT * FROM produto WHERE idproduto = %d" % idproduto
    curso = conexao.cursor(sqlconsultar)
    curso.execute(sqlconsultar)
    linhas = curso.fetchall()
    for linhas in linhas:
        nome = linhas[1]
        descricao = linhas[2]
        estoque = linhas[3]
        preco = linhas[4]
        imagem = linhas[5]
        return nome, descricao, estoque, preco, imagem

    curso.close()
