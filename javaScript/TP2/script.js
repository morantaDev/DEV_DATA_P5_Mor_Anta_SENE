let colorer = document.querySelector(".btns")
let boutonRightChoisi = document.querySelector("#right")
let boutonLeftChoisi =  document.querySelector("#left")
colorer.addEventListener("click", function(event){
    event.target.style.backgroundColor = "blue"
    event.target.style.color = "white"

    var translate = 0
    let deplacer = setInterval(()=>{
        if(translate == 200){
            clearInterval()
        } else {
            translate++;
        }
    }, 5)

    boutonLeftChoisi.addEventListener('click', function(event){
        event.style.left = deplacer() + "px";
    
    })
});



//créer un paragraphe au clic au niveau du champ choisi





