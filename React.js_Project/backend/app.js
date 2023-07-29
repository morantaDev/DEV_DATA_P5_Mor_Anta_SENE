const express = require('express'); 
const cors = require('cors');
const app = express();

const productRoutes = require('./router/index');

app.get('/', async(req, res, next) =>{
    res.status(200).json({
        message: 'Hello, World'
    });
    // res.send('Hello, World');
})
app.use("/products", productRoutes);
// app.use(
//     cors({
//       origin: 'http://localhost:3000', // Replace with your frontend URL
//     })
   
// );
// app.use(cors({
//     origin: 'http://localhost:3000',
//     credentials: true,
// }));

// app.use(cors({
// origin: 'http://localhost:3000',
// methods: ['GET', 'POST', 'PUT', 'DELETE'],
// }));

// app.use(cors({
// origin: 'http://localhost:3000',
// allowedHeaders: ['Authorization', 'Content-Type'],
// }));
  
  

module.exports = app;