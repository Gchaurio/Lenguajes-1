import math

# Se implementa esta clase Vector3D donde se define un objeto con 3 atributos que representan cada coordenada.
# El problema se resolvio sobrecargando los metodos de la clase creada utilizando las funciones propias de la clase definida por el lenguaje
# que afecta la manera en la que los simbolos interactuan con los objetos de la clase.
class Vector3D:

    # Se define las coordenadas de un vector para el objeto Vector3D
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Suma
    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector3D(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError("Valores no manejables por el operador + para: '{}' y '{}'".format(type(self), type(other)))

    # Resta
    def __sub__(self, other):

        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):
            return Vector3D(self.x - other, self.y - other, self.z - other)
        else:
             raise TypeError("Valores no manejables por el operador - para: '{}' y '{}'".format(type(self), type(other)))

    # Producto Cruz
    def __mul__(self, other):

        if isinstance(other, Vector3D):
            return Vector3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
        elif isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Valores no manejables por el operador * para: '{}' y '{}'".format(type(self), type(other)))
    def __rmul__(self, other):
        return self * other

    # Producto punto
    def __mod__(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    
    # Norma (Para sacar la norma de un solo vector, se debe operar con si mismo)
    def __and__(self, other):
        return math.sqrt((self.x * other.x) + (self.y * other.y) + (self.z * other.z))
    
    # Funciones para expresar los valores en strings
    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def __repr__(self):
        return f"<{self.x}, {self.y}, {self.z}>"
    