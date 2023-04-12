n = int(input('Informe o numero: '))

a, b = 0, 1

while a < n:
    a, b = b, a + b

print(a == n)