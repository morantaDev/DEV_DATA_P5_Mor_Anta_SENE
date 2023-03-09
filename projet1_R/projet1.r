library(lubridate)
library(stringr)
donnees = read.csv('/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv', sep= ',')
donnees


#Vérifier les numéros valides

donnees$Numero[which(nchar(donnees$Numero)==7)]




prenom <- donnees$Prénom
prenom

#=================================================================================#
date_de_naissance <-donnees$Date.de.naissance
date_de_naissance

valid_date = function(string_date){
    valide <- FALSE
    sup_espace <- function(string)   gsub("\\s+", " ", gsub("^\\s+|\\s+$", "", string)) 
    d <- sup_espace(string_date)
    d <- str_replace(d, "[[:punct:]]", "/")
    d <- str_replace(d, "-", "/")
    #print(d)
    d <- gsub("\\s", "/", d)
    #print(d)
    d <- gsub("Fev", "02", d)
    d <- gsub("mars", "03", d)
    d <- gsub("décembre", "12", d)
    d1 = as.Date(d, "%d/%m/%y", lang ="fr")
    #print(d1)
    d1 <- format(d1, "%Y/%m/%d")
  return(d1)
}

for (dates in date_de_naissance){
  d <- valid_date(dates)
  if(is.na(d)){
    print("Date invalide")
  } else {
    print(d)
  }
}


?is.na
# for(Date in date_de_naissance){
#   print(valid_date(Date))
# }
#===============================================================================#

classe <- donnees$Classe
classe


?gsub
#===============================================================================#
numero <- donnees$Numero
numero
valid_num <- function(argument){
    longueur <- nchar(num)
    if (longueur == 7){
      return((grepl("[[:upper:]]", numero) & grepl("[0-9]", numero) & !grepl("[[:lower:]]", numero) & !grepl("[[:punct:]]", numero)))
    } else {
      return(FALSE)
    }
}
# num ="AAÉA12+"
# valid_num(num)

for(num in numero){
  print(valid_num(num))
}

#Vérifier les noms valides

#===============================================================================#
nom <-donnees$Nom
nom
valid_nom = function(argument){
  valide <- FALSE
  if(grepl("^[a-zA-Z]", argument) & grepl("[a-zA-Z]{2,}", argument)){
    valide <- TRUE
  }
  return(valide)
}


# for (name in nom){
#   print(valid_nom(name))
# }

nom ="Ss1s2+4"
valid_nom(nom)
#===============================================================================#
valid_prenom = function(argument){
  valide <- FALSE
    if(grepl("^[a-zA-Z]", argument) & grepl("[a-zA-Z]{3,}", argument)){
      valide <- TRUE
    }
  return(valide)
}
for (pr in prenom){
  print(valid_prenom(pr))
}
#===============================================================================#


?strsplit



#===============================================================================#
valid_classe = function(argument){
  arg <- function(string)  gsub("\\s+", " ", gsub("^\\s+|\\s+$", "" , string))
  argu <- arg(argument)
  return(grepl("^[3_6]{1}",argu) & grepl("[A,B]{1}$", argu))
}
cl = "                     67 eime A "
valid_classe(cl)



#===============================================================================#

?sink()
is.character(numero)
?grepl()

#Create a working environnement
getwd()
setwd("/home/moranta/DEV_DATA_P5_Mor_Anta_SENE/projet1_R")
source("scripts/projet1.r")

View(donnees)
?str_replace
save.image()
