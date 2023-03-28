class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = km
        self.en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    def get_km(self):
        return self.km

    def set_km(self, km):
        self.km = km

    def get_en_marche(self):
        return self.en_marche

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def verifier_plein(self):
        if self.__reservoir > 5 :
            return True
        else : return False

    def demarrer(self):
        if self.verifier_plein() == True:
            self.en_marche = True
            print("La voiture a démarré!")
        else:
            print("Le réservoir est vide, impossible de démarrer la voiture.")

    def arreter(self):
        self.en_marche = False
        print("La voiture a été arrêtée.")

