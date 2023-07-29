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
    database:'fastapidb',
    port: 5432
});


async function autoScroll(page) {
  await page.evaluate(async () => {
    await new Promise((resolve, reject) => {
      let totalHeight = 0;
      const distance = 100;
      const maxScrolls = 1000; // Maximum number of times to scroll
      let scrolls = 0;

      const timer = setInterval(() => {
        const scrollHeight = document.documentElement.scrollHeight;
        window.scrollBy(0, distance);
        totalHeight += distance;
        scrolls++;

        if (scrolls >= maxScrolls || totalHeight >= scrollHeight) {
          clearInterval(timer);
          resolve();
        }
      }, 100);
    });
  });

  // Scrape the content after scrolling
  const materials = await page.evaluate(() => {
    // page.click('.yes')
    const materialElements = Array.from(document.querySelectorAll('.pure-u-xl-1-3'));

    return materialElements.map((element) => {
      const nomElement = element.querySelector('.vehicle-brand');
      const descriptionElement = element.querySelector('.vehicle-special-feature');
      const prixElement = element.querySelector('.vehicle-price');
      const imageElement = element.querySelector('img');

      const prixText = prixElement ? prixElement.textContent.trim() : '';
      const prix = parseFloat(prixText.replace('€', '').trim());


      return {
        nom: nomElement ? nomElement.textContent : '',
        description: descriptionElement ? descriptionElement.textContent : '',
        prix: isNaN(prix) ? 0 : prix * 1000000,
        image_url: imageElement ? imageElement.src : '',
      };
    });
  });

  console.log(materials);
  console.log(materials.length)

  try{
    const client = await pool.connect();
    const query = 'INSERT INTO puppeteer_materials (nom, description, prix, image_url) VALUES ($1, $2, $3, $4)';
  
    for(const material of materials){
      if(material.nom !==null && material.description !==null && material.prix !==0 && material.image_url !== null &&
        material.image_url !== ''){
        const values = [material.nom, material.description, material.prix, material.image_url];
        await client.query(query, values);
      }
    }
   
    client.release();
    
    console.log('Data inserted successfully into PostgreSQL');
  
  }catch(error){
    console.log('there is an error', error);
  }
  
}

async function scrapeAndInsertData() {
  try {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    await page.goto(
      'https://www.bossmachinery.nl/en/vehicles?qooqie_creative_id=529003977107&keywords=used%20heavy%20machinery&gad=1&gclid=CjwKCAjwzJmlBhBBEiwAEJyLu_E-a3UkppuQOUCcMuu6UK9BfSuqgiGa1X_9u-zJuhlVCv6F4P-QVxoCCJIQAvD_BwE'
    );

    // Scroll to the bottom of the page to load all content
    await autoScroll(page);

    await browser.close();
  } catch (e) {
    console.log(e);
  }
}

if (require.main === module) {
  scrapeAndInsertData();
}




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
