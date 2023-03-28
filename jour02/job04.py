class Forme:
    def aire ():
        return 0
    
class Rectangle (Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire (self):
        return self.hauteur * self.largeur
    
r=Rectangle(5,5)
print (r.aire())
