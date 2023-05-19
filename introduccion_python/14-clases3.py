class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo 
        self.categoria = categoria 
        self.__precio = precio # Default: PUBLIC, PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.__precio}')

    #GETTERS AND SETTERS - GET = Obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio

#Instanciar la clase
restaurant = Restaurant('pizzeria Mexico', 'Comida mexicana', 50)
# restaurant.__precio = 80 #No será posible modificarlo con PRIVATE 
restaurant.mostrar_informacion()
restaurant.set_precio(80)
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesas Python', 'Comida casual', 20)
# restaurant2.__precio = 40 
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()
