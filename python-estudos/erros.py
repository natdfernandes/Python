try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
    num/0
except NameError:
    print("Entre com o valor numérico e não letras")
except ZeroDivisionError:
    print("divisão por zero")
except:
    print("Error")