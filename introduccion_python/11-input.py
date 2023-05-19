nombre = input('Cuál es tu nombre: \r\n')

print(f'Hola {nombre}')

#Leer datos que serán números
edad = input('Cual es tu edad?')
#convertir edad (string) a int
edad = int(edad)

if edad >= 18:
    print('Puedes votar')
else:
    print('No puedes votar')

#Mezclarlo con operadores
numero = input('Agrega un nuumero y te diré si es par o no \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'El número {numero} es par')
else: 
    print(f'El número {numero} es inpar')