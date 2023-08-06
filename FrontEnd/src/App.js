import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Header from "./components/Header/Header";
import Home from "./components/Home/Home";
import Drivers from "./components/Drivers/Drivers";
import Buses from "./components/Buses/Buses";
import ActiveBuses from "./components/ActiveBus/AcitveBuses";

import "./App.css";

function App() {
  return (
    <Router>
      <div className="Appcontainer">
        <div className="Appcontent">
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/drivers" element={<Drivers />} />
            <Route path="/buses" element={<Buses />} />
          </Routes>
        </div>
        <div className="Appsidebar">
          <ActiveBuses />
        </div>
      </div>
    </Router>
  );
}

export default App;
