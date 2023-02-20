import mesFonctions
import os

def Suite_operateur():
    suite="""Orange,Tigo,Expresso,Promobile"""
    return suite


def identifi_oper(info):
    #si le numéro commence par 77 et compte 9 chiffres alors -> il est de orange
    for  item in range(len(info)):
        if info[2][0][0]=='7' and info[2][0][1]=='7' or info[2][0][1]=='8':
            operateur=='Orange'
        elif info[2][0][0]=='7' and info[2][0][1]=='6':
            operateur=='Tigo'
        elif info[2][0][0]=='7' and info[2][0][1]=='0':
            operateur=='Expresso'
        elif info[2][0][0]=='7' and info[2][0][0]=='5':
            operateur=='Promobile'
    return operateur



liste_Operateur=[]
tab_Num=[]
liste_client=[]
matrice=[]
word=""
#Saisir une suite d'opérateurs où ligne=nombre opérateurs saisies
#operateurs=str(input("Entrer la suite des opérateurs possibles"))

operateurs=Suite_operateur()
print(operateurs)


            
operateur=mesFonctions.decoupe(operateurs)
print(operateur)
liste_Operateur.append(operateur)
#print(liste_Operateur)

#chaque élément de la liste d'opérateurs est une liste


#Calculer la taille de la liste d'opérateur 
taille=mesFonctions.compteur(operateur)
print(taille)

for i in range(taille):
    matrice.append([])
    
print(matrice)

#Saisir les informations(nom, prénom, numéro) d'1 client et ranger dans ligne opérateur correspondant
def Saisie_info():
    info=[]
    tabNum=[]
    nom=str(input("Entrer le nom du client\n"))
    info.append(nom)
    prenom=str(input("Entrer le prénom du client\n"))
    info.append(prenom)
    numero=str(input("Entrer le numéro de téléphone du client\n"))
    num=mesFonctions.Check_validNum(numero)
    # op=operateur(numero)
    # if op=='Orange' or op=='orange':
    #     matrice[0].append()
    if num==True:
        tabNum.append(numero)
        info.append(tabNum)
    else:
        os.system('clear')

#liste_client=[nom, prenom, [numéro]]
    return info

inf=Saisie_info()
print(inf)


def affiche_clientOp():
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            
            if matrice[i][0]=='Orange':
                print(matrice[i][j])
                print("--------------------")
            if matrice[i][0]=='Tigo':
                print(matrice[i][j])
            
            if matrice[i][0]=='Expresso':
                print(matrice[i][j])
            
            if matrice[i][0]=='Kirene':
                print(matrice[i][j])

#Afficher les numéros téléphone d'un client
def affiche_num():
    pass

#Modifier ou ajouter un numéro de téléphone pour un client
def modifier_Num():
    pass

def ajouter_Num():
    pass

#Lorsque l'utilisateur quitte le programme, les données sont enregistrées dans un fichier texte
