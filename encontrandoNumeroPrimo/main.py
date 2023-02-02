num = int(input('Digite um numero: '))
primos = []

for i in range(1, num +1):
    if num % i == 0:
        primos.append(i)
    else:
        pass

if len(primos) ==2:
    print(f'O numero {num} é primo')
else:
    print(f'O numero {num} nao é primo')