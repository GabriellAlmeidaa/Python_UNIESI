a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))
delta = b**2 - 4*a*c
print ('Delta = ', delta)
rdel = delta**0.5
print ('Raiz de delta = ', rdel)
x1 = (-b+rdel)/(2*a)
x2 = (-b-rdel)/(2*a)
print ('x1 = ', x1)
print ('x2 = ', x2)