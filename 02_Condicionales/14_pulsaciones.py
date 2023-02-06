'''14. El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico 
se calcula con la fórmula:
Género femenino (1): número de pulsaciones = (220 - edad en años)/10
Género masculino (2): número de pulsaciones = (210 - edad en años)/10
Lea la edad y el género y muestre el número de pulsaciones.'''

edad = 0
genero = ''
nPulsaciones = 0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***LOCAL***')
print('****************************')
print()

genero = genero.lower()
genero = input('Digite el género de la persona: ')
edad = int(input('Digite la edad de la persona: '))
if genero == 'femenino' or genero == 'masculino':
    if genero == 'femenino':
        nPulsaciones = (220 - edad) / 10
    else:
        nPulsaciones = (210 - edad) / 10
else:
    print('Dato inválido')
print(f'El número de pulsaciones que debe tener esta persona de género {genero} es {nPulsaciones}')