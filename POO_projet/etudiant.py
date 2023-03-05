import datetime
import xml.etree.ElementTree as ET
import json
import csv
import mesfonctions

csvfile ="/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv"

#@dataclass
class etudiant:                 #Many
    # CODE : str
    # Numero : str
    # Nom : str
    # Prenom : str
    # date_naiss : str
    # Classe : str  
    # note : str
    def __init__(self, Numero, Nom, Prenom, date_de_naissance, Classe, Notes):
        #self.CODE = CODE
        self.Numero = Numero
        self.Nom = Nom
        self.Prenom = Prenom
        self.date_de_naissance = date_de_naissance
        self.Classe = Classe
        self.Notes = Notes
    
    def ajouter_etudiant(self):
        self.etudiant = []
    


class Notes:                        #One 
    def __init__(self):
        #self.notes = notes
        self.etudiant = []
    
    def ajout_note(self, objet_etudiant):
        self.etudiant.append(objet_etudiant)
        
note = Notes()

m = etudiant('', '', '', '', '', '')


note.ajout_note(m)
print(m.__dict__)
print(len(note.etudiant[0].date_de_naissance))

tableau = []
tabOb = []  
with open(csvfile, 'r') as csv_file:
    csvFile = csv.DictReader(csv_file)
    for row in csvFile:
        obj = etudiant(row['Numero'], row['Nom'], row['Prénom'], row['Date de naissance'], row['Classe'], row['Note'])     
        tabOb.append(obj)



for ob in tabOb:
    #print(ob.date_de_naissance)
    #print(mesfonctions.valide_etudiant(ob.__dict__))
    print(mesfonctions.Check_Classe(ob))
    pass


        
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    




    

    
