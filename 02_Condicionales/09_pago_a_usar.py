'''Programa que permita a un usuario tomar una decisión del tipo de pago a usar.
Si la cuenta es menor a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 pago con el celular
(dinero electrónico). Si es mayor a $300000 hasta $600000,
pago con la tarjeta de débito. Caso contrario, pago con la tarjeta de crédito.'''

pago = 0.0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***MODALIDAD DE PAGO***')
print('****************************')
print()

pago=float(input('Digite el monto a pagar: '))

if pago > 0 and pago < 150000:
    print('Pagar en efectivo')
else:
    if pago >= 150000 and pago <= 300000:
        print('Pagar con el celular (Dinero electrónico)')
    elif pago > 300000 and pago <= 600000:
        print('Pagar con tarjeta débito')
    elif pago > 600000:
        print('Pagar con tarjeta de crédito')
    else:
        print('Saldo incorrecto')
