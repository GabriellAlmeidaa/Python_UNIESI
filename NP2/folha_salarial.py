re = str(input('Digite o RE do funcinário: '))
nome = str(input('Digite o nome do funcionário: '))
a = 1

while a == 1:
    salario = float(input('Digite o salário do funcionário: '))
    if (salario>=998.00):
        a = 2
    else:
        print("Valor invalido")

if (salario<1751.82):
    inss = salario * 8/100
elif (salario<2919.73):
    inss = salario * 9/100
elif (salario<5839.45):
    inss = salario * 11/100
else:
     inss = salario * 11/100

if (salario>1903.98) and (salario<2826.65):
    IR = (salario*(7.5/100))-142.80
elif (salario>2826.65) and (salario<3751.06):
    IR = (salario*(15/100))-354.80
elif (salario>3751.05) and (salario<4664.69):
    IR = (salario*(22.5/100))-636.13
else: 
    IR = (salario*(27.5/100))-869.36

SL = (salario-inss-IR)
print ('RE = ',re)
print ('NOME = ',nome)
print ('SALÁRIO BRUTO = ',salario)
print ('INSS = ',inss)
print ('IR = ',IR)
print ('SALÁRIO LÍQUIDO = ', SL)