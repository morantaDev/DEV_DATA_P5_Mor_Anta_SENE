import mesFonctions


def liste():
    L=[['771234567', 'sene', 'mor anta', 'licence', 12.0, 13.0, 14.0, 13.0], ['78123456', 'sarr', 'mbaye', 'licence', 14.0, 13.0, 11.0, 13.67], ['782191001', 'diouf', 'saliou', 'licence1', 10.0, 10.0, 10.0, 13.10]]
    # for i,value in enumerate(L):
    #     print(i,value)
    return L

appel=liste()
tri=mesFonctions.tri_affiche(appel)   
print(tri)
#function de controle de numero    
for i in range(len(appel)):
    
    if(mesFonctions.Check_validNum(appel[i][0]))==True:
        print("Le numéro entré est valide")
    else:
        print("Le numéro entré est invalide")

#function qui controle le nom
#qui controle les notes et la moyenne

note=22
def intInput_control(integer):
    if 0>integer>20:
        print("entrer un entier compris entre 0 et 20\n")
    else:
        print("le nombre entré est la bonne")
intInput_control(note)
#function qui tri dans l'ordre décroissant              Fait
#function qui recherche selon un critère donné
def recherche(liste):
    print("Ci dessous vous entrez le critère de recherche")
    print("Vous avez les options suivantes:\n")
    print("1. Recherche par téléphone")
    print("2. Recherche par nom")
    print("3. Recherche par prénom")
    print("4. Recherche par classe")
    critere=int(input())
    if critere==1:
        print("Vous avez choisi l'option recherche par téléphone")
        tel=str(input("Entrer le numéro cible\n"))
        #Verifier si le numéro existe dans la liste de données
        def if_Exist_Num(liste):
            for i in range(len(liste)):
                return liste[0]==tel
        # if_Exist(liste)
        for i in liste:
            if (if_Exist_Num(i)==True):
                print("Le numéro entré existe dans la liste",i)
                break
        #On doit retourner la liste auquel le numéro appartient
            else:
                continue
        #Si oui, retourner le la liste  cible
        #Sinon, écrire "aucune réponse trouvé"
    if critere==2:
        print("Vous avez choisi l'option recherche par nom")
        nom=str(input("Entrer le nom\n"))
        #Verifier si le nom existe dans la liste de données
        def if_Exist_Name(liste):
            for i in range(len(liste)):
                return liste[1]==nom
        #Si oui, retourner le la liste  cible
        for i in liste:
            if(if_Exist_Name(i))==True:
                print("Le nom entré existe dans la liste",i)
        #Sinon, écrire "aucune réponse trouvé"
            else:
                continue
    if critere==3:
        print("Vous avez choisi l'option recherche par prénom")
        prenom=str(input("Entrer le prénom cible"))
        #Verifier si le prénom existe dans la base de données
        def if_Exist_First(liste):
            for i in range(len(liste)):
                return liste[2]==prenom
        # if_Exist(liste)
        for i in liste:
            if (if_Exist_First(i)==True):
                print("Le numéro entré existe dans la liste",i)
                break
        #On doit retourner la liste auquel le numéro appartient
            else:
                continue
        #Si oui, retourner le la liste  cible
        #Sinon, écrire "aucune réponse trouvé"
    if critere==4:
        print("Vous avez choisi l'option recherche par classe")
        classe=str(input("Entrer la classe cible\n"))
        #Verifier si la classe existe dans la base de données
        def if_Exist_Class(liste):
            for i in range(len(liste)):
                return liste[3]==classe
        # if_Exist(liste)
        for i in liste:
            if (if_Exist_Class(i)==True):
                print("Le numéro entré existe dans la liste",i)
                break
        #On doit retourner la liste auquel le numéro appartient
            else:
                continue
        #Si oui, retourner le la liste  cible
        #Sinon, écrire "aucune réponse trouvé"

#function de modification de notes pour un étudiant

def modification(liste):
    print("Choisir la note à modifier:\n")
    print("1. Note devoir")
    print("2. Note projet")
    print("3. Note examen")
    entree=int(input())
    if entree==1:
        tel=str(input("Entrer le numéro de l'étudiant concerné\n"))
        for i in range(len(liste)-1):
            if liste[i][0]==tel:
                new_note=float(input("Entrer la nouvelle note:\n"))
                liste[i][4]=new_note
    elif entree==2:
        tel=str(input("Entrer le numéro de l'étudiant concerné\n"))
        for i in range(len(liste)-1):
            if liste[i][0]==tel:
                new_note=float(input("Entrer le nouvelle note:\n"))
                liste[i][5]=new_note
    elif entree==3:
        tel=str(input("Entrer le numéro de l'étudiant concerné\n"))
        for i in range(len(liste)-1):
            if liste[i][0]==tel:
                new_note=float(input("Entrer la nouvelle note:\n"))
                liste[i][6]=new_note
    else:
        print("Choix indisponible")
            
    return liste
                


#une fonction qui définit l'unicité des numéros pour chaque étudiant
def Unicite(liste, numero):
    for i in range(len(liste)-1):
        if liste[0]==numero:
            print("Ce numéro existe déja dans la liste")
            break
        
def sortir():
    pass


#recherche(appel)
print(modification(appel))




with open("student.txt",'w') as fichier:
    for item in appel:
        for subitem in item:
            fichier.write(f"{subitem}"+"\n")    #utiliser des chaînes formater
fichier.close()
























