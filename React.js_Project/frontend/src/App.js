import './App.css';
// import {BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Footer from './composants/footer.jsx';
import Header from './composants/header.jsx';
import Product from './composants/products';
// import About from './composants/about';
// import Home from './composants/home';
// import Contacts from './composants/contacts';

function App() {
  return (
    <div className='min-h-screen'>
      <Header/>
      <main className='flex'>
        <Product />
      </main>
      <Footer />

      {/* //Routes */}
      {/* <Router>
        <Routes>
          <Route exact path ='/home' element={<Home />} />
          <Route exact path ='/about' element={<About />} />
          <Route exact path ='/contacts' element={<Contacts />} />
        </Routes>

      </Router> */}
    </div>


  );
}
export default App;
