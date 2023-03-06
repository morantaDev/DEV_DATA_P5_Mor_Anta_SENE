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


class Matiere:
    def __init__(self, tab):
        self.matiere = tab[0]
        self.devoir = tab[1:-1]
        self.examen = tab[-1]
        
        

m = etudiant('', '', '', '', '', '')


# note.ajout_note(m)
# print(m.__dict__)
# print(len(note.etudiant[0].date_de_naissance))

tableau = []
tabOb = []  
with open(csvfile, 'r') as csv_file:
    csvFile = csv.DictReader(csv_file)
    for row in csvFile:
        obj = etudiant(row['Numero'], row['Nom'], row['Prénom'], row['Date de naissance'], row['Classe'], row['Note'])     
        tabOb.append(obj)


split_note = []
split_final = []
tab = []
for ob in tabOb:
    #print(ob.date_de_naissance)
    #print(mesfonctions.valide_etudiant(ob.__dict__))
    #print(mesfonctions.Check_Classe(ob))
    split_note.append(ob.Notes.split("#"))
for item in split_note[0]:
    element=item.replace('[',':').replace(']',':').replace('|',':').replace(' ','').replace(',',':')
    element1 = element.split(":")
    #print(element1[0])
    del element1[-1]
    matiere = Matiere(element1)
    
    print(matiere.__dict__)
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    




    

    
