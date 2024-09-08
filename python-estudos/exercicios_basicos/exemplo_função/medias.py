import funcoes

alunos = []

for y in range(2):
    aluno = {}
    aluno["nome"] = input("Nome do aluno: ")

    for x in range(1, 5):
        aluno[f"prova-{x}"] = funcoes.entrada_nota_prova(
            f"Entre com a nota da prova {x} do aluno {aluno['nome']}: "
        )
    aluno["media-final"] = funcoes.calcular_media(
        aluno["prova-1"], aluno["prova-2"], aluno["prova-3"], aluno["prova-4"]
    )
    aluno["situacao"] = funcoes.situacao_aluno(aluno["media-final"])

    alunos.append(aluno)

for aluno in alunos:
    print(
        f"O aluno(a) {aluno['nome']} com média final: {aluno['media-final']} e situação: {aluno['situacao']}"
    )
