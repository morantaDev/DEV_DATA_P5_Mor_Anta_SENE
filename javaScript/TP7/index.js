const APIURL = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";

const IMGPATH = "https://image.tmdb.org/t/p/w1280";

const SEARCHAPI ="https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";


// fetch(APIURL)
// .then(function(response){
//     return response.json();
// })
// .then(function(data){
//     console.log(data)
// })

const image = document.querySelector('.images')

document.addEventListener("DOMContentLoaded", function(){
    fetch(APIURL).then(response => response.json().then((data)=> {
        console.log(data);
        let affichage = ""
        let title = ""
        for(let img of data.results){
            const img_title = document.createElement("section")
            img_title.setAttribute('class', 'imageEtTitre')
            img_title.innerHTML = `
            <img src="https://image.tmdb.org/t/p/w1280${img.backdrop_path}" alt="mon_image"/>
            <div id ='title'>${img.original_title}</div>
            `;
            console.log(img_title)
            affichage += img_title.outerHTML;

            image.innerHTML = affichage;
        }  
    } 
))
})