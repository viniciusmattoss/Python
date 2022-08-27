


nome = str(input("Digite o seu nome:"))

n1 = float(input("Digite a sua nota 1:"))
n2 = float(input("Digite a sua nota 2:"))
n3 = float(input("Digite a sua nota 3:"))

media = (n1+n2+n3)/3

if media >7:
    print(f"Parabéns {nome}!Você foi aprovado")
elif media <7 and media >=5:
    print(f"Você ficou com media {media} e esta de recuperação")
else:
    print(f"{nome},você está reprovado")