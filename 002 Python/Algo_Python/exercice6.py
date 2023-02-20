matrice=[]
tab_color=["Vert","Jaune","Rouge","Bleu"]
tab_position=['ADDS','EDDP','SDP','ADDS','EDDS','SDS']
tmp=""
l_tmp=[]

print("\nChoisir la position:\n")
print("1. Au dessus de la diagonale principale")
print("2. En dessous de la diagonale principale")
print("3. Sur la diagonale principale")
print("4. Au dessus de la diagonale secondaire")
print("5. En dessous de la diagonale secondaire")
print("6. Sur la diagonale seconde")
position=int(input())

print("Choisir la couleur\n")
print("1. Vert")
print("2. Jaune")
print("3. Rouge")
print("4. Bleu")
color=int(input())
taille=int(input("Entrer la taille de la matrice\n"))

#Diagonale principale, dessus, dessous 
if position==3:
    for i in range(taille):
        for j in range(taille):
        #Diagonale principale
            if i==j:
                tmp=tab_color[color]
        #ADDP
            elif i>j:
                tmp="..."
        #EDDP
            else:
                tmp="..."
            l_tmp.append(tmp)
        matrice.append(l_tmp)
        
elif position==2:
    for i in range(taille):
        for j in range(taille):
        #Diagonale principale
            if i==j:
                tmp="..."
        #ADDP
            elif i>j:
                tmp=tab_color[color]
        #EDDP
            else:
                tmp="..."
            l_tmp.append(tmp)
        matrice.append(l_tmp)
    
    
        l_tmp=[]
        
elif position==1:
    for i in range(taille):
        for j in range(taille):
        #Diagonale principale
            if i==j:
                tmp="..."
        #ADDP
            elif i>j:
                tmp="..."
        #EDDP
            else:
                tmp=tab_color[color]
            l_tmp.append(tmp)
        matrice.append(l_tmp)
    
    
        l_tmp=[]
elif position==4:
    for i in range(taille):
        for j in range(taille):
        #Diagonale principale
            if i==j:
                tmp="..."
        #ADDP
            elif i>j:
                tmp="..."
        #EDDP
            else:
                tmp=tab_color[color]
            l_tmp.append(tmp)
        matrice.append(l_tmp)
    
    
        l_tmp=[]

elif position==5:
    for i in range(taille):
        for j in range(taille):
        #Diagonale principale
            if i==j:
                tmp="..."
        #ADDP
            elif i>j:
                tmp=tab_color[color]
        #EDDP
            else:
                tmp="..."
            l_tmp.append(tmp)
        matrice.append(l_tmp)
    
    
        l_tmp=[]

elif position==6:
    for i in range(taille):
        for j in range(taille):
        #Diagonale principale
            if i+j==taille-1:
                tmp=tab_color[color]
        #ADDP
            elif i>j:
                tmp="..."
        #EDDP
            else:
                tmp="..."
            l_tmp.append(tmp)
        matrice.append(l_tmp)
    
    
        l_tmp=[]

        
for i in matrice:
    for j in i:
        print(j, end=" \t")
    print("")