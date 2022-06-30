from Grava_imagem import grava
import mysql.connector

host = 'localhost'
database = 'para_teste'
user = 'root'
password = 'admin'

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password)


def Alterar(id_produto, nome, descricao, estoque, preco, imagem):
    try:
        varid = id_produto
        varnome = nome
        vardescricao = descricao
        varestoque = estoque
        varc = preco
        varimagem = imagem
        curso = conexao.cursor()
        sobenome = "UPDATE produto SET nome= " '\'' + varnome + '\'' " WHERE idproduto= " + varid
        curso.execute(sobenome)
        conexao.commit()
        sobedescricao = "UPDATE produto SET descricao= " '\'' + vardescricao + '\'' " WHERE idproduto= " + varid
        curso.execute(sobedescricao)
        conexao.commit()
        sobeestoque = "UPDATE produto SET estoque= " + varestoque + " WHERE idproduto= " + varid
        curso.execute(sobeestoque)
        conexao.commit()
        sobevalor = "UPDATE produto SET valor= " + varc + " WHERE idproduto= " + varid
        curso.execute(sobevalor)
        conexao.commit()
        if varimagem != "":
            novodestino = grava(varid, varimagem)
            sobeimagem = "UPDATE produto SET imagem= " + novodestino + " WHERE idproduto= " + varid
            curso.execute(sobeimagem)
    except:

        curso.close()

#  UPDATE cadastro SET estoque = 40 WHERE idproduto=1;
# sobeestoque = "UPDATE cadastro SET estoque= " + varestoque + " WHERE idproduto= " + idproduto
