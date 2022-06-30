import mysql.connector

host = '***'
database = '****'
user = '****'
password = '****'

conexao = mysql.connector.connect(host=host, database=database, user=user, password=password)


def consulta(idproduto): #Função para consultar um produto no banco
    idproduto = idproduto
    sqlconsultar = "SELECT * FROM produto WHERE idproduto = %d" % idproduto #Comando aceitado pelo BD para realizar uma consulta
    curso = conexao.cursor() #Cria um cursor que poderá navegar no BD
    curso.execute(sqlconsultar) #Executa o comando salvo na variavel sqlconsulta
    linhas = curso.fetchall() #Cria um lista para receber os itens do BD
    for linhas in linhas: #Faz com que todos os itens da lista sejam salvos em suas respectivas variaveis
        nome = linhas[1]
        descricao = linhas[2]
        estoque = linhas[3]
        preco = linhas[4]
        imagem = linhas[5]
        return nome, descricao, estoque, preco, imagem #Retorna o valor das variaveis para o comando que chamou a função 

    curso.close()
