'''Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC 
de una persona que se calcula con la fórmula IMC=P/T en donde P es el peso en Kg. y T es la talla en metros.
Lea un valor de P y de T, calcule el IMC y muestre su estado según la siguiente tabla:

| IMC | Estado |
| --- | --- |
| Menor a 18.5 | Desnutrido |
| [18.5, 25) | Normal |
| [25,30) | Sobrepeso |
| [30,35) | Obesidad Grado 1 |
| [35,40) | Obesidad Grado 2 |
| Mayor a 40 | Obesidad Grado 3 |'''

indiceMC = 0.0
peso = 0.0
talla = 0.0
from datetime import date
print('Fecha: ',end=' ')
hoy = date.today()
print(hoy,'\n')
print('***LOCAL***')
print('****************************')
print()
peso = float(input('Digite el peso en kilogramos (Kg): '))
talla = float(input('Digite su talla en metros (m): '))

indiceMC = peso / ((talla/100)**2)
print(f'Indice de Masa Corporal: {round(indiceMC,2)}')
if indiceMC < 18.5:
    print('Denustrido')
elif indiceMC >= 18.5 and indiceMC < 25.30:
    print('Normal')
elif indiceMC >= 25.30 and indiceMC < 30.35:
    print('Sobrepeso')
elif indiceMC >= 30.35 and indiceMC < 35.40:
    print('Obesidad Grado 1')
elif indiceMC >= 35.40 and indiceMC < 40:
    print('Obesidad Grado 2')
elif indiceMC > 40:
    print('Obesidad Grado 3')
