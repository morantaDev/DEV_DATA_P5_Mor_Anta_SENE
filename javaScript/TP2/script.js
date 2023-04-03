//let colorer = document.querySelector(".gauche p")
let boutonRightChoisi = document.querySelector("#right")
let boutonLeftChoisi = document.querySelector("#left")

let listOfD = document.querySelector(".droite")

let paragrapheChoisi = document.querySelector(".btns p")

let listOfP = document.querySelectorAll(".gauche p")

console.log(listOfD)

listOfP.forEach(element => {
    
    element.addEventListener("mouseover", function(event){
        event.preventDefault()
        //console.log(event.target)
        event.target.style.backgroundColor = "blue"
        event.target.style.color = "white"
        //alert("jj")
        //listOfD.appendChild(event.target)

    })

    element.addEventListener("mouseout", function(event){
        element.style.backgroundColor = ""
        element.style.color = ""
    })
})
/*
colorer.addEventListener("mouseover", function(event){
    listOfP.forEach(element =>{
        element.style.backgroundColor = "blue"
        element.style.color = "white"

    const newP = document.createElement("p")
    newP.textContent = element.textContent
    console.log(newP)

    })
})

boutonRightChoisi.addEventListener('click', function(){
    document.querySelector(".droite").appendChild(newP)
    
})*/