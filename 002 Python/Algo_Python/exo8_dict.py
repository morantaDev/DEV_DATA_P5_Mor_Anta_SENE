def test():
    ajout=[{'sene mor': [876543, 'l1', 45.0, 234.0, 34.0]}, {'sarr mbaye': [98765, 'l1', 765.0, 345.0, 12.0]}, {'sene ousmane': [876543, 'l1', 45.0, 234.0, 34.0]}, {'sarr gora': [98765, 'l1', 765.0, 345.0, 12.0]}]
    return ajout
add=[]
dict={}
# reponse=True
# while reponse==True:
#     tel=int(input("Entrer le  numéro de téléphone:\n"))
#     nom=str(input("Entrer le nom:\n"))
#     prenom=str(input("Entrer le prénom:\n"))
    
#     classe=str(input("Entrer la classe:\n"))
#     note_devoir=float(input("Entrer la note de devoir\n"))
#     note_projet=float(input("Entrer la note de projet\n"))
#     note_examen=float(input("Entrer la note d'examen\n"))
    
#     dict[nom+" "+prenom]=[tel,classe,note_devoir,note_projet,note_examen]
#     add.append(dict)
#     x=int(input(("Entrer 1 pour continuer et 0 pour arrêter\n")))
#     if x==0:
#         break
#     else:
#         reponse==True

add=test()
print(add)

for i in add:
    print(i)

