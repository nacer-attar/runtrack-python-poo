class Animal:
    def __init__ (self):
        self.age = 0
        self.prenom = ' '

    def vieillir (self):
        self.age = self.age + 1
        return self.age
    
    def nommer (self,prenom):
        self.prenom = prenom
        return self.prenom

animal=Animal()
print (f"l'age de l'animal est {animal.age}")
animal.vieillir()
print (f"l'age de l'animal est {animal.age}")
animal.nommer('bobby')
print (f"l'animal se nomme {animal.prenom}")

