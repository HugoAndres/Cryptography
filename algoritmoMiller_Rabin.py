import random

numero = int(input("Introduce el numero: "))
numeroAuxiliar = numero - 1
print('Número auxiliar (n - 1) = ', numeroAuxiliar)
k = 0
cociente = numeroAuxiliar
residuo = 0
while residuo == 0:
    cociente, residuo = divmod(cociente, 2)
    k += 1
k -= 1
m = cociente * 2 + 1
for i in range(10):
    cuenta = i + 1
    numeroAlAzar = random.randint(1, numeroAuxiliar - 1)
    b = pow(numeroAlAzar, m, numero)
    if b == 1 or b == numeroAuxiliar:
        continue
    for j in range(k - 1):
        b = pow(b, 2, numero)
        cuentab = j + 1
        # print('b[', cuentab, '] = ', b)
        if b == 1:
            print('\n ===>>El número ', numero, ' es compuesto.')
            exit()
        if b == numeroAuxiliar:
            break
    if b != numeroAuxiliar:
        print('\n ===>>El número ', numero, ' es compuesto.')
        exit()
print('\n ===>>El número ', numero, ' es primo.')
