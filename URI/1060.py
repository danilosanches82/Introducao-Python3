#1060 - Números Positivos

cont = 0;
soma=0;
while cont<6:
  val = float(input( ))
  if val>0:
      soma +=1;
  cont +=1;

print("%d valores positivos" % soma)