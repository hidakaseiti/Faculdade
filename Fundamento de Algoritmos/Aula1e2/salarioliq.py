salario_hora = float(input('Ganho por hora: '))
horas_trabalhadas = int(input('Horas no mês: '))
print(
    f'{salario_hora*horas_trabalhadas:.2f}\n'
    f'{salario_hora*horas_trabalhadas*0.11:.2f}\n'
    f'{salario_hora*horas_trabalhadas*0.08:.2f}\n'
    f'{salario_hora*horas_trabalhadas*0.05:.2f}\n'
    f'{salario_hora*horas_trabalhadas*0.76:.2f}'
)