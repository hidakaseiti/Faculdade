n = int(input('Digite um número maior ou igual a 2: '))
for i in range(2,n):
    if n%i == 0:
        break
else:
    print(n)