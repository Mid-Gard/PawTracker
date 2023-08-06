// import React, { useState, useEffect } from "react";
// import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
// import "leaflet/dist/leaflet.css";

// import Header from "../Header/Header";
// import ActiveBuses from "../ActiveBus/AcitveBuses";

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

//   const center = {
//     lat: location?.lat || 0,
//     lng: location?.lng || 0,
//   };

//   return (
//     <div className="Home">
//       {location && (
//         <MapContainer center={center} zoom={15}>
//           <TileLayer
//             url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//             attribution='&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
//           />
//           <Marker position={center}>
//             <Popup>
//               Vehicle Location: <br /> Lat: {location.lat}, Lng: {location.lng}
//             </Popup>
//           </Marker>
//         </MapContainer>
//       )}
//     </div>
//   );
// }

// export default Home;
