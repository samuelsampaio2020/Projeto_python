import os
class exercicio:
    def __init__(self) -> None:
        self.alcance1 = 0
        self.alcance2 = 0
        self.alcance3 = 0
        self.alcance4 = 0
        self.votos = {}
        self.total = 0
        self.x = False
        self.votos_ana = 0
        self.votos_bruno = 0
        self.votos_carlos = 0
        self.votos_daniel = 0
        self.votos_nulo = 0
        self.votos_branco = 0
        self.pedidos = {}
        self.total = 0.0
    
    def Questao_17(self):
        import math
        area = float(input("area a ser pintada:"))
        litros_necessario = area/6
        litros_lata = 18
        litros_galao = 3.6
        preco_lata = 80
        preco_galao = 25
        q_latas = math.ceil(litros_necessario/litros_lata)
        custo_latas = q_latas*preco_lata
        print(f"_Comprando Apenas latas>\nO Cliente Precisa {q_latas} lata , que custaram:{custo_latas}")
        q_galoes = math.ceil(litros_necessario/litros_galao)
        custo_galao = q_galoes*preco_galao
        print(f"_Comprando Apenas Galoes>\no Cliente Precisa {q_galoes} galao, que custaram:{custo_galao}")
        folga_litros_necessario = litros_necessario * 1.1
        q_latas_c = int(folga_litros_necessario // litros_lata)
        faltando_litros_folga = folga_litros_necessario - (q_latas_c*litros_lata)
        q_galoes_c = int(math.ceil(faltando_litros_folga/litros_galao))
        custo_total = (q_latas_c * preco_lata) + (q_galoes_c*preco_galao)
        print(f"_O Custo Total>\no Cliente precisa comprar {q_latas_c} lata e {q_galoes_c} galao, que juntos custam {custo_total}")

    def Questao_18(self):
        tamanho = float(input("informe o tamanho do arquivo:"))
        velocidade = float(input("informe a velocidade em mbps:"))
        max = ((tamanho/velocidade)*60)
        if(max>60):
            max = max/60
            print(f"tempo: {max:.0f}:horas")

        else:print(f"tempo: {max:.0f}:min")

    def Questao_19(self):
        valores= []
        for x in range(1,3):
            valores.append(int(input(f"informe o valor {x}:")))
        if(valores[0] > valores[1]):
            print(f"O Maior é {valores[0]}\nMenor é {valores[1]}")
        else:
            print(f"O Maior é {valores[1]}\nMenor é {valores[0]}")

    def Questao_20(self):
        valor = int(input("informe um Numero_:"))

        if(valor<0):
            print(f"O valor {valor} é negativo")
        else:print(f"O valor {valor} é Positivo")

    def Questao_21(self):
        op = 1
        while(op ==1):
            valida = input("Informe Seu Genero \n'F' para Feminino\n'M' para Masculino\nEntão: ").upper()

            if(valida == "F"):
                print(f"Letra {valida} representa Feminino")
                op =0

            elif(valida == "M"):
                print(f"Letra {valida} representa Masculino")
                op = 0
            else:
                print("\nvalor Informado Está Errado\n")

    def Questao_22(self):
        Letra = input("informe um letra:")

        consoantes = ['B','C','D','F','G','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
        vogais = ['A','I','U','E','O']
        verificando = [x for x in consoantes if x == Letra]
        verificandoV = [x for x in vogais if x == Letra]
        if(verificando):
            print("A Letra é uma Consoante")
        elif(verificandoV):
            print("a Letra é uma vogal")

    def Questao_23(self):
        import math
        nota_1 = float(input("informe a primeira nota:"))
        nota_2 = float(input("informe a segunda nota:"))

        media = math.ceil((nota_1+nota_2)/2)
        if(media>=7 and media<10):
            print("Aprovado")
        elif(media==10):
            print("Aprovado Com Distinção")
        else:
            print("REPROVADO")

    def Questao_24_25(self):
        n1 = int(input("informe o valor de n1:"))
        n2 = int(input("informe o valor de n2:"))
        n3 = int(input("informe o valor de n3:"))
        numeros = [n1,n2,n3]
        maior = n1
        menor = n1
        for x in numeros:
            if(x > maior):
                print(f"{x} é Maior Que {maior} Então Recebe {x}")
                maior = x
            elif(x < menor):
                print(f"{x} é Menor Que {maior} Então Recebe {x}")
                menor = x
        print(f"O Maior = {maior}\nO Menor = {menor}")

    def Questao_26(self):
        produto1 = "Banana"
        produto2 = "Maça"
        produto3 = "Limao"
        valor_1 = float(input(f"informe o preço Da {produto1}:"))
        valor_2 = float(input(f"informe o preço Da {produto2}:"))
        valor_3 = float(input(f"informe o preço Da {produto3}:"))

        print(f"Pedido\nBanana preço:R${valor_1}\nMaça preço:R${valor_2}\nlimao preço:R${valor_3}")

        if(valor_1 < valor_2 and valor_1 <valor_3):
            print(f"O melhor Produto pro Seu Bolso é A {produto1} com Seu preço:R${valor_1}")
        elif(valor_2 < valor_1 and valor_2 < valor_3):
            print(f"O melhor Produto pro Seu Bolso é A {produto2} com Seu preço:R${valor_2}")
        else:
            print(f"O melhor Produto pro Seu Bolso é O {produto3} com Seu preço:R${valor_3}")

    def Questao_27(self):
        n1 = int(input("Informe o Numero_1:")) 
        n2 = int(input("Informe o Numero_2:"))
        n3 =int(input("Informe o Numero_3:"))
        print(n1,n2,n3)
        if(n3 > n2):
            aux = n3
            n3 = n2
            n2 = aux
        if(n2 > n1):
            aux = n2
            n2 = n1
            n1 = aux
        if(n3 > n2):
            aux = n3
            n3 = n2
            n2 = aux
        print(n1,n2,n3)

    def Questao_28(self):
        turno = input("em que turno você estuda\n'M'-Matutino\n'V'-Vespertino\n'N'-Noturno\nResp:").upper()

        if(turno == "M"):
            print("Bom Dia")
        elif( turno == "V"):
            print("Boa Tarde")
        elif( turno == "N"):
            print("Boa noite")
        else:
            print("Valor Invalido") 

    def Questao_29(self):
        salario_colaborador = float(input("Informe Seu Salario:"))
        salario_colaborador_inicial = salario_colaborador

        vinte_porcento = 1.20
        quinze_porcento = 1.15
        dez_porcento = 1.1
        cinco_porcento = 1.05

        if salario_colaborador <= 280:
            salario_colaborador *= vinte_porcento
            aumento_no_salario = salario_colaborador - salario_colaborador_inicial
            print(f"""\n
                O salario antes do reajuste:{salario_colaborador_inicial}
                o percentual de aumento aplicado:20%
                o Aumento do salario:{aumento_no_salario:.2f}
                o salario Final:{salario_colaborador:.2f}\n""")
            
        elif salario_colaborador >=281 and salario_colaborador <=700:
            salario_colaborador *= quinze_porcento
            aumento_no_salario = salario_colaborador - salario_colaborador_inicial
            print(f"""\n
                O salario antes do reajuste:{salario_colaborador_inicial}
                o percentual de aumento aplicado:15%
                o Aumento do salario:{aumento_no_salario:.2f}
                o salario Final:{salario_colaborador:.2f}\n""")
        elif salario_colaborador >= 701 and salario_colaborador <=1500:
            salario_colaborador *= dez_porcento
            aumento_no_salario = salario_colaborador - salario_colaborador_inicial
            print(f"""\n
                O salario antes do reajuste:{salario_colaborador_inicial}
                o percentual de aumento aplicado:10%
                o Aumento do salario:{aumento_no_salario:.2f}
                o salario Final:{salario_colaborador:.2f}\n""")
        elif salario_colaborador >=1501:
            salario_colaborador *= cinco_porcento
            aumento_no_salario = salario_colaborador - salario_colaborador_inicial
            print(f"""\n
                O salario antes do reajuste:{salario_colaborador_inicial}
                o percentual de aumento aplicado:5%
                o Aumento do salario:{aumento_no_salario:.2f}
                o salario Final:{salario_colaborador:.2f}\n""")

    def Questao_30(self):
        horas_trabalhadas = int(input("informe quantas horas voce trabalha no mês:"))
        ganho_por_hora = float(input("Informe O Ganho Por Hora:"))

        Salario_Bruto = ganho_por_hora*horas_trabalhadas

        INSS = 1.1
        FGTS = 1.11

        if(Salario_Bruto <= 900):
            IR = (0 * Salario_Bruto) - Salario_Bruto
            INSS = (INSS * Salario_Bruto) - Salario_Bruto
            FGTS = (FGTS * Salario_Bruto) - Salario_Bruto
            Desconto = IR + INSS
            Salario_Liquido = (Salario_Bruto - Desconto)
            print(f"""
            Salário Bruto:({ganho_por_hora} * {horas_trabalhadas})                                :R$ {Salario_Bruto}
            (-) IR (0%)                                              :R$ {IR}
            (-) INSS ( 10% )                                         :R$ {INSS}
            FGTS (11%)                                               :R$ {FGTS}
            Total Desconto                                           :R$ {Desconto}
            Salário Liquido                                          :R$ {Salario_Liquido}
            """)
        elif Salario_Bruto >=901 and Salario_Bruto<= 1500:
            IR = (1.05 * Salario_Bruto) - Salario_Bruto
            INSS = (INSS * Salario_Bruto) - Salario_Bruto
            FGTS = (FGTS * Salario_Bruto) - Salario_Bruto
            Desconto = IR + INSS
            Salario_Liquido = (Salario_Bruto - Desconto)
            print(f"""
            Salário Bruto:({ganho_por_hora} * {horas_trabalhadas})                                :R$ {Salario_Bruto}
            (-) IR (5%)                                              :R$ {IR}
            (-) INSS ( 10% )                                         :R$ {INSS}
            FGTS (11%)                                               :R$ {FGTS}
            Total Desconto                                           :R$ {Desconto}
            Salário Liquido                                          :R$ {Salario_Liquido}
            """)
        elif Salario_Bruto >= 1501 and Salario_Bruto <=2500:
            IR = (1.1 * Salario_Bruto) - Salario_Bruto
            INSS = (INSS * Salario_Bruto) - Salario_Bruto
            FGTS = (FGTS * Salario_Bruto) - Salario_Bruto
            Desconto = IR + INSS
            Salario_Liquido = (Salario_Bruto - Desconto)
            print(f"""
            Salário Bruto:({ganho_por_hora} * {horas_trabalhadas})                                :R$ {Salario_Bruto}
            (-) IR (10%)                                              :R$ {IR}
            (-) INSS ( 10% )                                         :R$ {INSS}
            FGTS (11%)                                               :R$ {FGTS}
            Total Desconto                                           :R$ {Desconto}
            Salário Liquido                                          :R$ {Salario_Liquido}
            """)
        elif Salario_Bruto >=2501 :
            IR = (1.2 * Salario_Bruto) - Salario_Bruto
            INSS = (INSS * Salario_Bruto) - Salario_Bruto
            FGTS = (FGTS * Salario_Bruto) - Salario_Bruto
            Desconto = IR + INSS
            Salario_Liquido = (Salario_Bruto - Desconto)
            print(f"""
            Salário Bruto:({ganho_por_hora} * {horas_trabalhadas})                                :R$ {Salario_Bruto}
            (-) IR (20%)                                              :R$ {IR}
            (-) INSS ( 10% )                                         :R$ {INSS}
            FGTS (11%)                                               :R$ {FGTS}
            Total Desconto                                           :R$ {Desconto}
            Salário Liquido                                          :R$ {Salario_Liquido}
            """)

    def Questao_31(self):
        dia = int(input("Informe o dia da semana:"))
        complemento = "-Feira"

        if dia == 1:
            print("Domingo")
        elif dia == 2:
            print("Segunda"+complemento)
        elif dia == 3:
            print("Terça"+complemento)
        elif dia == 4:
            print("Quarta"+complemento)
        elif dia == 5:
            print("Quinta"+complemento)
        elif dia == 6:
            print("Sexta"+complemento)
        elif dia == 7:
            print("Sábado")
        else:
            print("Valor Invalido")

    def Questao_32(self):
        nota_1 = float(input("Informe a nota 1:"))
        nota_2 = float(input("Informe a nota 2:"))

        media = (nota_1+nota_2)/2

        if media >=9 and media <=10:
            nota = "A"
            print(f"""
                Nota 1:{nota_1}
                Nota 2:{nota_2}
                Media:{media}
                Conceito:{nota}
                Status:!APROVADO!    
            """)
        elif media >=7.5 and media <=8.9:
            nota = "B"
            print(f"""
                Nota 1:{nota_1}
                Nota 2:{nota_2}
                Media:{media}
                Conceito:{nota}
                Status:!APROVADO!    
            """)
        elif media >=6 and media <=7.4:
            nota = "C"
            print(f"""
                Nota 1:{nota_1}
                Nota 2:{nota_2}
                Media:{media}
                Conceito:{nota}
                Status:!APROVADO!    
            """)
        elif media >=4 and media <=5.9:
            nota = "D"
            print(f"""
                Nota 1:{nota_1}
                Nota 2:{nota_2}
                Media:{media}
                Conceito:{nota}
                Status:!REPROVADO!    
            """)
        elif media >=0 and media <=3.9:
            nota = "E"
            print(f"""
                Nota 1:{nota_1}
                Nota 2:{nota_2}
                Media:{media}
                Conceito:{nota}
                Status:!REPROVADO!    
            """)
        
    def Questao_33(self):
        lado_1 = int(input("informe o Primeiro Lado:"))
        lado_2 = int(input("informe o Segundo Lado:"))
        lado_3 = int(input("informe o Terceiro Lado:"))
        if lado_1 == lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1:
            print("o Triângulo é Isósceles:Possui dois lados iguais")
        elif lado_1 != lado_2 != lado_3:
            print("o Triângulo Escaleno:Possui os três lados diferentes")
        elif lado_1 == lado_2 == lado_3:
            print("Triângulo Equilátero:Possui três lados iguais")

    def Questao_34(self):
        import math

        print("equação do segundo grau: A*x^2 + B*x + C = 0")

        a = int(input("informe o valor de A:"))

        if(a == 0):
            print("A Equação não é do segundo Grau")
        elif(a>0):
            b = int(input("informe o valor de B:"))
            c = int(input("informe o valor de C:"))
            print("calculando o Delta = B^2 -4*a*c")
            Delta = ((b**2)-4*(a*c))
            print(f"Valor de Delta:{Delta}")
            if(Delta < 0):
                print(f"""A Equação não possui Raizes reais , pois o Delta({Delta}) é Negativo""")

            elif(Delta == 0):
                raiz = int(math.sqrt(Delta))
                print(f"Raiz de Delta:{raiz}")
                Raiz_1 = float((-(b)+raiz)/(2*a))
                Raiz_2 = float((-(b)-raiz)/(2*a))
                print(f"""Delta possui apenas uma Raiz :{Raiz_1:.2f} e {Raiz_2:.2f}""")

            elif(Delta > 0):
                raiz = int(math.sqrt(Delta))
                print(f"Raiz de Delta:{raiz}")
                Raiz_1 = float((-(b)+raiz)/(2*a))
                Raiz_2 = float((-(b)-raiz)/(2*a))
                print(f"""Delta possui duas Raizes :{Raiz_1:.2f}, {Raiz_2:.2f}""")

    def Questao_35(self):
        ano = int(input("para Saber Se o Ano é Bisexto informe:"))

        if(ano%4==0 and ano%100!=0) or (ano%400==0):
            print(f"o ano {ano} é Bissexto")
        else:
            print(f"o ano {ano} NÃO é Bissexto")

    def Questao_36(self):
        dia = input("infome o Dia:")
        mes = input("informe o mes:")
        ano = input("informe o Ano:")
        print(f"{dia}/{mes}/{ano}")
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if dia != 0 and mes != 0 and ano != 0:
            if dia > 29 and mes == 2:
                print("Data Invalida\nNão Existe esse dia desse mes")
            elif dia <=31 and mes <= 12:
                print("Data Valida")
            else:
                print("Data Invalida")
        else:
            print("Data Invalida")

    def Questao_37(self):
        n_digitado = int(input("informe um numero até 1000:"))
        n = [n_digitado,326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 , 16]

        if n_digitado >0 and n_digitado <1000:
            for numero in n:
                numero_texto = str(numero)
                if numero >=100 and numero<1000:
                    centena = numero_texto[0]
                    dezena = numero_texto[1]
                    unidade = numero_texto[2]
                    print(f"""
                        {centena} Centenas, {dezena} Dezenas e {unidade} Unidades
                        """)
                elif numero <=99 and numero >= 10:
                    dezena = numero_texto[0]
                    unidade = numero_texto[1]
                    print(f"""
                        {dezena} Dezenas e {unidade} Unidades
                        """)
                elif numero >0 and numero <10:
                    unidade = numero_texto[0]
                    print(f"""
                        {unidade} Unidades
                        """)
        else:
            print("O Valor ultrapassou o limite dos 1000")

    def Questao_38(self):
        valor = int(input("Informe o um valor até 600:"))
        if valor >=10 and valor <= 600:
            cem = valor//100
            valor = valor - cem * 100
            cinquenta = valor//50
            valor = valor - cinquenta * 50
            dez = valor//10
            valor = valor - dez * 10
            cinco = valor//5
            valor = valor - cinco * 5
            um = valor
            if cem > 0:
                print(f"{cem} notas de cem")
            if cinquenta > 0:
                print(f"{cinquenta} notas de cinquenta")
            if dez > 0:
                print(f"{dez} notas de dez")
            if cinco > 0:
                print(f"{cinco} notas de cinco ")
            if um > 0:
                print(f"{um} notas de um")
        else:
            print("Valor minimo é 10 e o maximo é 600")

    def Questao_39(self):
        op =1
        while op == 1:
            numero = int(input("""
                    para Sair digite:'0'
                    ----------------------
                    informe um numero:"""))
            if numero == 0:
                print("saindo")
                op -=1
            elif numero % 2 == 0:
                print(f"""
                        {numero} é PAR""")
            else:
                print(f"""
                        {numero} é IMPAR""")

    def Questao_40(self):
        num = float(input("informe um numero:"))
        if num % 1 == 0:
            print("Inteiro")
        else:
            print("Decimal")

    def Questao_41(self):
        valor_1 = float(input("informe O Primeiro Numero:"))
        valor_2 = float(input("informe O Segundo Numero:"))
        op = input("""
                para somar informe:       '+'
                para subtrair informe:    '-'
                para multiplicar informe: '*'
                para dividir informe:     '/'
                Qual operação Deseja realizar:""")
        if op == '+':
            soma = valor_1 + valor_2
            print(f"\nO Valor {soma} é:",end="-")
            if soma % 2== 0:
                print("PAR",end="-")
            else:print("IMPAR",end="-")
            if soma >=0:
                print("POSITIVO",end="-")
            else:print("NEGATIVO",end="-")
            if soma % 1==0:
                print("INTEIRO",end="-")
            else:print("DECIMAL",end="-")
        elif op == '-':
            sub = valor_1 - valor_2
            print(f"\nO Valor {sub} é:",end="-")
            if sub % 2== 0:
                print("PAR",end="-")
            else:print("IMPAR",end="-")
            if sub >=0:
                print("POSITIVO",end="-")
            else:print("NEGATIVO",end="-")
            if sub % 1==0:
                print("INTEIRO",end="-")
            else:print("DECIMAL",end="-")
        elif op == '*':
            multi = valor_1 * valor_2
            print(f"\nO Valor {multi} é:",end="-")
            if multi % 2== 0:
                print("PAR",end="-")
            else:print("IMPAR",end="-")
            if multi >=0:
                print("POSITIVO",end="-")
            else:print("NEGATIVO",end="-")
            if multi % 1==0:
                print("INTEIRO",end="-")
            else:print("DECIMAL",end="-")
        elif op == '/':
            div = valor_1 / valor_2
            print(f"\nO Valor {div} é:",end="-")
            if div % 2== 0:
                print("PAR",end="-")
            else:print("IMPAR",end="-")
            if div >=0:
                print("POSITIVO",end="-")
            else:print("NEGATIVO",end="-")
            if div % 1==0:
                print("INTEIRO",end="-")
            else:print("DECIMAL",end="-")
        else:
            print("Valor de operação Invalido")

    def Questao_42(self):
        pergunta_1 = input("Telefonou para a vítima?\nsim ou não:")
        pergunta_2 = input("Esteve no local do crime?\nsim ou não:")
        pergunta_3 = input("Mora perto da vítima?\nsim ou não:")
        pergunta_4 = input("Devia para a vítima?\nsim ou não:")
        pergunta_5 = input("Já trabalhou com a vítima?\nsim ou não:")
        perguntas = [pergunta_1,pergunta_2,pergunta_3,pergunta_4,pergunta_5]
        count = 0
        status = 'Inocente'
        for x in perguntas:
            if x == 'sim':
                count = count + 1
                if count > 1 and count < 3:
                    status = "Suspeito"
                elif count >= 3 and count <= 4:
                    status = "Cumplice"
                elif count == 5:
                    status = "Assassino"
        print(f"O interrogado se mostrou ser {status} em relação as perguntas feitas")

    def Questao_43(self):
        preco =0
        pedido_litros = float(input("Quantidade De Litros:"))
        tipo_combustivel = input("A-álcool\nG-gasolina\ntipo:").upper()
        tipo = ''
        match tipo_combustivel:
            case 'A':
                tipo = "Alcool"
                preco = pedido_litros * 1.9
                if pedido_litros <=20:
                    preco -= 1.9 * pedido_litros *3/100
                else:
                    preco -= 1.9 * pedido_litros *5/100
            case 'G':
                tipo = "Gasolina"
                preco = pedido_litros * 2.5
                if pedido_litros <=20:
                    preco -= 2.5 * pedido_litros *4/100
                else:
                    preco -= 2.5 * pedido_litros *6/100
        print(f"preço a ser pago: R${preco:.2f} de {tipo}")

    def Questao_44(self):
        morango = int(input("informe quantidade de morango:"))
        laranja = int(input("informe quantidade de laranja:"))
        preco_morango_1 = morango * 2.5
        preco_morango_2 = morango * 2.2
        preco_laranja_1 = laranja * 1.8
        preco_laranja_2 = laranja * 1.5
        total = 0
        if morango > 5:
            total += preco_morango_2
        else:
            total += preco_morango_1
        if laranja > 5:
            total += preco_laranja_2
        else:
            total += preco_laranja_1
        if total > 25 or (morango + laranja) > 8:
            total = total - (total * 0.1)
            print(f"Total A pagar:R${total:.2f} desconto de 10%")
        else:
            print(f"Total A pagar:R${total:.2f}")

    def Questao_45(self):
        tipo = int(input("1-File Duplo\n2-Alcatra\n3-Picanha\npedido:"))
        Quantidade = float(input("Quantidade pedida Em KG:"))
        cartao = input("vair usar Cartao?\n\nsim ou nao\nR:").upper()
        total = 0
        desconto = 0
        match tipo:
            case 1:
                carne = "File Duplo"
                if Quantidade > 5 :
                    total = Quantidade * 5.8
                else:
                    total = Quantidade * 4.9
            case 2:
                carne = "Alcatra"
                if Quantidade > 5 :
                    total = Quantidade * 6.8
                else:
                    total = Quantidade * 5.9
            case 3:
                carne = "Picanha"
                if Quantidade > 5 :
                    total = Quantidade * 7.8
                else:
                    total = Quantidade * 6.9
        if cartao == "SIM":
            desconto = (total * 0.05)
            total = total - desconto
        print(f"""
        ------------------Cupom Fistal--------------------
            
        Tipo De Carne_______________________{carne}
        Quantidade de carne_________________{Quantidade}KG
        Cartão______________________________{cartao}
        Desconto____________________________R${desconto:.2f}
        Preço Total_________________________R${total:.2f}

        ------------------Cupom Fistal--------------------
        """)

    def Questao_46(self):
        n = 11
        while (n<0) or (n>10):
            n = int(input("informe um valor de 0 a 10:"))
            if(n>=0 and n <=10):
                print("numero Valido")
            else:
                print("numero Invalido")

    def Questao_47(self):
        usuario = input("digite o nome de usuario:")
        senha = input("digite sua senha:")

        while usuario == senha:
            print("\no Nome De Usuario não pode ser igual a Senha\n")
            usuario = input("digite o nome de usuario:")
            senha = input("digite sua senha:")
        else:
            print(f"\nBem Vindo {usuario} ^_^ \n")

    def Questao_48(self):
        nome = input("digite seu nome:")
        while len(nome) <=3:
            print("o nome Deve Ser maior")
            nome = input("digite seu nome:")
        idade = int(input("digite sua idade:"))
        while idade <0 or idade >150:
            print("a idade deve ser entre 0 a 150")
            idade = int(input("digite sua idade:"))
        salario = int(input("digite seu Salario:"))
        while salario <=0:
            print("seu salario nao pode ser negativo e nem 0")
            salario = int(input("digite seu Salario:"))
        sexo =input("digite seu Genero\n'f'\n'm'\nR:").upper()
        while sexo != 'F' and sexo !='M':
            print("Sexo invalido")
            sexo =input("digite seu Genero\n'f'\n'm'\nR:").upper()
        Estado_civil = input("digite Seu Estado Civil\n'S'-Solteiro\n'C'-Casado\n'V'-Viuvo\n'D'-Divorciado\nR:").upper()
        while Estado_civil != 'S' and Estado_civil != 'C' and Estado_civil != 'V' and Estado_civil != 'D':
            print("Estado Civil Invalido") 
            Estado_civil = input("digite Seu Estado Civil\n'S'-Solteiro\n'C'-Casado\n'V'-Viuvo\n'D'-Divorciado\nR:").upper()
        print(f"""
            Perfil
        Nome:{nome}
        Idade:{idade}
        Sexo:{sexo}
        Estado_civil:{Estado_civil}
        Salario:{salario}
        """)

    def Questao_49(self):
        população_A = 80000
        população_B = 200000
        ano = 0
        while população_A <= população_B:
            população_A += população_A * 0.03
            população_B += população_B * 0.015
            ano += 1
        print(f"depois de {ano} anos a População A Alcança à População B")

    def Questao_50(self):
        op = 1
        while op ==1:
            op = int(input("""
                    0-Sair
                    1-Repetir Operação
                    Escolha:"""))
            if( op == 0):
                print("Saindo........")
                break
            população_A = int(input("informe A Quantidade De pessoas Do Grupo A:"))
            população_B = int(input("informe A Quantidade De pessoas Do Grupo B:"))
            taxa_crescimento_A = float(input("Digite a Taxa De Crescimento Em Porcentagem Do Grupo A:"))
            taxa_crescimento_B = float(input("Digite a Taxa De Crescimento Em Porcentagem Do Grupo B:"))
            ano = 0
            while população_A <= população_B:
                população_A += população_A * taxa_crescimento_A
                população_B += população_B * taxa_crescimento_B
                ano += 1
            print(f"depois de {ano} anos a População A Alcança à População B")
    
    def Questao_51(self):
        for n in range(21):
            print(n,end=' ') 

    def Questao_52(self):
        lista_numero = []
        for x in range(1,6):
            lista_numero.append(int(input(f"informe o {x} Numero_:")))
        maior = max(lista_numero)
        print(maior)
    
    def Questao_53(self):
        notas = []
        for n in range(1,6):
            notas.append(int(input(f"informe {n} nota:")))
        print(f"""
        -Soma:{sum(notas)}
        -Media:{sum(notas)/len(notas)}
        """)

    def Questao_54(self):
        for x in range(1,51):
            if x%2==0:
                continue
            else:
                print(x,end=" ")
        impares = [x for x in range(1,51) if x%2!=0] #lista comprehension
        print(impares)

    def Questao_55_56(self):
        começo = int(input("digite o começo:"))
        fim = int(input("digite o fim:"))
        lista_numeros = []
        for x in range(começo+1,fim):#removendo O var(começo) e a var(fim) para gerar apenas os que estao entre eles
            print(x,end=f" ")
            lista_numeros.append(x)
        print(f"\n-Soma {sum(lista_numeros)}")

    def Questao_57(self):
        valor = int(input("Digite a tabuada que deseja ver N°:"))
        for tabuada in range(1,11):
            print(f"{valor} X {tabuada} = {valor*tabuada}")

    def Questao_58(self):
        Base = int(input("N°1 Base:"))
        Expoente = int(input("N°2 Expoente:"))
        print(Base**Expoente)#com linguagem
        resultado = Base
        for x in range(Expoente-1):#sem linguagem
            resultado = resultado * Base
        print(resultado)

    def Questao_59(self):
        lista_numeros =[]
        par = 0
        impar = 0
        for x in range(1,11):
            lista_numeros.append(int(input(f"digite N°{x}:")))
            if lista_numeros[x-1]%2==0:
                par += 1
            else:
                impar +=1
        print(f"Quantidade De Pares:{par}\nQuantidade de Impares:{impar}")

    def Questao_60(self):
        n = int(input("digite um Numero:"))
        inicio = 1
        fim = 0
        for x in range(n):
            print(inicio,end=' ')
            aux = inicio
            inicio += fim
            fim = aux
    
    def Questao_61(self):
        #questao 61 fatorial de um Numero
        n = int(input("informe N°:"))
        fatorial = n
        for fator in range(n,1,-1):
            fatorial = fatorial*(fator-1)
        print(fatorial)

    def Questao_62_63(self):
        #questao 62 e 63
        soma = 0
        lista_numero =[]
        for numeros in range(1,6):
            n = int(input(f"{numeros}° numero:"))
            while n <=0 or n >1000:
                print("so pode numeros entre 0 e 1000")
                n = int(input(f"{numeros}° numero:"))
            lista_numero.append(n)
            soma += lista_numero[numeros-1]
        maior = max(lista_numero)
        menor = min(lista_numero)
        print(f"Maior:{maior}\nMenor:{menor}\nSoma:{soma}\nLista:{lista_numero}")

    def Questao_64(self):
        #questao 64
        op = 1
        while op ==1:
            op = int(input("0-parar\n1-continuar:"))
            if op == 0:print("Saindo...");break
            n = int(input("informe N°:"))
            if n > 0 and n <=16:
                fatorial = n
                for fator in range(n,1,-1):
                    fatorial = fatorial*(fator-1)
                print(f"Fatorial de {n}! é {fatorial}")
            else:print("permitido Somente Numeros de 0 a 16")
    
    def Questao_65_66_67(self):
        #questao 65,66 e 67
        primos = []
        def primo(n):
            for val in range(2,n):
                if n % val == 0:
                    return False
            return True
        def exibe():
            count = 1
            n = int(input('\nExibir primos até o número: '))
            for val in range(2,n+1):
                count += 1
                if(primo(val)):
                    primos.append(val)
            print(f"Lista Primos:{primos}\nQuantidade De Divisoes:{count}")
        exibe()

    def Questao_68(self):
        #questao 68
        Qtd_notas = int(input("Quantidade de Notas:"))
        soma = 0
        print("Digite a Nota")
        for nota in range(1,Qtd_notas+1):
            soma += int(input(f"\tNota {nota}°_:"))
        media = soma/Qtd_notas
        print(f"Media:{media}")

    def Questao_69(self):
        n_pessoas = int(input("Quantidade de Pessoas:"))
        soma = 0
        print("Informe Sua Idade")
        for pessoa in range(1,n_pessoas+1):
            soma += int(input(f"\tpessoa {pessoa}°_:"))
        media = soma/n_pessoas
        if media <=26:
            print("A Turma é Jovem")
        elif media >26 and media <=60:
            print("A Turma é Adulta")
        else:
            print("A Turma é Idosa")

    def Questao_70(self):
        #questao 70
        Qtd_Eleitores = int(input("Quantidade de Eleitores:"))
        print("Informe Seu Candidato\n\t1-Ana\n\t2-Bruno\n\t3-Carlos")
        votos_Ana ,votos_Bruno ,votos_Carlos = 0,0,0
        for eleitor in range(1,Qtd_Eleitores+1):
            voto = int(input(f"Voto do eleitor {eleitor}:"))
            while voto <1 or voto >3:
                voto = int(input(f"Voto do eleitor {eleitor}:"))
            if voto == 1:
                votos_Ana += 1
            elif voto == 2:
                votos_Bruno += 1
            elif voto == 3:
                votos_Carlos += 1
            else:
                print("Candidato Inexistente")
        if votos_Ana == votos_Bruno:
            if votos_Ana < votos_Carlos and votos_Bruno < votos_Carlos:
                print(f"Ana e Bruno perderam\n\t Carlos é o Grande Vencedor Com {votos_Carlos} Votos")
            else:
                print("Carlos Perdeu\n\tAna e Bruno Devem ir pro segundo Turno")
        elif votos_Bruno == votos_Carlos:
            if votos_Bruno < votos_Ana and votos_Carlos < votos_Ana:
                print(f"Bruno e Carlos Perderam\n\t Ana é a Grande Vencedora Com {votos_Ana} Votos")
            else:
                print("Ana Perdeu\n\tBruno e Carlos Devem ir pro segundo Turno")
        elif votos_Carlos == votos_Ana:
            if votos_Carlos < votos_Bruno and votos_Ana < votos_Bruno:
                print(f"Carlos e Ana Perderam\n\t Bruno é o Grande Vencedor Com {votos_Bruno} Votos")
            else:
                print("Bruno Perdeu\n\tCarlos e Ana Devem ir pro segundo Turno")
        else:
            lista_Candidatos = {"Ana":votos_Ana,"Bruno":votos_Bruno,"Carlos":votos_Carlos}
            Vencedor = max(lista_Candidatos.values())
            if votos_Ana == Vencedor:
                Campeao = "Ana"
                votos_campeao = votos_Ana
            elif votos_Bruno == Vencedor:
                Campeao = "Bruno"
                votos_campeao = votos_Bruno
            elif votos_Carlos == Vencedor:
                Campeao = "Carlos"
                votos_campeao = votos_Carlos
            print(f"""
                Fim Da Votação
                    Candidatos      Votos
                        Ana           {votos_Ana}
                        Bruno         {votos_Bruno}
                        Carlos        {votos_Carlos}
                    Vencedor {Campeao} Com {votos_campeao} Votos
                """)
    
    def Questao_71(self):
        import math
        turmas = int(input("Quantidade de Turmas:"))
        media_turma = []
        for turma in range(1,turmas+1):
            alunos = int(input(f"\tA Turma {turma}° Tem quantos Alunos:"))
            while alunos > 40:
                print("Quantidade maxima é 40 alunos")
                alunos = int(input(f"\tA Turma {turma}° Tem quantos Alunos:"))
            media_turma.append(alunos)
        media_final_de_turmas = math.ceil(sum(media_turma)/turmas)
        print(f"Media de alunos por turma é {media_final_de_turmas}")
    
    def Questao_72(self):
        Quantidade_Discos = int(input("Quantos Discos voce possui:"))
        Lista_disco = []
        for disco in range(1,Quantidade_Discos+1):
            valor_por_disco = int(input(f"O Valor Do Disco {disco}°:"))
            Lista_disco.append(valor_por_disco)
        valor_total_pago = sum(Lista_disco)
        media_gastos_por_disco = valor_total_pago/Quantidade_Discos
        print(f"""
            Quantidade de discos:________{Quantidade_Discos}
            Media gasta por disco:_______R${media_gastos_por_disco}
            Valor Total:_________________R${valor_total_pago}
        """)

    def Questao_73_74(self):
        print("Tabela De Preços Dos Artigos".center(200,"-"))
        for item in range(1,51):
            preco = item * 1.99
            print(f"""(item {item}° - R${preco:.2f})""",end=" ")
            if item == 10 or item == 20 or item == 30 or item == 40 or item == 50:
                print(end="\n")
        print("Tabela De Preços Dos Artigos".center(200,"-"))
        print("Tabela De Preços Da Panificadora".center(200,"-"))
        for item in range(1,51):
            preco = item * 0.18
            print(f"""(item {item}° - R${preco:.2f})""",end=" ")
            if item == 10 or item == 20 or item == 30 or item == 40 or item == 50:
                print(end="\n")
        print("Tabela De Preços Da Panificadora".center(200,"-"))
    
    def Questao_75(self):
        while True:
            try:
                print("Loja Tabajara".center(100,"-"))
                produto = float(input("Valor Do produto:"))
                while produto == "":
                    print("o Valor não poder ser Vazio ou do tipo Texto")
                    produto = float(input("Valor Do produto:"))
                Quantidade_p = int(input("Quantidade:"))
                while Quantidade_p == "":
                    print("o Valor não poder ser Vazio ou do tipo Texto")
                    Quantidade_p = int(input("Quantidade:"))
                total = produto * Quantidade_p
                print(total)
                Din = int(input("Dinheiro:"))
                while Din == "":
                    print("o Valor não poder ser Vazio ou do tipo Texto")
                    Din = int(input("Dinheiro:"))
                while Din < total:
                    print(f"Dinheiro deve ser Maior Ou Igual ao {total}")
                    Din = int(input("Dinheiro:"))
                troca = Din - total
                print("""
                    Valor_Produto:R${}
                    Quantidade:{}
                    Total:R${}
                    Troco:R${}
                    """.format(produto,Quantidade_p,total,troca))
                parar = int(input("\nAlternativas\n0 - parar\n1 - Continuar\nEscolha:"))
                while parar == str or parar >1:
                    print("Option Invalid".center(20,"#"))
                    parar = int(input("\nAlternativas\n0 - parar\n1 - Continuar\nEscolha:"))
                if parar == 0:
                    print("Saindo".center(100,"-"))
                    break
                elif parar == 1:
                    continue
            except ValueError as valor_errado:
                print(f"{valor_errado}")
            except NameError as nome_errado:
                print(f"{nome_errado}")

    def Questao_76(self):
        self.maior = 0
        self.menor = 999
        count = 0
        temperatura_maxima = 0
        while True:
            print("Digite uma Numero Negativo para parar")
            temp = float(input("""Digite Uma Temperatura:"""))
            if temp <0:
                print("Parando...")
                break
            count += 1
            temperatura_maxima += temp
            if temp > self.maior:
                self.maior = temp
            if temp < self.menor:
                self.menor = temp
        print(f"""
            Temperatura_Maior= {self.maior}°C
            Temperatura_Menor= {self.menor}°C
            Temperatura_Media= {temperatura_maxima/count}°C
        """)

    def Questao_77(self):
        tabuada = int(input("Qual Tabuada Deseja Ver:"))
        start = int(input("A tabuada Vai Começar ex:(0...5):"))
        end = int(input("A tabuada Vai Terminar ex:(5...10):"))
        while end < start:
            print("\nO Valor do fim da tabuada não pode ser menor que o Inicio\n")
            end = int(input("A tabuada Vai Terminar ex:(5...10):"))
        for cal in range(start,end+1):
            print(f"{tabuada} x {cal} = {cal*tabuada}")
        
    def Questao_78(self):
        self.codigo_maior_altura = 0
        self.codigo_menor_altura = 0
        self.codigo_maior_peso = 0
        self.codigo_menor_peso = 0

        self.maior_altura = 0
        self.maior_peso= 0
        self.menor_altura = 200#centimetros
        self.menor_peso = 500#kg

        self.Soma_altura = 0
        self.Soma_peso = 0

        self.Qtd = 0

        while True:
            codigo = input("\n\ninforme Seu Codigo:")
            if codigo == '0':
                print("Saindo...")
                break
            altura = int(input("Informe A Sua Altura:"))
            peso = float(input("Informe Seu Peso:"))
            Qtd += 1
            if altura > self.maior_altura:
                self.maior_altura = altura
                self.codigo_maior_altura = codigo
            if altura < self.menor_altura:
                self.menor_altura = altura
                self.codigo_menor_altura = codigo

            if peso > self.maior_peso:
                self.maior_peso= peso
                self.codigo_maior_peso = codigo
            if peso < self.menor_peso:
                self.menor_peso= peso
                self.codigo_menor_peso = codigo
            Soma_altura += altura
            Soma_peso += peso
        Media_altura = Soma_altura/Qtd
        Media_peso = Soma_peso/Qtd
        print(f"""
        O Cliente_{self.codigo_menor_altura}_->>Menor_Altura->>_{self.menor_altura}Cm
        O Cliente_{self.codigo_maior_altura}_->>Maior_Altura->>_{self.maior_altura}Cm
        O Cliente_{self.codigo_menor_peso}_->>Menor_peso->>_{self.menor_peso}Kg
        O Cliente_{self.codigo_maior_peso}_->>Maior_Peso->>_{self.maior_peso}Kg
        Altura_Media->>{Media_altura:.1f}Cm   
        Peso_Medio->>{Media_peso:.1f}Kg """)

    def Questao_79(self):
        Salario = float(input("Informe Quanto voce Ganha:"))
        percentual = 1.5 / 100
        ano = int(input("Quantos anos Se passaram:"))
        for _ in range(1,ano+1):
            percentual = percentual * 2
        Salario +=percentual * Salario
        print(f"Salario Atual:R${Salario}")

    def Questao_80(self):
        self.menor_altura = 300
        self.maior_altura = 0
        self.n_Menor_altura =0
        self.n_Maior_altura =0

        while True:
            numero = int(input("\n\nNumero Da Chamada:"))
            if numero == 0:
                print("Encerrando...")
                break
            altura = int(input("Informe Sua Altura:"))
            if altura > self.maior_altura:
                self.maior_altura = altura
                self.n_Maior_altura = numero

            if altura < self.menor_altura:
                self.menor_altura = altura
                self.n_Menor_altura = numero
            
        print(f"""
            Numero_Do_Aluno:_<_{self.n_Maior_altura}°_>_Sua_Altura_<_{self.maior_altura}Cm_>Que é A Maior
            Numero_Do_Aluno:_<_{self.n_Menor_altura}°_>_Sua_Altura_<_{self.menor_altura}Cm_>Que é A Menor 
            """)
    
    def Questao_81(self):
        """
        Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
            Foram obtidos os seguintes dados: 
        Código da cidade; 
        Número de veículos de passeio (em 1999); 
        Número de acidentes de trânsito com vítimas (em 1999).
            Deseja-se saber: 
        Qual o maior e menor índice de acidentes de transito e a que cidade pertence; 
        Qual a média de veículos nas cinco cidades juntas; 
        Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
        """
        self.qtd_cidades = 5
        self.qtd_cidades_menos_2k =0
        self.codigo_maior_indice = ""
        self.codigo_menor_indice = ""

        self.maior_indice_acidentes = 0
        self.menor_indice_acidentes = 10**10

        self.media_acidentes =[]
        self.media_acidentes_menos_2k =[]
        self.acidentes_menos_2k = []
        self.codigo_media_acidentes_menos_2k =[]
        self.media_veiculos =0
        for _ in range(self.qtd_cidades):
            codigo = input("Digite o Codigo Da Cidade:")
            veiculos = int(input("Digite a Quantidade de Veiculos:"))
            acidentes = int(input("Digite a Numero de Acidentes:"))

            if acidentes > self.maior_indice_acidentes:
                self.maior_indice_acidentes = acidentes
                self.codigo_maior_indice = codigo
            if acidentes < self.menor_indice_acidentes:
                self.menor_indice_acidentes = acidentes
                self.codigo_menor_indice = codigo
            
            if veiculos < 2000:
                self.acidentes_menos_2k.append(acidentes)
                self.codigo_media_acidentes_menos_2k.append(codigo)
                self.qtd_cidades_menos_2k += 1
            self.media_veiculos +=veiculos 

        print(f"""
            Codigo_Maior_indice {self.codigo_maior_indice}
            Maior_indice_______ {self.maior_indice_acidentes}
            
            Codigo_Maior_indice {self.codigo_menor_indice}
            Menor_indice_______ {self.menor_indice_acidentes}

            Media_Veiculos = {self.media_veiculos/self.qtd_cidades}
            
            Codigos_menos_2k___________ {self.codigo_media_acidentes_menos_2k}
            Media_acidentes_menor_2k___ {sum(self.acidentes_menos_2k)/self.qtd_cidades_menos_2k}
        """)

    def Questao_82(self):
        """
        Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
        seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
        valor da parcela.

        Os juros e a quantidade de parcelas seguem a tabela abaixo:
            Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
            1       0
            3       10
            6       15
            9       20
            12      25

        Exemplo de saída do programa:
            Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
            R$ 1.000,00     0               1                       R$  1.000,00
            R$ 1.100,00     100             3                       R$    366,00
            R$ 1.150,00     150             6                       R$    191,67
        """

        self.valor_da_divida = float(input("Digite o valor da dívida: "))
        self.parcelas = [1,3,6,9,12]
        self.juros = iter([0,10,15,20,25])
        print(
            "|Valor da Dívida|Valor dos Juros|Quantidade de Parcelas |Valor da Parcela|"
        )
        for parcela in self.parcelas:
            juro = next(self.juros)

            valor_do_juros = self.valor_da_divida * (juro / 100)
            valor_total = self.valor_da_divida + valor_do_juros
            valor_da_parcela = valor_total / parcela
            print(
                f"|R$ {valor_total:.2f}\t"
                f"|R$ {valor_do_juros:.2f}\t"
                f"|{parcela}\t\t\t"
                f"|R$ {valor_da_parcela:.2f}"
            )
        
    def Questao_83(self):
        
        while True:
            self.numero = int(input("Informe Um Numero Inteiro até 100:"))
            
            if self.numero <0:
                print("Finalizando....")
                break
            if self.numero <=25:
                self.alcance1 +=1
            elif self.numero <=50:
                self.alcance2 +=1
            elif self.numero <=75:
                self.alcance3 +=1
            elif self.numero <=100:
                self.alcance4 +=1
        print(f"""
            0-25 apareceu {self.alcance1} Vezes
            25-50 apareceu {self.alcance2} Vezes
            25-75 apareceu {self.alcance3} Vezes
            75-100 apareceu {self.alcance4} Vezes
            """)
    
    def Questao_84(self):
        """
        O cardápio de uma lanchonete é o seguinte:
        Faça um programa que leia o código dos itens pedidos e as quantidades
        desejadas.

        Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
        geral do pedido.

        Considere que o cliente deve informar quando o pedido deve ser encerrado.
        """
        while True:
            print("""
            Especificação   Código  Preço
            Cachorro Quente 100     R$ 1,20
            Bauru Simples   101     R$ 1,30
            Bauru com ovo   102     R$ 1,50
            Hambúrguer      103     R$ 1,20
            Cheeseburguer   104     R$ 1,30
            Refrigerante    105     R$ 1,00""")
            self.conta = int(input("\n1-para fazer o pedido\n0-para fechar a conta\nentao:"))
            if self.conta == 0:
                print("Cupom fiscal".upper().center(100,"-"))
                for chave, valor in self.pedidos.items():
                    if chave == "Cachorro Quente":
                        self.preco = 1.20
                        self.valor_por_item = self.preco*valor
                    elif chave == "Bauru Simples":
                        self.preco = 1.30
                        self.valor_por_item = self.preco*valor
                    elif chave == "Bauru com ovo":
                        self.preco = 1.50
                        self.valor_por_item = self.preco*valor
                    elif chave == "Hambúrguer":
                        self.preco = 1.20
                        self.valor_por_item = self.preco*valor
                    elif chave == "Cheeseburguer":
                        self.preco = 1.30
                        self.valor_por_item = self.preco*valor
                    elif chave == "Refrigerante":
                        self.preco = 1.00
                        self.valor_por_item = self.preco*valor

                    self.total += self.valor_por_item
                    print(f"item {valor}x {chave} preco R$ {self.valor_por_item:.2f}".center(100,'-'))
                print(f"Total = R$ {self.total:.2f}".center(100,'-'))
                break
            self.codigo = int(input("informe o Codigo do Lanche:"))
            while self.codigo <100 or self.codigo >105:
                print("codigo invalido")
                self.codigo = int(input("informe o Codigo do Lanche:"))
            self.Quantidade = int(input("Quantidade:"))
            match self.codigo:
                case 100:
                    self.cachorro = "Cachorro Quente"
                    self.pedidos.update({self.cachorro:self.Quantidade})
                case 101:
                    self.cachorro = "Bauru Simples"
                    self.pedidos.update({self.cachorro:self.Quantidade})
                case 102:
                    self.cachorro = "Bauru com ovo"
                    self.pedidos.update({self.cachorro:self.Quantidade})
                case 103:
                    self.cachorro = "Hambúrguer"
                    self.pedidos.update({self.cachorro:self.Quantidade})
                case 104:
                    self.cachorro = "Cheeseburguer"
                    self.pedidos.update({self.cachorro:self.Quantidade})
                case 105:
                    self.cachorro = "Refrigerante"
                    self.pedidos.update({self.cachorro:self.Quantidade})

    def Questao_85(self):
        """
        Em uma eleição presidencial existem quatro candidatos.
        Os votos são informados por meio de código.
        Os códigos utilizados são:
            1, 2, 3, 4  - Votos para os respectivos candidatos
            (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
            5 - Voto Nulo
            6 - Voto em Branco

        Faça um programa que calcule e mostre:
            O total de votos para cada candidato;
            O total de votos nulos;
            O total de votos em branco;
            A percentagem de votos nulos sobre o total de votos;
            A percentagem de votos em branco sobre o total de votos.

        Para finalizar o conjunto de votos tem-se o valor zero.
        """
        while True:
            if self.votos_ana>0 and self.votos_bruno >0 and self.votos_carlos>0 and self.votos_daniel>0 and self.votos_nulo>0 and self.votos_branco>0:
                self.confirmação = int(input("0-Sair\n1-Votar\nAlternativa:"))
                if self.confirmação == 0:
                    print("\nEncerrando Votação\n".upper())
                    break
            self.voto = int(input("Candidatos:\n1-ana\n2-bruno\n3-carlos\n4-daniel\n5-nulo\n6-branco\nEscolha Seu Candidato:"))
            while self.voto >6 or self.voto <1:
                self.voto = int(input("Candidatos:\n1-ana\n2-bruno\n3-carlos\n4-daniel\n5-nulo\n6-branco\nEscolha Seu Candidato:"))
            self.total += 1
            match self.voto:
                case 1:
                    self.votos_ana +=1
                    self.votos.update({"ana":self.votos_ana})
                case 2:
                    self.votos_bruno +=1
                    self.votos.update({"Bruno":self.votos_bruno})
                case 3:
                    self.votos_carlos +=1
                    self.votos.update({"carlos":self.votos_carlos})
                case 4:
                    self.votos_daniel +=1
                    self.votos.update({"daniel":self.votos_daniel})
                case 5:
                    self.votos_nulo +=1
                    self.votos.update({"Nulo":self.votos_nulo})
                case 6:
                    self.votos_branco +=1
                    self.votos.update({"branco":self.votos_branco})
        for item in self.votos.keys():
            if self.votos.get(item) is not None:
                self.x = True
        if self.x == True:
            for chave,valor in self.votos.items():
                if chave == 'Nulo':
                    self.total_nulo = valor
                if chave == 'branco':
                    self.total_branco = valor
                print(f"{chave}\t possui \t{valor} votos")
            print(f"\nTotal De votos:{self.total}\nPorcentagem de votos nulos:{(100*self.total_nulo)/self.total:.2f}\nPorcentagem de votos brancos:{(100*self.total_branco)/self.total:.2f}")
            print("votação encerrada".upper())
        else:
            print("votação encerrada".upper())

    def Questao_86(self):
        """
        Desenvolver um programa para verificar a nota do aluno em uma prova com 10
        questões, o programa deve perguntar ao aluno a resposta de cada questão e ao
        final comparar com o gabarito da prova e assim calcular o total de acertos e a
        nota (atribuir 1 ponto por resposta certa).

        Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno
        vai utilizar o sistema.

        Após todos os alunos terem respondido informar:
            Maior e Menor Acerto;
            Total de Alunos que utilizaram o sistema;
            A Média das Notas da Turma.
        """
        self.totalAlunos = 0
        self.acertos = 0
        self.total_acertos = 0
        self.AlunoExemplar = ""
        self.AlunoMediano = ""
        self.Maior_Acerto = 0
        self.Menor_Acerto = 10
        self.alunos = {}
        self.aluno = {}
        self.gabarito = {
            "respostas":{
                1:'C',
                2:'C',
                3:'C',
                4:'E',
                5:'D',
                6:'E',
                7:'D',
                8:'A',
                9:'A',
                10:'C'
            }}
        self.prova = {
            "perguntas":{
                1:"""
                1 Questao
                    Em um projeto para a construção de um cinema, os arquitetos estão avaliando a relação entre a quantidade de fileiras e a quantidade de cadeiras em cada fileira. 
                    O projeto inicial prevê uma sala para 304 pessoas. 
                    No caso de utilizarem 19 fileiras, o número de cadeiras por fileira será:
                    a) 14.
                    b) 15.
                    c) 16.
                    d) 13.
                """,
                2:"""
                2 Questao
                Em uma escola de Ensino Fundamental um concurso estabelece regras para conceder uma bolsa de estudos para o Ensino Médio.
                Em cada bimestre os alunos do 9.º ano realizam uma avaliação e, após os quatro bimestres, as notas são somadas. 
                Os quatro alunos finalistas são os que alcançam as maiores pontuações. 
                Ganhará a bolsa aquele que possuir a média mais alta das quatro notas das avaliações.

                As notas dos quatro alunos finalistas são:

                1º bimestre	
                2º bimestre
                3º bimestre
                4º bimestre

                Aluno A	75	86	83	91
                Aluno B 78	98	67	99
                Aluno C 83	84	89	87
                Aluno D 98	65	87	77

                O aluno que ganhou a bolsa de estudos foi
                a) o aluno A.
                b) o aluno B.
                c) o aluno C.
                d) o aluno D.
                """,
                3:"""
                3 Questao
                (IF SUL — MG 2018) Celinho é o técnico do time de basquete de sua cidade.
                No seu time, os cinco titulares possuem altura média de 1,88 m. 
                No campeonato que o time de Celinho vai disputar, os jogadores dos outros times têm, em média, 1,91 m. 
                Para aumentar a altura média do seu time, Celinho tirou o jogador mais baixo do time, de altura de 1,79 m. 
                Se quiser igualar à média de altura dos outros times, o jogador que entrará no time deverá ter altura igual a:

                a) 1,88 m
                b) 1,91 m
                c) 1,94 m 
                d) 2,03 m
                """,
                4:"""
                4 Questao
                (UFRGS — 2019) A média aritmética das idades de um grupo de 10 amigos é 22 anos. 
                Ao ingressar mais um amigo nesse grupo, a média aritmética passa a ser de 23 anos. 
                A idade do amigo ingressante no grupo, em anos, é:

                a) 29.
                b) 30.
                c) 31.
                d) 32.
                e) 33.
                """,
                5:"""
                5 Questao
                (CESGRANRIO — 2012) O valor da conta de telefone de Sebastião variou muito nos três primeiros meses de 2012. 
                Em janeiro, Sebastião pagou R$ 48,50; 
                em fevereiro, R$ 78,00 
                e em março, R$ 65,20. 
                Qual foi, em reais, o valor mensal médio da conta telefônica de Sebastião no primeiro trimestre de 2012?

                a) 60,60
                b) 61,90
                c) 62,20
                d) 63,90 
                e) 64,20
                """,
                6:"""
                6 Questao
                Um produtor de café irrigado em Minas Gerais recebeu um relatório de consultoria estatística, constando, entre 
                outras informações, o desvio padrão das produções de uma safra dos talhões de sua propriedade. 
                Os talhões têm a mesma área de 30 000 m2 e o valor obtido para o desvio padrão foi de 90 kg/talhão. 
                O produtor deve apresentar as informações sobre a produção e a variância dessas produções em sacas de 60 kg por hectare (10 000 m2).
                A variância das produções dos talhões expressa em (sacas/hectare)2 é:

                a) 20,25
                b) 4,50
                c) 0,71
                d) 0,50
                e) 0,25.
                """,
                7:"""
                7 Questao
                Um professor de matemática aplica três provas em seu curso (P1 , P2 , P3 ), cada uma valendo de 0 a 10 pontos. 
                A nota final do aluno é a média aritmética ponderada das três provas, sendo que o peso da prova Pn é igual a n2 . 
                Para ser aprovado na matéria, o aluno tem que ter nota final maior ou igual a 5,4. 
                De acordo com esse critério, um aluno será aprovado nessa disciplina, independentemente das notas 
                tiradas nas duas primeiras provas, se tirar na P3 , no mínimo, nota:

                a) 7,6.
                b) 7,9.
                c) 8,2.
                d) 8,4.
                e) 8,6.
                """,
                8:"""
                8 Questao
                Um veículo viaja entre dois povoados da Serra da Mantiqueira, percorrendo a primeira terça parte do trajeto à velocidade média de 60 km/h, 
                a terça parte seguinte a 40 km/h e o restante do percurso a 20 km/h. 
                O valor que melhor aproxima a velocidade média do veículo nessa viagem, em km/h, é

                a) 32,5 
                b) 35
                c) 37,5
                d) 40
                e) 42,5
                """,
                9:"""
                9 Questao
                (Enem/2013) Numa escola com 1.200 alunos foi realizada uma pesquisa sobre o conhecimento desses em duas línguas estrangeiras: inglês e espanhol.
                Nessa pesquisa constatou-se que 600 alunos falam inglês, 500 falam espanhol e 300 não falam qualquer um desses idiomas.
                Escolhendo-se um aluno dessa escola ao acaso e sabendo-se que ele não fala inglês, qual a probabilidade de que esse aluno fale espanhol?

                a) 1/2 
                b) 5/8
                c) 1/4
                d) 5/6
                e) 5/14
                """,
                10:"""
                10 Questao
                Se lançarmos um dado, qual a probabilidade de obtermos um número maior que 4?

                a) 2/3
                b) 1/4
                c) 1/3 
                d) 3/2
                """,
            }}
        while True:
            if self.totalAlunos >0:
                self.confirmação = int(input("outro Aluno Irá Usar O Programa ?\n1-sim\n0-não\nEscolha:"))
                if self.confirmação == 0:
                    break
            self.NomeAluno = input("\nNome Completo Do Aluno:").upper()
            self.totalAlunos += 1

            for N_Questao,Questao in self.prova["perguntas"].items():
                print(Questao)#mostrando as perguntas
                self.resposta = input("Resposta:").upper()
                os.system("cls")

                if self.gabarito["respostas"][N_Questao] == self.resposta:
                    self.acertos += 1

            self.total_acertos += self.acertos
            self.Media_nota = self.total_acertos/self.totalAlunos

            if self.acertos > self.Maior_Acerto:
                self.Maior_Acerto = self.acertos
                self.AlunoExemplar = self.NomeAluno
            if self.acertos < self.Menor_Acerto:
                self.Menor_Acerto = self.acertos
                self.AlunoMediano = self.NomeAluno

                self.aluno.update({N_Questao:self.resposta})
            self.aluno.update({"acertos":self.acertos})
            self.alunos = {self.NomeAluno:self.aluno}
        print(f"""
            O Aluno {self.AlunoExemplar} obteve o Maior Resultado {self.Maior_Acerto} Pts
            O Aluno {self.AlunoMediano} obteve o Menor Resultado {self.Menor_Acerto} Pts

            Total De alunos Que Fizeram A prova {self.totalAlunos}
            Media das notas da Turma foi de {self.Media_nota} Pts
            """)
    
    def Questao_87(self):
        """
        Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
        No final da série de saltos de cada atleta, o melhor e o pior resultados são
        eliminados.

        O seu resultado fica sendo a média dos três valores restantes.
        Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
        pelo atleta em seus saltos e depois informe a média dos saltos conforme a
        descrição acima informada (retirar o melhor e o pior salto e depois
        calcular a média).

        Faça uso de uma lista para armazenar os saltos.
        Os saltos são informados na ordem da execução, portanto não são ordenados.
        O programa deve ser encerrado quando não for informado o nome do atleta.
        A saída do programa deve ser conforme o exemplo abaixo:
        Atleta: Rodrigo Curvêllo

        Primeiro Salto: 6.5 m
        Segundo Salto: 6.1 m
        Terceiro Salto: 6.2 m
        Quarto Salto: 5.4 m
        Quinto Salto: 5.3 m

        Melhor salto:  6.5 m
        Pior salto: 5.3 m
        Média dos demais saltos: 5.9 m

        Resultado final:
        Rodrigo Curvêllo: 5.9 m
        """
        self.Saltos = {}
        self.Maior_Salto = 0
        self.Menor_Salto = 100
        self.NomeAtleta = {}

        while True:
            os.system("cls")
            self.Nome = input("Informe o Nome Do Atleta:")
            if self.Nome == "":
                break
            for _ in range(1,6):
                self.salto = float(input(f"Quantos Metros Foi o Salto {_}°:".upper()))

                self.Saltos.update({_:self.salto})

                if self.salto > self.Maior_Salto:
                    self.Maior_Salto = self.salto
                if self.salto < self.Menor_Salto:
                    self.Menor_Salto = self.salto
                self.total += self.salto
            self.Media_Saltos = (self.total-(self.Maior_Salto+self.Menor_Salto))/3

            self.NomeAtleta = {self.Nome:self.Saltos}

        for chave,valor in self.NomeAtleta.items():
            print(f"Nome Atleta:{chave}")
            for N,saltos in valor.items():
                print(f"\t{N}° Salto {saltos} M")
            print(f"Maior Salto: {self.Maior_Salto:.1f} M\nMenor Salto: {self.Menor_Salto:.1f} M\nMedia dos Saltos: {self.Media_Saltos:.1f} M")
    
    def Questao_88(self):
        """
        Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
        A melhor e a pior nota são eliminadas.
        A sua nota fica sendo a média dos votos restantes.

        Você deve fazer um programa que receba o nome do ginasta e as notas dos sete
        jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
        média, conforme a descrição acima informada (retirar o melhor e o pior salto e
        depois calcular a média com as notas restantes).

        As notas não são informados ordenadas.
        Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
            Atleta: Aparecido Parente
            Nota: 9.9
            Nota: 7.5
            Nota: 9.5
            Nota: 8.5
            Nota: 9.0
            Nota: 8.5
            Nota: 9.7

            Resultado final:
            Atleta: Aparecido Parente
            Melhor nota: 9.9
            Pior nota: 7.5
            Média: 9,04
        """
        self.notas = {}
        self.Maior_nota = 0
        self.Menor_nota = 11
        self.Media_nota = 0
        while True:
            os.system("cls")
            self.Nome = input("Digite O Nome Do Atleta:").upper()
            os.system("cls")
            if self.Nome == "":
                break
            self.Qtd_Jurados = int(input("Quantidade de Jurados:"))
            
            for jurado in range(1,self.Qtd_Jurados+1):
                self.nota = float(input(f"Jurado {jurado}° Deu A nota:"))


                if self.nota > self.Maior_nota:
                    self.Maior_nota = self.nota
                if self.nota < self.Menor_nota:
                    self.Menor_nota = self.nota

                self.notas.update({jurado:self.nota})
                self.total += self.nota
            self.Lista_Atletas = {self.Nome:self.notas}
            self.excluidos = self.Maior_nota + self.Menor_nota
            self.Media_nota = (self.total-self.excluidos)/(self.Qtd_Jurados-2)

            self.notas["Maior Nota"] = self.Maior_nota
            self.notas["Menor Nota"] = self.Menor_nota
            self.notas["Media Total"] = self.Media_nota

        print("Resultado Final:")
        for chave,valor in self.Lista_Atletas.items():
            print(f"Atleta : {chave}")
            for N,notas in valor.items():
                if N == "Maior Nota":
                    print(f"{N} : {notas} Pts")
                elif N == "Menor Nota":
                    print(f"{N} : {notas} Pts")
                elif N == "Media Total":
                    print(f"{N} : {notas} Pts")
                else:
                    print(f"O Jurado {N}° Deu A nota: {notas:.1f} Pts")

    def Questao_89(self):
        """
        Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido. 
        Exemplo: 12376489 => 98467321
        """
        os.system("cls")
        self.Lista_Numero = []
        self.Lista_Reversa = []
        self.NumeroInteiro = int()
        self.confirmação = int(input("1-Mostrar Texto Invertido\n2-Mostrar Numero Invertido\nEscolha:"))
        self.numero = input("Digite Algo Para Converter-lo:")
        self.string = ""
        match self.confirmação:
            case 1: 
                self.string = str(self.numero)
                for tamanho in self.string:
                    self.Lista_Numero.append(tamanho)
                for negativo in range(1,len(self.Lista_Numero)+1):
                    self.Lista_Reversa.append(self.Lista_Numero[-negativo])
                self.string = ""
                for Texto in self.Lista_Reversa:
                    self.string += Texto
                print(f"\nTexto informado:{self.numero}\nTexto Invertido:{self.string}\n")
            case 2:
                self.NumeroString = str(self.numero)
                for tamanho in self.NumeroString:
                    self.Lista_Numero.append(tamanho)
                for negativo in range(1,len(self.Lista_Numero)+1):
                    self.Lista_Reversa.append(self.Lista_Numero[-negativo])
                self.NumeroString = ""
                for Texto in self.Lista_Reversa:
                    self.NumeroString += Texto
                self.NumeroInteiro = int(self.NumeroString)
                print(f"\nNumero Inteiro:{self.numero}\nNumero Inteiro Invertido:{self.NumeroInteiro}\n")

    def Questao_90(self):
        """
        Faça um programa que mostre os n termos da Série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
        Imprima no final a soma da série.
        """
        import math
        self.Lista_NumeroN = []
        self.Lista_NumeroM = []
        self.soma =0
        self.num =1
        os.system("cls")
        self.numeroN = int(input("informe o Valor De N:"))
        
        for num in range(1,self.numeroN+1):
            self.Lista_NumeroN.append(num)
        for nume in range(1,self.numeroN*5,2):
            self.Lista_NumeroM.append(nume)
            if len(self.Lista_NumeroM) == len(self.Lista_NumeroN):
                break
        for final in range(self.numeroN):
            self.soma += self.Lista_NumeroN[final]/self.Lista_NumeroM[final]
            print(f"{self.soma:.2f} += {self.Lista_NumeroN[final]} / {self.Lista_NumeroM[final]}")
        print(f"Soma:{self.soma:.2f}")

    def Questao_91(self):
        """
        Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
        Faça um programa que calcule o valor de H com N termos.
        """
        os.system("cls")
        self.h = 0
        self.n = int(input("informe o Valor De N:"))
        for x in range(1,self.n+1):
            self.h += 1/x
            print(f"{self.h:.2f} += 1/{x}")
        print(f"Valor De H:{self.h:.2f}")

    def Questao_92_e_93(self):
        """
        Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
        """
        os.system("cls")
        self.Lista_Numero = []
        for _ in range(1,11):
            self.Lista_Numero.append(int(input(f"{_}° Numero :")))
        print("\nLista Normal:")
        for n in self.Lista_Numero:
            print(n,end=' ')
        print("\nLista inversa:")
        for _ in range(1,len(self.Lista_Numero)+1):
            print(self.Lista_Numero[-_],end=" ")

    def Questao_94(self):
        """
        Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
        """
        os.system("cls")
        self.nota = int(input("Informe Quantas Notas:"))
        self.notas = []
        print("\n")
        for nota in range(1,self.nota+1):
            aux = float(input(f"{nota}° Nota:"))
            self.notas.append(aux)
            self.total += aux
        self.Media_nota = self.total/self.nota
        os.system("cls")
        for ex in range(1,len(self.notas)+1):
            print(f"{ex}° Nota:{self.notas[ex-1]}")
        print(f"Media:{self.Media_nota}")

    def Questao_95(self):
        """
        Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
        Imprima as consoantes.
        """
        os.system("cls")
        self.Consoantes = ['B','C','D','F','G','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
        self.ConsoantesCount = []
        self.char = ""
        for letra in range(1,11):
            self.char = input(f"Letra {letra}° :").upper()
            while len(self.char) >1:
                print("Isso não é Uma Letra:")
                self.char = input("informe Uma Letra:")
            aux = self.char in self.Consoantes
            if aux == True:
                self.ConsoantesCount.append(self.char)
        os.system("cls")
        print(f"\nConsoantes Lidas {len(self.ConsoantesCount)}\nLista Das Consoantes {self.ConsoantesCount}")

    def Questao_96(self):
        """
        Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
        Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
        Imprima os três vetores.
        """
        os.system("cls")
        self.Lista_Numero = []
        self.Lista_Par = []
        self.Lista_impar = []
        for n in range(1,21):
            self.numero = int(input(f"Numeros 20/{n}:"))
            os.system("cls")
            self.Lista_Numero.append(self.numero)
        for x in self.Lista_Numero:
            if x%2==0:
                self.Lista_Par.append(x)
            else:self.Lista_impar.append(x)
        print(f"\nLista Par:{self.Lista_Par}\nLista Impar:{self.Lista_impar}\n")
    
    def Questao_97(self):
        """
        Faça um Programa que peça as quatro notas de 10 alunos, 
        calcule e armazene num vetor a média de cada aluno, 
        imprima o número de alunos com média maior ou igual a 7.0.
        """
        os.system("cls")
        self.Alunos = int(input("Informe Quantos Alunos:"))
        self.nota = int(input("informe Quantas Notas:"))
        self.Media_nota = []
        self.Quantidade = 0
        os.system("cls")
        for aluno in range(1,self.Alunos+1):
            print(f"Aluno {aluno}\n")
            for notas in range(1,self.nota+1):
                self.notas = int(input(f"\tNota {self.nota}/{notas}:"))
                
                self.total += self.notas
            self.Media = self.total/self.nota
            if self.Media >= 7:
                self.Quantidade += 1#Quantidade dos alunos       
            self.Media_nota.append(self.Media)
            os.system("cls")
        print(f"Numero De Aluno Acima Da Media: {self.Quantidade}/{self.Alunos}")

    def Questao_98(self):
        """
        Faça um Programa que leia um vetor de 5 números inteiros, 
        mostre a soma, 
        a multiplicação e 
        os números.
        """
        os.system("cls")
        self.soma = 0
        self.multi = 1
        self.Lista_Numero = []
        for num in range(1,6):
            self.n = int(input(f"Vetor 5/{num}:"))
            self.soma += self.n
            self.multi *= self.n
            self.Lista_Numero.append(self.n)
        os.system("cls")
        print(f"Soma: {self.soma}\nMultiplicação: {self.multi}\nLista: {self.Lista_Numero}")
        
    def Questao_99(self):
        """
        Faça um Programa que peça a idade e a altura de 5 pessoas, 
        armazene cada informação no seu respectivo vetor. 
        Imprima a idade e a altura na ordem inversa a ordem lida.
        """
        os.system("cls")
        self.idade = []
        self.altura = []
        for valores in range(1,6):
            print(f"Pessoa 5/{valores}°\n\t")
            idade = int(input("Informe Sua Idade:"))
            self.idade.append(idade)
            altura = int(input("Informe Sua Altura Em Cm:"))
            self.altura.append(altura)
            os.system("cls")
        for Pessoa in range(1,6):
            print(f"\n\tIdade:{self.idade[-Pessoa]} Altura:{self.altura[-Pessoa]} Cm")
    
    def Questao_100(self):
        """
        Faça um Programa que leia um vetor A com 10 números inteiros, 
        calcule e mostre a soma dos quadrados dos elementos do vetor.
        """
        os.system("cls")
        self.Lista_Numero = []
        self.soma = 0
        for vetor in range(1,11):
            self.n = int(input(f" Numeros 10/{vetor}:"))**2
            
            self.Lista_Numero.append(self.n)
            os.system("cls")
        self.soma = sum(self.Lista_Numero)
        print(f"A Soma Dos Quadrados:{self.soma}")

    def Questao_101_102(self):
        """
        Questao 101
        Faça um Programa que leia dois vetores com 10 elementos cada. 
        Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
        
        Questao 102
        Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
        """
        os.system("cls")
        self.veto_A = []
        self.veto_B = []
        self.veto_C = []
        self.veto_D = []
        while True:
            while len(self.veto_A) <10:
                self.j = len(self.veto_A)+1
                self.veto_A.append(input(f"Espaço Do Vetor_A {self.j}/10:"))
                os.system("cls")
            while len(self.veto_B) <10:
                self.k =len(self.veto_B)+1
                self.veto_B.append(input(f"Espaço Do Vetor_B {self.k}/10:"))
                os.system("cls")
            while len(self.veto_C) <10:
                self.l =len(self.veto_C)+1
                self.veto_C.append(input(f"Espaço Do Vetor_C {self.l}/10:"))
                os.system("cls")
            break
        for vet in self.veto_A:
            self.veto_D.append(vet)
        for vet in self.veto_B:
            self.veto_D.append(vet)
        for vet in self.veto_C:
            self.veto_D.append(vet)
        print(f"\nVetor A : {self.veto_A} Tamanho :{len(self.veto_A)}\nVetor B : {self.veto_B} Tamanho :{len(self.veto_B)}\nVetor C : {self.veto_C} Tamanho :{len(self.veto_C)}\nVetor D : {self.veto_D} Tamanho :{len(self.veto_D)}")
    
    def Questao_103(self):
        """
        Foram anotadas as idades e alturas de 30 alunos. 
        Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
        """
        os.system("cls")
        self.idade = []
        self.altura = []
        self.AlunoIdade = []
        self.Alunoaltura = []
        self.totalAlunos = 20
        self.soma = 0
        for aluno in range(1,self.totalAlunos+1):
            print(f"\tAluno {aluno}/{self.totalAlunos}\n")
            idade = int(input("\tinforme Sua Idade:"))
            altura = int(input("\tinforme Sua Altura Em cm:"))
            
            if idade >13:
                self.idade.append(idade)
                self.altura.append(altura)
            
            self.soma += altura
            os.system("cls")
        self.Media = self.soma/self.totalAlunos
        for ideal in range(1,len(self.idade)):
            alturaideal = self.altura[ideal]
            if alturaideal < self.Media:
                self.AlunoIdade.append(self.idade[ideal])
                self.Alunoaltura.append(self.altura[ideal])
        print(f"Quantidade De Alunos Que Possuem A Altura Abaixo Da Media : {len(self.Alunoaltura)} \n\n\tAlunos Lista dos Alunos Abaixo Da Media :")
        for alx in range(len(self.Alunoaltura)):
            print(f"Aluno {alx+1}\n\tIdade: {self.AlunoIdade[alx]} Altura:{self.Alunoaltura[alx]}")

    def Questao_104(self):
        """
        Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
        Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
        e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
        """
        os.system("cls")
        self.Meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho',
                      'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        self.temperatura_mensal = []
        self.temp_acima_Da_Media = []

        self.soma = 0
        self.Lista = []
        for mes in range(1,len(self.Meses)+1):
            temp = float(input(f"Temperatura {mes}/12 :"))
            self.temperatura_mensal.append(temp)
            self.soma += temp
            os.system("cls")
        self.Media = self.soma/len(self.temperatura_mensal)#Media Anual
        for temp in range(len(self.temperatura_mensal)):
            aux = self.temperatura_mensal[temp]
            if aux > self.Media:#verificando se a temp é Maior Que a media
                self.temp_acima_Da_Media.append(self.temperatura_mensal[temp])
                self.Lista.append(self.Meses[temp])
        print("Temperaturas que Estão Acima Da Media Anual\n")
        for maximo in range(len(self.temp_acima_Da_Media)):
            print(f"\tMes de {self.Lista[maximo]} Com Temperatura {self.temp_acima_Da_Media[maximo]}° graus")

    def Questao_105(self):
        """
        Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
        encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
        Após esta entrada de dados, faça: 
            Mostre a quantidade de valores que foram lidos; 
            Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
            Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 
            Calcule e mostre a soma dos valores; 
            Calcule e mostre a média dos valores; 
            Calcule e mostre a quantidade de valores acima da média calculada; 
            Calcule e mostre a quantidade de valores abaixo de sete; Encerre o programa com uma mensagem;
        """
        os.system("cls")
        self.notas = []
        self.Lista_NumeroN = []
        self.Lista_NumeroM = []
        self.n = 0
        self.soma = 0
        while True:
            self.n += 1
            self.nota = float(input(f"Nota {self.n}° :"))
            os.system("cls")
            if self.nota < 0:
                break
            self.soma += self.nota
            self.notas.append(self.nota)
        self.Media = self.soma/len(self.notas)
        for valor in range(len(self.notas)):
            aux = self.notas[valor]
            if aux > self.Media:
                self.Lista_NumeroM.append(aux)#Valores Acima Da Media
            if aux < 7:
                self.Lista_NumeroN.append(aux)#Valores Abaixo Da Media
        print(f"""
            Quantidade de Notas {len(self.notas)}
            Soma: {self.soma}
            Media: {self.Media:.2f}
            Valores Acima Da Media: {len(self.Lista_NumeroM)} 
                            Lista : {self.Lista_NumeroM}
            Valores Abaixo Da Media: {len(self.Lista_NumeroN)} 
                            Lista : {self.Lista_NumeroN}
            """)
            
    def Questao_106(self):
        """
        Utilize uma lista para resolver o problema a seguir. 
        Uma empresa paga seus vendedores com base em comissões. 
        O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
        Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
        
        Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes 
        intervalos de valores: 
                $200 - $299 
                $300 - $399 
                $400 - $499 
                $500 - $599 
                $600 - $699 
                $700 - $799 
                $800 - $899 
                $900 - $999 
                $1000 em diante

                Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
        """
        os.system("cls")
        self.Lista_Numero = []
        self.Intervalo = [
                200,299,
                300,399,
                400,499,
                500,599, 
                600,699, 
                700,799, 
                800,899, 
                900,999,1000]
        while True:
            self.n = float(input("informe Seu Salario:"))
            if self.n <0:
                break
            self.Lista_Numero.append(self.n)
        try:
            for salario in range(1,len(self.Lista_Numero)+1):
                for valor in range(1,len(self.Intervalo)+1):
                    if self.Lista_Numero[salario-1] >= self.Intervalo[valor-1] and self.Lista_Numero[salario-1] <= self.Intervalo[valor]:
                        print(f"O Vendedor {salario} Tem salario R${self.Lista_Numero[salario-1]} e Esta entre A posição {valor-1} e {valor} do Invervalo {self.Intervalo[valor-1]} e {self.Intervalo[valor]} ")
                    elif self.Lista_Numero[salario-1] > 1000:
                        print(f"O Vendedor {salario} Possui R${self.Lista_Numero[salario-1]} e Está fora Do Intervalo")
                        break
        except IndexError as err:
            print()#Tratando o erro de IndexErro por conta do tamanho da lista Intervalo ser impar

    def Questao_107(self):
        """
        Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
        Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
        Sua equipe foi contratada para desenvolver este programa. 
        Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. 
        Um número de jogador igual zero, indica que a votação foi encerrada. 
        Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
        Após o final da votação, o programa deverá exibir: 
            O total de votos computados; 
            Os números dos respectivos votos de todos os jogadores que receberam votos; 
            O percentual de votos de cada um destes jogadores; 
            O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele. 
        
        Observe que os votos inválidos e o zero final não devem ser computados como votos. 
        O resultado aparece ordenado pelo número do jogador. 
        O programa deve fazer uso de arrays. 
        O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
        Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
        A função calculará o percentual e retornará o valor calculado.
        Resultado da votação:
        Foram computados 8 votos.
        Jogador Votos % 9 4 50,0% 10 3 37,5% 11 1 12,5% O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
        """
        os.system("cls")
        self.numero = {}
        self.Lista = []
        self.soma = 0
        self.total = 0
        self.Maior_nota = 0
        self.Jogador = 0
        while True:
            voto = int(input("Informe um valor entre 1 e 23 ou 0 para sair   :"))
            if voto == 0:
                break
            elif voto <1 or voto>23:
                print("Valor Invalido")
            else:
                self.total += 1
                self.Lista.append(voto)
        
        for x in self.Lista:
            self.soma = 0
            for y in self.Lista:
                if x == y:
                    self.soma += 1
            self.numero[x] = self.soma
        
        for chave,valor in self.numero.items():
            if valor > self.Maior_nota:
                self.Jogador = chave
                self.Maior_nota = valor
                self.n = (valor/self.total)*100
        self.numeroNovo = sorted(self.numero.keys())
        print(f"Foram computados {self.total} votos\n")
        for chave in self.numeroNovo:
            print(f"\tJogador Camisa {chave} Obteve {self.numero[chave]} Votos e {(self.numero[chave]/self.total)*100:.0f}% porcento")
        print(f"\tMelhor Jogador Camisa {self.Jogador} e Seus {self.Maior_nota} Votos e {self.n:.0f}% Porcentagem De Aceitação")
        
    def Questao_108(self):
        """
        Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 
        "Qual o melhor Sistema Operacional para uso em servidores?"

        As possíveis respostas são:
        1- Windows Server 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro
        Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
        O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
        Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
        Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
        Após os dados terem sido completamente informados, 
        o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
        O formato da saída foi dado pela empresa, e é o seguinte:

        Sistema Operacional         Votos           %

        Windows Server              1500            17% 
        Unix                        3500            40% 
        Linux                       3000            34% 
        Netware                      500             5% 
        Mac OS                       150             2% 
        Outro                        150             2%

                                    Total 8800

        O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
        """
        os.system("cls")
        self.SO = ['Windows Server','Unix','Linux','Netware','Mac OS','Outros']
        self.Lista = []
        self.votos = {}
        self.soma = 0
        self.Maior_nota = 0
        while True: 
            voto = int(input(f"1-{self.SO[0]} 2-{self.SO[1]} 3-{self.SO[2]} 4-{self.SO[3]} 5-{self.SO[4]} 6-{self.SO[5]} Escolha:"))
            if voto == 0:
                os.system("cls")
                break
            elif voto <1 or voto >6:
                print("\nValor Invalido\n")
            else:
                self.Lista.append(voto)
                os.system("cls")
        
        for x in self.Lista:
            self.soma = 0
            for y in self.Lista:
                if x == y:
                    self.soma += 1
            if self.soma > self.Maior_nota:
                self.Jogador = x
                self.Maior_nota = self.soma
            self.votos[self.SO[x-1]] = self.soma
        for chave,valor in self.votos.items():
            print(f"O {chave} Possui {valor} votos {valor/len(self.Lista)*100}%")
        print(f"Melhor Sistema {self.SO[self.Jogador-1]} Com {self.Maior_nota} Votos e {self.Maior_nota/len(self.Lista)*100}% \nTotal {len(self.Lista)}")
    
    def Questao_109(self):
        """
        Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
        O piso do abono será de 100 reais, isto é, aqueles funcionários cujo
        salário for muito baixo recebem este valor mínimo;
        Neste momento, não se deve ter nenhuma preocupação com colaboradores com
        tempo menor de casa, descontos, impostos ou outras particularidades.

        Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. 
        Um valor de salário igual a 0 (zero) encerra a digitação. 
        Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. 
        Ao final, o programa deverá apresentar:
            O salário de cada funcionário, juntamente com o valor do abono; 
            O número total de funcionários processados; 
            O valor total a ser gasto com o pagamento do abono; 
            O número de funcionários que receberão o valor mínimo de 100 reais; 
            O maior valor pago como abono;

        Salário: 1000 Salário: 300 Salário: 500 Salário: 100 Salário: 4500  
        Salário - Abono R$ 1000.00 - R$ 200.00 R$ 300.00 - R$ 100.00 R$ 500.00 - R$ 100.00 R$ 100.00 - R$ 100.00 R$ 4500.00 - R$ 900.00
        Foram processados 5 colaboradores Total gasto com abonos: R$ 1400.00 Valor mínimo foi pago a 3 colaboradores Maior valor de abono pago: R$ 900.00
        """
        os.system("cls")
        self.Maior_nota = 0
        self.Lista = []
        self.Abono = []
        self.total = 0
        self.valorMinimo = 0
        while True:
            val = len(self.Lista)+1
            salario = float(input(f"Salario {val}:"))
            if salario == 0:
                os.system("cls")
                break
            self.Lista.append(salario)
        for valor in self.Lista:
            aux = valor * 20/100
            if aux <= 100:
                aux = 100
                self.valorMinimo += 1
            if aux > self.Maior_nota:
                self.Maior_nota = aux
            self.Abono.append(aux)
            self.total += valor - aux
        
        for x in range(len(self.Lista)):
            print(f"Salario R${self.Lista[x]} e o Abono de R${self.Abono[x]}")
        print(f"Foram processados {len(self.Abono)} Colaboradores \nTotal Gasto Com os Abono R${self.total} \nValor mínimo foi pago a {self.valorMinimo} colaboradores\nMaior valor de abono pago:{self.Maior_nota}")
        
            