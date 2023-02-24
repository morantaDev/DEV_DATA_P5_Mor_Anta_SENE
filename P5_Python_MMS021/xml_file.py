import csv


data=[]
with open("/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv") as fichier:
    csv_lecteur=csv.reader(fichier)
    
    for rows in csv_lecteur:
        data.append(rows)
        
        
fichier.close()

#CODE,Numero,Nom,Prénom,Date de naissance,Classe,Note

def convert_rows(rows):
    return """<etudiant>
    <Numero id="%s">
        <Nom>%s</Nom>
        <Prénom>%s</Prénom>
        <Date_de_naissance>%s</Date_de_naissance>
        <Classe>%s</Classe>
        <Note>%s</Note>
    </Numero>
</etudiant>
""" % (
    rows[1], rows[2], rows[3], rows[4], rows[5], rows[6])

# print '\n'.join(fichier.apply(convert_rows, axis=1))

with open("xml_file.xml", "w") as xml_file:
    xml_file.write('\n'.join([convert_rows(rows) for rows in data]))
    
    
    
    
    
    
    
# <!ELEMENT etudiant (Numero)>
# <!ELEMENT Numero (Nom, Prénom, Date_de_naissance, Classe, Note)>
# <!ELEMENT Nom (#PCDATA)>
# <!ELEMENT Prénom (#PCDATA)>
# <!ELEMENT Date_de_naissance (#PCDATA)>
# <!ELEMENT Classe (#PCDATA)>
# <!ELEMENT Note (#PCDATA)>
# <!ATTLIST Numero id CDATA #REQUIRED>






# <etudiant>
#     <Numero id="%s">
#         <Nom>%s</Nom>
#         <Prénom>%s</Prénom>
#         <Date_de_naissance>%s</Date_de_naissance>
#         <Classe>%s</Classe>
#         <Matiere>
            # <Math>%d</Math>
            # <svt>%d</svt>
            # <pc>%d</pc>
            # <Anglais>%d</Anglais>
            # <Francais>%d</Francais>
#         </Matiere>
#     </Numero>
# </etudiant>




