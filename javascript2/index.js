document.addEventListener('DOMContentLoaded', function(){
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

    //Fonction qui récupère les clés des objets
    function getKeyByValue(obj, value) {
        for (let prop in obj) {
          if (obj.hasOwnProperty(prop)) {
            if (obj[prop] === value)
              return prop;
          }
        }
      }

    function creationModule(){
        //Revoir les listes ou peut-être utilisé une fonction pour récupérer ce type d'informations
        
        listheureDebut = ['Choisir une Heure', '8H', '9H', '10H', '11H', '12H', '13H', '14H', '15H', '16H', '17H']
        listheureFin = ['Choisir une Heure','9H', '10H', '11H', '12H', '13H', '14H', '15H', '16H', '17H']

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
        const module = document.createElement('span')
        module.textContent = "module"
        section1.append(module)
        const selectModule = document.createElement('select')
        // selectModule.setAttribute('id','selectModule')
        for (let i = 0; i < listeDesModules.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesModules[i]}`
            selectModule.append(option)
        }
        section1.appendChild(selectModule)

        const section2 = document.createElement('section')
        section2.classList.add('modalEnseign')
        const enseign = document.createElement('span')
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
        const salle = document.createElement('span')
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
        const debut = document.createElement('span')
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
        const fin = document.createElement('span')
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
        add.setAttribute('id', 'add')
        const resume = document.createElement('button')
        resume.textContent ='Annuler'
        resume.setAttribute('id', 'resume')
        footer.append(add)
        footer.append(resume)
        container1.appendChild(header)
        container1.appendChild(main)
        container1.appendChild(footer)
        content.appendChild(container1)
    }
    

    //Créer un tableau contenant des la liste des enseignants, la liste des salles, la liste des classes et la liste des modules
    const ENSEIGNANTS = [{},{1: 'Aly', modals: [3, 4]}, {2: 'Baila', modals:[2]},{3:'Ndoye', modals: [2]},{4:'Mbaye', modals:[6]},{5:'Djiby'}, {6:'Seckouba'}]
    const SALLES = [{},{1:'101', capacity: 20}, {2:'102', capacity: 20},{3:'103', capacity: 20},{4:'104', capacity: 20},{5:'201', capacity: 40}, {6:'incub', capacity: 30}]
    const CLASSES = [{},{1:'L2 GLRS A', effectif: 35},{2:'L2 GLRS B', effectif: 35}, {3:'L2 ETSE', effectif: 35}, {4:'L1 A', effectif: 35}, {5:'IAGE B', effectif: 35}, {6:'L2 CDSD', effectif: 35}]
    const MODULES = [{},{1: 'ALGO'},{2:'PHP'}, {3:'PYTHON'}, {6:'LC'}, {4:'JAVASCRIPT'}, {5:'JAVA'}]
    const JOURS = [{},{1: 'lundi'}, {2: 'mardi'}, {3: 'mercredi'}, {4: 'jeudi'}, {5: 'vendredi'}, {6: 'samedi'}]
    
    //Gérer la capacité et l'effectif des classes

    let currentCours = {}

    let cours = [
        {ensei: 1, sal: 5, clas: 6, mod: 3, heurDebut: 9, heureFin: 13, jour: 1},
        {ensei: 1, sal: 2, clas: 6, mod: 4, heurDebut: 15, heureFin: 17, jour: 3},
        {ensei: 2, sal: 2, clas: 6, mod: 2, heurDebut: 14, heureFin: 17, jour: 1},
        {ensei: 3, sal: 0, clas: 0, mod: 0, heurDebut: 0, heureFin: 0, jour: 0},
        {ensei: 4, sal: 6, clas: 6, mod: 6, heurDebut: 8, heureFin: 10, jour: 4},
        {ensei: 0, sal: 0, clas: 0, mod: 0, heurDebut: 0, heureFin: 0, jour: 0},
        {ensei: 0, sal: 0, clas: 0, mod: 0, heurDebut: 0, heureFin: 0, jour: 0}
    ]

    select.addEventListener('click', function(e){
        // const parent = document.querySelector('.content');
        // const children = document.querySelectorAll('.divCours');

        // children.forEach(child => {
        //     parent.removeChild(child);
        // });

        const clasValue = e.target.value
        console.log(clasValue)
        const obClas = CLASSES.find(element=>Object.values(element)[0]==clasValue)
        console.log(obClas)
        const clasKey = getKeyByValue(obClas, clasValue)
        console.log(clasKey)

        currentCours.clas = parseInt(clasKey)
        // currentCours.clas = parseInt(clasKey)

        

        const listeDesCouleurs = ['#D74DD0','#77B6AD', '#89398F', '#8C3691', '#D76164', '#F69229', '#BE8487', '#3CADEB', '#D76164', '#F78002', '#0BA00F']
        let COLOR = listeDesCouleurs[Math.floor(Math.random() * 10)]
        
        setInterval(function(){
            COLOR = listeDesCouleurs[Math.floor(Math.random() * 10)]
        }, 1000)
    

        const teacher = ENSEIGNANTS.find(element => Object.values(element)[0] == e.target.value)
        const room = SALLES.find(element => Object.values(element)[0]== e.target.value)
        const classroom = CLASSES.find(element => Object.values(element)[0]== e.target.value)
        const modle = MODULES.find(element => Object.values(element)[0]== e.target.value)


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
                drawCourse(classVALUE, modVALUE, salVALUE, jourVALUE, duree, marge, COLOR)
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
                drawCourse(classVALUE, teacherVALUE, modVALUE, jourVALUE, duree, marge, COLOR)
            })
        }else if(classroom){
            console.log(classroom)
            const classRoomId = Object.keys(classroom)[0]
            console.log(classRoomId)
            const courses = cours.filter(element => element.clas == classRoomId)
            console.log(courses)


            // if(course.length > 0){}

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
                drawCourse(teacherVALUE, modVALUE, salVALUE, jourVALUE,duree, marge, COLOR)
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

                drawCourse(classVALUE, teacherVALUE, salVALUE, jourVALUE, duree, marge, COLOR)
            })
            
        }
        // for (let i = 1; i < ENSEIGNANTS.length; i++) {
            
        // }
    })

    plusDays.forEach(plusDay => {
        plusDay.addEventListener('click', function(event){
            const selectElement =  event.target.parentElement.parentElement.id
            console.log(selectElement)

            creationModule()

            const jour = selectElement
            const obJour  = JOURS.find(element => Object.values(element)==jour)
            console.log(Object.keys(obJour))
            const idJour = parseInt(Object.keys(obJour)[0])
            console.log(idJour)

            currentCours.jour = idJour

            const selectModal = document.querySelector('.modalModule select')
            console.log(selectModal)
            selectModal.addEventListener('change', function(e){
                const moduleValue = e.target.value 
                console.log(moduleValue)

                const modalHeader = document.querySelector('#modalHeader')
                modalHeader.textContent = ''
                modalHeader.textContent = moduleValue
                const ObjMod = MODULES.find(element => Object.values(element)==moduleValue)

                
                const modKey = getKeyByValue(ObjMod, moduleValue)
                console.log(modKey)
                currentCours.mod = parseInt(modKey)

                
                const enseign = ENSEIGNANTS.filter(element => element.modals?.includes(parseInt(modKey)))
                console.log(enseign)


                const selectTeacher = document.querySelector('.modalEnseign select')
                selectTeacher.innerHTML = ''
                enseign.forEach(element => {
                    const option = document.createElement('option')
                    option.setAttribute('value', Object.values(element)[0])
                    option.textContent = Object.values(element)[0]
                    selectTeacher.appendChild(option)
                })

                selectTeacher.addEventListener('click', function(e){
                    const ensValue = e.target.value
                    console.log(ensValue)
                    const ObEns = enseign.find(element => Object.values(element)[0] == ensValue)
                    console.log(ObEns)
                    const ensKey = getKeyByValue(ObEns, ensValue)
                    console.log(ensKey)
                    
                    currentCours.ensei = parseInt(ensKey)
                })

            })

            const selectSalle = document.querySelector('.modalSalle select')
            selectSalle.addEventListener('click', function(e){
                const salValue = e.target.value
                console.log(salValue)
                const ObSalle = SALLES.find(element => Object.values(element)[0]==salValue)
                const salCapacite = ObSalle.capacity
                console.log(salCapacite)
                console.log(ObSalle)
                const salKey = getKeyByValue(ObSalle, salValue)
                console.log(salKey)
                
                
                console.log(currentCours.clas)
                const clasOb = CLASSES.find(element => Object.keys(element)[0]==currentCours.clas)
                console.log(clasOb.effectif)

                if(parseInt(clasOb.effectif) <= parseInt(ObSalle.capacity)){
                    currentCours.sal = parseInt(salKey)
                }else{
                    alert("La salle ne peut pas contenir l'effectif de cette classe")
                }
                
            })

            const selectDebut = document.querySelector('.modalBegin select')
            selectDebut.addEventListener('click', function(e){
                const debutValue = e.target.value
                // console.log(debutValue)

                begin = debutValue
                if(begin.length == 2){
                    begin = parseInt(begin.charAt(0))
                }else{
                    begin = parseInt(begin.match(/\d+/)[0]);
                }
                console.log(begin)

                currentCours.heurDebut = parseInt(begin)

                const selectFin = document.querySelector('.modalEnd select')
                selectFin.innerHTML = ''
                const taille = 17-begin
                const option = document.createElement('option')
                option.textContent = 'Choisir une heure de fin'
                selectFin.appendChild(option)
                for (let i = 1; i <= taille; i++) {
                    const option = document.createElement('option')
                    option.setAttribute('value', i)
                    option.textContent = begin+i + 'H'

                    selectFin.appendChild(option)
                }

                
            })
            const selectFin = document.querySelector('.modalEnd select')
            selectFin.addEventListener('click', function(e){
                const finValue = e.target.value
                // console.log(finValue)

                End = finValue
                if(End.length == 2){
                    End = parseInt(End.charAt(0))
                }else{
                    End = parseInt(End.match(/\d+/)[0]);
                }
                console.log(End)

                currentCours.heureFin = parseInt(End)+8
            })


            const modal = document.querySelector('.modal')
            const annuler = document.querySelector('#resume')
            const ajout = document.querySelector('#add')
            annuler.addEventListener('click', function(){
                // modal.style.display = 'none'
                content.removeChild(modal)
            })
        

            
            ajout.addEventListener('click', function(){
                cours.push(currentCours)
                content.removeChild(modal)
                console.log(currentCours)
                const duree = parseInt(currentCours.heureFin)+1 - parseInt(currentCours.heurDebut)
                const marge = currentCours.heurDebut - 8
                const color = '#77B6AD'
                //
                

                drawCourse(Object.values(ENSEIGNANTS[currentCours.ensei])[0], Object.values(MODULES[currentCours.mod])[0], Object.values(SALLES[currentCours.sal])[0],Object.values(JOURS[currentCours.jour])[0], duree, marge, color)
                cours.push(currentCours)
                console.log(cours)
            })
        })

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
            option.setAttribute('value', `${listeDesEnseign[i]}`+1)
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

    classes.addEventListener('click', function(e){

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
        
        // const selectClasse = document.querySelector('.')
        
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
    function drawCourse(element1, element2, element3, day, duree, marge, couleur){
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
        
        document.querySelector(`#${day}`).appendChild(section)
    }

    
})