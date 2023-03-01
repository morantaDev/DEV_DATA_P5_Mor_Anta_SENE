from dataclasses import dataclass


@dataclass
class etudiants:
    CODE : str
    Numero : str
    Prenom : str
    Classe : str
    Note : str
    
    #Les méthodes de étudiants
    
class etudiant(etudiants):
    pass
    

print(etudiant.CODE)
    
