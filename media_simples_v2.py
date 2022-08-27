cont = 0
soma = 0

nome = str(input("Digite o seu nome:"))

while cont <3:
    nota = float(input("Digite a sua nota:"))
    soma = soma+nota
    cont +=1

media = soma/3

if media >7:
    print(f"Parabéns {nome}!Você foi aprovado")
elif media <7 and media >=5:
    print(f"Você ficou com media {media} e esta de recuperação")
else:
    print(f"{nome},você está reprovado")




