const Koa = require('koa');
const Router = require('koa-router');
const axios = require('axios');
const cheerio = require('cheerio');
const {Pool} = require('pg')
const puppeteer = require('puppeteer')
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
        // for(let index=0; index <= 36; index++){
        //     var response = await axios.get(`https://french.alibaba.com/g/china-agricultural-machinery${index}.html`)
    
    
        //     var $ = cheerio.load(response.data);  //Parser la reponse html en utilisant cheerio
        //     // console.log(pretty($.html()));
        //     // console.log(pretty($.html()));
        //     // console.log($.html());
    
    
        //     $('.product-card').each((index, element) => {
        //         const material = {
        //             nom: $(element).find('.product-title span').text(),
        //             image_url: $(element).find('a img').attr('src'),
        //             description: $(element).find('.product-title span:eq(1)').text(),
        //             // categorie=; 
        //             prix: $(element).find('.product-price .price-number').text()
        //         };
        //         materials.push(material)
        //         // console.log(materials)
        //     });
            
        //     console.log(materials) 

        // }
        
        // const response = await axios.get("https://www.alibaba.com/premium/agriculture_machine_machinery.html?p4phangyebuliu=1&src=sem_ggl&field=UG&from=sem_ggl&cmpgn=18084521455&adgrp=143584075809&fditm=&tgt=kwd-1729857182300&locintrst=&locphyscl=9067846&mtchtyp=b&ntwrk=g&device=c&dvcmdl=&creative=619614436792&plcmnt=&plcmntcat=&aceid=&position=&gclid=CjwKCAjwzJmlBhBBEiwAEJyLu_pgB19i9oYbDEjbKPnjfnuFdveWHa7yFZjCjAt0extKpke9GIkGJBoC-nMQAvD_BwE");
        // const response = await axios.get("https://www.farmmachinerylocator.co.uk/listings/for-sale/planting-equipment/1103");
        const response = await axios.get("https://www.bossmachinery.nl/en/vehicles?qooqie_creative_id=529003977107&keywords=used%20heavy%20machinery&gad=1&gclid=CjwKCAjwzJmlBhBBEiwAEJyLu_E-a3UkppuQOUCcMuu6UK9BfSuqgiGa1X_9u-zJuhlVCv6F4P-QVxoCCJIQAvD_BwE");
        const $ = cheerio.load(response.data);
        // console.log($.html())

        $('.pure-u-xl-1-3').each((index, element)=>{
            var material = {
                nom: $(element).find('.vehicle-brand').text(),
                description: $(element).find('.vehicle-special-feature').text(),
                prix: $(element).find('.vehicle-price').text(),
                image_url: $(element).find('img').attr('src')
            }
            // console.log(material)
            materials.push(material)
        })
        console.log(materials)
        
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







// const axios = require('axios');
// const cheerio = require('cheerio');
// const puppeteer = require('puppeteer');

// async function scrapeAndScroll() {
//   try {
//     const browser = await puppeteer.launch();
//     const page = await browser.newPage();
//     await page.goto("https://www.bossmachinery.nl/en/vehicles?qooqie_creative_id=529003977107&keywords=used%20heavy%20machinery&gad=1&gclid=CjwKCAjwzJmlBhBBEiwAEJyLu_E-a3UkppuQOUCcMuu6UK9BfSuqgiGa1X_9u-zJuhlVCv6F4P-QVxoCCJIQAvD_BwE");

//     // Scroll to the bottom of the page
//     await autoScroll(page);

//     // Get the updated HTML content after scrolling
//     const htmlContent = await page.content();
//     const $ = cheerio.load(htmlContent);
//     const materials = [];

//     $('.pure-u-xl-1-3').each((index, element) => {
//       const material = {
//         nom: $(element).find('.vehicle-brand').text(),
//         description: $(element).find('.vehicle-special-feature').text(),
//         prix: $(element).find('.vehicle-price').text(),
//         image_url: $(element).find('img').attr('src')
//       };
//       materials.push(material);
//     });

//     console.log(materials);

//     // Close the browser
//     await browser.close();
//   } catch (e) {
//     console.log(e);
//   }
// }

// async function autoScroll(page) {
//   await page.evaluate(async () => {
//     await new Promise((resolve, reject) => {
//       let totalHeight = 0;
//       const distance = 100;
//       const timer = setInterval(() => {
//         const scrollHeight = document.documentElement.scrollHeight;
//         window.scrollBy(0, distance);
//         totalHeight += distance;
//         if (totalHeight >= scrollHeight) {
//           clearInterval(timer);
//           resolve();
//         }
//       }, 100);
//     });
//   });
// }

// scrapeAndScroll();
