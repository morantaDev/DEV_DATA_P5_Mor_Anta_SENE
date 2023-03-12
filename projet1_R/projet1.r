library(lubridate)
library(stringr)
Data = read.csv('/home/moranta/Downloads/Donnees_Projet_Python_DataC5(1).csv', sep= ',')
View(Data)

    
    #Vérifier les numéros valides
    
    # donnees$Numero[which(nchar(donnees$Numero)==7)]
    
    
    
    
    
    
    #=================================================================================#
    ddn <-Data$Date.de.naissance
    ddn
    
    valid_date = function(string_date){
        valide <- FALSE
        sup_espace <- function(string)   gsub("\\s+", " ", gsub("^\\s+|\\s+$", "", string)) 
        d <- sup_espace(string_date)
        d <- gsub("[[:punct:]]", "/",d)
        d <- gsub(" ", "/",d)
        d <- str_replace(d, "-", "/")
        #print(d)
        d <- gsub("fev", "02", d)
        d <- gsub("mars", "03", d)
        d <- gsub("decembre", "12", d)
        d1 = as.Date(d, "%d/%m/%y", lang ="fr")
        #print(d1)
        d1 <- format(d1, "%Y/%m/%d")
        
        if(is.na(d1)){
          valide <- FALSE
        } else {
          valide <- TRUE
        }
      return(valide)

    }
      
    # for (dates in date_de_naissance){
    #   d <- valid_date(dates)
    #   if(is.na(d)){
    #     print("Date invalide")
    #   } else {
    #     print(d)
    #   }
    # }
    
    
    # dates = "      11_12_2003 "
    # valid_date(dates)
    # 
    
    
    
    resultat <- vector("character", length(ddn))

    for(i in seq_along(ddn)){
      if(valid_date(ddn[i])){
        resultat[i] <- ddn[i]
      } else {
        resultat[i] <- paste(NA,":", ddn[i])
      }
    }
    Data$Date.de.naissance <- resultat
    View(Data)
    #===============================================================================#

    #===============================================================================#
    numero <- Data$Numero
    numero
    valid_num <- function(argument){
        longueur <- nchar(argument)
        if (longueur == 7){
          return((grepl("[[:upper:]]", argument) & grepl("[0-9]", argument) & !grepl("[[:lower:]]", argument) & !grepl("[[:punct:]]", argument)))
        } else {
          return(FALSE)
        }
    }
    # num ="AAÉA12+"
    # valid_num(num)
    
    resultat <- vector("character", length(numero))
    for(i in seq_along(numero)){
      #valid_num(num)
      #resultat <- ifelse(valid_num(num), num, NA)
      if(valid_num(numero[i])){
        resultat[i] <- numero[i]
      } else {
        resultat[i] <- paste(NA,":", numero[i])
      }
    }
    Data$Numero <- resultat
    #Vérifier les noms valides
    
    #===============================================================================#
    nom <-Data$Nom
    nom
    valid_nom = function(argument){
      valide <- FALSE
      if(grepl("^[a-zA-Z]", argument) & grepl("^[a-zA-Z]*{2,}", argument)){
        valide <- TRUE
      }
      return(valide)
    }
    
    
    # for (name in nom){
    #   valid_nom(name)
    # }
    
    # nom ="S1s2+4"
    # valid_nom(nom)

    resultat <- vector("character", length(nom))

    for(i in seq_along(nom)){
      if(valid_nom(nom[i])){
        resultat[i] <- nom[i]
      } else {
        resultat[i] <- paste(NA,":", nom[i])
      }
    }
    Data$Nom <- resultat
     View(donnees)
#===============================================================================#
  prenom <- Data$Prénom
  prenom
  
  valid_prenom = function(argument){
    valide <- FALSE
      if(grepl("^[a-zA-Z]", argument) & grepl("[a-zA-Z]{3,}", argument)){
        valide <- TRUE
      }
    return(valide)
  }
  
  
  resultat <- vector("character", length(nom))
  
  for(i in seq_along(prenom)){
    if(valid_nom(prenom[i])){
      resultat[i] <- prenom[i]
    } else {
      resultat[i] <- NA
    }
  }
  Data$Prénom <- resultat
#===============================================================================#
classe = Data$Classe
valid_classe = function(argument){
  arg <- function(string)  gsub("\\s+", " ", gsub("^\\s+|\\s+$", "" , string))
  argu <- arg(argument)
  return(grepl("^[3-6]{1}", argu) & grepl("[A,B]{1}$", argu))
}
# cl = "                     7 eime A "
# valid_classe(cl)

# for(cl in classe){
#   print(valid_classe(cl))
# }

  resultat <- vector("character", length(classe))
  
  for(i in seq_along(classe)){
    if(valid_classe(classe[i])){
      resultat[i] <- classe[i]
    } else {
      resultat[i] <- paste(NA,":", classe[i])
    }
  }
  Data$Classe <- resultat

  
  View(Data)
#===============================================================================#

Nt <- Data$Note

Nt

# resultat <- vector("character", length(notes))
# resultat1 <- vector("character", length(notes))
# result <- list()
# ?data.frame()

valid_note <- function(argument) { 
  splt <- str_split(argument, "#")[[1]] 
  notes <- c() 
  valide <- FALSE
  for (i in seq_along(splt)) { 
    matière_note <- str_split(trimws(splt[i]), "\\[|\\]")[[1]] 
    note <- matière_note[2] 
    note <- str_replace(note, "\\|", ":") 
    note <- str_replace(note, ",", ".")
    notes <- c(notes, str_split(note, ":") [[1]]) 
  } 
  # print(notes)
  if (any(is.na(suppressWarnings(as.numeric(notes)))) || length(notes) == 0) {
    # cat("Les notes invalides sont: ", notes, "\n")
    valide <- FALSE
  } else {
    # cat("Toutes les notes sont valides.\n")
    valide <- TRUE
  }
  
  return(valide)
}

Note <- "Math[o1|13:06] #Francais[08|17:12] #Anglais[13|13:12] #PC[09|18,07] #SVT[15|10:10] #HG[14|19:17]" 
Note <- trimws(Note)

test <- "Math[o1|13:06] #Francais[08|17:12] #Anglais[13|13:12] #PC[09|18,07] #SVT[15|10:10] #HG[14|19:17]" 
test <- str_split(test,"#")
test
for(i in seq_along(test[[1]])){
  
  print(test[[1]][i])
}
test <- str_replace_all(test,"[[:punct:]]", ":")
test
N <- ""

for (variable in vector) {
  
}
for(nt in Nt){
  print(valid_note(nt))
  
}






?subset
?str_replace
?list
?gsub
?append
?apply
?as.numreric
?str_replace_all
?str_split
#===============================================================================#



?sink()
is.character(numero)
?grepl()

#Create a working environnement
getwd()
setwd("/home/moranta/DEV_DATA_P5_Mor_Anta_SENE/projet1_R")
source("scripts/projet1.r")


?str_replace
?strsplit
save.image()
