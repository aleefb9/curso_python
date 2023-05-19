#ejemplo con elif
ocupacion = 'Estudiante'

if ocupacion == 'Estudiante': 
    print('Tienes 50% de Descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de Descuento')
elif ocupacion == 'Desempleado':
    print('Tienes un 10% de descuento')
else: 
    print('debes pagar el 100%')