'''Solicitar número al usuario y determinar si es par, impar o es cero.'''

num=0.0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***Par-Impar-Igual que cero***')
print('******************************')
print()
num = float(input('Digite un número: '))
if num < 0 or num > 0:
    if num < 0:
        print(f'El número {num} es menor a cero')
    else:
        print(f'El número {num} es mayor a cero')
else:
    print(f'El número {int(num)} es equivalente a cero')
print('Fin')