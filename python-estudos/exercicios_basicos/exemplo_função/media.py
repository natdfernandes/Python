import funcoes

prova_1 = funcoes.entrada_nota_prova("Entre com a nota da prova 1: ")
prova_2 = funcoes.entrada_nota_prova("Entre com a nota da prova 2: ")
prova_3 = funcoes.entrada_nota_prova("Entre com a nota da prova 3: ")
prova_4 = funcoes.entrada_nota_prova("Entre com a nota da prova 4: ")

media_final = funcoes.calcular_media(prova_1, prova_2, prova_3, prova_4)

print(funcoes.situacao_aluno(media_final))
print(f"Média final: {media_final}")
