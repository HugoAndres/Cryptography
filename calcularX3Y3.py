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

p = int(input("\nIntroduce el valor de p de la curva elíptica: "))
x1 = int(input("Introduce el valor de x1 : "))
y1 = int(input("Introduce el valor de y1 : "))
x2 = int(input("Introduce el valor de x2 : "))
y2 = int(input("Introduce el valor de y2 : "))

# Calcular lambda = (y2 - y1)(x2 -x1)⁻¹ mod p
# Calcular (x2 -x1)⁻¹
numeroExponencial = algoritmoExponenciacion((x2 - x1), 1, p)
numeroInverso = algoritmoInversoMultiplicativo(p, numeroExponencial)
lam = algoritmoExponenciacion(((y2 - y1) * numeroInverso), 1, p)
# print('lambda = ', lam)
x3 = algoritmoExponenciacion((pow(lam, 2) - (x1 + x2)), 1, p)
y3 = algoritmoExponenciacion((lam * (x1 - x3) - y1), 1, p)
nuevasCoordenadas = [(x3, y3)]
print(" = ", nuevasCoordenadas)


