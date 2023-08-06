
// import React, { useState, useEffect } from "react";
// import "./Home.css";
// import WrappedMap from "../gMap/Map";
// import config from "../gMap/config";

// import Header from "../Header/Header";
// import ActiveBuses from "../ActiveBus/AcitveBuses";
// import Buses from "../Buses/Buses";
// import Drivers from "../Drivers/Drivers";

// import Box from "@mui/material/Box";
// import LinearProgress from "@mui/material/LinearProgress";

// function Home() {
//   const [coordinates, setCoordinates] = useState(null);
//   const mapURL = `https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=${config.mapsKey}`;

//   useEffect(() => {
//     const intervalId = setInterval(() => {
//       fetch("http://127.0.0.1:8000/location/location")
//         .then((response) => response.json())
//         .then((data) => setCoordinates(data));
//     }, 1000);
//     return () => clearInterval(intervalId);
//   }, []);

//   return (
//     <div className="App">
//       <div className="containerr">
//         {coordinates ? (
//           <WrappedMap
//             googleMapURL={mapURL}
//             loadingElement={<div style={{ height: `100%` }} />}
//             containerElement={<div className="mapContainer" />}
//             mapElement={<div style={{ height: `100%` }} />}
//             coordinates={coordinates}
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

## SIMPLE CODE TO TEST

// import React, { useState, useEffect } from "react";
// import "./Home.css";
// import config from "../gMap/config";
// import { GoogleMap, Marker } from "@react-google-maps/api";

// function Home() {
//   const [location, setLocation] = useState(null);

//   useEffect(() => {
//     const interval = setInterval(() => {
//       fetch("http://127.0.0.1:8000/location/location")
//         .then((response) => response.json())
//         .then((data) => setLocation(data));
//     }, 1000);
//     return () => clearInterval(interval);
//   }, []);

//   const mapURL = `https://maps.googleapis.com/maps/api/js?key=${config.mapsKey}`;

//   const containerStyle = {
//     width: "100vw",
//     height: "100vh",
//   };

//   const center = {
//     lat: location?.lat || 0,
//     lng: location?.lng || 0,
//   };

//   return (
//     <div className="App">
//       {location && (
//         <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={15}>
//           <Marker position={center} />
//         </GoogleMap>
//       )}
//     </div>
//   );
// }

// export default Home;

## giving oops message

```
import React, { useState, useEffect } from "react";
import "./Home.css";
import config from "../gMap/config";
// import { GoogleMap, Marker } from "@react-google-maps/api";
import { GoogleMap, Marker, useLoadScript } from "@react-google-maps/api";
import ActiveBuses from "../ActiveBus/AcitveBuses";

function Home() {
  const [location, setLocation] = useState(null);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://127.0.0.1:8000/location/location")
        .then((response) => response.json())
        .then((data) => setLocation(data));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const REACT_APP_GOOGLE_API_KEY = `https://maps.googleapis.com/maps/api/js?key=${config.mapsKey}`;
  const { isLoaded } = useLoadScript({
    googleMapsApiKey: REACT_APP_GOOGLE_API_KEY || "",
  });
  // const { isLoaded } = useLoadScript({
  //   googleMapsApiKey: process.env.`https://maps.googleapis.com/maps/api/js?key=${config.mapsKey}`,
  // });
  const mapURL = `https://maps.googleapis.com/maps/api/js?key=${config.mapsKey}`;

  const containerStyle = {
    width: "80vw",
    height: "100vh",
  };

  const center = {
    lat: location?.lat || 0,
    lng: location?.lng || 0,
  };

  const [showMap, setShowMap] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowMap(true);
    }, 3000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="Home">
      <div className="containerr">
        {location && (
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={15}
            className="mapContainer"
          >
            <Marker position={center} />
          </GoogleMap>
        )}
      </div>
    </div>
  );
}

export default Home;

```

## Using delay to load the module correctly

import React, { useState, useEffect } from "react";
import "./Home.css";
import config from "../gMap/config";
import { GoogleMap, Marker } from "@react-google-maps/api";
import ActiveBuses from "../ActiveBus/AcitveBuses";

function Home() {
  const [location, setLocation] = useState(null);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://127.0.0.1:8000/location/location")
        .then((response) => response.json())
        .then((data) => setLocation(data));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const mapURL = `https://maps.googleapis.com/maps/api/js?key=${config.mapsKey}`;

  const containerStyle = {
    width: "100vw",
    height: "100vh",
  };

  const center = {
    lat: location?.lat || 0,
    lng: location?.lng || 0,
  };

  return (
    <div className="App">
      <div className="containerr">
        {location && (
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={15}
          >
            <Marker position={center} />
          </GoogleMap>
        )}
        <ActiveBuses className="sidebar" />
      </div>
    </div>
  );
}

function HomeDelayed() {
  const [showHome, setShowHome] = useState(false);

  useEffect(() => {
    setTimeout(() => setShowHome(true), 2000);
  }, []);

  return showHome ? <Home /> : null;
}

export default HomeDelayed;
