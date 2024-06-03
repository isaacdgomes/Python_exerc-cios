#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

# Solicita ao usuário que insira a sua altura
altura = float(input("Informe sua altura em metros: "))

# Calcula o peso ideal usando a fórmula dada
peso_ideal = (72.7 * altura) - 58

# Imprime o peso ideal formatado com duas casas decimais
print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
