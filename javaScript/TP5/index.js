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

    //création de la carte
    const ma_question = tableau_questions[i]

    const card = document.createElement("div");
    card.classList.add("cadre");
    
    const ask = document.createElement("div");
    ask.setAttribute('id', 'ask');
    card.appendChild(ask);
    
    const header = document.createElement("header");
    header.textContent = ma_question.question;
    ask.appendChild(header);
    
    const choices = document.createElement("div");
    choices.setAttribute('id', 'choices');
    
    for (let i = 0; i < 4; i++) {
    const choice = document.createElement("div");
    choice.classList.add('choice');
    
    const input = document.createElement("input");
    input.setAttribute("type", "radio");
    input.classList.add("input");
    //   input.setAttribute("name", "");
    input.setAttribute("value", ma_question[String.fromCharCode(97 + i)]);
        
    const label = document.createElement("label")
    label.setAttribute("for", "")

    const inputContent = document.createTextNode(ma_question[String.fromCharCode(97 + i)]);
        
    label.appendChild(inputContent)
    choice.appendChild(input);
    choice.appendChild(label);
    choices.appendChild(choice);

    
    ask.appendChild(choices)
    }
        const button1 = document.createElement("div")
        button1.classList.add('button')
        const btn = document.createElement('button')
        btn.classList.add("btn")
        btn.textContent = "Suivant"
        button1.appendChild(btn)
        card.appendChild(button1)
        console.log(card);
    
    

        // console.log(ma_question.question)
        // card.innerHTML =`<div class="ask"><header>${ma_question.question}</header><div><div class="choice"><input type="radio" id="java" name="java" value="java"><label for="java">${ma_question.a}</label></div><div class="choice"><input type="radio" id="c" name="c" value="c"><label for="c">${ma_question.b}</label></div><div class="choice"><input type="radio" id="python" name="python" value="python"><label for="python">${ma_question.c}</label></div><div class="choice"><input type="radio" id="javascript" name="javascript" value="javascript"><label for="javascript">${ma_question.d}</label></div></div></div><div class="button"><button class="btn">Suivant</button></div>`
        const button = card.querySelector(".button button")
        // console.log(button)
        button.disabled = true
        
        button.addEventListener('click', function(){
                const nextCard = card.nextElementSibling;
                if (nextCard) {
                  nextCard.querySelector(".button button").disabled = false;
                  card.style.display = "none";
                  nextCard.style.display = "block";
                } else {
                    button.disabled = true;
                }
        })
    
        document.querySelector(".container").appendChild(card)

        if (i === 0) {
            button.disabled = false;
            card.style.display = "block";
          }
        }
        const question1 = tableau_questions[1]
        console.log(question1.correct)
        const choix1 = document.querySelector('input')
        console.log(choix1)

})

    