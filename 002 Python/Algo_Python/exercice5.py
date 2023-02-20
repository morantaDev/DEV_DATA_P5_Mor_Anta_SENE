
option=0
matrice=[]
tmp=[]
Choix=['Bleu', 'Rouge']
var=""
x=int(input("Entrer l'ordre de la matrice. Ce nombre doit être supérieur à 5\n"))


print("********* POSITION ***********\n")

print("Vous avez l'option:\n")
print("1. HAUT ")
print("2. BAS\n")
print("******************************\n")
position=int(input())

if x>5:
    if position==1:
        for i in range(x):
            for j in range(x):
                if i==j:
                    var=('....')
                elif i<j:
                    var=Choix[0]
                elif i>j:
                    var='....'
                tmp.append(var)
            matrice.append(tmp)
        
            tmp=[]
    elif position==2:
        for i in range(x):
            for j in range(x):
                if i==j:
                    var="\x1b[32;40m...."
                elif i<j:
                    var=Choix[1]
                elif i>j:
                    var='....'
                tmp.append(var)
            matrice.append(tmp)
        
            tmp=[]
else:
    print("Le nombre entré est inférieur à 5. Veuillez entrer un nombre supérieur à 5")

for i in matrice:
    for j in i:
        print(j, end=" \t")
    print("")
    
    

print("\x1b[32;40m....")

print("\x1b[1;38;5;226mBonjour")

print("\x1b[31;40mBonjour")

print("\x1b[34;40mBonjour")