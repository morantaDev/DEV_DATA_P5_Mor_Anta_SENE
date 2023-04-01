
// définir la date cible
var date_cible = new Date("January 1, 2024 00:00:00");



var x = setInterval(function(){
    const date = document.querySelector(".date")
    var date_courante = Date.now()

    console.log(date_cible.getTime())
    
    let difference = date_cible - date_courante
    
    // console.log(difference)
    
    
    var jour = Math.floor(difference / (1000 * 60 * 60 * 24))
    // console.log(jour)
    
    var diff = difference - (jour * 1000 * 60 * 60 * 24)
    // console.log(diff)
    
    var heure = Math.floor(diff / (1000 * 60 * 60))
    // console.log(heure)
    
    var diff1 =  diff - (heure * 1000 * 60 * 60)
    var minute = Math.floor(diff1 / (1000 * 60))
    // console.log(minute)
    
    var diff2 = diff1 - (minute * 1000 * 60)
    var seconde = Math.floor(diff2 / 1000)
    // console.log(seconde)
    date.innerHTML = "-" + jour +" 0-"+heure +" 0-"+minute +" 0-"+seconde

    if(difference < 0){
        clearInterval(x)
    }
}, 1000);














































// // mettre à jour le compte à rebours toutes les secondes
// var x = setInterval(function() {

//     // obtenir la date et l'heure actuelles
//     var maintenant = new Date().getTime();

//     // calculer la durée restante
//     var delta = cible - maintenant;

//     // extraire les jours, heures, minutes et secondes de la durée restante
//     var jours = Math.floor(delta / (1000 * 60 * 60 * 24));
//     var heures = Math.floor((delta % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//     var minutes = Math.floor((delta % (1000 * 60 * 60)) / (1000 * 60));
//     var secondes = Math.floor((delta % (1000 * 60)) / 1000);

//     // afficher le compte à rebours dans un élément HTML
//     document.getElementById("compte-a-rebours").innerHTML = jours + "j " + heures + "h "
//     + minutes + "m " + secondes + "s ";

//     // afficher un message lorsque le compte à rebours est terminé
//     if (delta < 0) {
//         clearInterval(x);
//         document.getElementById("compte-a-rebours").innerHTML = "EXPIRÉ";
//     }
// }, 1000);
