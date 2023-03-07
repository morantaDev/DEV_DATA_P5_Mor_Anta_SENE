donnees = read.csv('/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv', sep= ',')
donnees

numero <- donnees$Numero
numero


#Vérifier les numéros valides

valid_num <- function(numero){
  valide <- FALSE
  for (caractere in numero){
    longueur <- nchar(num)
    if (longueur == 7){
      if (grepl("[[:lower:]]", num) == FALSE & grepl("[0-9]", num)==TRUE){
        valide <- TRUE
      }
    }
  }
  return(valide)
}

for(num in numero){
  print(valid_num(num))
}

is.character(numero)

?grepl()


#Vérifier les noms valides



donnees$Numero[which(nchar(donnees$Numero)==7)]


nom <-donnees$Nom
nom

prenom <- donnees$Prénom
prenom

date_de_naissance <-donnees$Date.de.naissance
date_de_naissance

classe <- donnees$Classe
classe


save.image()
