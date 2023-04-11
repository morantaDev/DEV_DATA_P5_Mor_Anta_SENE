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
        }
    })


    function creationModule(){
        const container1 = document.createElement('div')
        container.classList.add('modal')
        const header = document.createElement('header')
        header.setAttribute('id', 'modalHeader')
        const main = document.createElement('main')
        main.classList.add('main')
        const footer = document.createElement('footer')
        const add = document.createElement('button')
        const resume = document.createElement('button')
        footer.append(add)
        footer.append(resume)
        container1.appendChild(header)
        container1.appendChild(main)
        container1.appendChild(footer)
        // document.body.appendChild(container1)
        // container1.style.display = 'block';
    }

    //Créer un tableau contenant des la liste des enseignants, la liste des salles, la liste des classes et la liste des modules
    listeDesEnseign = ['Enseignants','Aly', 'Balla', 'Ndoye', 'Mbaye', 'Djiby', 'Seckouba']
    listeDesSalles = ['101','102', '103', '104', '201', 'incub']
    listeDesClasses = ['Classes', 'L2 GLRS A', 'L2 GLRS B', 'L2 ETSE', 'L1 A', 'IAGE B', 'L2 CDSD']
    listeDesModules = ['Modules','ALGO','PHP', 'PYTHON', 'LC', 'JAVASCRIPT', 'JAVA']

    
    enseignants.addEventListener('click', function(){
        enseignants.style.backgroundColor = '#4EB2D7';
        for (let i = 0; i < listeDesEnseign.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesEnseign[i]}`
            select.appendChild(option)
        }
        // creationModule()
        // console.log(creationModule());
    })
    salles.addEventListener('click', function(){
        salles.style.backgroundColor = '#2AAA30';
        for (let i = 0; i < listeDesSalles.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesSalles[i]}`
            select.appendChild(option)
        }
    })
    classes.addEventListener('click', function(){
        classes.style.backgroundColor = '#D98341';
        for (let i = 0; i < listeDesClasses.length; i++) {
            const option = document.createElement('option')
                option.textContent = `${listeDesClasses[i]}`
                select.appendChild(option)
        }
    })
    modules.addEventListener('click', function(){
        modules.style.backgroundColor = '#CC0A33';
        for (let i = 0; i < listeDesModules.length; i++) {
            const option = document.createElement('option')
            option.textContent = `${listeDesModules[i]}`
            select.appendChild(option)
        }
    })

    

})