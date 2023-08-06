import React, { useState, useEffect } from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import AccountCircle from "@mui/icons-material/AccountCircle";
import MenuItem from "@mui/material/MenuItem";
import Menu from "@mui/material/Menu";

import "./ActiveBuses.css";

function ActiveBuses({ title }) {
  const [anchorEl, setAnchorEl] = useState(null);
  const [busList, setBusList] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:8000/location/in_campus");
      const data = await response.json();
      const busList = data.map((bus) => (
        <div className="subline" key={bus.id}>
          <p>GPS No.: {bus.busNumber}</p>
          <p>Location : {bus.departureTime}</p>
          <p>Time been Inactive : {bus.arrivalTime}</p>
          <p>Status : {bus.Status}</p>
        </div>
      ));
      setBusList(busList);
    };

    fetchData();
    console.log(busList);
    const intervalId = setInterval(fetchData, 3000);

    return () => clearInterval(intervalId);
  }, []);

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div className="sidebar-background">
      <div className="sidebar">
        <div className="grid">
          <h2>Non-Active</h2>
          {busList}
          {busList}
        </div>

        <hr></hr>
        <div className="grid">
          <h2>Injured</h2>
          {busList}
        </div>
        <hr></hr>
        <div className="grid">
          <h2>Critical</h2>
          {busList}
        </div>
      </div>
    </div>
  );
}

export default ActiveBuses;
