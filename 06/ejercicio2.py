class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        print(self.nombre)
        print(self.nota)

    def aprobado(self):
        msg = ("su nota es de " + str(self.nota) + " por lo tanto esta aprobado") if self.nota >= 6 else (
                    "su nota es de " + str(self.nota) + " por lo tanto esta desaprobado")
        print(msg)

a = Alumno("juan", 5)

a.__str__()
a.aprobado()