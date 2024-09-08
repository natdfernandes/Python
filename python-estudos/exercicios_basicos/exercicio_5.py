def par_ou_impar(numero):
    if numero % 2 == 0: 
        return(f'O número {numero} é par' ) 
    else: 
        return(f'O numero {numero} é ímpar:')

# ============    
numero=int(input("informe um numero inteiro qualquer: "))
print(par_ou_impar(numero))                    
