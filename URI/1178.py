lista = []
var = float(input())
lista.append(var)

for i in range (1,100):
   lista.append(lista[i-1]/2)
  
for i in range (0,100):
  print("N[%d] = %.4f" % (i, lista[i]))

