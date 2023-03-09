valor = int(input())
val100=0
val50=0
val20=0
val10=0
val5=0
val2=0
val1=0
aux = valor
while aux >=100:
    aux-=100
    val100+=1
while aux >=50:
    aux-=50
    val50+=1
while aux >=20:
    aux-=20
    val20+=1
while aux >=10:
    aux-=10
    val10+=1
while aux >=5:
    aux-=5
    val5+=1
while aux >=2:
    aux-=2
    val2+=1
while aux >=1:
    aux-=1
    val1+=1
print('%d\n'%(valor))
print('%d nota(s) de R$ 100,00'%(val100))
print('%d nota(s) de R$ 50,00'%(val50))
print('%d nota(s) de R$ 20,00'%(val20))
print('%d nota(s) de R$ 10,00'%(val10))
print('%d nota(s) de R$ 5,00'%(val5))
print('%d nota(s) de R$ 2,00'%(val2))
print('%d nota(s) de R$ 1,00'%(val1))