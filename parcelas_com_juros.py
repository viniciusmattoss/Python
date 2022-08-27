valor = float(input("Digite o valor de sua compra:"))
parcelas = int(input("Digite a quantidade de parcelas:"))

juros = (valor*7/100)+valor

divisao = juros/parcelas

print(f"O valor total de sua compra com 7% de juros é de {juros} reais \n e voce pagara mensalmente {divisao} reais por {parcelas} meses.")