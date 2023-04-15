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

    const listeDesEnseign = ['Aly', 'Baila', 'Ndoye', 'Mbaye', 'Djiby', 'Seckouba']
    const listeDesSalles = ['101','102', '103', '104', '201', 'incub']
    const listeDesModules = ['ALGO','PHP', 'PYTHON', 'LC', 'JAVASCRIPT', 'JAVA']
    const listeDesClasses = ['L2 GLRS A', 'L2 GLRS B','L2 ETSE', 'L1 A', 'IAGE B', 'L2 CDSD']

    function creationModule(){
        //Revoir les listes ou peut-être utilisé une fonction pour récupérer ce type d'informations
        
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
        add.value = 'submit'
        const resume = document.createElement('button')
        resume.textContent ='Annuler'
        resume.value = 'reset'
        footer.append(add)
        footer.append(resume)
        container1.appendChild(header)
        container1.appendChild(main)
        container1.appendChild(footer)
        content.appendChild(container1)
    }

    //Créer un tableau contenant des la liste des enseignants, la liste des salles, la liste des classes et la liste des modules
    const ENSEIGNANTS = [{1: 'Aly', modals: [3, 4]}, {2: 'Baila', modals:[2]},{3:'Ndoye'},{4:'Mbaye', modals:[2]},{5:'Djiby'}, {6:'Seckouba'}]
    const SALLES = [{1:'101', capacity: 20}, {2:'102', capacity: 20},{3:'103', capacity: 20},{4:'104', capacity: 20},{5:'201', capacity: 40}, {6:'incub', capacity: 30}]
    const CLASSES = [{1:'L2 GLRS A', effectif: 35},{2:'L2 GLRS B', effectif: 35}, {3:'L2 ETSE', effectif: 35}, {4:'L1 A', effectif: 35}, {5:'IAGE B', effectif: 35}, {6:'L2 CDSD', effectif: 35}]
    const MODULES = [{1: 'ALGO'},{2:'PHP'}, {3:'PYTHON'}, {6:'LC'}, {4:'JAVASCRIPT'}, {5:'JAVA'}]
    const JOURS = [{1: 'lundi'}, {2: 'mardi'}, {3: 'mercredi'}, {4: 'jeudi'}, {5: 'vendredi'}, {6: 'samedi'}]
    
    //Gérer la capacité et l'effectif des classes

    let cours = []
    const cours1 = {ensei: 1, sal: 5, clas: 6, mod: 3, heurDebut: 9, heureFin: 13, jour: 1}
    const cours2 = {ensei: 1, sal: 2, clas: 6, mod: 4, heurDebut: 15, heureFin: 17, jour: 3}
    const cours3 = {ensei: 2, sal: 2, clas: 6, mod: 2, heurDebut: 14, heureFin: 17, jour: 1}
    const cours4 = {ensei: 3, sal: 0, clas: 0, mod: 0, heurDebut: 0, heureFin: 0, jour: 0}
    const cours5 = {ensei: 4, sal: 6, clas: 6, mod: 6, heurDebut: 8, heureFin: 10, jour: 4}
    const cours6 = {ensei: 0, sal: 0, clas: 0, mod: 0, heurDebut: 0, heureFin: 0, jour: 0}
    const cours7 = {ensei: 0, sal: 0, clas: 0, mod: 0, heurDebut: 0, heureFin: 0, jour: 0}


    cours.push(cours1, cours2, cours3, cours4, cours5, cours6, cours7)
    console.log(cours)

    select.addEventListener('change', function(e){
        const indexValue = e.target.value
        console.log(indexValue)

        const titre = document.getElementById('choix')
        console.log(choix)
        titre.innerHTML = ''
        titre.append(indexValue)

        const listeDesCouleurs = ['#D74DD0','#77B6AD', '#89398F', '#8C3691', '#D76164', '#F69229', '#BE8487', '#3CADEB', '#D76164', '#F78002', '#0BA00F']
        let COLOR = listeDesCouleurs[Math.floor(Math.random() * 10)]
        
        setInterval(function(){
            COLOR = listeDesCouleurs[Math.floor(Math.random() * 10)]
        }, 1000)
    

        for (let i = 0; i < ENSEIGNANTS.length; i++) {
            const teacher = ENSEIGNANTS.find(element => element[i] == indexValue)
            const room = SALLES.find(element => element[i] == indexValue)
            const classroom = CLASSES.find(element => element[i] == indexValue)
            const modle = MODULES.find(element => element[i] == indexValue)


            if(teacher){
                console.log(teacher)
                const teacherId = Object.keys(teacher)[0]
                console.log(teacherId)
                const courses = cours.filter(element => element.ensei == teacherId)
                console.log(courses)

                //Récupéper la classe, la salle, le module
                courses.forEach(course => {

                    const classId = course.clas
                    console.log(classId)
                    
                    const dictClass = CLASSES.find(element =>  Object.keys(element)[0] == course.clas)
                    const classVALUE = dictClass[course.clas]
                    console.log(classVALUE)
                    const dictSalle = SALLES.find(element => Object.keys(element)[0] == course.sal)
                    const salVALUE = dictSalle[course.sal]
                    console.log(salVALUE)
                    const dictMod = MODULES.find(element => Object.keys(element)[0] == course.mod)
                    const modVALUE = dictMod[course.mod]
                    console.log(modVALUE)
                    const dictJour = JOURS.find(element => Object.keys(element)[0] == course.jour)
                    const jourVALUE = dictJour[course.jour]
                    console.log(jourVALUE)
                    
                    const HeureDebut = course.heurDebut
                    const HeureFin = course.heureFin
                    // console.log(HeureFin)
    
                    const duree = HeureFin - HeureDebut
                    const marge = HeureDebut - 8
                    createCours(classVALUE, modVALUE, salVALUE, jourVALUE, duree, marge, COLOR)
                })

            } else if (room){
                console.log(room)
                const roomId = Object.keys(room)[0]
                console.log(roomId)
                const courses = cours.filter(element => element.sal == roomId)
                console.log(courses)

                //Récupéper la classe, le nom, le module

                // const classId = courses.clas
                // console.log(classId)
                courses.forEach(course => {
                    const dictClass = CLASSES.find(element =>  Object.keys(element)[0] == course.clas)
                    const classVALUE = dictClass[course.clas]
                    console.log(classVALUE)
    
                    const dictNom = ENSEIGNANTS.find(element => Object.keys(element)[0] == course.ensei)
                    const teacherVALUE = dictNom[course.ensei]
                    console.log(teacherVALUE)
    
                    const dictMod = MODULES.find(element => Object.keys(element)[0] == course.mod)
                    const modVALUE = dictMod[course.mod]
                    console.log(modVALUE)
    
                    const dictJour = JOURS.find(element => Object.keys(element)[0] == course.jour)
                    const jourVALUE = dictJour[course.jour]
                    console.log(jourVALUE)
                    
                    const HeureDebut = course.heurDebut
                    const HeureFin = course.heureFin
                    // console.log(HeureFin)
    
                    const duree = HeureFin - HeureDebut
                    const marge = HeureDebut - 8
                    createCours(classVALUE, teacherVALUE, modVALUE, jourVALUE, duree, marge, COLOR)
                })
            }else if(classroom){
                console.log(classroom)
                const classRoomId = Object.keys(classroom)[0]
                console.log(classRoomId)
                const courses = cours.filter(element => element.clas == classRoomId)
                console.log(courses)

                //Récupéper le nom, le module , la salle

                courses.forEach(course => {
                    const dictNom = ENSEIGNANTS.find(element => Object.keys(element)[0] == course.ensei)
                    const teacherVALUE = dictNom[course.ensei]
                    console.log(teacherVALUE)
    
                    const dictMod = MODULES.find(element => Object.keys(element)[0] == course.mod)
                    const modVALUE = dictMod[course.mod]
                    console.log(modVALUE)
    
                    const dictSalle = SALLES.find(element => Object.keys(element)[0] == course.sal)
                    const salVALUE = dictSalle[course.sal]
                    console.log(salVALUE)
    
    
                    const dictJour = JOURS.find(element => Object.keys(element)[0] == course.jour)
                    const jourVALUE = dictJour[course.jour]
                    console.log(jourVALUE)
                    
                    const HeureDebut = course.heurDebut
                    const HeureFin = course.heureFin
                    // console.log(HeureFin)
    
                    const duree = HeureFin - HeureDebut
                    const marge = HeureDebut - 8
                    createCours(teacherVALUE, modVALUE, salVALUE, jourVALUE,duree, marge, COLOR)
                })

            }else if(modle){
                console.log(modle)
                const modleId = Object.keys(modle)[0]
                console.log(modleId)
                const courses = cours.filter(element => element.mod == modleId)
                console.log(courses)

                //Récupéper la classe, le nom , la salle
                courses.forEach(course => {
                    const dictClass = CLASSES.find(element =>  Object.keys(element)[0] == course.clas)
                    const classVALUE = dictClass[course.clas]
                    console.log(classVALUE)
    
                    const dictNom = ENSEIGNANTS.find(element => Object.keys(element)[0] == course.ensei)
                    const teacherVALUE = dictNom[course.ensei]
                    console.log(teacherVALUE)
    
                    const dictSalle = SALLES.find(element => Object.keys(element)[0] == course.sal)
                    const salVALUE = dictSalle[course.sal]
                    console.log(salVALUE)
    
    
                    const dictJour = JOURS.find(element => Object.keys(element)[0] == course.jour)
                    const jourVALUE = dictJour[course.jour]
                    console.log(jourVALUE)
                    
                    const HeureDebut = course.heurDebut
                    const HeureFin = course.heureFin
                    // console.log(HeureFin)
    
                    const duree = HeureFin - HeureDebut
                    const marge = HeureDebut - 8
    
                    createCours(classVALUE, teacherVALUE, salVALUE, jourVALUE, duree, marge, COLOR)

                })
                
            }
            
        }
    })

    //Trouver le cours correpondant à l'enseignant ayant l'identifiant 1
    const coursAly  = cours.find(cours => cours.ensei === 1)
    console.log(coursAly)

    //Trouver le nom de l'enseignant correspondant

    const enseignantAly = ENSEIGNANTS.find(enseigna => enseigna[1] === 'Aly')

    //Afficher le nom de l'enseignant correspondant
    console.log(enseignantAly[1])

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
    
    // plusDays.forEach(day => {
    //     day.addEventListener('click', function(){
    //         creationModule()
    //     })
    // })
    function createCours(element1, element2, element3, day, duree, marge, couleur){
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
        section.style.width = `${9 * duree}%`
        section.style.marginLeft = `${9 * marge}%`
        section.style.backgroundColor = `${couleur}`
        // const days = document.querySelectorAll(`.${day}`)
        // days.forEach((day) => day.appendChild(section))
        document.querySelector(`#${day}`).appendChild(section)
    }
})