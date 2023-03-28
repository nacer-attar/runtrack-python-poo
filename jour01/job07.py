class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
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

# Créer un livre avec les attributs initiaux
livre1 = Livre("1984", "George Orwell", 328)

# Modifier les attributs avec les mutateurs
livre1.set_titre("Animal Farm")
livre1.set_auteur("George Orwell")
livre1.set_nb_pages(150)

# Afficher les attributs avec les accesseurs
livre1.afficher()
