#
with open('ejemplo.txt','w') as archivo: # este metodo abre el fichero "ejemplo.txt" y lo asocia a la variable  archivo
    #indicandole w porque vamos a escribir en el

    archivo.write('Este es un ejemplo de cómo escribir en un archivo en Python.\n')#aqui indicambos lo que queremos escribir en el archivo

    archivo.write('hola que tal')

f = open("ejemplo.txt", "r") #aqui llamamos al metodo open que creara un nuevo objeto que va a manipular el archivo

print(f.read())#leemos el objeto fichero y posteriormente se imprime
