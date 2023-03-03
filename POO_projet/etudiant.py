import datetime
import xml.etree.ElementTree as ET
import json
import csv
from dataclasses import dataclass


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
    
    def calcul(self):
        pass
    


class Notes:                        #One 
    def __init__(self, notes):
        self.notes = notes
        self.etudiant = []
    
    def ajout_note(self, objet_etudiant):
        self.etudiant.append(objet_etudiant)
        
note = Notes("12")

m = etudiant('12345', 'SENE', 'Mor Anta', '21/09/2019', '4emeA', '20')

note.ajout_note(m)
type
print(note.__dict__)
print(note.etudiant[0].date_de_naissance)

#Récupèrer les données de bases

    
# data = "/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv"


    

class Convertisseur:
    def csv_dictList(csvfile):
        etudiants=[]
        with open(csvfile, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                etudiants.append(row)
            
        return etudiants
    
    def json_dictList(jsonfile):
        etudiants = []
        with open(jsonfile, 'r') as json_file:
            etudiants= json.load(json_file)
            
        return etudiants
    
    def xml_dictList(xmlfile):
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        etudiants=[]
        for elem in root:
            etudiant={}
            for child in elem:
                etudiant[child.tag] = child.text
            etudiants.append(etudiant)
            
        return etudiants
        
    # etudiants = []
    #     with open(csv_file, 'r') as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             etudiant = {}
    #             for key, value in row.items():
    #                 etudiant[key.strip()] = value.strip()
    #             etudiants.append(etudiant)
    #     return etudiants
    
    
    def json_dictList(jsonfile):
        with open(jsonfile, 'r') as jfile:
            etudiants = json.load(jfile)
            
        return etudiants
    
    def dictList_to_xml(dict, filename):
        
        root = ET.Element("etudiants")
        
        #Parcours du dictionnaire et ajouter les différents étudiants dans le fichier xml
        for item in dict:
            etudiant = ET.SubElement(root, "etudiant")
            code = ET.SubElement(etudiant, "CODE")
            code.text = item["CODE"]
            numero = ET.SubElement(etudiant, "Numero")
            numero.text = item["Numero"]
            nom = ET.SubElement(etudiant, "Nom")
            nom.text = item["Nom"]
            prenom = ET.SubElement(etudiant, "Prénom")
            prenom.text = item["Nom"]
            date_de_naiss = ET.SubElement(etudiant, "Date de naissance")
            date_de_naiss.text = item["Date de naissance"]
            note = ET.SubElement(etudiant, "Notes")
            note.text = item["Notes"]
        
        tree = ET.ElementTree(root)
        
        result = tree.write(filename, encoding="UTF-8", xml_declaration=True, method = "xml")
        
        return  result
    
    def dictList_to_json(self, dictList, filename):
        with open(filename, "w") as jsonfile:
            jsonfile.write(json.dumps(dictList))

            
    def dictList_to_csv(dictList):
        header = []
        for item in dictList[0]:
            header.append(item)
        
        with open("csvfile", "w") as csvfile:
            csv_file = csv.writer(csvfile)

            csv_file.writerow(header)
            
            for item in dictList.values():
                csv_file.writerows(item)
        
            
            

csvfile = "/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv"
jsonfile = "/home/moranta/DEV_DATA_P5_Mor_Anta_SENE/POO_projet/json_database.json"
xmlfile = "/home/moranta/DEV_DATA_P5_Mor_Anta_SENE/POO_projet/xml_data.xml"

#print(Convertisseur.json_dictList(jsonfile))
    
class validateur(Convertisseur):
    def is_lower(self, item):
        for i in item:
            if i>='a' and i<='z':
                return False
        return True
 
    def cpt_lettre(self, item):     
        counter=0
        for i in item:
            if i.isalpha()==True:
                counter+=1
        return counter
    def check_Numero(self, item):
        for  i in range(len(item['Numero'])-1):
            return len(item['Numero'])==7 and (item['Numero']).isalnum()==True and item.is_lower(self['Numero'])
    def Check_Nom(self, item):
        for  i in range(len(item['Nom'])-1):
            return item['Nom'][0].isalpha()==True and item.cpt_lettre(item['Nom'])>=2
    def Check_prenom(self, item):
        for  i in range(len(item)-1):
            return item.cpt_lettre(item['Prénom'])>=3
    def Check_Date(self, new_item):
        mois=0
        try:
            mois_en_chiffres = {'janvier': '01', 'fev': '02', 'février': '02', 'mars': '03', 'avril': '04', 'mai': '05', 'juin': '06', 'juillet': '07', 'août': '08', 'septembre': '09', 'octobre': '10', 'novembre': '11', 'décembre': '12'}
            sep=['/','-','_','|',' ',',',':']
            element=new_item['Date de naissance'].strip()
            for i in element:
                if i in sep:
                    item=element.split(i)
            jour=int(item[0])
            if item[1].isdigit():
                mois=int(item[1])
            else:
                mois=mois_en_chiffres[item[1].lower()]
                mois=int(mois)
            if item[2].isdigit()==True and item[2] in '^(0?[0-9]|1[0-9]|2[0-3])$':
                item[2]='20'+i
                    
            else:
                item[2]='19'+i
            annee=int(item[2])
            dt=datetime.datetime(annee, mois, jour)
            dt2=dt.strftime("%d/%m/%Y")
            return True
        except:
            return False
        
        
        
        #return dt2
    def Check_Classe(self, item):
        element=item['Classe'].strip()
        if len(element)!=0:
            return element[0] in ['3','4','5','6'] and element[-1] in ['A','B']
        else:
            return False

    def Search(self, item, num):
        try:
            if item['Numero']==num:
                print(item)
        except ValueError:
                return None

    def control_note(self, item):
        for i in item:
            if float(i)<=0 and float(i)>=20:
                return True
        return False
        
    def Check_Note(self, item):
        tab=[]
        mat=[]
        subject=item['Note'].split('#')
        for i in range(len(subject)):
            item=subject[i].replace('[',':')
            item1=item.replace(']',':')
            item2=item1.replace('|',':')
            item3=item2.replace(' ','').replace(',',':')
            Split_2=item3.split(':')
            tab.append(Split_2)
            tab1=[]
            for item in tab:
                tab1.append(item[1:-1])
            mat.append(item[0])
            # print(mat)
            
            for item in tab1:
                for i in range(len(item)-1):
            #Convertir les éléments de chaque sous-liste en entier
                    if item[i].isnumeric()==False:
                        return False 
                    elif float(item[i])>0 and float(item[i])>20:
                        return False
        return True
    
    
    def valide_etudiant(etudiant):
        return(
            validateur.check_Numero(etudiant) and 
            validateur.Check_Nom(etudiant) and 
            validateur.Check_prenom(etudiant) and
            validateur.Check_Date(etudiant) and
            validateur.Check_Classe(etudiant) and
            validateur.Check_Note(etudiant)
        )
        



# @dataclass
# class note(etudiant):
#     matiere : list
    
    
#     def calcul(subdict):
#         tab=[]
#         moyG=0
#         element=subdict['Note']
        
#         subject=element.split('#')
#         for i in range(len(subject)):
#             item3=subject[i].replace('[',':').replace(']',':').replace('|',':').replace(' ','').replace(',',':')
#             Split_2=item3.split(':')
#             tab.append(Split_2)
            
#             subdict1={}
            
#             for i  in tab:
#                 key=i[0]
#                 subdict1[key]=[float(x) for x in i[1:-1]]  
#                 #subdict1["Matière"]=subdict[key] 
                

#                 subdict['Matieres']=subdict1
                
#         del subdict['Note']

#         moy=[]
#         som=0
#         for items in subdict['Matieres'].items():
#             #print(items[1])
#             if len(items[1])!=0:
#                 for i in items[1]:
#                     moyG=sum(i for i in items[1])/len(items[1])
#                     moyG=float("%.2f"%moyG)
                    
#                 moy.append(moyG)
                
#             items[1].append(moyG)
            
#         for i in moy:
#             som+=i
#         #som=float('%.2f'%som)
#         moyenne=som/len(subdict['Matieres'])
        
#         subdict['Moyenne']=float('%.2f'%moyenne)
        

        
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    




    

    
