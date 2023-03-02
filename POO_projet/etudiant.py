from dataclasses import dataclass
import datetime
import xml.etree.ElementTree as ET
import csv
import json

@dataclass
class etudiant:
    CODE : str
    Numero : str
    Prenom : str
    Classe : str
    Note : str
    
    #Les méthodes de étudiant


def is_lower(sublist):

    for i in sublist:
        if i>='a' and i<='z':
            return False
    return True

def cpt_lettre(sublist):
    
            
    counter=0
    for i in sublist:
        if i.isalpha()==True:
            counter+=1
    return counter
def check_Numero(item):
    for  i in range(len(item['Numero'])-1):
        return len(item['Numero'])==7 and (item['Numero']).isalnum()==True and is_lower(item['Numero'])
def Check_Nom(item):
    for  i in range(len(item['Nom'])-1):
        return item['Nom'][0].isalpha()==True and cpt_lettre(item['Nom'])>=2
def Check_prenom(item):
    for  i in range(len(item)-1):
        return cpt_lettre(item['Prénom'])>=3
def Check_Date(new_item):
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
def Check_Classe(item):
    element=item['Classe'].strip()
    if len(element)!=0:
        return element[0] in ['3','4','5','6'] and element[-1] in ['A','B']
    else:
        return False

def Search(item,num):
    try:
        if item['Numero']==num:
            print(item)
    except ValueError:
            return None

def control_note(notes):
    for i in notes:
        if float(i)<=0 and float(i)>=20:
            return True
    return False
    
def Check_Note(item):
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

def calcul(subdict):
    tab=[]
    moyG=0
    element=subdict['Note']
    
    subject=element.split('#')
    for i in range(len(subject)):
        item3=subject[i].replace('[',':').replace(']',':').replace('|',':').replace(' ','').replace(',',':')
        Split_2=item3.split(':')
        tab.append(Split_2)
        
        subdict1={}
        
        for i  in tab:
            key=i[0]
            subdict1[key]=[float(x) for x in i[1:-1]]  
            #subdict1["Matière"]=subdict[key] 
            

            subdict['Matieres']=subdict1
            
    del subdict['Note']

    moy=[]
    som=0
    for items in subdict['Matieres'].items():
        #print(items[1])
        if len(items[1])!=0:
            for i in items[1]:
                moyG=sum(i for i in items[1])/len(items[1])
                moyG=float("%.2f"%moyG)
                
            moy.append(moyG)
            
        items[1].append(moyG)
        
    for i in moy:
        som+=i
    #som=float('%.2f'%som)
    moyenne=som/len(subdict['Matieres'])
    
    subdict['Moyenne']=float('%.2f'%moyenne)
        

    
            
    
    return subdict


    
def convert_to_dict_list(data, format):
    
    if format == 'xml' or "xml":
        root = ET.fromstring(data)
        result = []
        for child in root:
            d = {}
            for subchild in child:
                d[subchild.tag] = subchild.text
            result.append(d)
        return result
    # elif format == "yaml":
    #     return yaml.safe_load(data)
    elif format == "json":
        return json.loads(data)
    else:
        raise ValueError("Format invalide. Veuillez sélectionner 'xml', 'yaml' ou 'json'.")
    
    
def convert_to_xml(dic, filename):

    root = ET.Element("etudiants")




    for item in dic:

    
        etudiant = ET.SubElement(root, "etudiant")
        etudiant.attrib['id']= item['Numero']
        numero = ET.SubElement(etudiant, "Numero")
        numero.text = item['Numero']
        nom = ET.SubElement(etudiant, "Nom")
        nom.text = item['Nom']
        prenom = ET.SubElement(etudiant, "Prénom")
        prenom.text = item['Prénom']
        Classe = ET.SubElement(etudiant, "Classe")
        Classe.text = item['Classe']
        Note = ET.SubElement(etudiant, "Note")
        Note.text = item['Matieres']
        
        
    tree = ET.ElementTree(root)

    tree.write(filename, encoding="UTF-8", xml_declaration=True, method='xml')




    

        
            
    
