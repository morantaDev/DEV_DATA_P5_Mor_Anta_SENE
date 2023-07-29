const fs = require('fs').promises;
const connection = require('./helpers');

const InsertDatas = async () => {
    try{
        const data = await fs.readFile("./json/jsonFile.json", "utf-8");

        console.log(data)
        for (const dta of JSON.parse(data)) {
          const { name, price, url} = dta;
          const sql = "INSERT INTO products(name, price, url) VALUES(?, ?, ?)"
          const value = [name, price, url]
          connection.query(sql,value, (err, result) => {
            if(err) {
                console.error("Error inserting data:", err);
            } else { 
                console.log("Data inserted successfully!");
            }
          });
        }
        console.log("Data inserted successfully!");
    } catch(err) {
        console.error("Error reading data from the file:", err);
    }
};
  
  
InsertDatas();
  