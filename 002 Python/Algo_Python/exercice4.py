import mesFonctions

tab=[]
tab_inv=[]
ponct=[",","-","|","/","\n","\t"]

Resultat=""
tmp=""
def Numero():
    chaine="""77 8656 63 22, 7645656793,7 8 9 0 4 1 3 3 4, 778903423,335678900,7812376342,7812345"""
    return chaine
chaine=Numero()
print(chaine)
Chaine=mesFonctions.Delete_Spaces(chaine)
print(Chaine)
num=mesFonctions.decoupe(Chaine)
last=mesFonctions.last_num(chaine)
num +=last

print(num)

val_and_invalid=mesFonctions.phone_numbers(num)
print(val_and_invalid)

for item in val_and_invalid:
    if len(item)==9:
        tab.append(item)
    else:
        tab_inv.append(item)

print(tab)
print(tab_inv)

print("\nLes nombres valides:")
for i in tab:
    print(i)   

print("\nLes nombres invalides")
for j in tab_inv:
    print(j)
    

        



# def Deplacer(string):
#     width=70
#     return width*' ' +string

# def get_number(string):
#     deuxieme=['5','6','7','8']
#     tab=[]
#     start=0
#     number=""
#     for start in range(start,len(string)-1):
#         #number+=string[i]
#         #start=i
#         if string[start]=='7' and string[start+1] in deuxieme:
#             tab.append(string[start:start+9])
#             start+=start+9
#         #number=""
#     return tab

# def Delete_Spaces(string):
#     text=""
#     for i in range(len(string)):
#         if string[i]==' ':
#             continue
#         else:
#             text+=string[i]
#     return text


# chaine=Numero()
# x=Delete_Spaces(chaine)

# y=(get_number(x))

# for i in y:
#     if len(i)>=9:
#         dep=Deplacer(i)
#         print(dep)
#     else:
#         print(i) 