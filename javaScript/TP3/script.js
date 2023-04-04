const projet = document.querySelector('.projet')
const success = document.querySelector('.success')
const danger = document.querySelector('.danger')
const warning = document.querySelector('.warning')
const info = document.querySelector('.info')


let events = []

projet.style.display = "none"


success.addEventListener('click', function(event){
    projet.style.display = "block"
    projet.style.backgroundColor = "green"
    let x = setInterval(function(){
        projet.style.display = "block"
        x += 1
        console.log(x)
        if (x > 1){
            projet.style.display = "none"
            clearInterval(x)
        }
    }, 1000)
})

danger.addEventListener('click', function(){
    projet.style.display = "block"
    projet.style.backgroundColor = "red"
    let x = setInterval(function(){
        projet.style.display = "block"
        x += 1
        console.log(x)
        if (x > 1){
            projet.style.display = "none"
            clearInterval(x)
        }  
    }, 1000)
})
warning.addEventListener('click', function(){
    projet.style.display = "block"
    projet.style.backgroundColor = "orange"
    let x = setInterval(function(){
        projet.style.display = "block"
        x += 1
        console.log(x)
        if (x > 1){
            projet.style.display = "none"
            clearInterval(x)
        }  
    }, 1000)
})
let infoEvent = info.addEventListener('click', function(){
    projet.style.display = "block"
    projet.style.backgroundColor = "blue"
    let x = setInterval(function(){
        projet.style.display = "block"
        x += 1
        console.log(x)
        if (x > 1){
            projet.style.display = "none"
            clearInterval(x)
        }  
    }, 1000)
})

events.push(infoEvent)

//je veux afficher les événements en forme de pile où lévenement précédant s'affichera au dessus de l'élément actuel ainsi de suite jusqu'à la fin des événements

/*procédé
je veux créér un tableau d'événement
j'ajoute les différents événements et retourne le tableau à chaque fois un événement est ajouté

*/


// const events = []; // Tableau pour stocker les événements

// projet.style.display = "none";

// success.addEventListener('click', function(event){
//     const eventDiv = document.createElement('div'); // Créer un élément div pour représenter l'événement
//     eventDiv.textContent = "Success"; // Contenu de l'événement
//     eventDiv.classList.add('event'); // Ajouter une classe à l'élément div pour le style
//     eventDiv.style.backgroundColor = "green"; // Couleur de fond de l'événement
//     events.push(eventDiv); // Ajouter l'événement au tableau des événements
//     updateEvents(); // Mettre à jour l'affichage des événements
// });

// danger.addEventListener('click', function(){
//     const eventDiv = document.createElement('div');
//     eventDiv.textContent = "Danger";
//     eventDiv.classList.add('event');
//     eventDiv.style.backgroundColor = "red";
//     events.push(eventDiv);
//     updateEvents();
// });

// warning.addEventListener('click', function(){
//     const eventDiv = document.createElement('div');
//     eventDiv.textContent = "Warning";
//     eventDiv.classList.add('event');
//     eventDiv.style.backgroundColor = "orange";
//     events.push(eventDiv);
//     updateEvents();
// });

// info.addEventListener('click', function(){
//     const eventDiv = document.createElement('div');
//     eventDiv.textContent = "Info";
//     eventDiv.classList.add('event');
//     eventDiv.style.backgroundColor = "blue";
//     events.push(eventDiv);
//     updateEvents();
// });

// function updateEvents() {
//     projet.innerHTML = ""; // Vider le contenu de l'élément projet

//     // Afficher les événements dans l'ordre inverse dans l'élément projet
//     for (let i = events.length - 1; i >= 0; i--) {
//         projet.appendChild(events[i]);
//     }
// }
