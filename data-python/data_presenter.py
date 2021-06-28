cupcakeFile = open('CupcakeInvoices.csv')
import matplotlib.pyplot as plt

total = 0

choco = 0
vanilla = 0
strawberry = 0

for i in cupcakeFile:
  i = i.rstrip('\n').split(',')
  #print(i)
  #print(i[2])
  #print(round(float(i[3]) * float(i[4]), 2))

  if i[2] == "Chocolate":
    choco += round(float(i[3]) * float(i[4]), 2)
  elif i[2] == "Vanilla":
    vanilla += round(float(i[3]) * float(i[4]), 2)
  elif i[2] == "Strawberry":
    strawberry += round(float(i[3]) * float(i[4]), 2)

  total += round(float(i[3]) * float(i[4]), 2)



print(round(total, 2))
print(round(choco, 2))
print(round(vanilla, 2))
print(round(strawberry, 2))

types = ["choco", "vanilla", "strawberry"]
totals = [choco, vanilla, strawberry]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(types, totals)

plt.show()