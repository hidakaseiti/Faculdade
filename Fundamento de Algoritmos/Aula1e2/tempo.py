dias = int(input('dias: '))
horas = int(input('horas: '))
minutos = int(input('minutos: '))
segundos = int(input('segundos: '))
total = dias*86400 + horas*3600 + minutos*60 + segundos
print(f'tempo total foi de: {total}')