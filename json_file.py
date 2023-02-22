import json
import csv


def make_json(csvfile, jsonfile):
    data={}
    with open(csvfile) as fichier:
        reader=csv.DictReader(fichier)
        
        for lignes in reader:
            key = lignes['Numero']
            data[key] = lignes
            
    with open(jsonfile, "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

    return jsonFile
        
csvfile='/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv'
jsonfile='json_file'


print(make_json(csvfile,jsonfile))