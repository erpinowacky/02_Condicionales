'''Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay descuento.
Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%.
Si compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y 
el valor del precio unitario original. Calcule y muestre el valor total a pagar.'''

cantidad = 0
valorUnitario = 0.0
totalPagar = 0.0
descuento = 0.0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***LOCAL***')
print('****************************')
print()
valorUnitario = float(input('Digite el valor unitario del producto: '))
cantidad = int(input('Digite la cantidad de productos: '))
if cantidad < 6:
    descuento = 0.0
elif cantidad > 5 and cantidad < 10:
    descuento = valorUnitario * (5/100)
    valorUnitario = valorUnitario - descuento
elif cantidad >= 10:
    descuento = valorUnitario * (8/100)
    valorUnitario = valorUnitario - descuento
totalPagar = valorUnitario * cantidad
print(f'El total a pagar es de: ${totalPagar}')