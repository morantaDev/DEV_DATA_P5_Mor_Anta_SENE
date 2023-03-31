let colorer = document.querySelector(".gauche p")
let boutonRightChoisi = document.querySelector("#right")
let boutonLeftChoisi = document.querySelector("#left")
let paragrapheChoisi = document.querySelector(".btns p")

let listOfP = document.querySelectorAll(".gauche p")

console.log(listOfP)

listOfP.forEach(element => {
    console.log(element)
})

colorer.addEventListener("mouseover", function(event){
    listOfP.forEach(element =>{
        element.style.backgroundColor = "blue"
        element.style.color = "white"

    const newP = document.createElement("p")
    newP.textContent = element.textContent
    console.log(newP)

boutonRightChoisi.addEventListener('click', function(){
    document.querySelector(".droite").appendChild(newP)
    
})


        // var translate = 50
        // let deplacer = setInterval(()=>{
        //     if(translate == 200){
        //         clearInterval(deplacer)
        //     } else {
        //         translate++;
        //         element.style.right = `${translate}px`;
        //     }
        // }, 5)

        // var dx = 50
        // boutonRightChoisi.addEventListener('click', function(event){
        //     var x = parseInt(element.style.right)
        //     element.style.right = `${x+dx}px`;
        //     console.log(x)
        // })

        // boutonLeftChoisi.addEventListener('click', function(event){
        //     var x = parseInt(element.style.right)
        //     element.style.right = `${x-dx}px`;
        //     console.log(x)
        // })
    })
})
