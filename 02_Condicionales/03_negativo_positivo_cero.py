'''Solicitar número al usuario y determinar si es negativo, positivo o cero.'''

num=0.0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***Negativo-Positivo-Cero***')
print('****************************')
print()
num = float(input('Digite un número: '))
if num != 0:
    if num > 0:
        print(f'El número {num} es positivo')
    else:
        print(f'El número {num} es negativo')
else:
    print(f'El número {int(num)} es equivalente a cero')
print('Fin')