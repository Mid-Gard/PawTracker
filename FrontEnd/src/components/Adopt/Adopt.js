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

import "./Adopt.css";

function Adopt({ title }) {
  const [anchorEl, setAnchorEl] = useState(null);
  const [Adopt, setAdopt] = useState([]);

  useEffect(() => {
    const fetchAdopt = async () => {
      const response = await fetch("http://127.0.0.1:8000/bus_details/");
      const data = await response.json();
      setAdopt(data);
    };
    fetchAdopt();
  }, []);

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div className="AdoptHome">
      <div className="Busecontainer">
        <div className="MainContent">
          <div className="dataHeading">
            <h4> Animal Nearby</h4>
            <h5>Cats</h5>
          </div>
          <div className="data-containerr">
            {Adopt.map((data) => (
              <div className="data-card" key={data.id}>
                <div className="data-image-container">
                  <img
                    className="data-image"
                    src={data.data_Pic}
                    alt={`data ${data.Name}`}
                  />
                </div>
                <div className="data-info">
                  <div className="data-name">{data.Name}</div>
                  <div className="data-phone">{data.Phone_Number}</div>
                </div>
              </div>
            ))}
          </div>
          <div className="dataHeading">
            <h5>Dogs</h5>
          </div>
          <div className="data-containerr">
            {Adopt.map((data) => (
              <div className="data-card" key={data.id}>
                <div className="data-image-container">
                  <img
                    className="data-image"
                    src={data.data_Pic}
                    alt={`data ${data.Name}`}
                  />
                </div>
                <div className="data-info">
                  <div className="data-name">{data.Name}</div>
                  <div className="data-phone">{data.Phone_Number}</div>
                </div>
              </div>
            ))}
          </div>
          <div className="dataHeading">
            <h5>Cows</h5>
          </div>
          <div className="data-containerr">
            {Adopt.map((data) => (
              <div className="data-card" key={data.id}>
                <div className="data-image-container">
                  <img
                    className="data-image"
                    src={data.data_Pic}
                    alt={`data ${data.Name}`}
                  />
                </div>
                <div className="data-info">
                  <div className="data-name">{data.Name}</div>
                  <div className="data-phone">{data.Phone_Number}</div>
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

export default Adopt;




/*
  return (
    <div className="AdoptHome">
      <div className="Busecontainer">
        <div className="MainContent">
          <div className="AdoptHeading">
            <p> Animal Nearby </p>
          </div>
          <div className="Adopt-container">
            {Adopt.map((Bus) => (
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

  */