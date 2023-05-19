class Restaurant:

    def __init__(self, nombre):
        self.nombre = nombre # Atributo 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#Instanciar la clase
restaurant = Restaurant('pizzeria Mexico')
restaurant.agregar_restaurant()

restaurant2 = Restaurant('Hamburguesas Python')
restaurant2.agregar_restaurant()
