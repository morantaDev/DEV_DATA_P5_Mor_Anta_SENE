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
    let affichage = ""
    fetch(APIURL).then(response => response.json().then((data)=> {
        ///console.log(data);
        for(let img of data.results){
            let img_title = document.createElement("section")
            img_title.setAttribute('class', 'imageEtTitre')

            img_title.innerHTML = `
            <img src="https://image.tmdb.org/t/p/w1280${img.backdrop_path}" alt="mon_image"/>
            <div id ='title'>
            ${img.original_title} 
            <span>${img.vote_average}</span>
            </div>
            <div class="descript">
            ${img.overview}
            </div>
            `;
            // console.log(img_title)
            if (img.vote_average >=6){
                img_title.querySelector('span').style.color = "green";
            } else if (img.vote_average > 5 && img.vote_average<6) {
                img_title.querySelector('span').style.color = "orange";
            } else {
                img_title.querySelector('span').style.color = "red";
            }


            const description = img_title.querySelector('.descript');
            description.style.display ="none"   
            //console.log(description)
            //console.log(img_title)

            img_title.addEventListener("mouseover", function(event){
                description.style.display = "block";
                console.log(event.target)

            })
            img_title.addEventListener("mouseout", function(){
                description.style.display = 'none';
                description.style.backgroundColor = 'white'
            })


           // affichage += img_title.outerHTML;
            //image.innerHTML = affichage;
            image.appendChild(img_title)
        }  
        
    }))

    // Rechercher un film par son nom
        // get input value 
    function searchMoviesByTitle(title) {
        const url = SEARCHAPI + encodeURIComponent(title);
        return fetch(url)
        .then(response => response.json())
        .then(data => data.results)
        .catch(error => console.error(error));
    }
    
    // Exemple d'utilisation :
    const searchInput = document.querySelector('#search');
    searchInput.addEventListener("change", () => {
        const title = searchInput.value;
        searchMoviesByTitle(title)
        .then(results => console.log(results))
        .catch(error => console.error(error));
    });


})