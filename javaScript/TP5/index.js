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


const button = document.querySelector(".btn")
console.log(button)
document.addEventListener('DOMContentLoaded', function(){
    button.disabled = false
    
    for(let i = 0; i<tableau_questions.length; i++){
        const question = tableau_questions[i]
        console.log(question.question)
    
    }
})

    