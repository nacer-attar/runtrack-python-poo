class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def aire(self):
        return self.__longueur * self.__largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

# Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5
r = Rectangle(10, 5)

# Changer la valeur de la longueur et de la largeur
r.set_longueur(15)
r.set_largeur(8)

# Vérifier que les modifications soient bien prises en compte
print("Longueur :", r.get_longueur()) 
print("Largeur :", r.get_largeur()) 
print("Aire :", r.aire())
print("Périmètre :", r.perimetre())
