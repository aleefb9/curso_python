puntos = 0

pregunta1 = input('¿Te gusta python? \r\n')
if pregunta1 == 'SI':
    puntos += 1
    print(f'Puntos: {puntos}')
elif pregunta1 == 'NO':
    print('RESPUESTA INCORRECTA')
    print(f'Puntos: {puntos}')

pregunta2 = input('¿Debería de ser legal la pizza con piña? \r\n')
if pregunta2 == 'SI':
    print('RESPUESTA INCORRECTA')
    print(f'Puntos: {puntos}')
elif pregunta1 == 'NO':
    puntos += 1
    print(f'Puntos: {puntos}')

pregunta2 = input('¿El pantano es de Valverde? \r\n')
if pregunta2 == 'SI':
    print('RESPUESTA INCORRECTA')
    print(f'Puntos: {puntos}')
elif pregunta1 == 'NO':
    puntos += 1
    print(f'Puntos: {puntos}')

print(f'Puntos totales: {puntos}')