cont=0
contPositivo=0
soma=0
while cont<6:
  val = float(input())
  if val >0:
    contPositivo +=1;
    soma +=val
  cont +=1  

print("%d valores positivos" % contPositivo)
print("%.1f" % (soma/contPositivo))