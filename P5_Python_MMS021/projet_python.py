import csv
import Fonctions_veille



data=[]

with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv","r+") as fichier:

    monLecteur = csv.reader(fichier)
    
    for ligne in monLecteur:
        data.append(ligne)
tabValid=[]
tabInValid=[]

# print(data)

for sublist in range(len(data)-1):
    num=Fonctions_veille.check_Numero(data[sublist])
    #numéro valide
    if num==False:
        tabInValid.append(data[sublist])
    else:
        tabValid.append(data[sublist])

print(len(tabInValid))  #1111111111

    #Nom valide
tabValid_Nom=[]
tabInValid_Nom=[]
for i in range (len(tabValid)-1):
    nom=Fonctions_veille.Check_Nom(tabValid[i])
    if nom==False:
        tabInValid.append(tabValid[i])
    else:
        tabValid_Nom.append(tabValid[i])
        
print(len(tabInValid))      #2222222222222222222222

#prénom valide

tabValid_Prenom=[]
tabInValid_Prenom=[]

for i in range(len(tabValid_Nom)-1):
    prenom=Fonctions_veille.Check_prenom(tabValid_Nom[i])
    if prenom==False:
        tabInValid.append(tabValid_Nom[i])
    else:
        tabValid_Prenom.append(tabValid_Nom[i])
        
print(len(tabInValid))      #33333333333333333333333

#Date valide
tabValid_Date=[]
tabInValid_Date=[]

for i in range(len(tabValid_Prenom)-1):
    date=Fonctions_veille.Check_Date(tabValid_Prenom[i])
    if date==False:
        tabInValid.append(tabValid_Prenom[i])
    else:
        tabValid_Date.append(tabValid_Prenom[i])

print(len(tabInValid))      #444444444444444444444

#classe valide
tabValid_classe=[]
tabInValid_classe=[]

for i in range(len(tabValid_Date)-1):
    classe=Fonctions_veille.Check_Classe(tabValid_Date[i])
    if classe==False:
        tabInValid.append(tabValid_Date[i])
    else:
        tabValid_classe.append(tabValid_Date[i])

print(len(tabInValid))             #55555555555555555

#Note valide 
tabInValid_note=[]
tabValid_note=[]

for i in range(len(tabValid_classe)-1):
    note=Fonctions_veille.Check_Note(tabValid_classe[i])
    if note==False:
        tabInValid_note.append(tabValid_classe[i])
    else:
        tabValid_note.append(tabValid_classe[i])
        
print(len(tabInValid))          #66666666666666666666666

tableau_valide=tabValid_note
tableau_invalide=tabInValid


print(len(tableau_valide))


# test=Fonctions_veille.tester()

#print(Fonctions_veille.cinq_premier(tableau_valide))

# #print(Fonctions_veille.n_premier(tableau_valide,2))



tableau_valide1=[]

for i in tableau_valide:
    tableau_valide1.append(Fonctions_veille.calcul(i)) 
    
#print(tableau_valide1[1])

valide=tableau_valide1

    
# print(tableau_valide1[5])

tableau_valide2=[]

for item in tableau_valide1:
    del item[0]
    del item[5]
    item[3]=item[3].strip()
    for i in range(len(item[4])):
        item[4]=item[4][0]+'eme'+item[4][-1]
        
    tableau_valide2.append(item)
    
#print(tableau_valide2)
    
entete1=["Numero", "Nom", "Prénom", "Date", "Classe", "Moyenne"]

#print(Fonctions_veille.affiche_tableau(tableau_valide1,entete1))


#cinq_premier=Fonctions_veille.affiche_cinqPremier(tableau_valide2)

#print(Fonctions_veille.affiche_tableau(cinq_premier,entete1))


Fonctions_veille.menu(tableau_valide, tableau_invalide)

fichier.close()