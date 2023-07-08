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


async function autoScroll(page) {
  await page.evaluate(async() => {
    await new Promise((resolve, reject) => {
      let totalHeight = 0;
      const distance = 100;
      const maxScrolls = 100; // Maximum number of times to scroll
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

    const maxScrolls = 100; // Maximum number of times to scroll
    let scrolls = 0;

    while (scrolls < maxScrolls) {
      await autoScroll(page);
      scrolls++;

      // Check if there is more content to load
      const scrollHeight = document.documentElement.scrollHeight;
      const totalHeight = 0;
      const distance = 100;

      for (let i = 0; i < distance; i++) {
        const currentHeight = document.documentElement.scrollHeight;
        totalHeight += currentHeight - scrollHeight;
        scrollHeight = currentHeight;
      }

      if (totalHeight < scrollHeight) {
        break;
      }
    }

    const materials = await page.evaluate(() => {
      const materialElements = Array.from(document.querySelectorAll('.pure-u-xl-1-3'));

      return materialElements.map((element) => {
        const nomElement = element.querySelector('.vehicle-brand');
        const descriptionElement = element.querySelector('.vehicle-special-feature');
        const prixElement = element.querySelector('.vehicle-price');
        const imageElement = element.querySelector('img');

        return {
          nom: nomElement ? nomElement.textContent : '',
          description: descriptionElement ? descriptionElement.textContent : '',
          prix: prixElement ? prixElement.textContent : '',
          image_url: imageElement ? imageElement.src : '',
        };
      });
    });

    console.log(materials);

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
