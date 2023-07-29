import React, { useState } from "react";

const ShowAndHide = ({ onClick }) => {
    return (
        <button className="bg-lime-400 z-0 fixed" onClick={onClick}>
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" className="bi bi-arrow-left-right" viewBox="0 0 16 16">
                <path fillRule="evenodd" d="M1 11.5a.5.5 0 0 0 .5.5h11.793l-3.147 3.146a.5.5 0 0 0 .708.708l4-4a.5.5 0 0 0 0-.708l-4-4a.5.5 0 0 0-.708.708L13.293 11H1.5a.5.5 0 0 0-.5.5zm14-7a.5.5 0 0 1-.5.5H2.707l3.147 3.146a.5.5 0 1 1-.708.708l-4-4a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 4H14.5a.5.5 0 0 1 .5.5z" />
            </svg>
        </button>
    );
};

const Sidebar = () => {
    const [sidebarVisible, setSidebarVisible] = useState(false);

    const toggleSidebar = () => {
        setSidebarVisible(!sidebarVisible);
    };

    return (
        <div className="">
            <div><ShowAndHide onClick={toggleSidebar} /></div>
            <p className={`w-48 h-2/5 z-50 ${sidebarVisible ? 'block' : 'hidden'}`}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facere cupiditate eveniet veritatis eum eius quia fuga, sapiente temporibus vero blanditiis voluptas ratione dolorem officiis nemo autem, magnam quam iusto debitis.</p>
        </div>
    );
};

export default Sidebar;
