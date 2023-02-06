'''11. El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado,
como se muestra a continuación:
    
    
    | Tamaño | Precio |
    | --- | --- |
    | 1 | $15.000 |
    | 2 | $24.000 |
    | 3 | $36.000 |
    
    Si cada ingrediente adicional cuesta $4.000. Escribir un programa que solicite al empleado encargado
    de registrar las ventas, el tamaño de la pizza y el número de ingredientes adicionales 
    y muestre al cliente el precio que debe pagar.'''

PRECIO1 = 15000
PRECIO2 = 24000
PRECIO3 = 36000
ADICIONAL = 4000
precio = 0
cantidadPizzas = 0
cantidadAdicion = 0
valorPagar = 0.0
tamaño = 0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***PIZZAS***')
print('****************************')
print()
tamaño = input('''Digite el tamaño de la pizza
1. Pequeña
2. Mediana
3. Grande ''')
cantidadPizzas = int(input('Digite la cantidad de pizzas: '))
cantidadAdicion = int(input('Digite el número de adicionales: '))
if tamaño in ('123'):
    if tamaño == '1':
        precio = PRECIO1
    elif tamaño == '2':
        precio = PRECIO2
    else:
        precio = PRECIO3
    valorPagar = (cantidadPizzas * precio) + (cantidadAdicion * ADICIONAL)
    print(f'El valor a pagar es de: ${valorPagar}')
else:
    print('Tamaño incorrecto')



