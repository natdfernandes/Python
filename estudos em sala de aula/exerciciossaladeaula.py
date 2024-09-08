num1= float(input('primeiro sensor '))
num2= float(input('segundo sensor '))
media= (num1+num2)/2
if media <=30:
    print("Está quente")
    print((num1+num2)/2)
elif media <=20:
    print("um pouco quente")
    print((num1+num2))/2
elif(num1+num2)/2 <=10:
    print("quente")
    print((num1+num2))/2
else:
    print("muito quente ou muito frio")
    print((num1+num2)/2)
    print("Fim do programa")

