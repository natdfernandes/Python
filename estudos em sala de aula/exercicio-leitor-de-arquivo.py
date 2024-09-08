#precisar usar as bibliotecas os, platform
import os
import platform


#solicitar ao usuario nome de um arquivo 
nome_arquivo = input("digite o nome do arquivo: ")

#verificar se o arquivo existe 
if os.path.exists(nome_arquivo):
    print("Arquivo existe")
try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        #verificar se o arquivo não esta vazio
        if len(conteudo)==0:
            print("o arquivo está vazio")
        else:
            #contar a quantidade de linhas do arquivo
            numero_de_linhas = conteudo.count("\n") + 1
            print(f"Arquivo possui {numero_de_linhas} linha(s)")

            #mostrar conteudo do arquivo
            print(conteudo)
except IOError:
    print ("o arquivo não existe!")
