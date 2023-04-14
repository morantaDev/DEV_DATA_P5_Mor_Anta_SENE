document.addEventListener('DOMContentLoaded', function(){
    const body = document.querySelector('body')
    const toggle1 = document.querySelector('.toggle1')
    const toggle2 = document.querySelector('.toggle2')
    const content = document.querySelector('.content')
    const dayName = document.querySelectorAll('.name')
    const daySection = document.querySelectorAll('.jour')
    const sidebar = document.querySelector('.sidebar')
    const tables = document.querySelectorAll('.table')
    const allSpan = document.querySelectorAll('.table span')
    const search = document.querySelector('#search')
    const container =document.querySelector('.container')
    const navbar = document.querySelector('.navbar')
    const header = document.querySelector('h1')
    const select = document.querySelector('#select')
    const enseignants = document.querySelector('#enseign')
    const salles = document.querySelector('#salles')
    const classes = document.querySelector('#classes')
    const modules = document.querySelector('#modules')
    const plusDays = document.querySelectorAll('.plusDay')
    console.log(allSpan)
    console.log(toggle2)

    container.style.backgroundColor = '#5F5F5F';
    toggle1.style.display = 'none'

    $('.toggle2').click(function(){
           $(".toggle2").toggle() 
           $(".toggle1").toggle()

           //Vérifier si le deuxième button est visible et mettre de la couleur
           if($(".toggle1").is(":visible")){
            container.style.backgroundColor = 'none'
            content.style.backgroundColor = '#F0AFB1'
            // toggle2.style.color = 'black'
            toggle1.style.color = 'black'
            dayName.forEach(day => {
                day.style.backgroundColor = '#EE9A9F'
                day.style.color = 'black'
            });
            // dayName.style.backgroundColor = '#EE9A9F'
            sidebar.style.backgroundColor = '#B7C3CD'

            tables.forEach(table => {
             table.style.backgroundColor = "#DBE0E5"
             table.querySelector('.title').style.color = 'black'
             
            });

            allSpan.forEach(span=>{
                span.style.color = 'black'
            })

            daySection.forEach(section =>{
                section.style.backgroundColor = '#C1BFC8'
            })
            search.style.backgroundColor = '#D0DCDF'
            header.style.color = 'black'
            navbar.style.backgroundColor = '#B7C3CD'
            container.style.backgroundColor = '#F4F3F4'
           }
    })
    $('.toggle1').click(function(){
        $(".toggle1").toggle()
        $(".toggle2").toggle()
        
        //Vérifier si le premier button est visible et annulé les couleurs précédentes
        if($('.toggle2').is(":visible")){
            container.style.backgroundColor = 'none'
            content.style.backgroundColor = ''
            dayName.forEach(day => {
                day.style.backgroundColor = ''
                day.style.color = ''
            });
            sidebar.style.backgroundColor = ''

            tables.forEach(table => {
             table.style.backgroundColor = ""
             table.querySelector('.title').style.color = ''
             
            });

            allSpan.forEach(span=>{
                span.style.color = 'white'
            })

            daySection.forEach(section =>{
                section.style.backgroundColor = ''
            })
            search.style.backgroundColor = ''
            header.style.color = ''
            navbar.style.backgroundColor = ''
            container.style.backgroundColor = ''
        }
    })


    function creationModule(){
        listeDesEnseign = ['','Aly', 'Balla', 'Ndoye', 'Mbaye', 'Djiby', 'Seckouba']
        listeDesSalles = ['Choisir une Salle','101','102', '103', '104', '201', 'incub']
        listeDesModules = ['Choisir un Module','ALGO','PHP', 'PYTHON', 'LC', 'JAVASCRIPT', 'JAVA']
        listheureDebut = ['Choisir une Heure', '8H', '9H', '10H', '11H', '12H', '13H', '14', '15H', '16', '17H']
        listheureFin = ['Choisir une Heure','9H', '10H', '11H', '12H', '13H', '14', '15H', '16', '17H']

        // listeDesClasses = ['Classes', 'L2 GLRS A', 'L2 GLRS B', 'L2 ETSE', 'L1 A', 'IAGE B', 'L2 CDSD']
        
        const container1 = document.createElement('div')
        container1.classList.add('modal')
        const header = document.createElement('header')
        header.setAttribute('id', 'modalHeader')
        header.textContent = "Modal Title"
        const main = document.createElement('main')
        main.classList.add('mainModal')

        const section1 = document.createElement('section')
        section1.classList.add('modalModule')
        const module = document.createElement('p')
        module.textContent = "module"
        section1.append(module)
        const selectModule = document.createElement('select')
        for (let i = 0; i < listeDesModules.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesModules[i]}`
            selectModule.append(option)
        }
        section1.appendChild(selectModule)

        const section2 = document.createElement('section')
        section2.classList.add('modalEnseign')
        const enseign = document.createElement('p')
        enseign.textContent = "Enseignant"
        section2.append(enseign)
        const selectEnseign = document.createElement('select')
        let count = 0
        for (let i = 0; i < listeDesEnseign.length; i++) {
            const option = document.createElement('option')
            option.setAttribute('id', `${count}`)
            option.textContent = `${listeDesEnseign[i]}`
            selectEnseign.append(option)
            count++;
        }
        section2.appendChild(selectEnseign)

        const section3 = document.createElement('section')
        section3.classList.add('modalSalle')
        const salle = document.createElement('p')
        salle.textContent = "Salle"
        section3.append(salle)
        const selectSalle = document.createElement('select')
        for (let i = 0; i < listeDesSalles.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesSalles[i]}`
            selectSalle.append(option)
        }
        section3.appendChild(selectSalle)

        const section4 = document.createElement('section')
        section4.classList.add('modalBegin')
        const debut = document.createElement('p')
        debut.textContent = "Heure de Début"
        section4.append(debut)
        const selectDebut = document.createElement('select')
        for (let i = 0; i < listheureDebut.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listheureDebut[i]}`
            selectDebut.append(option)
        }
        section4.appendChild(selectDebut)

        const section5 = document.createElement('section')
        section5.classList.add('modalEnd')
        const fin = document.createElement('p')
        fin.textContent = "Heure de Fin"
        section5.append(fin)
        const selectFin = document.createElement('select')
        for (let i = 0; i < listheureFin.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listheureFin[i]}`
            selectFin.append(option)
        }
        section5.appendChild(selectFin)

        main.appendChild(section1)
        main.appendChild(section2)
        main.appendChild(section3)
        main.appendChild(section4)
        main.appendChild(section5)

        const footer = document.createElement('footer')
        const add = document.createElement('button')
        add.textContent = 'Ajouter'
        const resume = document.createElement('button')
        resume.textContent ='Annuler'
        footer.append(add)
        footer.append(resume)
        container1.appendChild(header)
        container1.appendChild(main)
        container1.appendChild(footer)
        content.appendChild(container1)
    }

    //Créer un tableau contenant des la liste des enseignants, la liste des salles, la liste des classes et la liste des modules
    listeDesEnseign = ['Aly', 'Baila', 'Ndoye', 'Mbaye', 'Djiby', 'Seckouba']
    listeDesSalles = ['101','102', '103', '104', '201', 'incub']
    listeDesClasses = ['L2 GLRS A', 'L2 GLRS B', 'L2 ETSE', 'L1 A', 'IAGE B', 'L2 CDSD']
    listeDesModules = ['ALGO','PHP', 'PYTHON', 'LC', 'JAVASCRIPT', 'JAVA']


    const ENSEIGNANT1 = {nom: 'Aly', salle: '201', classe: 'L2 CDSD', module: 'PYTHON'}
    const ENSEIGNANT2 = {nom: 'Aly', salle: '102', classe: 'L2 CDSD', module: 'JAVASCRIPT'}
    const ENSEIGNANT3 = {nom: 'Baila', salle: '102', classe: 'L2 CDSD', module: 'PHP'}
    const ENSEIGNANT4 = {nom: 'Ndoye', salle: '201', classe: '', module: 'PYTHON'}
    const ENSEIGNANT5 = {nom: 'Mbaye', salle: 'incub', classe: 'L2 CDSD', module: 'LC'}
    const ENSEIGNANT6 = {nom: 'Djiby', salle: '201', classe: '', module: 'PYTHON'}
    const ENSEIGNANT7 = {nom: 'Seckouba', salle: '201', classe: '', module: 'PYTHON'}

    const ENSEIGNANTS = [ENSEIGNANT1, ENSEIGNANT2, ENSEIGNANT3, ENSEIGNANT4,ENSEIGNANT5, ENSEIGNANT6, ENSEIGNANT7]

    let compteurId = 1
    for (let i = 0; i < ENSEIGNANTS.length; i++) {
        localStorage.setItem(`${compteurId}`, JSON.stringify(ENSEIGNANTS[i]))
        compteurId++
    }

    const titre = document.getElementById('choix')
    console.log(choix)
    

    select.addEventListener('click', function(e){
        titre.innerHTML =''
        titre.innerHTML = e.target.value
        console.log(titre)
        // const indexElement = e.target.selectedIndex;
        // console.log(indexElement)
        const indexValue = e.target.value
        console.log(indexValue)

        // var getData = localStorage.getItem(indexElement)
        // const liste = JSON.parse(getData)

        // console.log(liste)
        // console.log(liste.classe)

        localStorage.removeItem('compteurId')
        const localStorageData = [];

        for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        localStorageData.push(JSON.parse(localStorage.getItem(key)));
        }

        console.log(localStorageData);

        const listeDesCouleurs = ['#D74DD0','#77B6AD', '#89398F', '#8C3691', '#D76164', '#F69229', '#BE8487', '#3CADEB', '#D76164', '#F78002', '#0BA00F']
        let COLOR = listeDesCouleurs[Math.floor(Math.random() * 10)]

        setInterval(function(){
            COLOR = listeDesCouleurs[Math.floor(Math.random() * 10)]
        }, 1000)


        for(id in localStorageData) {
            if (localStorageData[id].nom == indexValue){
                console.log(localStorageData[id].salle)
                console.log(localStorageData[id].module)
                console.log(localStorageData[id].classe)
                // const allDivCours = document.querySelectorAll('.divCours')
                // allDivCours.forEach(divCours => {
                // })
                if(localStorageData[id].module == 'JAVASCRIPT' && indexValue == 'Aly'){
                    createCours(localStorageData[id].salle, localStorageData[id].module, localStorageData[id].classe,'#mercredi', 2, 8,COLOR)
                } 
                if(localStorageData[id].module == 'PYTHON' && indexValue == 'Aly'){

                    createCours(localStorageData[id].salle, localStorageData[id].module, localStorageData[id].classe,'#lundi', 4, 1,COLOR)
                }
                if (indexValue == 'Baila'){
                    createCours(localStorageData[id].salle, localStorageData[id].module, localStorageData[id].classe,'#lundi', 3, 6,COLOR)
                }
                if (indexValue == 'Mbaye'){
                    createCours(localStorageData[id].salle, localStorageData[id].module, localStorageData[id].classe,'#jeudi', 2, 0,COLOR)
                }

            } else if (localStorageData[id].salle == indexValue){
                // alert('la salle existe dans la base de données')
                console.log(localStorageData[id].nom)
                console.log(localStorageData[id].classe)
                console.log(localStorageData[id].module)
                createCours(localStorageData[id].nom, localStorageData[id].classe, localStorageData[id].module, '#mardi', 3, 0,COLOR)
                const divCours = document.querySelectorAll('.divCours')
                const pCoursId = document.querySelectorAll('#pCours')
                const pCours = document.querySelectorAll('.pCours')
                divCours.forEach(div => {

                    //Ajouter un tableau de couleurs et ajouter une couleur de fond aléatoirement
                    // div.style.backgroundColor = 'blue'
                    pCoursId.forEach(pCoursid => {
                        pCoursid.style.color = 'white'
                    });
                    pCours.forEach(pcours => {
                        pcours.style.color = 'white'
                    })
                })
            } else if (localStorageData[id].classe == indexValue){
                // alert('la classe existe dans la base de données')
                console.log(localStorageData[id].nom)
                console.log(localStorageData[id].salle)
                console.log(localStorageData[id].module)
                if(localStorageData[id].nom=='Aly' && localStorageData[id].module == 'PYTHON'){
                    createCours(localStorageData[id].nom, localStorageData[id].salle, localStorageData[id].module, '#lundi', 4, 1,COLOR)
                } 
                if(localStorageData[id].nom=='Aly' && localStorageData[id].module == 'JAVASCRIPT'){
                    createCours(localStorageData[id].nom, localStorageData[id].salle, localStorageData[id].module, '#mercredi', 2, 8,COLOR)
                }
                if(localStorageData[id].nom=='Baila'){
                    createCours(localStorageData[id].nom, localStorageData[id].salle, localStorageData[id].module, '#lundi', 3, 1,COLOR)
                }
                if(localStorageData[id].nom=='Mbaye'){
                    createCours(localStorageData[id].nom, localStorageData[id].salle, localStorageData[id].module, '#jeudi', 2, 0,COLOR)
                }
            } else if (localStorageData[id].module == indexValue){
                // alert('le module existe dans la base de données')
                const divCours = document.querySelectorAll('.divCours')
                const pCoursId = document.querySelectorAll('#pCours')
                const pCours = document.querySelectorAll('.pCours')
                console.log(localStorageData[id].nom)
                console.log(localStorageData[id].salle)
                console.log(localStorageData[id].classe)
                daySection.forEach(day => {
                    // divCours.forEach(div => {
                    // })
                    // day.removeChild(divCours)
                })
                createCours(localStorageData[id].nom, localStorageData[id].salle, localStorageData[id].classe, '#jeudi', 3, 0)
            }
        }
    })
    //Remplissage de la balise select
    enseignants.addEventListener('click', function(){
        enseignants.style.backgroundColor = '#4EB2D7';
        salles.style.backgroundColor = '';
        classes.style.backgroundColor = '';
        modules.style.backgroundColor = '';
        let count = 0
        select.innerHTML = ""
        const option = document.createElement('option')
        select.appendChild(option)
        for (let i = 0; i < listeDesEnseign.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesEnseign[i]}`
            option.setAttribute('value', `${listeDesEnseign[i]}`)
            console.log(option)
            select.add(option)
            count++;
        }
    })

    salles.addEventListener('click', function(){
        enseignants.style.backgroundColor = '';
        salles.style.backgroundColor = '#2AAA30';
        classes.style.backgroundColor = '';
        modules.style.backgroundColor = '';
        let count = 0;
        // tables.forEach(table => {table.innerHTML = ""})
        select.innerHTML = ""
        const option = document.createElement('option')
        select.appendChild(option)
        for (let i = 0; i < listeDesSalles.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesSalles[i]}`
            option.setAttribute('id', `${count}`)
            console.log(option)
            select.add(option)
            count++;
        }
    })
    classes.addEventListener('click', function(){
        const selectElement = document.getElementById("select");
        // const selectedOption = selectElement.options[selectElement.selectedIndex];
        // const selectedOptionId = selectedOption.id;
        // console.log(selectedOptionId)
        enseignants.style.backgroundColor = '';
        salles.style.backgroundColor = '';
        classes.style.backgroundColor = '#D98341';
        modules.style.backgroundColor = '';
        let count = 0;
        select.innerHTML = ""
        const option = document.createElement('option')
        select.appendChild(option)
        for (let i = 0; i < listeDesClasses.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesClasses[i]}`
            option.setAttribute('id', `${'option'+count}`)
            console.log(option)
            select.add(option)
            count++;
        }
    })
    modules.addEventListener('click', function(){
        enseignants.style.backgroundColor = '';
        salles.style.backgroundColor = '';
        classes.style.backgroundColor = '';
        modules.style.backgroundColor = '#CC0A33';
        let count = 0; 
        select.innerHTML = ""
        const option = document.createElement('option')
        select.appendChild(option)
        for (let i = 0; i < listeDesModules.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesModules[i]}`
            option.setAttribute('id', `${count}`)
            console.log(option)
            count++;
            select.add(option)
        }
    })
    
    plusDays.forEach(day => {
        day.addEventListener('click', function(){
            creationModule()
        })
    })
  function createCours(element1, element2, element3, day, difference, marge, couleur){
      const section = document.createElement('div')
      section.classList.add('divCours')
      const first = document.createElement('p')
      first.classList.add('pCours')
      first.innerHTML = `${element1}`
      const second = document.createElement('p')
      second.setAttribute('id', 'pCours')
      second.innerHTML = `${element2}`
      const third  = document.createElement('p')
      third.classList.add('pCours')
      third.innerHTML = `${element3}`
      section.append(first)
      section.append(second)
      section.append(third)
    //   const offwidth = section.offsetWidth
    //   console.log(offwidth)
      const larg =  `${difference}`//section.offsetWidth * `${difference}`
      console.log(larg)
      section.style.width = `${9 * difference}%`
      section.style.marginLeft = `${9 * marge}%`
      section.style.backgroundColor = `${couleur}`
      document.querySelector(`${day}`).appendChild(section)
    }
    
})