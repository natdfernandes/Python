def entrada_nota_prova(mensagem):
    return float(input(mensagem))


def calcular_media(prova_1: float, prova_2: float, prova_3: float, prova_4: float):
    return (prova_1 + prova_2 + prova_3 + prova_4) / 4


def situacao_aluno(media_final: float):
    if media_final >= 7:
        return "Aprovado"
    elif media_final <= 5:
        return "Recuperação"
    else:
        return "Reprovado"
