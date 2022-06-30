import os
from pathlib import Path
import shutil
from skimage.transform import resize
import matplotlib.pyplot as plt


def grava(id_produto, imagem): #Recebe as variaveis necessarias para a funcção
    nome = id_produto
    filename = imagem
    consultadire = 'C:/teste/' + nome + '.jpg'  #Esta variavel vai receber o caminho da pasta e o nome da imagem
    if Path('C:/teste').is_dir(): # Vai verificar se existe uma pasta com o nome C:/teste
        direorigem = r'' + filename + '' #variavel que irá receber o diretorio de origem da imagem
        fileA = open(direorigem, 'rb') #variavel que irá receber a imagem/arquivo e vai abri-lo
        if os.path.isfile(consultadire): #Consulta se o arquivo já está existe na pasta
            os.remove(consultadire) #caso já existe o mesmo irá apaga-lo
        filename2 = r'C:/teste/' + nome + '.jpg' #Variavel que irá receber o novo caminho e o nome do arquivo copia
        fileB = open(filename2, 'wb') #Vai abrir o arquivo para edita-lo e salva-lo
        shutil.copyfileobj(fileA, fileB) #Cria uma copia do arquivo original
    else:
        dir = 'C:/teste' #variavel que irá receber o nome e caminho da pasta, caso não exista
        os.makedirs(dir) #ira criar a pasta no local e nome
        direorigem = r'' + filename + ''
        fileA = open(direorigem, 'rb')
        if os.path.isfile(consultadire):
            os.remove(consultadire)
        filename2 = r'C:/teste/' + nome + '.jpg'
        fileB = open(filename2, 'wb')
        shutil.copyfileobj(fileA, fileB)

    return filename2
