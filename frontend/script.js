document.getElementById("get-movies").addEventListener("click", fetchMovies);

function fetchMovies() {
    const apiUrl = "http://127.0.0.1:8000"; // Reemplaza con la URL de tu API

    // Realizar la solicitud GET
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error("ERRORRRRR");
            }
            return response.json(); // Parsear la respuesta a JSON
        })
        .then(data => {
            displayMovies(data); // Mostrar las películas
        })
        .catch(error => {
            console.error("Error fetching movies:", error);
        });
}

function displayMovies(movies) {
    const movieList = document.getElementById("movie-list");
    movieList.innerHTML = ""; // Limpiar la lista anterior

    // Crear un elemento <li> para cada película
    movies.forEach(movie => {
        const listItem = document.createElement("li");
        listItem.textContent = `${movies} ${movie.title} (${movie.year})`; // Ajusta según los campos de tu API
        movieList.appendChild(listItem);
    });
}
