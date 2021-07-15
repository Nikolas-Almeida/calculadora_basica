# Calculadora Basica

import math

print(
    '\n==================' +
    '\nCALCULADORA BÁSICA' +
    '\n=================='
    )

valor1 = float(input('\nPrimeiro valor: '))

valor2 = float(input('\nSegundo valor: '))

operador = input(
    '\nOperadores:' +
    '\nAdição: +' +
    '\nSubtração: -' +
    '\nMultiplicação: *' +
    '\nDivisão: /' +
    '\nPotência: **' +
    '\nRaíz quadrada (de ambos os valores): #' +
    '\n\nColoque o símbolo do operador desejado: '
    )

if operador == '+':
    print(
        f'\nResultado: {valor1 + valor2}'
        )
elif operador == '-':
    print(
        f'\nResultado: {valor1 - valor2}'
        )
elif operador == '*':
    print(
        f'\nResultado: {valor1 * valor2}'
        )
elif operador == '/':
    print(
        f'\nResultado: {valor1 / valor2}'
        )
elif operador == '**':
    print(
        f'\nResultado: {valor1 ** valor2}'
        )
elif operador == '#':
    raiz1 = math.sqrt(valor1)
    raiz2 = math.sqrt(valor2)

    print(f'\nRaíz quadrada de {valor1} é {raiz1}')
    print(f'\nRaíz quadrada de {valor2} é {raiz2}')
else:
    print('\nOperador inválido.')

print('\nFIM!')
