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
        Personne.__init__ (self)

    def allerEnCours (self):
        print ('je vais en cours')

    def affichageAge (self):
        print (f"j'ai {self.age} ans")

class Professeur (Personne) :
    def __init__(self,_matiereEnseignee):
        Personne.__init__(self)
        self._matiereEnseignee = _matiereEnseignee

    def enseigner (self):
        print ("le cours va commencer")


prof = Professeur('histoire')
pion1 = Eleve()
pion1.bonjour()
pion1.allerEnCours()
pion1.modifierAge(15)
prof.modifierAge(40)
prof.bonjour()