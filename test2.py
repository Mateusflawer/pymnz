import pymnz


valor1 = 10
valor2 = 20

resultado = pymnz.calculos.soma(valor1, valor2)

if str(resultado) == '30':
    print('A soma foi:', resultado)
else:
    print('Resultado não esperado')
