#-----------------------------------------9
print ("Hora de Calcular a media escolar dos alunos!")
print("")



def registro(x):
    if (x==1):
        re01 = int(input("Digite o número de registro do aluno (números inteiros): "))
        print ("O RE do Aluno 1 é: ", re01)
    elif (x==2):
        re02 = int(input("Digite o número de registro do primeiro aluno (números inteiros): "))
        re021 = int(input("Digite o número de registro do segundo aluno (números inteiros): "))
        print ("O RE do Aluno 1 é: ", re02)
        print ("O RE do Aluno 2 é: ", re021)
    else:
        re03 = int(input("Digite o número de registro do primeiro aluno (números inteiros): "))
        re031 = int(input("Digite o número de registro do segundo aluno (números inteiros): "))
        re032 = int(input("Digite o número de registro do terceiro aluno (números inteiros): "))
        print ("O RE do Aluno 1 é: ", re03)
        print ("O RE do Aluno 2 é: ", re031)
        print ("O RE do Aluno 3 é: ", re032)



def media(x):
    if (x==1):
        z=1
        for x in range (1):
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            nota3 = float(input("Digite a terceira nota: "))
            nota4 = float(input("Digite a quarta nota: "))
            print("")

            media = (nota1+nota2+nota3+nota4)/4

            print ("A media do ", z ,"Aluno é: ", media)

            if (media > 6):
                    print("Aluno Aprovado")
            elif (media<7 and media>4):
                    print("Aluno de Exame")
            else:
                    print('Aluno de DP')

            print('')

            z+=1

    elif (x==2):
        z=1
        for x in range (2):
            nota01 = float(input("Digite a primeira nota: "))
            nota02 = float(input("Digite a segunda nota: "))
            nota03 = float(input("Digite a terceira nota: "))
            nota04 = float(input("Digite a quarta nota: "))
            print("")

            media = (nota01+nota02+nota03+nota04)/4

            print ("A media do ", z ,"Aluno é: ", media)

            if (media > 6):
                    print("Aluno Aprovado")
            elif (media<7 and media>4):
                    print("Aluno de Exame")
            else:
                    print('Aluno de DP')

            print('')

            z+=1

    else:
        z=1
        for x in range (3):
            nota001 = float(input("Digite a primeira nota do aluno"))
            nota002 = float(input("Digite a segunda nota do aluno"))
            nota003 = float(input("Digite a terceira nota do aluno"))
            nota004 = float(input("Digite a quarta nota do aluno "))
            print("")

            media = (nota001+nota002+nota003+nota004)/4

            print ("A media do ", z ,"Aluno é: ", media)

            if (media > 6):
                    print("Aluno Aprovado")
            elif (media<7 and media>4):
                    print("Aluno de Exame")
            else:
                    print('Aluno de DP')

            print('')

            z+=1