import mesFonctions

phrase = mesFonctions.Chaine()

print(phrase)
No_space=mesFonctions.Delete_Spaces(phrase)

cut=mesFonctions.Cut_Up(No_space)

TableauN=[]
for item in cut:
    if mesFonctions.Verify(item)==True:
        if mesFonctions.Check_length(item)<25:
            print("La phrase",item,"est correcte mais compte moins de 25 caractères.")
            continue
        else:
            TableauN.append(item)
print(TableauN)




















