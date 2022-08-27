salario = float(input("Digite o seu salario:"))

if salario <=1903.98:
    print("isento")

elif salario >=1903.99 and salario <=2826.65:
    print("Aliquóta:7,50%,Deduçã0: R$142,80")

elif salario >=2826.66 and salario <=3751.05:
    print("Aliquóta:15%.Dedução: R$354,80")

elif salario >=3751.06 and salario <=4664.68:
    print("Aliquóta:22,50%,Dedução: R$636,13")

elif salario >= 4664.68:
    print("Aliquóta 27,50%,Dedução R$868,36")