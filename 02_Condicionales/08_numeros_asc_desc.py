'''Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente. '''

mayor=0
medio=0
menor=0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***NÚMEROS ASCENDENTES-DESCENDENTES***')
print('****************************')
print()
num1 = int(input('Digite el primer número entero: '))
num2 = int(input('Digite el segundo número entero: '))
num3 = int(input('Digite el tercer número entero: '))

if num1 > num2 and num1 > num3:
    mayor = num1
    if num2 > num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    mayor = num2
    if num1 > num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1
else:
    mayor = num3
    if num1 > num2:
        medio = num1
        menor = num2
    else:
        medio = num2
        menor = num1
print(f'''Mayor = {mayor}
Medio = {medio}
Menor = {menor}''')
