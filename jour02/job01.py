class Personne:
    def __init__ (self):
        self.age = 14

    def afficherAge (self):
        print (self.age)
    
    def bonjour (self):
        print ('Hello')
    
    def modifierAge (self,age):
        self.age = age
        return self.age
    
class Eleve (Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours (self):
        print ('je vais en cours')

    def affichageAge (self):
        print (f"j'ai {self.age} ans")

class Professeur (Personne) :
    def __init__(self):
        self._matiereEnseignee = str

    def enseigner (self):
        print ("le cours va commencer")

prof=Professeur
pion1 = Eleve()
print (pion1.age)

