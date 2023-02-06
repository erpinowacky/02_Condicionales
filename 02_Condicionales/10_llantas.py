'''Leer el número de llantas de una compra y mostrar el valor que debe pagarse.
El almacén las vende con la siguiente política: Si se compran menos de 6 llantas,
el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000,
y si se compran más de 7 llantas, el precio unitario es $180000.'''

cantidad = 0
precioUnitario = 0.0
precioTotal= 0.0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***MODALIDAD DE PAGO***')
print('****************************')
print()
cantidad = int(input('Digite el número de llantas compradas: '))
if cantidad >= 6 and cantidad < 8 :
    precioUnitario = 221000
elif cantidad > 7:
    precioUnitario = 180000
else:
    precioUnitario = 240000
precioTotal = precioUnitario * cantidad
print(f'El valor a pagar es de : ${precioTotal}')