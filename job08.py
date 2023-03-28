class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un nombre entier positif.")
    
    def afficher(self):
        print(f"Livre : {self.__titre} - Auteur : {self.__auteur} - Nombre de pages : {self.__nb_pages}")
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")
    
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")
    
# Créer un livre avec les attributs initiaux
livre1 = Livre("1984", "George Orwell", 328)

# Vérifier si le livre est disponible
print(livre1.verification())

# Emprunter le livre
livre1.emprunter()

# Vérifier si le livre est disponible
print(livre1.verification())

# Rendre le livre
livre1.rendre()

# Vérifier si le livre est disponible
print(livre1.verification())
