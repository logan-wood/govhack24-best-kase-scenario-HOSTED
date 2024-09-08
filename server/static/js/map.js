const SERVER_DOMAIN = 'http://127.0.0.1:5000'

var map; // to be initialized once DOM content is loaded
var markers = [];

document.addEventListener('DOMContentLoaded', (event) => {
    // Initialize the map and set its view to the chosen geographical coordinates and zoom level
    map = L.map('map').setView([-36.75642, 144.26456], 13);

    // Add a tile layer to the map (using OpenStreetMap tiles)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);
});

// on button click, refresh map markers with new points
async function onSearchButtonClick() {
    bounds = map.getBounds()

    const data = await fetch(`${SERVER_DOMAIN}/getDataWithinBounds?lat_min=${bounds.getWest()}&lat_max=${bounds.getEast()}&lon_min=${bounds.getSouth()}&lon_max=${bounds.getNorth()}`)
    const dataPoints = await data.json()

    localStorage.setItem("crashData", JSON.stringify(dataPoints));

    // Clear existing markers
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];

    // add each datapoint to map
    dataPoints.forEach(element => {
        const lat = parseFloat(element.LAT);
        const lng = parseFloat(element.LONG);

console.log(element)

        if (!isNaN(lat) && !isNaN(lng)) {
            console.log(`Adding spot at (${lat}, ${lng})`)
            L.marker([lng, lat]).addTo(map)
                .bindPopup(element.ACCIDENT_TYPE_DESC, {autoPan: false})
                .openPopup();
            markers.push(L.marker([lat, lng]));
        } else {
            console.error('Invalid coordinates:', element);
        }
    });
}