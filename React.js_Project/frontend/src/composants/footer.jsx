import React from "react";



const Footer = () => { 
    return(
        <footer className="bg-gray-400 mt-6 py-10 text-white text-center">
            <p>&copy; {new Date().getFullYear()} Mor Anta SENE. All rights reserved.</p>
            <p>Contact: info@morantasene_Company.com</p>

        </footer>
    );
};

export default Footer;