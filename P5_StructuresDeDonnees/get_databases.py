import csv
import json
# from xml.dom import minidom
# import os
import xml.etree.ElementTree as ET


data=[]

with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv",'r') as fichier:
    lecteur=csv.DictReader(fichier)
    for row in lecteur:
        data.append(row)
        
        
print(data)
        
        
# with open('json_database','w') as f:
#     f.write(json.dumps(data, indent=4, ensure_ascii=False))


# def convertir(item):
#     return"""<etudiant>
#     <CODE>%s</CODE>
#     <Numero>%s</Numero>
#     <Nom>%s</Nom>
#     <Prénom>%s</Prénom>
#     <Date de naissance>%s</Date de naissance>
#     <Classe>%s</Classe>
#     <Note>%s</Note>
# </etudiant>
# """%(item['CODE'],item['Numero'],item['Nom'],item['Prénom'],item['Date de naissance'],item['Classe'],item['Note'])
    
    
# with open('xml_database', 'w') as m:
#     m.write('\n'.join(convertir(item) for item in data))
    


# root = minidom.Document()
    
    
# for item in data:
#     xml = root.createElement('etudiants')
#     root.appendChild(xml)

#     etudiant = root.createElement('etudiant')
#     etudiant.setAttribute('id', item['Numero'])
    
#     xml.appendChild(etudiant)
    
#     code = root.createElement('CODE')
#     code.setAttribute("CODE", item['CODE'])
#     etudiant.appendChild(code)
    
#     xml_str = root.toprettyxml(indent="\t")
    
    
    
    
#     with open("xml_data.xml", 'w') as f:
#         f.write(xml_str)
    






def convert_to_xml(dic):

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
        Note.text = item['Note']
        
        
    tree = ET.ElementTree(root)

    tree.write("etudiant.xml", encoding="UTF-8", xml_declaration=True, method='xml') #indent=" "
    
    
convert_to_xml(data)

# ET.dump(root)