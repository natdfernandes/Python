import csv
import os
import platform



def menu():
   print("1 - Buscar arquivos")
   print("2 - Verificar se o arquivo esta vazio ou não")
   print("3 - Mostra conteudo do arquivo")
   print("4 - Quantidade de linhas do arquivo")
   print("5 - Sair")


def opcao_1():

   nome_arquivo = input("\nDigite o nome do arquivo: ")

   try:
      with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
         # Cria um leitor CSV com o delimitador especificado
         reader = csv.reader(csvfile, delimiter=';')
         print(f"\n\n{nome_arquivo} encontrado com sucesso\n\n")
   except FileNotFoundError:
      print(f"\n\nO arquivo {nome_arquivo} não foi encontrado.\n\n")
   except Exception as e:
      print(f"Ocorreu um erro: {e}")


def opcao_2():
   nome_arquivo = input("\nDigite o nome do arquivo: ")

   try:
      with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
         # Cria um leitor CSV com o delimitador especificado
         reader = csv.reader(csvfile, delimiter=';')
         numero_linhas = sum(1 for row in reader)
         if numero_linhas == 0:
            print("\n O arquivo ESTÁ VAZIO !!!\n")
         else:
            print("\n\n O arquivo NÃO esta VAZIO !!! \n\n")

   except FileNotFoundError:
      print(f"\n\nO arquivo {nome_arquivo} não foi encontrado.\n\n")
   except Exception as e:
      print(f"Ocorreu um erro: {e}")


def opcao_3():
   total = 0
   nome_arquivo = input("\nDigite o nome do arquivo: ")

   with open(nome_arquivo, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=';')
      for row in reader:
         total += float(row[1])
         print(row)


def opcao_4():
   nome_arquivo = input("\nDigite o nome do arquivo: ")

   with open(nome_arquivo, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=';')
      numero_linhas = sum(1 for row in reader)
      print(f'\n Numero de linhas = {numero_linhas}\n')


while True:
   menu()
   escolha = input("Escolha uma opcao:")

   if escolha == '1':
      opcao_1()
   elif escolha == '4':
      opcao_4()
   elif escolha == '3':
      opcao_3()
   elif escolha == '2':
      opcao_2()
   ##elif escolha == '5':
   ##  opcao_5()
