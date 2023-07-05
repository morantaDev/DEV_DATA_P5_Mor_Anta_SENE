// const http = require('http');
// const server = http.createServer(app);
// server.listen(port, ()=>{
//     console.log(`The server is running on port ${port}`);
// })

const app = require("./app");
const port = process.env.PORT || 7000;
app.listen(port);