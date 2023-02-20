import csv
import Fonctions_veille



data=[]

with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv","r+") as fichier:

    monLecteur = csv.reader(fichier)
    
    for ligne in monLecteur:
        data.append(ligne)
        

#print(data)    


tabValid=[]
tabInValid=[]

prenom=Fonctions_veille.Check_prenom(test)


for sublist in range(len(data)-1):
    num=Fonctions_veille.check_Numero(data[sublist])
    #numéro valide
    if num==False:
        tabInValid.append(data[sublist])
    else:
        tabValid.append(data[sublist])
    #Nom valide
tabValid_Nom=[]
tabInValid_Nom=[]
for i in range (len(tabValid)-1):
    nom=Fonctions_veille.Check_Nom(tabValid[i])
    if nom==False:
        tabInValid_Nom.append(tabValid[i])
    else:
        tabValid_Nom.append(tabValid[i])
        
#print(tabInValid_Nom)

#prénom valide

tabValid_Prenom=[]
tabInValid_Prenom=[]

for i in range(len(tabValid_Nom)-1):
    prenom=Fonctions_veille.Check_prenom(tabValid_Nom[i])
    if prenom==False:
        tabInValid_Prenom.append(tabValid_Nom[i])
    else:
        tabValid_Prenom.append(tabValid_Nom[i])
        
#print(tabValid_Prenom)

#Date valide
tabValid_Date=[]
tabInValid_Date=[]

for i in range(len(tabValid_Prenom)-1):
    date=Fonctions_veille.Check_Date(tabValid_Prenom[i])
    if date==False:
        tabInValid_Date.append(tabValid_Prenom[i])
    else:
        tabValid_Date.append(tabValid_Prenom[i])
        
#print(tabValid_Date)

#classe valide

tabValid_classe=[]
tabInValid_classe=[]

for i in range(len(tabValid_Date)-1):
    classe=Fonctions_veille.Check_Classe(tabValid_Date[i])
    if classe==False:
        tabInValid_classe.append(tabValid_Date[i])
    else:
        tabValid_classe.append(tabValid_Date[i])
        
        
#print(tabInValid_classe)


#Note valide 

tabInValid_note=[]
tabValid_note=[]

for i in range(len(tabValid_classe)-1):
    note=Fonctions_veille.Check_Note(tabValid_classe[i])
    if note==False:
        tabInValid_note.append(tabValid_classe[i])
    else:
        tabValid_note.append(tabValid_classe[i])
        
#print(tabValid_note)


tableau_valide=tabValid_note
tableau_invalide=tabInValid_note


Fonctions_veille.menu(tableau_valide,tableau_invalide)

# num="M60GRTL"
# for item in tableau_valide:
#     try:
#         print(Fonctions_veille.Search(item,num))
#     except:
#         print("L'information recherchée n'existe pas.")



    

test=Fonctions_veille.tester()
    
    





# test=Fonctions_veille.tester()
# print(Fonctions_veille.Check_Note(test))


# num="20149LH"


# print(Fonctions_veille.check_Numero(test))

# num="20149LH"
# Fonctions_veille.Search(test,num)

#print(Fonctions_veille.Check_Note(test))

#print(Fonctions_veille.modify(test))




