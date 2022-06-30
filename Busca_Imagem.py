from tkinter.filedialog import askopenfilename


def imagem(): # Comando para fará a busca do local de uma imagem ou aquivo
    filename = askopenfilename()

    return filename #retorna o local que o arquivo estava e até o proprio arquivo

