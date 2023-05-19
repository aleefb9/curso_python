class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo 
        self.categoria = categoria 
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}')

#Instanciar la clase
restaurant = Restaurant('pizzeria Mexico', 'Comida mexicana', 50)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas Python', 'Comida casual', 20)
restaurant2.mostrar_informacion()
