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

x = int(input("Introduce el valor de x: "))
a = int(input("Introduce el valor de a: "))
n = int(input("Introduce el valor de n: "))
aBinario = decimal_a_binario(a)
i = 0
tamano = len(aBinario) - 1
z = 1

# print('x =', x)
# print('a =', a)
# print('n =', n)
# print('binario =', aBinario)
# print('i =', tamano)
# print('z =', z)

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

# print('|\t\ti\t\t|\t\tb[ i ]\t\t|\t\tz = z²\t\t|\t\tz = x*z mod n')
# for i in range(len(listaI)):
    # print('|\t  ', listaInversa[i], '\t\t|\t\t ', listaBinario[i], '\t\t|\t\t', listaZCuadrada[i], '\t\t|\t\t\t',
          # listaZ[i])
print('\n===>>(', x, '^', a, ') mod', n, '=', listaZ[len(aBinario)-1])
