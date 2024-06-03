#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A)o produto do dobro do primeiro com metade do segundo .
#B)a soma do triplo do primeiro com o terceiro.
#C)o terceiro elevado ao cubo.

primeiro_inteiro = int(input("Informe um número: "))
segundo_inteiro = int(input("Informe um número: "))
terceiro_real = float(input("Informe um número: "))

a = (primeiro_inteiro * 2) * (segundo_inteiro / 2)
b = (primeiro_inteiro * 3) + terceiro_real
c = terceiro_real ** 3

print("O produto do dobro do primeiro com metade do segundo:", a)
print("A soma do triplo do primeiro com o terceiro:", b)
print("O terceiro elevado ao cubo:", c)