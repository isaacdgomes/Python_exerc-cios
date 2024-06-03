#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#A)Para homens: (72.7*h) - 58
#B)Para mulheres: (62.1*h) - 44.7


# Solicita ao usuário que insira a altura e o sexo
altura = float(input("Informe sua altura em metros: "))
sexo = input("Informe o sexo (M para masculino e F para feminino): ").strip().upper()

# Calcula o peso ideal usando as fórmulas fornecidas
peso_homens = (72.7 * altura) - 58
peso_mulheres = (62.1 * altura) - 44.7

# Verifica o sexo do usuário e imprime o peso ideal correspondente
if sexo == "M":
    print(f"Seu peso ideal é: {peso_homens:.2f} kg")
elif sexo == "F":
    print(f"Seu peso ideal é: {peso_mulheres:.2f} kg")
else:
    print("Sexo inválido. Por favor, informe 'M' para masculino ou 'F' para feminino.")


