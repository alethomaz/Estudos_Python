import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione a pasta com os arquivos')

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": ["jpg", "png", "jpeg", "gif"], 
    "planilhas": ["xlsx", "csv", "ods"],
    "pdfs": ["pdf"],
    "csvs": ["csv"],
}

for arquivo in lista_arquivos:
    # 01. arquivo.pdf
    nome, extensao = os.path.splitext(arquivo)
    for pasta in locais:
        if extensao[1:] in locais[pasta]:
            caminho_origem = os.path.join(caminho, arquivo)
            caminho_destino = os.path.join(caminho, pasta, arquivo)
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(caminho_origem, caminho_destino)

