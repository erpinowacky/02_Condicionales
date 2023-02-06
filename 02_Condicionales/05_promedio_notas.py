'''Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  
Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0,
o mostrar "No aprobó" si su nota es menor a 3.0. '''

nota = 0.0
promedio = 0.0
notas = 0.0
contador = 0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***Promedio Notas***')
print('****************************')
print()
print('Digite -1 para terminar el programa')
while True:
    nota = float(input('Digite notas del estudiante: '))
    if (nota < 0 or nota > 5) and (nota != -1):
        print('Nota fuera de rango')
        continue
    elif nota == -1:
        break
    else:
        contador += 1 
        notas += nota
        promedio = notas / contador
if promedio >= 3.0:
    print(f'{promedio} Aprobó')
else:
    print(f'{promedio} No Aprobó')
print('Fin')