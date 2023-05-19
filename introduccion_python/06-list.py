lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

# Los arrays (lists) comienzan en la posición 0
print(lenguajes[0]) # python

#Ordenar los elementos 
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Modificando valores de un array
lenguajes[2] = 'PHP'

#Agregar elementos a un array
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar de un array
del lenguajes[1]
print(lenguajes)

#Eliminar ultimo elemento
lenguajes.pop()
print(lenguajes)

#Eliminar elemento específico
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)