print()
print("Avec quel type de fichier souhaitez-vous travailler?")
print("Entrer:\n1 pour le csv\n2 pour le json\n3 pour le xml")
choix=int(input())


print()


data=[]
# valide=[]
# invalide=[]
# tabValid=[]
# tabInValid=[]

















if choix==1:
    print("Afficher les valides sous format:")
    print("Entrer:\n1 pour le json\n2 pour le xml")
    format=int(input())

    if format==1:

        with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv",'r') as fichier:
            lecteur=csv.DictReader(fichier)
            for row in lecteur:
                data.append(row)
                
            valide=[]
            invalide=[]
            tabValid=[]
            tabInValid=[]

                
        for i in data:
            if check_Numero(i) and Check_Nom(i) and Check_prenom(i) and Check_Classe(i) and Check_Note(i):
                tabValid.append(i)
                
            else:
                tabInValid.append(i)
                
                
        for i in tabValid:
            valide.append(calcul(i))

        for j in tabInValid:
            invalide.append(j)
            

        tri=sorted(valide, key=lambda x: x['Moyenne'], reverse=True)

        with open("json_file", "w") as jsonFile:
            jsonFile.write(json.dumps(valide, indent=4, ensure_ascii=False))

        #Problème pour récuperer les notes de math, de Français...
        def convert_rows(items):
                return """<etudiant>
                <Numero id="%s">
                    <Nom>%s</Nom>
                    <Prénom>%s</Prénom>
                    <Date_de_naissance>%s</Date_de_naissance>
                    <Classe>%s</Classe>
                    <Note>%s</Note>
                </Numero>
            </etudiant>
        """ % (
            items['Numero'], items['Nom'], items['Prénom'], items['Date de naissance'],items['Classe'], items['Note'])

        with open("xml_file.xml", "w") as xml_file:
            xml_file.write('\n'.join(convert_rows(dictio) for dictio in tabInValid))

    elif format==2:
        #Problème pour récuperer les notes de math, de Français...
        
        with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv",'r') as fichier:
            lecteur=csv.DictReader(fichier)
            for row in lecteur:
                data.append(row)
                
            valide=[]
            invalide=[]
            tabValid=[]
            tabInValid=[]
                
        for i in data:
            if check_Numero(i) and Check_Nom(i) and Check_prenom(i) and Check_Classe(i) and Check_Note(i):
                tabValid.append(i)
                
            else:
                tabInValid.append(i)
                
                
        for i in tabValid:
            valide.append(calcul(i))

        for j in tabInValid:
            invalide.append(j)
        
        
        def convert_rows(items):
                return """<etudiant>
                <Numero id="%s">
                    <Nom>%s</Nom>
                    <Prénom>%s</Prénom>
                    <Date_de_naissance>%s</Date_de_naissance>
                    <Classe>%s</Classe>
                    <Note>%s</Note>
                </Numero>
            </etudiant>
        """ % (
            items['Numero'], items['Nom'], items['Prénom'], items['Date de naissance'],items['Classe'], items['Matieres'])

        with open("xml_file.xml", "w") as xml_file:
            xml_file.write('\n'.join(convert_rows(dictio) for dictio in valide))
        
        with open("json_file", "w") as json_File:
            json_File.write(json.dumps(invalide, indent=4, ensure_ascii=False))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

