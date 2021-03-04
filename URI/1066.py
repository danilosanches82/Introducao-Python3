cont=0
par=0
impar=0
positivo=0
negativo=0

while cont<5:
  val = int(input())
  if val % 2 ==0:
    par +=1    
  else:
    impar +=1    
  
  if val!=0:
    if val > 0:
      positivo +=1    
    else:
      negativo +=1     
      
  cont +=1  

print("%d valor(es) par(es)" % par)
print("%d valor(es) impar(es)" % impar)
print("%d valor(es) positivo(s)" % positivo)
print("%d valor(es) negativo(s)" % negativo)
