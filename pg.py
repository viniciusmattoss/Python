
a = int(input("Digite o primeiro termo: "))
r = int(input("Digite a Razão: "))
qts = 5

pg = [ a * r ** (n - 1) for n in range(1, qts + 1) ]

print( pg )