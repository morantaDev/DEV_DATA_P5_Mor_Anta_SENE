const projet = document.querySelector('.projet')
const success = document.querySelector('.success')
const danger = document.querySelector('.danger')
const warning = document.querySelector('.warning')
const info = document.querySelector('.info')

let events = []



success.addEventListener('click', function(){
    const newSuccess = document.createElement('div')
    newSuccess.classList.add('Projet')
    newSuccess.textContent ="Success"
    newSuccess.style.backgroundColor = "green"
    console.log(newSuccess)
    // projet.appendChild(newSuccess)
    events.push(newSuccess)
    updateEvents()
})
danger.addEventListener('click', function(){
    const newDanger = document.createElement('div')
    newDanger.classList.add('Projet')
    newDanger.textContent ="Danger"
    newDanger.style.backgroundColor = "red"
    console.log(newDanger)
    // projet.appendChild(newDanger)
    events.push(newDanger)
    updateEvents()
})
warning.addEventListener('click', function(){
    const newWarning = document.createElement('div')
    newWarning.classList.add('Projet')
    newWarning.textContent ="Warning"
    newWarning.style.backgroundColor = "orange"
    console.log(newWarning)
    // projet.appendChild(newWarning)
    events.push(newWarning)
    updateEvents()
})
info.addEventListener('click', function(){
    const newInfo = document.createElement('div')
    newInfo.classList.add('Projet')
    newInfo.textContent ="Info"
    newInfo.style.backgroundColor = "blue"
    console.log(newInfo)
    // projet.appendChild(newInfo)
    events.push(newInfo)
    updateEvents()
})

function updateEvents(){
        let x = setInterval(function(){
            projet.innerHTML =""
            if (x > 1){
                clearInterval(x)
            }
        }, 1000)
        for (let i = events.length - 1; i >= 0; i--) {
                    projet.appendChild(events[i]);
        }
    }

