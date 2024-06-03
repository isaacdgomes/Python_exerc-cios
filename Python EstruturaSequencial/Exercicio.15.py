#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#A)salário bruto.
#B)quanto pagou ao INSS.
#C)quanto pagou ao sindicato.
#D)o salário líquido.
#E)calcule os descontos e o salário líquido, conforme a tabela abaixo:

#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganha_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))

salario_bruto = ganha_por_hora * horas_trabalhadas

imposto_renda = (11/100) * salario_bruto
inss = (8/100) * salario_bruto 
sindicato = (5/100) * salario_bruto

salario_liquido = salario_bruto - imposto_renda - inss - sindicato


print(f"+ Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (11%) : R$ {imposto_renda:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato ( 5%) : R$ {sindicato:.2f}")
print(f"= Salário Liquido : R$ {salario_liquido:.2f}")