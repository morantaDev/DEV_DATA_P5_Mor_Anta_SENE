const Koa = require('koa');
const Router = require('koa-router');
const axios = require('axios');
const cheerio = require('cheerio');
const {Pool} = require('pg')
const pretty = require('pretty')

const pool = new Pool({
    user:'moranta21',
    password:'Wizzle21#',
    host:'localhost',
    database:'my_database',
    port: 5542
});

async function scrapeAndInsertData(){
    try{
        // const response = await axios.get("https://www.terre-net-occasions.fr/tracteur/c1");
        // const response = await axios.get("https://www.agriaffaires.com/occasion/1/tracteur-agricole.html")
        materials=[]
        for(let index=0; index <= 36; index++){
            var response = await axios.get(`https://french.alibaba.com/g/china-agricultural-machinery${index}.html`)
    
    
            var $ = cheerio.load(response.data);  //Parser la reponse html en utilisant cheerio
            // console.log(pretty($.html()));
            // console.log(pretty($.html()));
            // console.log($.html());
    
    
            $('.product-card').each((index, element) => {
                const material = {
                    nom: $(element).find('.product-title span').text(),
                    image_url: $(element).find('a img').attr('src'),
                    description: $(element).find('.product-title span:eq(1)').text(),
                    // categorie=; 
                    prix: $(element).find('.product-price .price-number').text()
                };
                materials.push(material)
                // console.log(materials)
            });
            
            console.log(materials) 

        }
    }catch(e){
        console.log(e)
    }
}
scrapeAndInsertData();

// const axios = require('axios')

// const endpoint = 'https://api.withleaf.io/api/authenticate'

// const data = { username:'morantadev@gmail.com', password:'Wizzle21#', rememberMe:'true'}

// axios.post(endpoint, data)
//     .then(res => console.log(res.data))
//     .catch(console.error)

// const TOKEN = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJtb3JhbnRhZGV2QGdtYWlsLmNvbSIsImF1dGgiOiJST0xFX1VTRVIiLCJpYXQiOjE2ODg0NzI5NzQsImV4cCI6MTY5MTA2NDk3NH0.2u2uWM0WCBIvqae_M_Utky7If6B1p0Bk7dEggSrzw1p--Qy0IeZcKBoYBiYlpmBNmRl7y54ml6x2WUbok5gjkw'   

// const endpoint ='https://api.withleaf.io/services/operations/api/files'
// const headers = { 'Authorization': `Bearer ${TOKEN}` }

// axios.get(endpoint, { headers })
//     .then(res => console.log(res.data))
//     .catch(console.error)


const app = new Koa();
const router = new Router();

router.get('/', async (ctx) => {
    ctx.body = "Hello, World";

})
router.get('/about', async (ctx) => {
    ctx.body = 'This is the about page';
  });
// app.use(async (ctx) =>{
//     ctx.body = "Hello, World"
// })

app.use(router.routes());

// app.use(router.routes()).use(router.allowedMethods());

module.exports =app;