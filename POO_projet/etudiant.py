import datetime
import xml.etree.ElementTree as ET
import json
import csv
import mesfonctions

csvfile ="/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv"


class etudiant:                 #Many
    def __init__(self, Numero, Nom, Prenom, date_de_naissance, Classe, Notes):
        #self.CODE = CODE
        self.Numero = Numero
        self.Nom = Nom
        self.Prenom = Prenom
        self.date_de_naissance = date_de_naissance
        self.Classe = Classe
        self.Notes = Notes
        self.Matiere = [Matiere]

class Matiere:
    def __init__(self, tab):
        self.matiere = tab[0]
        self.devoir = tab[1:-1]
        self.examen = tab[-1]
    
    def ajouter_note(self, MG):
        self.MG = MG
        self.MG.append(Matiere)
        

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
valide = []
tab = []
for ob in tabOb:
    
    if mesfonctions.valide_etudiant(ob) == True:
        valide.append(ob)
#print(len(valide))
#print(valide)
for i in valide:
    etu = i
    #print(etu.Notes)
    #print(etu)
    etu1=etu.Notes.split("#")
    #print(etu1)
    for item in etu1:
        #print(item)
        element=item.replace('[',':').replace(']',':').replace('|',':').replace(' ','').replace(',',':')
        element1 = element.split(":")
        #print(element1)
        try:
            if len(element1)!=0:
                del element1[-1]
                matiere = Matiere(element1)
                matiere.devoir=[float(x) for x in matiere.devoir]
                matiere.examen =float(matiere.examen)
                moy=((sum(matiere.devoir)/len(matiere.devoir))+2*matiere.examen)/3
                print(moy)
                print(matiere.__dict__)
                
        except:
            print("Les notes sont nulles")


    
    




    
    
    
    
    
    
    
    
    
    
    




    

    
