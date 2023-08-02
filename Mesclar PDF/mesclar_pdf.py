import PyPDF2
import os

merger = PyPDF2.PdfMerger()

caminho_pasta = "/home/dvdpericles/Programação/Vscode/NovosEstudos/Notebooks/Introdução Orientação Objetos/POO/Estudos_Dados/Mesclar PDF"

lista_arquivos = os.listdir(caminho_pasta)
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"{lista_arquivos}/{arquivo}")

merger.write('PDF_final.pdf')