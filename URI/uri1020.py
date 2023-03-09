dias=int(input())
anos=0
meses=0
while dias>=365:
    anos+=1
    dias-=365
while dias >=30:
    meses+=1
    dias-=30
print('%d ano(s)'%(anos))
print('%d mes(es)'%(meses))
print('%d dia(s)'%(dias))