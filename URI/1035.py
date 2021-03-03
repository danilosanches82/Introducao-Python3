#	1035 - Teste de Seleção 1

a,b,c,d = input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)

soma1=c+d
soma2=a+b
if ( b>c ) and ( d>a ) and ( soma1>soma2 ) and ( a%2==0):
    print( "Valores aceitos" )
else:
    print( "Valores nao aceitos" )