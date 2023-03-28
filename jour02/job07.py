import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        
class Jeu:
    couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
    valeurs = {'As': 1, 'Deux': 2, 'Trois': 3, 'Quatre': 4, 'Cinq': 5,
               'Six': 6, 'Sept': 7, 'Huit': 8, 'Neuf': 9, 'Dix': 10,
               'Valet': 10, 'Dame': 10, 'Roi': 10}
    
    def __init__(self):
        self.paquet = [Carte(v, c) for c in self.couleurs for v in self.valeurs]

    def melanger(self):
        random.shuffle(self.paquet)
        
    def donner_carte(self):
        return self.paquet.pop()
    
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        self.total = 0
        
    def ajouter_carte(self, carte):
        self.main.append(carte)
        self.total += Jeu.valeurs[carte.valeur]
        
    def afficher_main(self):
        print(f"Main de {self.nom}:")
        for carte in self.main:
            print(f"{carte.valeur} de {carte.couleur}")
        print(f"Total: {self.total}")
        
class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")
        
    def jouer(self):
        self.joueur.ajouter_carte(self.jeu.donner_carte())
        self.croupier.ajouter_carte(self.jeu.donner_carte())
        self.joueur.ajouter_carte(self.jeu.donner_carte())
        self.croupier.ajouter_carte(self.jeu.donner_carte(hidden=False))
        
        self.joueur.afficher_main()
        self.croupier.afficher_main()

        while self.joueur.total < 21:
            choix = input("Voulez-vous prendre une carte ? (o/n) ")
            if choix.lower() == "o":
                self.joueur.ajouter_carte(self.jeu.donner_carte())
                self.joueur.afficher_main()
            else:
                break

        while self.croupier.total < 17:
            self.croupier.ajouter_carte(self.jeu.donner_carte())
        self.croupier.afficher_main()

        if self.joueur.total > 21:
            print("Vous avez perdu.")
        elif self.croupier.total > 21:
            print("Le croupier a perdu.")
        elif self.joueur.total > self.croupier.total:
            print("Vous avez gagné !")
        elif self.joueur.total < self.croupier.total:
            print("Le croupier a gagné.")
        else:
            print("Égalité.")
        
blackjack = Blackjack()
blackjack.jouer()