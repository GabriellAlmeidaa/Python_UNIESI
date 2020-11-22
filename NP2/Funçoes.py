#-----------------------------------------6
def rud(a):
    if (a % 2 == 1):
        print(1)
    else:
        print(0)

x = int(input("Digite um valor inteiro: "))

rud(a)
#-----------------------------------------7
def função(x):
    if (a>=1):
        print(1)
    elif (a<=-1):
        print(-1)
    else:
        print(0)

x = int(input("Digite um valor inteiro: "))

função(a)
#-----------------------------------------8
def form(forma):
    if (forma == 1):
      r = float(input("Digite o raio do círculo: ")) 
      A = 3,14*(r**2)
      print(A)
    elif (forma == 2):
       l = float(input("Digite o lado do quadrado: ")) 
       ll = l*l
       print(ll)
    elif (forma == 3):
      lu = float(input("Digite a base do retângulo: ")) 
      ld = float(input("Digite o lado do retângulo: "))
      la = lu*ld
      print(la)
    else:
      tb = float(input("Digite a base do triângulo: ")) 
      th = float(input("Digite o altura do triângulo: "))
      ta = (tb*th)/2
      print(ta)
        


forma = int(input("Digite (1) para círculo, (2) para quadrado, (3) para retângulo e (4) para triângulo: "))

form(forma)