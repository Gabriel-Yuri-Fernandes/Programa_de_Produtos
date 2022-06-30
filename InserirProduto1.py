from Grava_imagem import grava
import mysql.connector

host = 'localhost'
database = 'para_teste'
user = 'root'
password = 'admin'

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password)

def inserir(idproduto, nome, descricao, estoque, valor, imagem=""):
    idproduto = idproduto
    nome = nome
    descricao = descricao
    estoque = estoque
    valor = valor
    imagem = imagem
    if imagem != " ":
        novodestino = grava(idproduto, imagem)
    curso = conexao.cursor()
    dados = "INSERT INTO produto (idproduto, nome, descricao, estoque, preco, imagem) VALUES (" + idproduto + ',\'' + nome + '\',' + '\'' + descricao + '\',' + estoque +',' + valor + ',\'' + novodestino +'\');'
    curso.execute(dados)
    conexao.commit()

    curso.close()