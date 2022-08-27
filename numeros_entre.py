p1 = int(input("Digite um numero:"))

p2 = int(input("Digite outro numero"))


if p1 < p2:
    p2 = p2-1

    for i in range(p1,p2):
        print(i+1)


else:
    p1= p1+1
    p2 = p2+2

    for i in range (p2,p1): 
        print(i-1)






