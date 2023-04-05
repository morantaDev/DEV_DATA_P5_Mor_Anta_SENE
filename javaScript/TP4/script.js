const zone = document.querySelector('.text_zone')
const generer = document.querySelector('.btn')
const length = document.querySelector('input#length').value



console.log(length)


let generateurNbr =function generateIntervalleNum(){
    var alNum = Math.floor(Math.random() * 10)
    return alNum;
}

let generateurLettreMin = function generateLowLetter(){
    var letter = String.fromCharCode(Math.floor(Math.random()*26)+97)
    return letter
}

let generateurLettreMaj = function generateUpperLetter(){
    var letter = String.fromCharCode(Math.floor(Math.random()*26)+65)
    return letter
}

let generateurCharSpe = function generateSpecialChar(){
    const symbols = '!@#$%^&*(){}[]=<>/,.'
	var symbol = symbols[Math.floor(Math.random() * symbols.length)];    
    return symbol
}

// console.log(generateur())
generer.addEventListener('click', function(){
    for (let i=1; i<=length; i++){
        zone.append(generateurCharSpe())
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