elif choix==2:
    print("Afficher les valides sous format:")
    print("Entrer:\n1 pour le csv\n2 pour le xml")
    format=int(input())
    valide=[]
    invalide=[]
    tabValid=[]
    tabInValid=[]
    if format==1:
        with open('json_database', 'r') as f:
            data=json.load(f)

        #Obtenir une liste de dictionnnaires
        for i in data:
            if check_Numero(i) and Check_Nom(i) and Check_prenom(i) and Check_Classe(i) and Check_Note(i):
                tabValid.append(i)
            
        else:
            tabInValid.append(i)
        
        print(tabInValid) 
        valide=[]
        invalide=[]
        for i in tabValid:
            valide.append(calcul(i))
            
        for i in tabInValid:
            invalide.append(i)
        
        #Conversion en csv
        #Récupèrer les entetes et les stockées dans la liste entete
        entete = [i for i in valide[0]]
   
        
        
        
        with open('data_csv.csv', 'w') as csv_data:
            csv_file = csv.writer(csv_data)
            
        #Parcourir entete et l'écrire dans le fichier csv
            csv_file.writerow(entete)
            
        #Parcourir la variable des données et l'écrire dans le fichier csv
            for i in valide:
                csv_file.writerow(i.values())
        
        
        #print(valide)
        
        # for i in tabInValid:
        #     invalide.append(i)
    
        #print(invalide)
    
        convert_to_xml(invalide, "invalide.xml")      
    # csv_file.close()
        
    elif format==2:
        
        with open('json_database', 'r') as f:
            data=json.load(f)

        #Obtenir une liste de dictionnnaires
        for i in data:
            if check_Numero(i) and Check_Nom(i) and Check_prenom(i) and Check_Classe(i) and Check_Note(i):
                tabValid.append(i)
            
            else:
                tabInValid.append(i)
        valide=[]
        invalide=[]
        for i in tabValid:
            valide.append(calcul(i))
        
        for i in tabInValid:
            invalide.append(i)
        
        #print(len(invalide))
        
    #     def convert_rows(items):
    #         return """<etudiant>
    #         <Numero id="%s">
    #             <Nom>%s</Nom>
    #             <Prénom>%s</Prénom>
    #             <Date_de_naissance>%s</Date_de_naissance>
    #             <Classe>%s</Classe>
    #             <Matieres>%s</Matieres>
    #         </Numero>
    #     </etudiant>
    # """ % (
    #     items['Numero'], items['Nom'], items['Prénom'], items['Date de naissance'],items['Classe'], items['Matieres'])

         
    #     with open("xml_file.xml", "w") as xml_file:
    #         xml_file.write('\n'.join(convert_rows(dictio) for dictio in valide))
    

        convert_to_xml(valide, "Valide.xml")  
        data1=[]
        
        #Retourner un fichier csv pour les invalide
        entete = [i for i in invalide[0]]
        
        with open('data_csv.csv', 'w') as csv_file:
            csvfile = csv.writer(csv_file)
            csvfile.writerow(entete)
            
            for i in invalide:
                csvfile.writerow(i.values())
                
            csvfile.close()
         
        
        
    
    
    
elif choix==3:
    print("Afficher les valides sous format:")
    print("Entrer:\n1 pour le csv\n2 pour le json")
    format=int(input())
    tree = ET.parse("xml_data.xml")
    root = tree.getroot()

    # Initialisation de la liste de dictionnaires
    data1 = []

    # Parcours des éléments "etudiant" du fichier XML
    for etudiant in root.findall("etudiant"):
        item = {}
        # Stockage de l'identifiant de l'étudiant dans le dictionnaire
        #item["id"] = etudiant.attrib["id"]
        # Parcours des éléments enfants de l'étudiant
        for child in etudiant:
            # Stockage des éléments enfants dans le dictionnaire
            item[child.tag] = child.text

        data1.append(item)

    # Affichage de la liste de dictionnaires
    print(data1)
    
    valide=[]
    invalide=[]
    tabValid=[]
    tabInValid=[]
    
    if format==1:
        for i in data1:
            if check_Numero(i) and Check_Nom(i) and Check_prenom(i) and Check_Classe(i) and Check_Note(i):
                tabValid.append(i)
                
            else:
                tabInValid.append(i)
                    
                
        for i in tabValid:
            valide.append(calcul(i))

        for j in tabInValid:
            invalide.append(j)
        
        print(len(valide))
        
        
        
        #Retourner un fichier csv pour les invalide
        entete = [i for i in valide[0]]
        
        with open('data_csv.csv', 'w') as csv_file:
            csvfile = csv.writer(csv_file)
            csvfile.writerow(entete)
            
            for i in invalide:
                csvfile.writerow(i.values())
                
            csvfile.close()
            
        with open("json_file.json", "w") as jsonfile:
            jsonfile.write(json.dumps(invalide, indent=4, ensure_ascii=False))
    


else:
    print('Choix indisponible')
    
    
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    




    

    
