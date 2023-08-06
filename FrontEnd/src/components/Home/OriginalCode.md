// ORIGINAL WORKING CODE :

// import React from "react";
// import "./Home.css";
// import WrappedMap from "../gMap/Map";
// import config from "../gMap/config";
// import useFetch from "../../hooks/useFetch";

// import Header from "../Header/Header";
// import ActiveBuses from "../ActiveBus/AcitveBuses";
// import Buses from "../Buses/Buses";
// import Drivers from "../Drivers/Drivers";

// import Box from "@mui/material/Box";
// import LinearProgress from "@mui/material/LinearProgress";

// function Home() {
//   const { data: paths } = useFetch(
//     "https://61a4a0604c822c0017041d33.mockapi.io/shuttle/v1/path"
//   );
//   const { data: stops } = useFetch(
//     "https://61a4a0604c822c0017041d33.mockapi.io/shuttle/v1/stops"
//   );
//   const mapURL = `https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=${config.mapsKey}`;

//   return (
//     <div className="App">
//       <div className="containerr">
//         {paths && stops ? (
//           <WrappedMap
//             paths={paths}
//             stops={stops}
//             googleMapURL={mapURL}
//             loadingElement={<div style={{ height: `100%` }} />}
//             containerElement={<div className="mapContainer" />}
//             mapElement={<div style={{ height: `100%` }} />}
//           />
//         ) : (
//           <Box sx={{ width: "80%" }}>
//             <LinearProgress />
//           </Box>
//         )}
//         <ActiveBuses className="sidebar" />
//       </div>
//     </div>
//   );
// }

// export default Home;
