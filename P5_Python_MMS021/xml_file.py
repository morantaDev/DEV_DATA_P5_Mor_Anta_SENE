import csv
import P5_StructuresDeDonnees.csv_to_json_and_xml as csv_to_json_and_xml

import P5_StructuresDeDonnees.function_json_xml as function_json_xml



data=[]
with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv") as fichier:
    csv_lecteur=csv.DictReader(fichier)
    
    for rows in csv_lecteur:
        data.append(rows)
        
        
        
    tabValid=[]
    tabInValid=[]
        
for i in data:
    if function_json_xml.check_Numero(i) and function_json_xml.Check_Nom(i) and function_json_xml.Check_prenom(i) and function_json_xml.Check_Classe(i) and function_json_xml.Check_Note(i):
        tabValid.append(i)
        
    else:
        tabInValid.append(i)
        
valide=[]
for i in tabValid:
    valide.append(function_json_xml.calcul(i))

#print(valide)

tri=sorted(valide, key=lambda x: x['Moyenne'], reverse=True)

print(tri)
        
        
fichier.close()

#CODE,Numero,Nom,Prénom,Date de naissance,Classe,Note

def convert_rows(dictio):
        return """<etudiant>
        <Numero id="%s">
            <Nom>%s</Nom>
            <Prénom>%s</Prénom>
            <Date_de_naissance>%s</Date_de_naissance>
            <Classe>%s</Classe>
        </Numero>
    </etudiant>
""" % (
    dictio['Numero'], dictio['Nom'], dictio['Prénom'], dictio['Date de naissance'],dictio['Classe'])

# print '\n'.join(fichier.apply(convert_rows, axis=1))

with open("xml_file.xml", "w") as xml_file:
    xml_file.write('\n'.join(convert_rows(dictio) for dictio in tabInValid))
    
    
    
    
    
    
    
# <!ELEMENT etudiant (Numero)>
# <!ELEMENT Numero (Nom, Prénom, Date_de_naissance, Classe, Note)>
# <!ELEMENT Nom (#PCDATA)>
# <!ELEMENT Prénom (#PCDATA)>
# <!ELEMENT Date_de_naissance (#PCDATA)>
# <!ELEMENT Classe (#PCDATA)>
# <!ELEMENT Note (#PCDATA)>
# <!ATTLIST Numero id CDATA #REQUIRED>






# <etudiant>
#     <Numero id="%s">
#         <Nom>%s</Nom>
#         <Prénom>%s</Prénom>
#         <Date_de_naissance>%s</Date_de_naissance>
#         <Classe>%s</Classe>
#         <Matiere>
            # <Math>%d</Math>
            # <svt>%d</svt>
            # <pc>%d</pc>
            # <Anglais>%d</Anglais>
            # <Francais>%d</Francais>
#         </Matiere>
#     </Numero>
# </etudiant>




