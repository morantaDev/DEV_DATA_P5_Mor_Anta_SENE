def calcul_moy(a,b,c):
    moy=(a+b+c)/3
    return "%.2f"%(moy)

def tri_affiche(liste):
    tmp=[]
    for i in range(len(liste)-1):
        j=i+1
        if (liste[i][-1] > liste[j][-1]):
            tmp=liste[j]
            liste[j]=liste[i]
            liste[i]=tmp
    return liste[::-1]   
    

def recherche():
    pass

def modifier():
    pass

def compteur(Chaine):
    count = 0
    for i in range(len(Chaine)):
        count += 1
    return count


def Chaine():    
    text="""   Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus quibusdam odio laudantium ad delectus. Delectus culpa doloribus quis saepe similique placeat autem, temporibus perferendis. Rem non dolores nesciunt consequatur nostrum. Je vais au stade.
    
    """
    return text


def Cut_Up(text):
    sentence=[]
    ponct = [".","!","?"]
    word=""
    for i in text:
        word += i
        if i in ponct:
            sentence.append(word)
            word=""
        
    return sentence

def Verify(string):
    ponct=['.','?','!']
    return (string[0]>='A' and string[0]<='Z' and string[-1] in ponct)


#Check and delete special characters
def Check_delete(string):
    tabSpe=['#','~','-','/','\\','"','(']
    T=[]
    word=""
    for i in string:
        if i in tabSpe:
            continue
        else:
            word+=i
    T.append(word)
    return T

def Delete_Spaces_Next(string):
    text=""
    for i in range(len(string)):
        if not(string[i-1] in [' ','.'] and string[i]==' '):
            text+=string[i]
    return text


def Delete_Spaces(string):
    text=""
    for i in range(len(string)):
        if string[i] in [' ']:
            continue
        else:
            text+=string[i]
    return text


#fonction qui compte le nombre de caractères dans la chaîne
def Check_length(string):
    count = 0
    for i in string:
        count += 1
    return count



def decoupe1(text):
    word=""
    tab=[]
    for i in range(len(text)-1):
        word+=text[i]
        if text[i+1]==",":
            tab.append(word)
            word=""
            
    return tab



def last_num(chaine):
    ponct=[",","-","|","/","\n","\t"]
    word=""
    tab=[]
    reverse=chaine[::-1]
    for i in reverse:
        if i not in ponct:
            word+=i
        else:
            tab.append(word[::-1])
            word=""
            break
    return tab

def decoupe(chaine):
    ponct=[",","-","|","/","\n","\t"]
    word=""
    tab=[]
    for i in range(len(chaine)-1):
        if chaine[i] not in ponct:
            word+=chaine[i]
        else:
            tab.append(word)
            word=""
    return tab
    
    
def phone_numbers(string):
    second=['0','5','6','7','8']
    tab=[]
    word=""
    for chaine in string:
        if chaine[0]=='7' and chaine[1] in second and len(chaine)==9:
            tab.append(chaine)
        else:
            continue
        
    return tab    

def valid_numbers(string):
    tab=[]
    tab_inv=[]
    for item in string:
        if len(item)==9:
            tab.append(item)
        else:
            tab_inv.append(item)
    return tab


def myappend(liste, element):
    return liste + [element]



def input_control():
    etudiant=[]
    add=[]
    reponse=True


    while reponse==True:
        phone=str(input("Entrer le  numéro de téléphone:\n"))

        add.append(phone)
        n=str(input("Entrer le nom:\n"))
        add.append(n)
        pr=str(input("Entrer le prénom:\n"))
        add.append(pr)
        cl=str(input("Entrer la classe:\n"))
        add.append(cl)
        note_devoir=float(input("Entrer la note de devoir\n"))
        add.append(note_devoir)
        note_projet=float(input("Entrer la note de projet\n"))
        add.append(note_projet)
        note_examen=float(input("Entrer la note d'examen\n"))
        add.append(note_examen)
        moy=float(calcul_moy(note_devoir,note_examen,note_projet))
        add.append(moy)
        etudiant.append(add)
        x=int(input(("Entrer 1 pour continuer et 0 pour arrêter\n")))
        if x==0:
            break
        else:
            reponse==True
        add=[]
    return etudiant
            
def affiche():
    #tous les affichages doivent se faire sous forme de tableau
    tab_Menu=["Prénom","Nom","Téléphone","Classe","Dev","Proj","Exam","Moyenne"]
    pass



def Check_validNum(liste):
    second=['0','5','6','7','8']
    for i in range(len(liste)):
        return liste[0]=="7" and liste[1] in second and len(liste)==9
    
    
    
def menu():
    entete=["Prénom","nom","Téléphone","Classe","Dev","Proj","Exam","Moyenne"]