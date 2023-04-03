document.addEventListener('DOMContentLoaded', function(){
let score = 0

const tableau_questions = [
    {
        question: "Quel est le MeilleurLangage de Programmation en 2022",
        a: "Java",
        b: "C",
        c: "Python",
        d: "JavaScript",
        correct: "d"
    },
    {
        question: "Quelle est la plus grande Université du Sénégal",
        a: "Université Cheikh Anta DIOP",
        b: "Université Gaston Berger",
        c: "Université du Sine-Saloum",
        d: "Université de Assane Seck de Ziguinchor",
        correct: "a"
    },
    {
        question: "Combien de temps dure la gestation chez les éléphants (en mois)",
        a: "10",
        b: "30",
        c: "8",
        d: "22",
        correct: "d"
    },
    {
        question: "Combien de joueurs compte une équipe de foot américain en phase de jeu?",
        a: "16",
        b: "14",
        c: "11",
        d: "9",
        correct: "c"
    },
    {
        question: "Lequel de ses éléments suivants n'est un élément de jeu d'échec",
        a: "roi",
        b: "fou",
        c: "pion",
        d: "puce",
        correct: "d"
    }
];


    
    
for(let i = 0; i<tableau_questions.length; i++){
        const card = document.createElement("div")
        card.classList.add("cadre")

        const question = tableau_questions[i]
            console.log(question.question)
            card.innerHTML =`<div class="ask"><header>${question.question}</header><div><div class="choice"><input type="radio" id="java" name="java" value="java"checked><label for="java">${question.a}</label></div><div class="choice"><input type="radio" id="c" name="c" value="c"><label for="c">${question.b}</label></div><div class="choice"><input type="radio" id="python" name="python" value="python"><label for="python">${question.c}</label></div><div class="choice"><input type="radio" id="javascript" name="javascript" value="javascript"><label for="javascript">${question.d}</label></div></div></div><div class="button"><button class="btn">Suivant</button></div>`
            const button = card.querySelector(".button button")
            console.log(button)
            button.disabled = true
        
        button.addEventListener('click', function(){
                const nextCard = card.nextElementSibling;
                if (nextCard) {
                  nextCard.querySelector(".button button").disabled = false;
                  card.style.display = "none";
                  nextCard.style.display = "block";
                }
        })
    
        document.querySelector(".container").appendChild(card)

        if (i === 0) {
            button.disabled = false;
            card.style.display = "block";
          }
    }
})

    