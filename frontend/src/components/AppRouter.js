import React from 'react';
import {BrowserRouter as Router, Link, Route, Routes} from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
// import Search from "../pages/Search";
// import Signup from "../pages/Signup";
import Main from "../pages/Main";
// import Signin from "../pages/Signin";
// import Profile from "../pages/Profile";
// import MakeAd from "../pages/MakeAd";
// import UpdateProfile from "../pages/UpdateProfile";
// import Moderation from "../pages/Moderation";
// import Offer from "../pages/Offer";
// import Cookies from "js-cookie";


const authButtons = () => {
    return (
        <ul className="link-list right-links">
            {/*<li className="nav-item right-link">*/}
            {/*    <Link to="/signin" className="nav-link">*/}
            {/*        <div className="logo">*/}
            {/*            <img src={"profile_logo.png"} alt="Профиль" height="22px" width="auto"/>*/}
            {/*        </div>*/}
            {/*    </Link>*/}
            {/*</li>*/}

            {/*<li className="nav-item right-link">*/}
            {/*    <Link to="/signup" className="nav-link">Регистрация</Link>*/}
            {/*</li>*/}
        </ul>
    )
}
const profileLogo = () => {
    return (
        <ul className="link-list right-links">
            {/*<li className="nav-item right-link">*/}
            {/*    <Link to="/profile" className="nav-link" id="profile-logo">*/}
            {/*        <div className="logo">*/}
            {/*            <img src={"profile_logo.png"} alt="Профиль" height="30px" width="auto"/>*/}
            {/*        </div>*/}
            {/*    </Link>*/}
            {/*</li>*/}

        </ul>
    )
}
const AppRouter = () => {
    return (
        <div>
             <Router>
                 {/*<nav className="navbar">*/}
                 {/*    <ul className="link-list left-links">*/}
                 {/*        <li className="nav-item left-link">*/}
                 {/*            <Link to="/" className="nav-link main-link">*/}
                 {/*                <div className="logo">*/}
                 {/*                    <img src={"home_logo.png"} alt="Главная" height="20px" width="auto"/>*/}
                 {/*                </div>*/}
                 {/*            </Link>*/}
                 {/*        </li>*/}
                 {/*        <li className="nav-item left-link">*/}
                 {/*            <Link to="/offers" className="nav-link ">Объявления</Link>*/}
                 {/*        </li>*/}
                 {/*    </ul>*/}
                     {/*{Cookies.get("auth_token") ? profileLogo() : authButtons()}*/}

                 {/*</nav>*/}

                 <Navbar expand="lg" className="bg-body-tertiary">
                     <Container>
                         <Navbar.Brand href="/">Радар клиентского сервиса</Navbar.Brand>
                         <Navbar.Toggle aria-controls="basic-navbar-nav" />
                         <Navbar.Collapse id="basic-navbar-nav">
                             <Nav className="me-auto">
                                 <Nav.Link href="#home">Дашборд</Nav.Link>
                                 <Nav.Link href="#link">Отзывы</Nav.Link>
                             </Nav>
                         </Navbar.Collapse>
                     </Container>
                 </Navbar>
                 <br/><br/>
                 <main>
                     <Routes>
                         <Route path="/" element={<Main/>}/>
                         <Route path="/action/3.1" element={<Main/>}/>
                         {/*<Route path="/signup" element={<Signup/>}/>*/}
                         {/*<Route path="/signin" element={<Signin/>}/>*/}
                         {/*<Route path="/offers" element={<Search/>}/>*/}
                         {/*<Route path="/offers/:id" element={<Offer/>} />*/}
                         {/*<Route path="/profile/*" element={<Profile/>}/>*/}
                         {/*<Route path="/makead" element={<MakeAd/>}/>*/}
                         {/*<Route path="/profileupd" element={<UpdateProfile/>}/>*/}
                         {/*<Route path="/moderation" element={<Moderation/>}/>*/}

                     </Routes>
                 </main>
             </Router>
         </div>
    );
};

export default AppRouter;
