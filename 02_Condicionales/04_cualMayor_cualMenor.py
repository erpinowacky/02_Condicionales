'''Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.'''

num1=0.0
num2=0.0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***Mayor-Menor-Cero***')
print('****************************')
print()
num1 = float(input('Digite primer número: '))
num2 = float(input('Digite segundo número: '))
if num1 == num2:
    print('Los números son iguales')
else:
    if num1 > num2:
        print(f'Mayor: {num1}\nMenor: {num2}')
    else:
        print(f'Mayor: {num2}\nMenor: {num1}') 
print('Fin')