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
    function createSection(element, addInHtml){
    let imgFound = document.createElement('section')
        imgFound.classList.add('imageEtTitre')
        let img = document.createElement('IMG')
        img.setAttribute('src', `https://image.tmdb.org/t/p/w1280${element.poster_path}`)
        img.setAttribute('id', 'image')
        let title = document.createElement('div')
        title.setAttribute('id', 'title')
        title_content = `${element.original_title}`
        let vote = document.createElement('span')
        let vote_content = `${element.vote_average}`
        vote.append(vote_content)
        title.append(title_content)
        title.append(vote)
        let description = document.createElement('div')
        let descript_Content = `${element.overview}`
        description.classList.add('descript');
        description.append(descript_Content)
        imgFound.append(img)
        imgFound.append(title)
        imgFound.append(description)
        // console.log(imgFound)
        addInHtml.appendChild(imgFound)

        if (element.vote_average >=6){
            imgFound.querySelector('span').style.color = "green";
        } else if (element.vote_average > 5 && element.vote_average<6) {
            imgFound.querySelector('span').style.color = "orange";
        } else {
            imgFound.querySelector('span').style.color = "red";
        }

        const image_section = imgFound.querySelector('#image')
        const descript = imgFound.querySelector('.descript')
        descript.style.display ="none"
        imgFound.addEventListener('mouseover', function(){
            descript.style.display = "block"
            image_section.style.opacity = 0.3
        })
        imgFound.addEventListener('mouseout', function(){
            descript.style.display = "none"
            image_section.style.opacity = 1
        })
    }

    fetch(APIURL).then(response => response.json().then((data)=> {
        console.log(data);
        for(let objt of data.results){
           createSection(objt, image)

            const searchInput = document.querySelector('#search');
            searchInput.addEventListener("keydown", () => {
            image.innerHTML = ""
            const title = searchInput.value;
            
            
            searchMoviesByTitle(title)
            .then(results => {
                for (element of results) {
                    createSection(element, image)
                }
            })

        })
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
})