import datetime
#from operator import itemgetter
def tester():

    liste = ['AAD003', '20149LH', 'CISSE', 'baba', '16 fev 99', '                   6ieme A', 'Math[11:10|13:06] #Francais[08|12:12] #Anglais[13|13:12] #PC[09|18:07] #SVT[15|10:10] #HG[11|14|19:17]']
    liste2 = [['AAD003', '20149LH', 'CISSE', 'baba', '16 fev 99', '6ieme A', 'Math[11:10|13:06] #Francais[08|12:12] #Anglais[13|13:12] #PC[09|18:07] #SVT[15|10:10] #HG[11|14|19:17]'],['AAD003', '20123LH', 'SARR', 'Ousmane', '13/12/97', '6ieme A', 'Math[11:10|17:06] #Francais[10|12:12] #Anglais[13|15:12] #PC[09|18:07] #SVT[15|11:10] #HG[10|14|12:16]']]
    return liste2
def is_lower(sublist):

    for i in sublist:
        if i>='a' and i<='z':
            return False 
    return True
 
def cpt_lettre(sublist):
     
            
    counter=0
    for i in sublist:
        if i.isalpha()==True:
            counter+=1
    return counter
def check_Numero(items):
    for  i in range(items['Numero']):
        return len(items['Numero'])==7 and (items['Numero'][i]).isalnum()==True and is_lower(items['Numero'])
    #verifier s'il y a une/+ lettre minuscule
def Check_Nom(sublist):
    for  i in range(len(sublist)-1):
        return sublist[2][0].isalpha()==True and cpt_lettre(sublist[2])>=2
def Check_prenom(sublist):
    for  i in range(len(sublist)-1):
        return cpt_lettre(sublist[3])>=3
def Check_Date(sublist):
    mois=0
    try:
        mois_en_chiffres = {'janvier': '01', 'fev': '02', 'février': '02', 'mars': '03', 'avril': '04', 'mai': '05', 'juin': '06', 'juillet': '07', 'août': '08', 'septembre': '09', 'octobre': '10', 'novembre': '11', 'décembre': '12'}
        sep=['/','-','_','|',' ',',',':']
        element=sublist[4].strip()
        for i in element:
            if i in sep:
                item=element.split(i)
        jour=int(item[0])
        if item[1].isdigit():
            mois=int(item[1])
        else:
            mois=mois_en_chiffres[item[1].lower()]
            mois=int(mois)
        if item[2].isdigit()==True and item[2] in '^(0?[0-9]|1[0-9]|2[0-3])$':
            item[2]='20'+i
                
        else:
            item[2]='19'+i
        annee=int(item[2])
        dt=datetime.datetime(annee, mois, jour)
        dt2=dt.strftime("%d/%m/%Y")
        return True
    except:
        return False
    
    
    #return dt2
def Check_Classe(sublist):
    element=sublist[5].strip()
    if len(element)!=0:
        return element[0] in ['3','4','5','6'] and element[-1] in ['A','B']
    else:
        return False

def Search(sublist,num):
    try:
        if sublist[1]==num:
            print(sublist)
    except ValueError:
            return None

def control_note(notes):
    for i in notes:
        if float(i)<=0 and float(i)>=20:
            return True
    return False
    
def Check_Note(sublist):
    tab=[]
    mat=[]
    subject=sublist[6].split('#')
    for i in range(len(subject)):
        item=subject[i].replace('[',':')
        item1=item.replace(']',':')
        item2=item1.replace('|',':')
        item3=item2.replace(' ','').replace(',',':')
        Split_2=item3.split(':')
        tab.append(Split_2)
        tab1=[]
        for item in tab:
            tab1.append(item[1:-1])
        mat.append(item[0])
        # print(mat)
        
        for item in tab1:
            for i in range(len(item)-1):
        #Convertir les éléments de chaque sous-liste en entier
                if item[i].isnumeric()==False:
                    return False 
                elif float(item[i])>0 and float(item[i])>20:
                    return False
    return True

