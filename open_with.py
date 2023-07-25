'''arquivo = open("meu_arquivo.txt", "w")
arquivo.write("meu primeiro arquivo em python")
arquivo.close()
'''
caminho_arquivo = '/home/dvdpericles/Programação/Vscode/NovosEstudos/Notebooks/Introdução Orientação Objetos/POO/Estudos_Dados/meu_arquivo.txt'

with open(caminho_arquivo, 'a') as arquivo:
    arquivo.write('meu primeiro arquivo em python 1\n')