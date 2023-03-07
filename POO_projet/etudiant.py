import datetime
import xml.etree.ElementTree as ET
import json
import csv
import mesfonctions

csvfile ="/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv"


class etudiant:                 #Many
    def __init__(self, CODE, Numero, Nom, Prenom, date_de_naissance, Classe, Notes):
        self.CODE = CODE
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
        

m = etudiant('', '', '', '', '', '', '')


tableau = []
tabOb = []  
with open(csvfile, 'r') as csv_file:
    csvFile = csv.DictReader(csv_file)
    for row in csvFile:
        obj = etudiant(row['CODE'],row['Numero'], row['Nom'], row['Prénom'], row['Date de naissance'], row['Classe'], row['Note'])     
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
                # print(moy)
                # matiere.ajouter_note(moy)
                #matiere.update({'moyenne':moy})
                #ajouter la moyenne dans la classe Matiere
                # matiere.moyenne=float('%.2f'%moy)
                # print(vars(matiere))
                
                
                
        except:
            print("Les notes sont nulles")



    print(vars(etu))
    print()
    
    
#Convertir le fichier csv en json

# def dictList_to_json(filename, dict):
#     with open(filename, "w") as jsonfile:
#         jsonfile.write(json.dump(dict))

# dictList_to_json('jsonfile', etu.__dict__)


#Convertir un fichier csv en xml


def dictList_to_xml(dict, filename):

    root = ET.Element("etudiants")

    #Parcours du dictionnaire et ajouter les différents étudiants dans le fichier xml
    
    etudiant = ET.SubElement(root, "etudiant")
    code = ET.SubElement(etudiant, "CODE")
    code.text = dict.CODE
    numero = ET.SubElement(etudiant, "Numero")
    numero.text = dict.Numero
    nom = ET.SubElement(etudiant, "Nom")
    nom.text = dict.Nom
    prenom = ET.SubElement(etudiant, "Prénom")
    prenom.text = dict.Prenom
    date_de_naiss = ET.SubElement(etudiant, "Date de naissance")
    date_de_naiss.text = dict.date_de_naissance
    note = ET.SubElement(etudiant, "Notes")
    note.text = dict.Notes
    # matiere = ET.SubElement(etudiant, "Matiere")
    # matiere.text = dict.Matiere

    tree = ET.ElementTree(root)

    result = tree.write(filename, encoding="UTF-8", xml_declaration=True, method = "xml")

    return  result


for i in valide:

    dictList_to_xml(i,'xmlfile')

    
    
    
    
    
    
    
    
    
    




    

    
