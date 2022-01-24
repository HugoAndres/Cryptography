import random


def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario


def algoritmoPrimalidad(numero):
    numeroAuxiliar = numero - 1
    k = 0
    cociente = numeroAuxiliar
    residuo = 0
    while residuo == 0:
        cociente, residuo = divmod(cociente, 2)
        k += 1
    k -= 1
    m = cociente * 2 + 1
    for i in range(10):
        numeroAlAzar = random.randint(1, numeroAuxiliar - 1)
        b = pow(numeroAlAzar, m, numero)
        if b == 1 or b == numeroAuxiliar:
            continue
        for j in range(k - 1):
            b = pow(b, 2, numero)
            if b == 1:
                return 0
            if b == numeroAuxiliar:
                break
        if b != numeroAuxiliar:
            return 0
    return numero


def algoritmoExponenciacion(x, a, n):
    binarioInverso = []
    ZCuadrada = []
    Z = []
    Binario = []
    I = []
    i = 0
    z = 1

    numeroBinario = decimal_a_binario(a)
    tamanoNumeroBinario = len(numeroBinario) - 1

    for digito in numeroBinario:
        Binario.append(digito)

    while i <= tamanoNumeroBinario:
        I.append(i)
        valorB = int(Binario[i])
        z = pow(z, 2) % n
        ZCuadrada.append(z)
        if valorB == 1:
            z = (x * z) % n
            Z.append(z)
        else:
            Z.append('---')
        i += 1
    for digito in reversed(I):
        binarioInverso.append(digito)

    valorExponencial = Z[len(numeroBinario) - 1]

    if valorExponencial != '---':
        return valorExponencial
        # print('\n>>(', x, '^', a, ') mod', n, '=', valorExponencial)
    else:
        return ZCuadrada[len(numeroBinario) - 1]
    # return Z[len(numeroBinario) - 1]


def algoritmoInversoMultiplicativo(mod, n):
    listaQ = []
    r0 = mod
    r1 = n
    cociente = r0 // r1
    resto = r0 % r1
    listaQ.append(cociente)
    if r0 > r1:
        while resto != 0:
            r0 = r1
            r1 = resto
            cociente = r0 // r1
            resto = r0 % r1
            # print(r0, '=', cociente, '*', r1, '+', resto)
            listaQ.append(cociente)
        if r1 == 1:
            listaT = [0, 1]
            for n in range(len(listaQ) - 1):
                t = (listaT[n] - listaQ[n] * listaT[n + 1]) % mod
                listaT.append(t)
            tamano = len(listaT) - 1
            # print('\nInverso multiplicativo:', listaT[tamano])
            # comprobacion = (listaT[tamano] * n) % mod
            # print('Comprobación:', listaT[tamano], '*', n, 'mod', mod, '=', comprobacion)
            return listaT[tamano]
        else:
            return 0
            # print('\nMCD = (', n, ',', mod, ') =', r1)
            # print(n, 'no tiene inverso multiplicativo modulo', mod, '\n')
    else:
        return 0
        # print('No se cumple la regla mod > n')


# Declaración de variables
listaBinario = []

# Inputs
a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))


# Calculamos p = a² + b²
p = pow(a, 2) + pow(b, 2)
print("\nCalculamos p = ", p)

# Verificamos que sea número primo
numeroPrimo = algoritmoPrimalidad(p)
if numeroPrimo != 0:
    print('>> El número ', numeroPrimo, ' es primo.')
else:
    print('>> El número ', p, 'no es primo')
    exit()

# Verificamos p mod 4 = 1
numeroExponencial = algoritmoExponenciacion(p, 1, 4)
if numeroExponencial == 1:
    print('>>', p, 'mod 4 =', numeroExponencial)
else:
    print('>>', p, 'mod 4 != 1 ->', numeroExponencial)
    exit()

# Verificamos a + b mod 4 = 1
numeroExponencial = algoritmoExponenciacion(a + b, 1, 4)
if numeroExponencial == 1:
    print('>>', a + b, 'mod 4 =', numeroExponencial)
else:
    print('>>', a + b, 'mod 4 != 1 ->', numeroExponencial)
    exit()

# Calculamos q = (p + 2a +1) / 4
q = int((p + 2 * a + 1) / 4)
print("\nCalculamos q =", q)

# Verificamos que q sea número primo
numeroPrimo = algoritmoPrimalidad(q)
if numeroPrimo != 0:
    print('>> El número ', numeroPrimo, ' es primo.')
else:
    print('>> El número ', p, 'no es primo')
    exit()

alphaX = int(input("\nIntroduce el valor de x1: "))
alphaY = int(input("Introduce el valor de y1: "))

abscisa = alphaX
ordenada = alphaY

# Calculamos k = (x³ - y²)(x)⁻¹ mod p
# Calculamos x⁻¹
x = algoritmoExponenciacion(alphaX, 1, p)
alphaXInverso = algoritmoInversoMultiplicativo(p, x)
k = algoritmoExponenciacion((pow(alphaX, 3) - pow(alphaY, 2)) * alphaXInverso, 1, p)
print("\nCalculamos k =", k)

