// // Team members : 1. Prarthana, 2.Ibtisam, 3. Nandaj, 4.Ayman

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

import "./Data.css";

function Data({ title }) {
  const [anchorEl, setAnchorEl] = useState(null);
  const [Data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:8000/driver_details/");
      const data = await response.json();
      setData(data);
    };
    fetchData();
  }, []);

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <div className="dataHome">
      <div className="datacontainer">
        <div className="MainContent">
          <div className="dataHeading">
            <h4> Animal Details</h4>
            <h5>Critical</h5>
          </div>
          <div className="data-containerr">
            {Data.map((data) => (
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
            <h5>Injured</h5>
          </div>
          <div className="data-containerr">
            {Data.map((data) => (
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
            <h5>Inactive</h5>
          </div>
          <div className="data-containerr">
            {Data.map((data) => (
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
        <div className="Datasidebar"></div>
      </div>
    </div>
  );
}

export default Data;

// import React, { useState } from "react";
// import Box from "@mui/material/Box";
// import ActiveBuses from "../ActiveBus/AcitveBuses";

// import AppBar from "@mui/material/AppBar";
// import Toolbar from "@mui/material/Toolbar";
// import Typography from "@mui/material/Typography";
// import IconButton from "@mui/material/IconButton";
// import MenuIcon from "@mui/icons-material/Menu";
// import AccountCircle from "@mui/icons-material/AccountCircle";

// import MenuItem from "@mui/material/MenuItem";
// import Menu from "@mui/material/Menu";

// import "./Data.css";

// function Data({ title }) {
//   const [anchorEl, setAnchorEl] = useState(null);

//   const handleMenu = (event) => {
//     setAnchorEl(event.currentTarget);
//   };

//   const handleClose = () => {
//     setAnchorEl(null);
//   };

//   return (
//     <div className="Home">
//       <div className="container">
//         <Box sx={{ flexGrow: 1 }} className="dataContainer">
//           <i className="headingg" aria-hidden="true">
//             Write your code here
//           </i>
//         </Box>
//         <ActiveBuses />
//       </div>
//     </div>
//   );
// }

// export default Data;
