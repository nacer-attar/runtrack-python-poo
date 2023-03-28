class Vehicule :
    def __init__ (self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix 

    def informationVehicule (self):
        return f'Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}'

    def demarrer (self):
        print ("attention je roule")

class Voiture (Vehicule):
    def __init__ (self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4

    def informationVehicule (self):
        return f'Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}\nPortes = {self.portes}'
    
    def demarrer (self):
        print ("LOOK AT THIS THE SPEEEEEED !")

class Moto (Vehicule):
    def __init__ (self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = 2

    def informationVehicule (self):
        return f'Marque = {self.marque}\nModèle = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}\nPortes = {self.roue}'

    def demarrer (self):
        print ("J'arrive en Y !")

y = Moto('Yamaha', '1200 Vmax', '1987', '4500')
gova = Voiture('Peugeot', '207', '2009', '5000')

print ("Info voiture : ")
print (gova.informationVehicule())
gova.demarrer()
print (" ")
print ("Info moto : ")
print (y.informationVehicule())
y.demarrer()