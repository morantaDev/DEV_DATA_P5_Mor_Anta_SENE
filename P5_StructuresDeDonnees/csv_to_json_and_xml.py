import json
import csv
import function_json_xml

import xml.etree.ElementTree as ET

print()
print("Avec quel type de fichier souhaitez-vous travailler?")
print("Entrer:\n1 pour le csv\n2 pour le json\n3 pour le xml")
choix=int(input())


print()


data=[]

if choix==1:
    print("Afficher les valides sous format:")
    print("Entrer:\n1 pour le json\n2 pour le xml")
    format=int(input())

    if format==1:

        with open(" ",'r') as fichier:
            lecteur=csv.DictReader(fichier)
            for row in lecteur:
                data.append(row)
                
            valide=[]
            invalide=[]
            tabValid=[]
            tabInValid=[]

                
        for i in data:
            if function_json_xml.check_Numero(i) and function_json_xml.Check_Nom(i) and function_json_xml.Check_prenom(i) and function_json_xml.Check_Classe(i) and function_json_xml.Check_Note(i):
                tabValid.append(i)
                
            else:
                tabInValid.append(i)
                
                
        for i in tabValid:
            valide.append(function_json_xml.calcul(i))

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
            if function_json_xml.check_Numero(i) and function_json_xml.Check_Nom(i) and function_json_xml.Check_prenom(i) and function_json_xml.Check_Classe(i) and function_json_xml.Check_Note(i):
                tabValid.append(i)
                
            else:
                tabInValid.append(i)
                
                
        for i in tabValid:
            valide.append(function_json_xml.calcul(i))

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
            
#=============================================================================================    

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
            if function_json_xml.check_Numero(i) and function_json_xml.Check_Nom(i) and function_json_xml.Check_prenom(i) and function_json_xml.Check_Classe(i) and function_json_xml.Check_Note(i):
                tabValid.append(i)
            
        else:
            tabInValid.append(i)
        
        print(tabInValid) 
        valide=[]
        invalide=[]
        for i in tabValid:
            valide.append(function_json_xml.calcul(i))
            
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
    
        function_json_xml.convert_to_xml(invalide, "invalide.xml")      
    # csv_file.close()
        
    elif format==2:
        
        with open('json_database', 'r') as f:
            data=json.load(f)

        #Obtenir une liste de dictionnnaires
        for i in data:
            if function_json_xml.check_Numero(i) and function_json_xml.Check_Nom(i) and function_json_xml.Check_prenom(i) and function_json_xml.Check_Classe(i) and function_json_xml.Check_Note(i):
                tabValid.append(i)
            
            else:
                tabInValid.append(i)
        valide=[]
        invalide=[]
        for i in tabValid:
            valide.append(function_json_xml.calcul(i))
        
        for i in tabInValid:
            invalide.append(i)

        function_json_xml.convert_to_xml(valide, "Valide.xml")  
        data1=[]
        
        #Retourner un fichier csv pour les invalide
        entete = [i for i in invalide[0]]
        
        with open('data_csv.csv', 'w') as csv_file:
            csvfile = csv.writer(csv_file)
            csvfile.writerow(entete)
            
            for i in invalide:
                csvfile.writerow(i.values())
                
            csvfile.close()
         
#=====================================================================================
 
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
            if function_json_xml.check_Numero(i) and function_json_xml.Check_Nom(i) and function_json_xml.Check_prenom(i) and function_json_xml.Check_Classe(i) and function_json_xml.Check_Note(i):
                tabValid.append(i)
                
            else:
                tabInValid.append(i)
                    
                
        for i in tabValid:
            valide.append(function_json_xml.calcul(i))

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
    	
    	
    	
    	#############
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
        


else:
    print('Choix indisponible')





















        
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
    #     items['Numero'], items['Nom'], items['Prénom'], items['Date de naissance'],items['Classe'], items['Notes'])

    #         """etudiants = etree.Element("etudiants")
    #             etudiant = etree.SubElement(etudiants, "etudiant")
    #             etudiant.set('id', dict['Numero'])
    #             numero = etree.subElement(etudiant, "Numero")
    #             numero.text = dict['Numero']
    #             nom = etree.SubElement(etudiant, "Nom")
    #             nom.text = dict['Nom']
    #             prenom = etree.SubElement(etudiant, "Prénom")
    #             prenom.text = dict['Prénom']
    #             Classe = etree.SubElement(etudiant, "Classe")
    #             Classe.text = dict['Classe']
    #             Note = etree.SubElement(etudiant, "Note")data
    #             Note.text = dict['Note']
    #             print(etree.tostring(etudiants, pretty_print=True))
                
    #         """
    #     with open("xml_file.xml", "w") as xml_file:
    #         xml_file.write('\n'.join(convert_rows(dictio) for dictio in invalide))








        
# <eleve>
#     <CODE>ABD009</CODE>
#     <Numero>ZRDFD4S</Numero>
#     <Nom>Ndiareme</Nom>
#     <Prénom>Sylla</Prénom>
#     <Date_de_naissance>03/09/05</Date_de_naissance>
#     <Classe>3eme A</Classe>
#     <Matieres>
#         <Math>1.0 4.0 15.0 6.67</Math>
#         <Francais>0.0 19.0 8.0 10.0 9.25</Francais>
#         <Anglais>2.0 19.0 1.0 5.0 6.75</Anglais>
#         <PC>10.0 11.0 10.5</PC>
#         <SVT>10.0 20.0 16.0 10.0 9.0 13.0</SVT>
#         <HG>9.0 1.0 5.0</HG>
#     </Matieres>
#     <Moyenne>8.53</Moyenne>
# </eleve>
