function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
    console.log('test')
}

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
    console.log('test')
}

document.addEventListener('DOMContentLoaded', (event) => {
    // Initialize the map and set its view to the chosen geographical coordinates and zoom level
    var map = L.map('map').setView([-36.75642, 144.26456], 13);

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



// window.onclick = function(event) {
//     if (!event.target.matches('.dropbtn')) {
//         var dropdowns = document.getElementsByClassName("dropdown-content");
//         var i;
//         for (i = 0; i < dropdowns.length; i++) {
//         var openDropdown = dropdowns[i];
//         if (openDropdown.classList.contains('show')) {
//             openDropdown.classList.remove('show');
//         }
//         }
//     }
// }