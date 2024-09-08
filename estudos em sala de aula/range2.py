nomes =["N0", "N1", "N2", "N3", "N4"]
for n in nomes:
    print(n)
    print('\n - - -')
    cont = 0
    for v in range(0, 5):
     if cont <2:
        print(nomes[v], end=',')
    if (cont % 2 ==1):

        print('')
        print('teste')
        