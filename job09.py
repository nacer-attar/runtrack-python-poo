class Student:
    def __init__(self, nom, prenom, id):
        self._nom = nom
        self._prenom = prenom
        self._id = id
        self._credits = 0
        self._level = self._studentEval()
    
    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def studentInfo(self):
        print("Nom :", self._nom)
        print("Prénom :", self._prenom)
        print("Identifiant :", self._id)
        print("Niveau :", self._level)
    
    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._studentEval()

# Instancier un objet représentant l’étudiant John Doe qui possède le numéro d’étudiant 145
john = Student("Doe", "John", 145)

# Ajouter des crédits à John
john.add_credits(30)
john.add_credits(40)
john.add_credits(20)

# Imprimer le total de crédits de John en console
print("Total de crédits de John :", john._credits)

# Afficher les informations de l'étudiant John Doe en console
john.studentInfo()
