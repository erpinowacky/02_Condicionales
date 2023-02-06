'''Conversión de temperaturas. Crear un menú de opciones. '''

fahrenheit = 0.0
celsius = 0.0
kelvin = 0.0
ranquine = 0.0
reaumur = 0.0
opcionP = ''
opcionS = ''
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***CONVERSIONES GRADOS***')
print('****************************')
print()
MENU_P = '''***MENÚ CONVERSIONES***
1. Fahrenheit
2. Celsius
3. Kelvin
4. Ranquine
5. Reaumur
6. Fin'''

MENU_F = '''1. Celsius
2. Kelvin
3. Ranquine
4. Reaumur'''

MENU_C = '''1. Fahrenheit
2. Kelvin
3. Ranquine
4. Reaumur'''

MENU_K = '''1. Fahrenheit
2. Celsius
3. Ranquine
4. Reaumur'''

MENU_RA = '''1. Fahrenheit
2. Celsius
3. Kelvin
4. Reaumur'''

MENU_RE = '''1. Fahrenheit
2. Celsius
3. Kelvin
4. Ranquine'''

while True:
    print(MENU_P)
    opcion = input('Elegir una opción: ')
    if (opcion not in '12345') and opcion != '6':
        print('Número no válido')
        continue
    elif opcion == '6':
        print('Adiós')
        exit()
    else:
        if opcion == '1':
            print('***FAHRENHEIT***')
            fahrenheit = float(input('Digite el valor en grados fahrenheit: '))
            print(MENU_F)
            print('Elegir una opción: ')
            opcionS = input()
            if opcionS not in ('1234'):
                print('Opción inválida')
            else:
                if opcionS == '1':
                    celsius = (fahrenheit - 32) / 1.8
                    print(f'Celsius = {celsius}')
                elif opcionS == '2':
                    kelvin = (fahrenheit + 459.67) / 1.8
                    print(f'Kelvin = {kelvin}')
                elif opcionS == '3':
                    ranquine = fahrenheit + 459.67
                    print(f'Ranquine = {ranquine}')
                else:
                    reaumur = (fahrenheit - 32) / 2.25
                    print(f'Reaumur = {reaumur}')
        elif opcion == '2':
            print('***CELSIUS***')
            celsius = float(input('Digite el valor en grados celsius: '))
            print(MENU_C)
            print('Elegir una opción: ')
            opcionS = input()
            if opcionS not in ('1234'):
                print('Opción inválida')
            else:
                if opcionS == '1':
                    fahrenheit = celsius * 1.8 + 32
                    print(f'Fahrenheit = {fahrenheit}')
                elif opcionS == '2':
                    kelvin = celsius + 273.15
                    print(f'Kelvin = {kelvin}')
                elif opcionS == '3':
                    ranquine = celsius + 1.8 + 32 + 459.67
                    print(f'Ranquine = {ranquine}')
                else:
                    reaumur = celsius * 0.8
                    print(f'Reaumur = {reaumur}')
        elif opcion == '3':
            print('***KELVIN***')
            kelvin = float(input('Digite el valor en grados kelvin: '))
            print(MENU_K)
            print('Elegir una opción: ')
            opcionS = input()
            if opcionS not in ('1234'):
                print('Opción inválida')
            else:
                if opcionS == '1':
                    fahrenheit = kelvin * 1.8 - 459.67
                    print(f'Fahrenheit = {fahrenheit}')
                elif opcionS == '2':
                    celsius = kelvin - 273.15
                    print(f'Celsius = {celsius}')
                elif opcionS == '3':
                    ranquine = kelvin * 1.8
                    print(f'Ranquine = {ranquine}')
                else:
                    reaumur = (kelvin - 273.15) * 0.8
                    print(f'Reaumur = {reaumur}')
        elif opcion == '4':
            print('***RANQUINE***')
            ranquine = float(input('Digite el valor en grados ranquine: '))
            print(MENU_RA)
            print('Elegir una opción: ')
            opcionS = input()
            if opcionS not in ('1234'):
                print('Opción inválida')
            else:
                if opcionS == '1':
                    fahrenheit = ranquine - 459.67
                    print(f'Fahrenheit = {fahrenheit}')
                elif opcionS == '2':
                    celsius = (ranquine - 32 - 459.67) / 1.8
                    print(f'Celsius = {celsius}')
                elif opcionS == '3':
                    kelvin = ranquine / 1.8
                    print(f'Kelvin = {kelvin}')
                else:
                    reaumur = (ranquine - 32 - 459.67) / 2.25
                    print(f'Reaumur = {reaumur}')
        elif opcion == '5':
            print('***REAUMUR**')
            reaumur = float(input('Digite el valor en grados ranquine: '))
            print(MENU_RE)
            print('Elegir una opción: ')
            opcionS = input()
            if opcionS not in ('1234'):
                print('Opción inválida')
            else:
                if opcionS == '1':
                    fahrenheit = reaumur * 2.25 + 32
                    print(f'Fahrenheit = {fahrenheit}')
                elif opcionS == '2':
                    celsius = reaumur * 1.25
                    print(f'Celsius = {celsius}')
                elif opcionS == '3':
                    kelvin = reaumur * 1.25 + 273.15
                    print(f'Kelvin = {kelvin}')
                else:
                    ranquine = reaumur * 2.25 + 32 + 459.67
                    print(f'Ranquine = {ranquine}')
        else:
            exit()