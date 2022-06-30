import os
from pathlib import Path
import shutil
from skimage.transform import resize
import matplotlib.pyplot as plt


def grava(id_produto, imagem):
    nome = id_produto
    filename = imagem
    consultadire = 'C:/teste/' + nome + '.jpg'
    if Path('C:/teste').is_dir():
        direorigem = r'' + filename + ''
        fileA = open(direorigem, 'rb')
        if os.path.isfile(consultadire):
            os.remove(consultadire)
        filename2 = r'C:/teste/' + nome + '.jpg'
        fileB = open(filename2, 'wb')
        shutil.copyfileobj(fileA, fileB)
    else:
        dir = 'C:/teste'
        os.makedirs(dir)
        direorigem = r'' + filename + ''
        fileA = open(direorigem, 'rb')
        if os.path.isfile(consultadire):
            os.remove(consultadire)
        filename2 = r'C:/teste/' + nome + '.jpg'
        fileB = open(filename2, 'wb')
        shutil.copyfileobj(fileA, fileB)

    return filename2