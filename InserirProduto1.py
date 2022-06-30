from Grava_imagem import grava
import mysql.connector

host = ***
database = ****
user = ****
password = ****

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password) #Criar uma conexao com o BD

def inserir(idproduto, nome, descricao, estoque, valor, imagem=""): #Recebe as varaiveis que serao passadas ao chamar a função
    idproduto = idproduto
    nome = nome
    descricao = descricao
    estoque = estoque
    valor = valor
    imagem = imagem
    if imagem != " ": #Verificar se a variavel imagem não esta vazia
        novodestino = grava(idproduto, imagem) #Caso não esteja vazia chama a função para copia a imagem em um novo destino
    curso = conexao.cursor() #cria um cursor para trabalhar no BD
    #abaixo cria uma variavel onde é passados todos os dados para o BD no formado especifico do banco
    dados = "INSERT INTO produto (idproduto, nome, descricao, estoque, preco, imagem) VALUES (" + idproduto + ',\'' + nome + '\',' + '\'' + descricao + '\',' + estoque +',' + valor + ',\'' + novodestino +'\');'
    curso.execute(dados) #Executa no banco as informações passadas pela variavel
    conexao.commit() #Confirmar a execução da funçao acima

    curso.close() #Fecha o cursor
