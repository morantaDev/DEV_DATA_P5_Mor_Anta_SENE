const zone = document.querySelector('.text_zone')
const generer = document.querySelector('.btn')
// const length = document.querySelector('.length input.value')

console.log(length)

//generer des valeurs entre le min et max avec le max exclu
function randNumber(min, max){
    return Math.random * (max - min) + min;
}

var Length = 15
let generateurNbr =function generateIntervalleNum(){
    var alNum = Math.floor(Math.random() * 10)
    return alNum;
}

// console.log(generateur())
generer.addEventListener('click', function(){
    for (let i=1; i<=Length; i++){
        zone.append(generateurNbr())
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