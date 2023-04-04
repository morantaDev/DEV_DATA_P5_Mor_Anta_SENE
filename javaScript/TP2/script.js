//let colorer = document.querySelector(".gauche p")
let boutonRightChoisi = document.querySelector("#right")
let boutonLeftChoisi = document.querySelector("#left")

let listOfD = document.querySelector(".droite")
let listOfG = document.querySelector(".gauche")

let paragrapheChoisi = document.querySelector(".btns p")

let listOfP = document.querySelectorAll(".gauche p")

// console.log(listOfD)

listOfP.forEach(element => {
    
    element.addEventListener("mouseover", function(event){
        event.preventDefault()
        //console.log(event.target)
        event.target.style.backgroundColor = "blue"
        event.target.style.color = "white"
        
        boutonRightChoisi.addEventListener('click', function(){
            listOfD.appendChild(event.target)
            listOfG.removeChild(event.target)
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
