import json
import csv
import function_json


print()
print("Avec quel type de fichier souhaitez-vous travailler?")
print("Entrer:\n1 pour le csv\n2 pour le json\n3 pour le xml")
choix=int(input())
print()


data=[]
if choix==1:

    with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv",'r') as fichier:
        lecteur=csv.DictReader(fichier)
        for row in lecteur:
            data.append(row)
            
        tabValid=[]
        tabInValid=[]
            
    for i in data:
        if function_json.check_Numero(i) and function_json.Check_Nom(i) and function_json.Check_prenom(i) and function_json.Check_Classe(i) and function_json.Check_Note(i):
            tabValid.append(i)
            
        else:
            tabInValid.append(i)
            
    valide=[]
    invalide=[]
    for i in tabValid:
        valide.append(function_json.calcul(i))

    # for j in tabInValid:
    #     invalide.append(function_json.calcul(j))
        

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
        
elif choix==2:
    tabValid=[]
    tabInValid=[]
    with open('json_database', 'r') as f:
        data=json.load(f)
    
        for i in data:
            if function_json.check_Numero(i) and function_json.Check_Nom(i) and function_json.Check_prenom(i) and function_json.Check_Classe(i) and function_json.Check_Note(i):
                tabValid.append(i)
            
        else:
            tabInValid.append(i)
            
    valide=[]
    invalide=[]
    for i in tabValid:
        valide.append(function_json.calcul(i))
    #print(data)
    
    print(valide)
    
    for i in tabInValid:
        invalide.append(i)
    
    def convert_rows(items):
        return """<etudiant>
        <Numero id="%s">
            <Nom>%s</Nom>
            <Prénom>%s</Prénom>
            <Date_de_naissance>%s</Date_de_naissance>
            <Classe>%s</Classe>
            <Matieres>%s</Matieres>
        </Numero>
    </etudiant>
""" % (
    items['Numero'], items['Nom'], items['Prénom'], items['Date de naissance'],items['Classe'], items['Matieres'])

        """etudiants = etree.Element("etudiants")
            etudiant = etree.SubElement(etudiants, "etudiant")
            etudiant.set('id', dict['Numero'])
            numero = etree.subElement(etudiant, "Numero")
            numero.text = dict['Numero']
            nom = etree.SubElement(etudiant, "Nom")
            nom.text = dict['Nom']
            prenom = etree.SubElement(etudiant, "Prénom")
            prenom.text = dict['Prénom']
            Classe = etree.SubElement(etudiant, "Classe")
            Classe.text = dict['Classe']
            Note = etree.SubElement(etudiant, "Note")
            Note.text = dict['Note']
            print(etree.tostring(etudiants, pretty_print=True))
            
        """
    
    data1=[]
    with open("xml_file.xml", "w") as xml_file:
        xml_file.write('\n'.join(convert_rows(dictio) for dictio in valide))
    
    
    #Retourner un fichier csv pour les invalide
    
    with open('data_csv', 'w') as csv_file:
        csvfile = csv.writer(csv_file)
        
    for item in csvfile:
        data1.append(item)
        
    
    
    
elif choix==3:
    pass


else:
    print('Choix indisponible')





























        
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
