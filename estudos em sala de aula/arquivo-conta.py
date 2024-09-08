#importar biblioteca
import csv

total= 0

with open('arquivo.csv', newline='')as csvfile:
    reader = csv.reader (csvfile, delimiter= ',')
    for row in reader:
        total += float(row[1])
        print(row)

  # total = 0
  # totaln += row[1]   

saldo= "{:.2f}".format(total)   
print(f'saldo R$ {saldo}')