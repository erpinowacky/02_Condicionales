'''Preguntar al usuario el nombre y la edad, si es mayor o igual a
 18 años mostrar el mensaje "Usted es mayor de edad", de lo contrario "Usted es menor de edad". 
 Si el número ingresado es negativo o la edad ingresada es mayor a 100 años, mostrar 
al usuario un mensaje de ingresar una edad válida.'''

nombre=''
edad=0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***Programa Mayor de Edad***')
print('****************************')
print()
nombre = input('Digite su nombre: ')
edad = int(input('Digite su edad: '))
print(f'{nombre} su edad ingresada es: {edad}')
if edad < 0 or edad > 100:
    print('Edad no válida')
else:
    if edad < 18:
        print('Usted es menor de edad')
    else:
        print('Usted es mayor de edad')
print('Fin')