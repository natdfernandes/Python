# 3 input: nome, nota1 float, nota2 float
# processamento: calcular media do aluno
# saida: output informações do aluno
# apenas uma variavel aluno
aluno = {}
aluno["nome"] = input("nome do aluno: ")
aluno["nota1"] = float(input("nota da prova1: "))
aluno["nota2"] = float(input("nota da prova2: "))

aluno["mediafinal"] = (aluno["nota1"] + aluno["nota2"]) / 2
if aluno["mediafinal"] >=5:
    aluno["status"]="aprovado"
else:
    aluno["status"]="reprovado"


print("informção do aluno: ", aluno)
print("Média final: ", aluno["mediafinal"])
