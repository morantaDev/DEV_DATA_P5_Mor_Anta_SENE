const express = require("express");
const router = express.Router();
const cors = require('cors')
const { mesProduits} = require("../controllers/products");



router.get('/', cors(), mesProduits);


module.exports = router;