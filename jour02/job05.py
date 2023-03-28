import math

class Forme:
    def aire ():
        return 0
    
class Cercle (Forme) : 
    def __init__(self,radius):
        self.radius = radius
    
    def aire(self):
        return math.pi * (self.radius) ** 2

class Rectangle (Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire (self):
        return self.hauteur * self.largeur
    
r=Rectangle(5,5)
c=Cercle(5)
print (c.aire())
print (r.aire())
