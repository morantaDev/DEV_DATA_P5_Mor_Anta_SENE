let boutonRightChoisi = document.querySelector("#right")
let boutonLeftChoisi = document.querySelector("#left")

let listOfD = document.querySelector(".droite")
let listOfD_par = document.querySelector('.droite p')
let listOfG = document.querySelector(".gauche")

let paragrapheChoisi = document.querySelector(".btns p")

console.log(listOfD_par)

if (listOfD_par === null) {
    boutonLeftChoisi.disabled = false
}

let listOfP = document.querySelectorAll(".gauche p")

listOfP.forEach(element => { 
    element.addEventListener("mouseover", function(event){
        event.preventDefault()
        //console.log(event.target)
        event.target.style.backgroundColor = "blue"
        event.target.style.color = "white"
        boutonRightChoisi.addEventListener('click', function(){
            listOfD.appendChild(event.target)
            listOfG.removeChild(event.target)   // celà equivaut à écrire listOfG.removeChild(element) de même que pour le appendChild
        })
        boutonLeftChoisi.addEventListener('click', function(){
            listOfD.removeChild(event.target)
            listOfG.appendChild(event.target)
        })
    })
    element.addEventListener("mouseout", function(event){   
        element.style.backgroundColor = ""
        element.style.color = ""
    })
})
