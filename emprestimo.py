reload = True
while reload == True:

    print("---------------------------")
    print("-------Bem-Vindo(a)--------")
    print("--Simulador de emprestimo--")
    print("---------------------------")

    conta = str(input("ja é nosso cliente?:"))

    if conta == 'S' or conta == 's':

        cont = 0

        valor = float(input("Digite o valor do emprestimo:"))
        parcela = int(input("Digite a quantidade de parcelas:"))
        desemprego = str(input("Deseja adicionar o seguro desemprego?:"))

        if desemprego == 'S' or desemprego == 's':
            seguro = (valor*3.5/100)+valor
            iof = (seguro*0.38/100)+seguro

            while cont < parcela:
                iof = (iof*4/100)+iof
                cont +=1

            mensal = iof/parcela        
        else:
            iof = (valor*0.38/100)+valor

            while cont < parcela:

                iof = (iof*4/100)+iof
                cont +=1

            mensal = iof/parcela
            
    
        print("----------------------------------------")    
        print("A quantidade de parcelas é",parcela)
        print("Valor das parcelas:{:.2f}".format(mensal))
        print("taxa de juros:4%")
        print("custo efetivo total:{:.2f}" .format(iof))
        print("----------------------------------------")    

    else:

        cont = 0

        serasa = int(input("Digite o seu serasa score:"))
        valor = float(input("Digite o valor do emprestimo:"))
        parcela = int(input("Digite a quantidade de parcelas:"))
        desemprego = str(input("Deseja adicionar o seguro desemprego?:"))

        if serasa <=299:
            porcentagem = 20

        elif serasa >=300 and serasa <=499:
            porcentagem = 15

        elif serasa >=500 and serasa <=699:
            porcentagem = 10

        else:
            porcentagem = 5

        if desemprego == 'S' or desemprego == 's':

            valor = valor+35
            seguro = (valor*3.5/100)+valor
            iof = (seguro*0.38/100)+seguro

            while cont < parcela:
                iof = (iof*porcentagem/100)+iof
                cont +=1

            mensal = iof/parcela  
        else:
            iof = (valor*0.38/100)+valor

        while cont < parcela:

                iof = (iof*porcentagem/100)+iof
                cont +=1

                mensal = iof/parcela

            
        print("----------------------------------------")    
        print("A quantidade de parcelas é",parcela)
        print("Valor das parcelas:{:.2f}".format(mensal))
        print(f"taxa de juros: {porcentagem}%")
        print("custo efetivo total:{:.2f}" .format(iof))
        print("---------------------------------------")

    


    reload = str(input("Deseja fazer outra simulação?"))

    if reload == 's' or reload == 'S':
        reload = True

    else:
        reload = False
        print("fim algoritimo")
        










        


    
        





    




    

    

    


    
       

