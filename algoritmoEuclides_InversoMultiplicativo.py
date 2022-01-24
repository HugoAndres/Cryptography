# Algoritmo de Euclides

# r0_inicial = 143
# r1_inicial = 8
# 9978
r0_inicial = int(input("Introduce el valor de r0: "))
r1_inicial = int(input("Introduce el valor de r1: "))
listaQ = []
r0 = r0_inicial
r1 = r1_inicial
cociente = r0 // r1
resto = r0 % r1
print(r0, '=', cociente, '*', r1, '+', resto)
listaQ.append(cociente)
if r0 > r1:
    while resto != 0:
        r0 = r1
        r1 = resto
        cociente = r0 // r1
        resto = r0 % r1
        print(r0, '=', cociente, '*', r1, '+', resto)
        listaQ.append(cociente)
    if r1 == 1:
        print('\nMCD = (', r1_inicial, ',', r0_inicial, ') =', r1)
        print(r1_inicial, 'si tiene inverso multiplicativo modulo', r0_inicial, '\n')
        # for q in range(len(listaQ) - 1):
            # print('q[', q, '] = ', listaQ[q])
        listaT = [0, 1]
        # print('')
        # print('t[ 0 ] =', listaT[0])
        # print('t[ 1 ] =', listaT[1])
        for n in range(len(listaQ) - 1):
            t = (listaT[n] - listaQ[n] * listaT[n + 1]) % r0_inicial
            # print('t[', n + 2, '] =', listaT[n], '-', listaQ[n], '*', listaT[n + 1], '%', r0_inicial, '=', t)
            listaT.append(t)
        tamano = len(listaT) - 1
        print('Inverso multiplicativo:', listaT[tamano])
        comprobacion = (listaT[tamano] * r1_inicial) % r0_inicial
        print('Comprobación:', listaT[tamano], '*', r1_inicial, '%', r0_inicial, '=', comprobacion)
    else:
        print('\nMCD = (', r1_inicial, ',', r0_inicial, ') =', r1)
        print(r1_inicial, 'no tiene inverso multiplicativo modulo', r0_inicial, '\n')
else:
    print('No se cumple la regla r0 > r1')
