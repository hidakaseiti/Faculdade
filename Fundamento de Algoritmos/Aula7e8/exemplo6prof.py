n = 8
i = 2
eh_primo = True
while i < n:
    if n%i==0:
        eh_primo = False
        break
    i += 1

if eh_primo:
    print(n)