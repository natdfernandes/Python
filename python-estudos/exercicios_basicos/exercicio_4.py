def par_ou_impar(numero):       
    return numero % 2 == 0
# ============

numero=int(input("informe um numero inteiro qualquer: "))
if par_ou_impar(numero):
    print(f'O número {numero} é par' ) 
else: 
    print(f'O numero {numero} é ímpar:')
