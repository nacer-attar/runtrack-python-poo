class operation :
    def __init__(self) :
        self.nombre1=12
        self.nombre2=3
        self.somme = 0

    def addition(self):
        self.somme = self.nombre1 + self.nombre2
        return self.somme



nombre = operation()
nombre.addition()
print (f"la somme est {nombre.somme}")
