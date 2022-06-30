import os
import mysql.connector

host = '****'
database = '****'
user = '***'
password = '****'

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password) #Cria conexão com o BD


def Excluir(idproduto, endimg): #Função que irá excluir o produto do BD
    end = endimg
    idproduto = idproduto
    dados = "DELETE FROM produto WHERE idproduto = %d" % idproduto #Comando para excluir o item do BD, no formado que o BD aceita
    curso = conexao.cursor()#Cria um cursor para navegar e editar no BD
    curso.execute(dados) #Executa o comando salvo na variavel dado
    conexao.commit() #Confirma a execução do comando acima
    os.remove(end)

    curso.close() #Fecha o cursor


