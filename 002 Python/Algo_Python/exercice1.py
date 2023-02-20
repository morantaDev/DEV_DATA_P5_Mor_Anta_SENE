tab = [["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aôut", "Septembre", "Octobre", "Novembre", "Décembre"],["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Décember"]]


i = 0
max_espace = 10
add = 0

#print("********************")
print("*********** MENU *************")
print("1. Taper 1 pour le Francais")
print("2. Taper 2 pour l'anglais ")
print("3. Taper 3 pour quitter")
print("******************************")

def compteur(Chaine):
    count = 0
    for i in range(len(Chaine)):
        count += 1
    return count

x = int(input())

#fonction pour compter le nombre de caractères

if x==1:
    #Affichage des mois en français
    print(max_espace*4*"_")
    print(end="|")
    for i in range(0,11,3):
    #print(end="|")
        x = compteur(tab[0][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[0][i]+add*' ', end="|")

    print(end="\n")


    print(max_espace*4*"_")
    print(end="|")
    for i in range(1,11,3):
    #print(end="|")
        x = compteur(tab[0][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[0][i]+add*' ', end="|")
    print(end="\n")

    print(max_espace*4*"_")
    print(end="|")
    for i in range(2,12,3):
    #print(end="|")
        x = compteur(tab[0][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[0][i]+add*' ', end="|")


    print(end="\n")
    print(max_espace*4*"_")

elif x==2:
#Tableau en englais

#Affichage des mois
    print(max_espace*4*"_")
    print(end="|")
    for i in range(0,11,3):
    #print(end="|")
        x = compteur(tab[1][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[1][i]+add*' ', end="|")

    print(end="\n")


    print(max_espace*4*"_")
    print(end="|")
    for i in range(1,11,3):
    #print(end="|")
        x = compteur(tab[1][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[1][i]+add*' ', end="|")
    print(end="\n")

    print(max_espace*4*"_")
    print(end="|")
    for i in range(2,12,3):
    #print(end="|")
        x = compteur(tab[1][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[1][i]+add*' ', end="|")


    print(end="\n")
    print(max_espace*4*"_")

elif x==3:
    exit()

else:
     #Affichage des mois en français
    print(max_espace*4*"_")
    print(end="|")
    for i in range(0,11,3):
    #print(end="|")
        x = compteur(tab[0][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[0][i]+add*' ', end="|")

    print(end="\n")


    print(max_espace*4*"_")
    print(end="|")
    for i in range(1,11,3):
    #print(end="|")
        x = compteur(tab[0][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[0][i]+add*' ', end="|")
    print(end="\n")

    print(max_espace*4*"_")
    print(end="|")
    for i in range(2,12,3):
    #print(end="|")
        x = compteur(tab[0][i])
        if x < max_espace:
            add = max_espace - x
            print(tab[0][i]+add*' ', end="|")


    print(end="\n")
    print(max_espace*4*"_")

