'''Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas
 (cuadrado, rectángulo, triángulo, círculo, rombo y trapecio).'''
 

PI = 3.1416
radio = 0.0
baseMayor = 0.0
baseMenor = 0.0
diagMayor = 0.0
diagMenor = 0.0
base = 0.0
altura = 0.0
lado = 0.0
area = 0.0
opcion = ''
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***ÁREAS***')
print('****************************')
print()
MENU = '''***MENÚ ÁREAS***
1. Cuádrado
2. Rectángulo
3. Triángulo
4. Círculo
5. Rombo
6. Trapecio
7. Fin'''
while True:
    print(MENU)
    opcion = input('Elegir una opción: ')
    if (opcion not in '123456') and opcion != '7':
        print('Número no válido')
        continue
    elif opcion == '7':
        print('Adiós')
        exit()
    else:
        if opcion == '1':
            print('***CUÁDRADO***')
            lado = float(input('Digite la base del triángulo: '))
            area = lado * lado
            print(f'El área del cuádrado es: {area}')
        elif opcion == '2':
            print('***RECTÁNGULO***')
            base = float(input('Digite la base del rectángulo: '))
            altura = float(input('Digite la altura del rectángulo: '))
            area = base * altura
            print(f'El área del rectángulo es: {area}')
        elif opcion == '3':
            print('***TRIÁNGULO***')
            base = float(input('Digite la base del triángulo: '))
            altura = float(input('Digite la altura del triángulo: '))
            area = (base * altura) / 2
            print(f'El área del triángulo es: {area}')
        elif opcion == '4':
            print('***CÍRCULO***')
            radio = float(input('Digite el radio del círculo: '))
            area = PI * radio**2
            print(f'El área del círculo es: {area}')
        elif opcion == '5':
            print('***ROMBO***')
            diagMayor = float(input('Digite la medida del diagonal mayor: '))
            diagMenor = float(input('Digite la medida del diagonal menor: '))
            area = (diagMayor * diagMenor) / 2 
            print(f'El área del rombo es: {area}')
        else:
            print('***TRAPECIO***')
            baseMayor = float(input('Digite la base mayor: '))
            baseMenor = float(input('Digite la base menor: '))
            altura = float(input('Digite la altura: '))
            area = ((baseMayor * baseMenor) / 2) * altura
            print(f'El área del trapecio es: {area}')