# Verificamos que k = k^((p -1) / 4) mod p != 1, k no es potencia cuarta de ningun elemento de Fp
potenciaCuarta = algoritmoExponenciacion(k, int((p - 1) / 4), p)
if potenciaCuarta != 1:
    print('>> (', k, '^', int((p - 1) / 4), ') mod', p, '=', potenciaCuarta,
          'como es != 1,k no es potencia cuarta de ningun elemento de Fp')
else:
    print('>> (', k, '^', int((p - 1) / 4), ') mod', p, '=', potenciaCuarta,
          ', k es potencia cuarta de algun elemento de Fp')
    exit()

# Verificamos que k = k^((p -1) / 2) mod p = 1, k es potencia cuadrada de algun elemento de Fp
potenciaCuadrada = algoritmoExponenciacion(k, int((p - 1) / 2), p)
if potenciaCuadrada == 1:
    print('>> (', k, '^', int((p - 1) / 2), ') mod', p, '=', potenciaCuadrada,
          ', k es potencia cuadrada de algun elemento de Fp')
else:
    print('>> (', k, '^', int((p - 1) / 2), ') mod', p, '=', potenciaCuadrada,
          ', k no es potencia cuadrada de ningun elemento de Fp')
    exit()

qMenosUno = q - 1
qMenosUnoBinario = decimal_a_binario(qMenosUno)
listaQmenosUnoBinario = []
print('\nCalculamos (q - 1) =', qMenosUno, '=', qMenosUnoBinario, '\n')

for digito in qMenosUnoBinario:
    listaBinario.append(digito)
# print(listaBinario)

tamanoNumeroBinario = len(qMenosUnoBinario) - 1
# print(tamanoNumeroBinario)

a = -k
i = 0
coordenadas = [(alphaX, alphaY)]
while i < tamanoNumeroBinario:
    # Calculamos lambda = (3x² + a)(2y)⁻¹ mod p
    # Calculamos (y1⁻¹)
    y1 = algoritmoExponenciacion(alphaY * 2, 1, p)
    alphaYInverso = algoritmoInversoMultiplicativo(p, y1)
    # print(alphaYInverso)
    lam = algoritmoExponenciacion(((3 * pow(alphaX, 2) + a) * alphaYInverso), 1, p)
    # print("lambda = ", lam)
    # Calculamos x3 = lambda² - 2*x1 mod p
    x3 = algoritmoExponenciacion((pow(lam, 2) - 2 * alphaX), 1, p)
    # print('x3 =', x3)
    # Calculamos y3 = lambda(x1 - x3) - y1 mod p
    y3 = algoritmoExponenciacion((lam * (alphaX - x3) - alphaY), 1, p)
    # print('y3 =', y3)
    coordenadas.append((x3, y3))
    alphaX = x3
    alphaY = y3
    i += 1
# print(coordenadas)
listaBinario.reverse()

for tupla in range(len(coordenadas)):
    if tupla == 0:
        print("1 X = ", coordenadas[tupla], "->", listaBinario[tupla])
    else:
        print(pow(2, tupla), "X = ", coordenadas[tupla], "->", listaBinario[tupla])

coordenadasParaSumar = []
item = 0
i = 0
while i <= tamanoNumeroBinario:
    if listaBinario[i] == '1':
        # print(listaBinario[item])
        coordenadasParaSumar.append(coordenadas[i])
    i += 1
# print(coordenadasParaSumar)


# ----------------SUMA ABSCISAS DIFERENTES------------------------------------------------
i = 0
numeroCordenadas = len(coordenadasParaSumar)
# print(numeroCordenadas)
# print(i)
# for punto in range(numeroCordenadas-1):
x1 = coordenadasParaSumar[i][0]
y1 = coordenadasParaSumar[i][1]
while i <= numeroCordenadas - 2:
    # print('valor i: ', i)
    for coordenada in range(0, 1):
        # print('coordenada:', coordenada)

        x2 = coordenadasParaSumar[i + 1][coordenada]
        y2 = coordenadasParaSumar[i + 1][coordenada + 1]

        # print('x1 = ', x1)
        # print('y1 = ', y1)
        # print('x2 = ', x2)
        # print('y2 = ', y2)
        # Calcular lambda = (y2 - y1)(x2 -x1)⁻¹ mod p
        # Calcular (x2 -x1)⁻¹
        numeroExponencial = algoritmoExponenciacion((x2 - x1), 1, p)
        numeroInverso = algoritmoInversoMultiplicativo(p, numeroExponencial)
        lam = algoritmoExponenciacion(((y2 - y1)*numeroInverso), 1, p)
        # print('lambda = ', lam)
        x3 = algoritmoExponenciacion((pow(lam, 2) - (x1 + x2)), 1, p)
        y3 = algoritmoExponenciacion((lam * (x1 - x3) - y1), 1, p)
        nuevasCoordenadas = [(x3, y3)]
        x1 = x3
        y1 = y3
        i += 1
print('\n',qMenosUno, 'X = ', nuevasCoordenadas[0])
print(-ordenada, 'mod', p, '=', algoritmoExponenciacion(-ordenada, 1, p))
