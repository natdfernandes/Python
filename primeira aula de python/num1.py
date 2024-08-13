num1=float(input('primeira nota do aluno'))
num2=float(input('segunda nota do aluno'))
if(num1+num2)/2>=5:
    print("passou primeira parte")
    print((num1+num2)/2)
    if(num1+num2)/2>7:
        print("aluno aprovado")
        print((num1+num2)/2)
    else:
        print("aluno em exame")
        print((num1+num2)/2)
    else:
        print("aluno reprovado")     
        print((num1+num2)/2)  
    print("fim do programa")       