def calcul(sublist):
    tab=[]
    mat=[]
    moyG=0
    subject=sublist[6].split('#')
    for i in range(len(subject)):
        item=subject[i].replace('[',':')
        item1=item.replace(']',':')
        item2=item1.replace('|',':')
        item3=item2.replace(' ','').replace(',',':')
        Split_2=item3.split(':')
        tab.append(Split_2)
        tab1=[]
        for item in tab:
            tab1.append(item[1:-1])
        mat.append(item[0])
        # print(mat)
        
        moyg=[]
        tab2=[]
        my_tuple=[]
        for item in tab1:
            newListe=[float(x) for x in item]
            if len(newListe) != 0:
                moyenne=sum(newListe)/len(newListe)
                moy=(moyenne+2*newListe[-1])/3
                moy="%.2f"%moy
                
                newListe.append(moy)
                moyg.append(moy)
                intMoy=[float(item) for item in moyg]
                moyG=sum(i for i in intMoy)/len(intMoy)
                #print(moyG)
    moyG=float("%.2f"%moyG)
    sublist.append(moyG)
        
    return sublist

#Ajouter une information en vérifiant la validité des informations données
def Ajouter():
    newElement=["CODE"]
    numero=str(input("Entrer le numéro de la personne a ajouter\n"))
    newElement.append(numero)
    nom=str(input("Entrer le nom de la personne à ajouter\n"))
    newElement.append(nom)
    prenom=str(input("Entrer le prénom de la personne a ajouter\n"))
    newElement.append(prenom)
    date=str(input("Entrer la date de la personne a ajouter\n")) 
    newElement.append(date)
    classe=str(input("Entrer la classe de la personne à ajouter\n"))
    newElement.append(classe)
    
    tabNote=[]
    note_math=[]
    math=int(input("Entrer la note de math:\n"))
    while control_note(math)==False:
        math=int(input("Entrer la note de math à nouveau:\n"))
    tabNote.append(math)
    note_math.append(note_math)
    
    note_franc=[]
    fr=int(input("Entrer la/les note de français:\n"))
    while control_note(fr)==False:
        fr=int(input("Entrer la/les note de français:\n"))
    tabNote.append(fr)
    note_franc.append(tabNote)
    
    note_ang=[]
    ang=int(input("Entrer la/les note d'anglais:\n"))
    while control_note(ang)==False:
        ang=int(input("Entrer la/les note d'anglais:\n"))
    note_ang.append(ang)
    tabNote.append(note_ang)
    
    note_pc=[]
    pc=int(input("Entrer la note de physique-Chimie:\n"))
    while control_note(pc)==False:
        pc=int(input("Entrer la note de physique-Chimie:\n"))
    note_pc.append(pc)
    tabNote.append(note_pc)
    
    note_svt=[]
    svt=int(input("Entrer la note de svt:\n"))
    while control_note(svt)==False:
        svt=int(input("Entrer la note de svt:\n"))
    note_svt.append(svt)
    tabNote.append(note_svt)
    
    note_hg=[]
    hg=int(input("Entrer la note d'histoire et de géographie:\n"))
    while control_note(hg)==False:
        hg=int(input("Entrer la note d'histoire et de géographie:\n"))
    note_hg.append(hg)
    tabNote.append(note_hg) 
    return newElement

