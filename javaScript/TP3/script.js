const projet = document.querySelector('.projet')
const success = document.querySelector('.success')
const danger = document.querySelector('.danger')
const warning = document.querySelector('.warning')
const info = document.querySelector('.info')



projet.style.display = "none"


success.addEventListener('click', function(){
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
info.addEventListener('click', function(){
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