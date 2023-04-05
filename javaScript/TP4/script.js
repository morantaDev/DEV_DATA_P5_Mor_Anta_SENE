const zone = document.querySelector('.text_zone')
const generer = document.querySelector('.btn')
const length = document.querySelector('#length')
const majus = document.querySelector('#majuscule')
const minus = document.querySelector('#minuscule')
const numbers = document.querySelector('#numbers')
const speChar = document.querySelector('#character')

var inputLength = 0

//Récupérer la taille du code
length.addEventListener('input', function(event){
    inputLength = event.target.value
    console.log(inputLength)
})



//Vérifier les cases cochées

majus.addEventListener('change', function(){
    console.log('true')
})
minus.addEventListener('change', function(){
    console.log('true')
})
numbers.addEventListener('change', function(){
    console.log('true')
})
speChar.addEventListener('change', function(){
    console.log('true')
})



//Générer des nombres aléatoirement de 0 à 9 (une fois)
let generateurNbr =function generateIntervalleNum(){
    var alNum = Math.floor(Math.random() * 10)
    return alNum;
}

//Générer des lettres minuscules aléatoirement de a à z (une fois)
let generateurLettreMin = function generateLowLetter(){
    var letter = String.fromCharCode(Math.floor(Math.random()*26)+97)
    return letter
}

//Générer des lettres majuscules aléatoirement de A à Z (une fois)
let generateurLettreMaj = function generateUpperLetter(){
    var letter = String.fromCharCode(Math.floor(Math.random()*26)+65)
    return letter
}

//Générer des caractères spéciaux aléatoirement (une fois)
let generateurCharSpe = function generateSpecialChar(){
    const symbols = '!@#$%^&*(){}[]=<>/,.'
	var symbol = symbols[Math.floor(Math.random() * symbols.length)];    
    return symbol
}

generer.addEventListener('click', function(){
    for (let i=1; i<=inputLength; i++){
        zone.append(generateurLettreMin())
    }
    
})

















// function strRandom(o) {
    //     var a = 15,
    //         b = 'abcdefghijklmnopqrstuvwxyz',
    //         c = '',
    //         d = 0,
    //         e = ''+b;
    //     if (o) {
        //         if (o.startsWithLowerCase) {
            //         c = b[Math.floor(Math.random() * b.length)];
            //         d = 1;
            //         }
            //         if (o.length) {
                //         a = o.length;
                //         }
                //         if (o.includeUpperCase) {
                    //         e += b.toUpperCase();
                    //         }
                    //         if (o.includeNumbers) {
                        //         e += '1234567890';
                        //         }
//     }
//     for (; d < a; d++) {
    //         c += e[Math.floor(Math.random() * e.length)];
    //     }
    //     return c;
    //     }
    
    //     var randu = strRandom({
        //     includeUpperCase: true,
        //     includeNumbers: true,
        //     length: 15,
        //     startsWithLowerCase: true
        //     });
        
        //     console.log(randu)