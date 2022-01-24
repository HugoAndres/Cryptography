import random

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario


listaZCuadrada = []
listaZ = []
listaBinario = []
listaI = []
listaDatos = []

# x = 52810244494725830222899320608968523977001967001745
#a = 12345
# n = 6543

x = random.randint(10000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000)
a = random.randint(1000000000000000, 10000000000000000)
n = random.randint(10000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000)
aBinario = decimal_a_binario(a)
i = 0
tamano = len(aBinario) - 1
z = 1


print('x =', x, ' -> TAMAÑO MAXIMO = 50')
print('a =', a, ' -> TAMAÑO MAXIMO = 16')
print('n =', n, ' -> TAMAÑO MAXIMO = 50')
print('binario =', aBinario)
print('i =', tamano)
print('z =', z)

for digito in aBinario:
    listaBinario.append(digito)

while i <= tamano:
    listaI.append(i)
    valorB = int(listaBinario[i])
    z = pow(z, 2) % n
    listaZCuadrada.append(z)
    if valorB == 1:
        z = (x * z) % n
        listaZ.append(z)
    else:
        listaZ.append('---')
    i += 1

listaInversa = []
for item in reversed(listaI):
    listaInversa.append(item)

print('|\ti\t|\tb[ i ]\t|\t\t\t\t\t\t\t\t\tz = z²\t\t\t\t\t\t\t\t|\t\t\t\t\t\t\tz = x*z mod n')
for i in range(len(listaI)):
    print('| ', listaInversa[i], '\t|\t ', listaBinario[i], '\t|\t\t', listaZCuadrada[i], '\t\t\t|\t\t\t',
          listaZ[i])
print('\n===>>(', x, '^', a, ') mod', n, '=', listaZ[len(aBinario)-1])
