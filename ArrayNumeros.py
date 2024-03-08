#Crear un array con números y sumar sus valores

class SumadorArray:
    def __init__(self, array):
        self.array = array

    def sumar(self):
        suma = sum(self.array)
        return suma

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
sumador = SumadorArray(numeros)
resultado = sumador.sumar()
print("La suma de los números en el array es:", resultado)