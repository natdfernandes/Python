salarioAntigo = 3000
valeAntigo = 20
ajuste = 0.05
valorDoAjuste = salarioAntigo * ajuste
novoSalario = salarioAntigo + valorDoAjuste
valeNovo = 28
diasUteis = 20
horasDeTrabalho = 6

novoSalario += (valeNovo * diasUteis)
valorPorHora = novoSalario / (diasUteis * horasDeTrabalho)

print("salario", novoSalario)
print(f"salario por hora {valorPorHora:.2f}")
