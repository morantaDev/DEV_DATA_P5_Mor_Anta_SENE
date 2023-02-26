import csv
import json



data=[]

with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv",'r') as fichier:
    lecteur=csv.DictReader(fichier)
    for row in lecteur:
        data.append(row)
        
        
with open('json_database','w') as f:
    f.write(json.dumps(data, indent=4, ensure_ascii=False))


def convertir(item):
    return"""<etudiant>
    <CODE>%s</CODE>
    <Numero>%s</Numero>
    <Nom>%s</Nom>
    <Prénom>%s</Prénom>
    <Date de naissance>%s</Date de naissance>
    <Classe>%s</Classe>
    <Note>%s</Note>
</etudiant>
"""%(item['CODE'],item['Numero'],item['Nom'],item['Prénom'],item['Date de naissance'],item['Classe'],item['Note'])
    
    
with open('xml_database', 'w') as m:
    m.write('\n'.join(convertir(item) for item in data))