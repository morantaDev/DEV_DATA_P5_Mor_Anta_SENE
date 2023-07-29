const mysql = require('mysql2/promise'); // Use 'mysql2/promise' for the promise-based version

// Create a MySQL connection pool
const pool = mysql.createPool({
  host: 'localhost',
  user: 'phpmyadmin',
  password: 'Wizzle21#',
  database: 'reactDB',
  connectionLimit: 10, // Adjust the connection limit as needed
});

// Connect to the MySQL server
pool.getConnection()
  .then((connection) => {
    console.log('Connected to MySQL database');
    // pool.release(); // Release the connection after connecting
  })
  .catch((err) => {
    console.error('Error connecting to MySQL database', err);
  });

// Export the pool for use in other modules
module.exports = pool;
