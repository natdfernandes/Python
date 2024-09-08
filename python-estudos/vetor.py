tamanho = 2
vetor1 = [0] * tamanho
vetor2 = [0] * tamanho
vetor3 = [0] * tamanho

for i in range(tamanho):
    vetor1[i] = float(input(f"Digite um número do vetor1[{i}]: "))

    while True:
        vetor2[i] = float(input(f"Digite o número do vetor2[{i}] Diferente de zero: "))
        if vetor2[i] != 0:
            break

operacao = input("Digite a operação: [/,*,-,+]: ")

for i in range(tamanho):

    match operacao:
        case "/":
            vetor3[i] = vetor1[i] / vetor2[i]
        case "*":
            vetor3[i] = vetor1[i] * vetor2[i]
        case "+":
            vetor3[i] = vetor1[i] + vetor2[i]
        case "-":
            vetor3[i] = vetor1[i] - vetor2[i]
        case _:
            print("opção invalida")

    print(f"vetor3[{i}] = {vetor3[i]:.2f}")
