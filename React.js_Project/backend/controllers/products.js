const express = require('express');
const connection = require("../helpers")



const mesProduits = async (req, res) => {
    try{
        const [products]  = await connection.query('SELECT * FROM products')
        // connection.release;
        res.json(products);
    }catch (error){
        console.error("There is an error when trying to get products", error)
    }
}

module.exports = {
    mesProduits
}
