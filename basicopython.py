print()


#calculadora con 4 metodos y parametros con enteros
#queremos usar type() para ver como python decide los tipos en base a los valores de inicializacion que le damos
#calculadora con 4 metodos y parametros con decimales

class calculadora:

    def suma(self,num1, num2):
        return num1 + num2

    def resta(num1, num2):
        return num1 - num2

    def multiplicacion(self,num1, num2):
        return num1 * num2

    def division(self,num1, num2):
        return num1 / num2
cal=calculadora()
cal2=calculadora()
print("Resultado:",cal.suma(2,4))
print("Resultado:",type(cal2.suma(2,4)))
print("Resultado:",cal.multiplicacion())