def modify(listeValid,sublist):
    #Se positionner sur la chaîne cible et affecter l'ancienne valeur à la nouvelle
    print("1. Pour modifier le numéro")
    print("2. Pour modifier le nom")
    print("3. Pour modifier le prénom")
    print("4. Pour modifier la date de naissance")
    print("5. Pour modifier la classe")
    print("6. Pour modifier une note")
    to_modify=int(input("Choisir l'élément à modifier"))
    
    if to_modify==1:
        num=str(input("Entrer le nouveau numéro:"))
        if check_Numero(num)==True:
            sublist[1]=num 

    elif to_modify==2:
        nom=str(input("Entrer le nouveau nom"))
        if Check_Nom(nom)==True:
            sublist[2]=nom

    elif to_modify==3:
        prenom=str(input("Entrer le nouveau prénom"))
        if Check_prenom(prenom):
            sublist[3]=prenom
        
    elif to_modify==4:
        date=str(input("Entrer le nouveau nom"))
        if Check_Date(date)==True:
            sublist[4]=date

    elif to_modify==5:
        classe=str(input("Entrer le nouveau Classe"))
        if Check_Classe(classe):
            sublist[5]=classe
            
    elif to_modify==6:
        #modification de la note
        pass
    #il faut vérifier si tous les critères de validité et l'ajouter dans la liste des éléments valides
    listeValid.append(sublist)
        
    return listeValid


def affichage_pag(listeValid):
    reponse=1
    while reponse==1:
        for i in range(0,len(listeValid),5):
            pagin=listeValid[i:i+5]
        reponse=input("Entrer 1 pour continuer de paginer ou 0 pour arrêter\n")
        if reponse==0:
            break
        else:
            reponse==1
    return pagin

def affichage_pagin(listeValid,counter):
    reponse=1
    while reponse==1:
        for i in range(0,len(listeValid),counter):
            pagin=listeValid[i:i+counter]
        reponse=input("Entrer 1 pour continuer de paginer ou 0 pour arrêter\n")
        if reponse==0:
            break
        else:
            reponse==1
    return pagin
    


def affiche_tableau(donnees, entete):# Détermination de la largeur des colonnes
    largeurs = [max(len(str(donnees[i][j])) for i in range(len(donnees))) for j in range(len(entete))]

    # Affichage du tableau
    def print_ligne(ligne, debut="+", intersection="+", fin="+", separateur="-"):
        print(debut + separateur.join([separateur * largeurs[j]*2 for j in range(len(ligne))]) + fin)
        print(intersection + intersection.join("    {:^{}}  ".format(str(ligne[j]), largeurs[j]) for j in range(len(ligne))) +'\t  '+intersection)
        print(debut + separateur.join([separateur * largeurs[j]*2 for j in range(len(ligne))]) + fin)

    print_ligne(entete)
    print_ligne([], debut="+", intersection="+", fin="+", separateur="+")
    for ligne in donnees:
        print_ligne(ligne)
    
    return print_ligne      
    
    
def menu(listeValid, listeInvalid):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("----------MENU---------------MENU------------------------MENU----------------------MENU------------------")
    print("Que souhaitez-vous vous faire?")
    print("1. Afficher la liste des informations valides")
    print("2. Afficher la liste des informations invalides")
    print("3. Afficher une information par son numéro")
    print("4. Afficher les cinq premiers")
    print("5. ajouter une information en vérifiant la validité des informations données")
    print("6. Modifier une information invalide ensuite le transférer dans la structure où les informations valides")
    print("7. Affichage par pagination de 5 lignes")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    choix=int(input())
    try:
        if choix==1:
            print("Les informations valides sont:\n",listeValid)
        elif choix==2:
            print("Les informations invalides sont:\n",listeInvalid)
        elif choix==3:
            num=str(input("Entrer le numéro cible\n"))
            for item in listeValid:
                #print(Search(item,num))
                if item[1]==num:
                    print(item)
                else:
                    continue
        elif choix==4:
            pass
        elif choix==5:
            new=Ajouter()
            listeValid.append(new)
        elif choix==6:
            num=str(input("Entrer le numéro de l'information à modifier"))
            for item in listeInvalid:
                sublist=Search(item,num)
                print(sublist)
        print(modify(listeValid,sublist))
            
    except:
        print("Veuillez entrer une bonne valeur")


def affiche_cinqPremier(liste):
    tri=sorted(liste, key=lambda x: x[-1], reverse=True)
    
    return tri[1:6]


    

        
            
    
    
    
    
        
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    



