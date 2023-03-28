class Rectangle:
    def __init__ (self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur 

    def perimetre (self):
        self.périmètre = self._longueur * 2 + self._largeur * 2
        return self.périmètre

    def surface (self):
        self.aire = self._longueur * self._largeur
        return self.aire
    
    ############ SET ET GET / LONGUEUR ET LARGEUR #########
    def setlongeur (self, longueur):
        self._longueur = longueur
        return self._longueur
    
    def getlongueur (self):
        return "la longueur est de" + " " + str(self._longueur)

    def setlargeur (self, largeur):
        self._largeur = largeur
        return self._largeur
    
    def getlargeur (self):
        return "la largeur est de" + " " + str(self._largeur)
    ############ SET ET GET / LONGUEUR ET LARGEUR #########

class Parallélépipède (Rectangle) :
    def __init__ (self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        self.volum = self.aire*self.hauteur
        return self.volum

#instanciation 
carre = Rectangle (5,5)

print (carre.getlongueur(),'\n',carre.getlargeur(),'\n',carre.perimetre(),'\n',carre.surface())

cube = Parallélépipède (5,5,5)

print (cube.getlongueur(),'\n',cube.getlargeur(),'\n',cube.perimetre(),'\n',cube.surface(),'\n',cube.volume())