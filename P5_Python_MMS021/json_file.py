import json
import csv
from projet_python import valide



mat=["Numero","Nom","Prenom","Date de naissance","Classe","Moyenne"]
dict={}


resultat=[]
for sublist in (valide):
    for j in range(len(sublist)):
        dict[mat[j]]=sublist[j]
        resultat.append(dict)

#Retourner une liste de dictionnaires   
#print(resultat)
   
# Afficher le JSON

with open("json_file", "w") as jsonFile:
    jsonFile.write(json.dumps(resultat, indent=4, ensure_ascii=False))







# "MN45LD5": {
#         "CODE": "ALT020",
#         "Numero": "MN45LD5",
#         "Nom": "SENGHOR",
#         "Prénom": "Mbegane",
#         "Date de naissance": "12/05/68",
#         "Classe": "4emeA",
#         "Note": "MATH[19|04:08]#SVT[12|05:16]#PC[07|13:09]#ANGLAIS[13|17:14]#FRANCAIS[19|17:11]#HG[15|11:12]#"
#     }


# "MN45LD5": {
#         "CODE": "ALT020",
#         "Numero": "MN45LD5",
#         "Nom": "SENGHOR",
#         "Prénom": "Mbegane",
#         "Date de naissance": "12/05/68",
#         "Classe": "4emeA",
#         "Matiere": [
        #       "MATH" : [19, 04, 08]
        #       "SVT" : [12, 05, 16]
        #       "PC" : [07, 13, 09]
        #       "ANGLAIS" : [13, 17, 14]
        #       "FRANCAIS" : [19, 17, 11]
        #       "HG"  : [15, 11, 12]
        #       ]
    # 

#     }