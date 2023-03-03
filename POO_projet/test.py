dictList = [{'CODE': 'BNT021', 'Numero': 'FTR3456G', 'Nom': 'Drame', 'Prénom': 'Rama', 'Date de naissance': '12/03/92', 'Classe': '5 eme B', 'Note': 'SVT[12|20:19] #PC[13|14:10] #Francais[14|18:19] #SVT[16|19:14] #Anglais[14|15:18] #HG[10|07:20] #Math[19|17:18]'}]


header = []

for item in dictList[0].values():
    header.append(item)
    
print(header)