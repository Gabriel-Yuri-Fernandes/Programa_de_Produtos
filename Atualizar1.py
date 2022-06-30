from Grava_imagem import grava
import mysql.connector

host = '****'
database = '****'
user = '***'
password = '****'

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password)


def Alterar(id_produto, nome, descricao, estoque, preco, imagem): #Função que irá realizar a alteração dos dados no BD
    try:
        varid = id_produto
        varnome = nome
        vardescricao = descricao
        varestoque = estoque
        varc = preco
        varimagem = imagem
        curso = conexao.cursor() #Cria um cursor para que possa alterar ou mexer no BD
        sobenome = "UPDATE produto SET nome= " '\'' + varnome + '\'' " WHERE idproduto= " + varid #Variavel que receberá a função para mexer no BD
        curso.execute(sobenome) #Execulta o comando salvo na variavel sobenome
        conexao.commit() #Confirmar a execução do comando acima
        sobedescricao = "UPDATE produto SET descricao= " '\'' + vardescricao + '\'' " WHERE idproduto= " + varid
        curso.execute(sobedescricao)
        conexao.commit()
        sobeestoque = "UPDATE produto SET estoque= " + varestoque + " WHERE idproduto= " + varid
        curso.execute(sobeestoque)
        conexao.commit()
        sobevalor = "UPDATE produto SET valor= " + varc + " WHERE idproduto= " + varid
        curso.execute(sobevalor)
        conexao.commit()
        if varimagem != "": #Verificar se a varimagem não está vazia
            novodestino = grava(varid, varimagem) #Chama a função que vai gravar a imagem em uma pasta
            sobeimagem = "UPDATE produto SET imagem= " + novodestino + " WHERE idproduto= " + varid
            curso.execute(sobeimagem)
    except:

        curso.close()
