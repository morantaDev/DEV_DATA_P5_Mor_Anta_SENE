import React from 'react';
import logo192 from '../images/logo192.png';
import Button from './button';
// import { Link } from 'react-router-dom';
// // import About from './about';
// // import Contacts from './contacts';


const Search = () => {
    return(
        <div className='flex relative'>
            <input className ="rounded-lg px-2" type="text" name='recherche' value="" placeholder='Recherche'/>
            <svg className='my-1 ml-1 mt-1' xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
      </svg>
        </div>
    )
}
const Header = () => { 
    return(
            <div className="sticky top-0 z-50 flex bg-lime-500 py-8 shadow-lg pl-14 shadow-lime-500">
            <img src={logo192} alt="" className="w-8 h-8 mr-2" />
            <span className='text-2xl font-bold font-serif'>ReactProject</span>
            <ul className='flex ml-12'>
                <li className='mt-1 mx-20'><Search /></li>
                <li className='mr-6 my-1 cursor-pointer'>Nos Produits</li>
                <li className='mr-6 my-1 cursor-pointer'>Nos événements à venir</li>
                <li className='mr-6 my-1 cursor-pointer'>contacts</li>
                <li className='mr-6 my-1 cursor-pointer'>A Propos</li>
            </ul>
            <Button />
            </div>
       
    );
}

export default Header;