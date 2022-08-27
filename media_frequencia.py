media = float(input("Digite a sua média(0 a 10):"))

frequencia = int(input("Digite a sua frequencia nas aulas(0 a 100):"))

if frequencia <75:
    print("Você foi reprovado")

elif frequencia>=75 and media<7:
    print("Você esta de recuperação")


elif frequencia >=75 and frequencia <=100 and media >=7 and media <=10:
    print("Você foi aprovado")

else:
    print("Valor da media e/ou da frequencia estão incorretas")


