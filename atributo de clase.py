class Estudiante:
    num_students=0

    def __init__(self): #inicializar el objeto
        Estudiante.num_students += 1 #para que cuente los objetos


s1=Estudiante()
s2=Estudiante()
s3=Estudiante()

print(Estudiante.num_students)