p1=0
p2=0
p3=0
p4=0

p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())

mediafinal= (p1 + p2 + p3 + p4)/4
if mediafinal >=7:
    print("aprovado")
elif mediafinal <=5:
    print("recuperação")
else:
    print("reprovado")

print(mediafinal)
