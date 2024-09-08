var map; // to be initialized once DOM content is loaded

document.addEventListener('DOMContentLoaded', (event) => {
    // Initialize the map and set its view to the chosen geographical coordinates and zoom level
    map = L.map('map').setView([-36.75642, 144.26456], 13);

    // Add a tile layer to the map (using OpenStreetMap tiles)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add a marker to the map at the given coordinates
    L.marker([-36.75642, 144.26456]).addTo(map)
        .bindPopup('Car Crash Data 101')
        .openPopup();

        L.marker([-36.77334, 144.30782]).addTo(map)
        .bindPopup('Car Crash Data 102')
        .openPopup();

        L.marker([-36.72944, 144.28036]).addTo(map)
        .bindPopup('Car Crash Data 103')
        .openPopup();

});

// on button click, refresh map markers with new points
function onSearchButtonClick() {
    bounds = map.getBounds()
    console.log(bounds)
}