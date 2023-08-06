// Team Members : 1. Aizaz, 2.Pradhnesh, 3. Sahil

import React, { useState, useEffect } from "react";

import Box from "@mui/material/Box";
import ActiveBuses from "../ActiveBus/AcitveBuses";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import AccountCircle from "@mui/icons-material/AccountCircle";
import MenuItem from "@mui/material/MenuItem";
import Menu from "@mui/material/Menu";

import "./Buses.css";

function Buses({ title }) {
  const [anchorEl, setAnchorEl] = useState(null);
  const [Buses, setBuses] = useState([]);

  useEffect(() => {
    const fetchBuses = async () => {
      const response = await fetch("http://127.0.0.1:8000/driver_details/");
      const data = await response.json();
      setBuses(data);
    };
    fetchBuses();
  }, []);

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div className="BusesHome">
      <div className="Busecontainer">
        <div className="MainContent">
          <div className="BusesHeading">
            <p> Buses Details</p>
          </div>
          <div className="Buses-container">
            {Buses.map((Bus) => (
              <div className="Bus-card" key={Bus.id}>
                <div className="Bus-image-container">
                  <img
                    className="Bus-image"
                    src={"https://picsum.photos/seed/${Bus}/200/200"}
                    alt={`Bus ${Bus.Bus_Name}`}
                  />
                </div>
                <div className="Bus-info">
                  <div className="Bus-name">{Bus.Bus_Name}</div>
                  <div className="Bus-phone">{Bus.Bus_Phone}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
        <div className="BusSidebar"></div>
      </div>
    </div>
  );
}

export default Buses;
