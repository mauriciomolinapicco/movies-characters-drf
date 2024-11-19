// Verificar si el usuario está logueado
const token = localStorage.getItem('authToken'); // Usa sessionStorage si prefieres

//creo los encabezados para las request
function createHeaders() {
    return {
        "Content-Type": "application/json",
        "Authorization": `Token ${token}`
    };
}


// Redirigir a login si no hay token
if (!token) {
    window.location.href = '/trabajopractico/frontend/login.html';
} else {
    // Validar el token con el servidor
    fetch('http://127.0.0.1:8000/api/validate-token/', { // Asegúrate de usar la URL completa del endpoint
        method: 'GET',
        headers: { 
            'Authorization': `Token ${token}`
        }
    })
    .then(response => {
        if (!response.ok) {
            // Token inválido o caducado, redirigir a login
            localStorage.removeItem('authToken'); // Limpia el token almacenado
            window.location.href = '/trabajopractico/frontend/login.html';
        }
    })
    .catch(() => {
        // Error de conexión, redirigir a login como precaución
        localStorage.removeItem('authToken'); // Limpia el token almacenado
        window.location.href = '/trabajopractico/frontend/login.html';
    });
}




//Funcionalidad de la pagina
const apiBase = "http://127.0.0.1:8000";


function ocultarPelis() {
    const moviesTableBody = document.querySelector("#moviesTable tbody");
    moviesTableBody.innerHTML = '';
}

function ocultarPersonajes() {
    const charactersTableBody = document.querySelector("#charactersTable tbody");
    charactersTableBody.innerHTML = '';
}

// Obtener todas las películas
async function getMovies() {
    const response = await fetch(`${apiBase}`, {
        headers: createHeaders()
    });
    const data = await response.json();
    const moviesTableBody = document.querySelector("#moviesTable tbody");
    moviesTableBody.innerHTML = "";
    data.forEach(movie => {
        moviesTableBody.innerHTML += `
            <tr>
                <td>${movie.id}</td>
                <td>${movie.title}</td>
                <td>${movie.year}</td>
                <td>${movie.genre}</td>
                <td>
                    <button onclick="deleteMovie(${movie.id})">Eliminar</button>
                    <button onclick="populateUpdateForm(${movie.id}, '${movie.title}', '${movie.genre}', ${movie.year})">Actualizar</button>
                </td>
            </tr>`;
    });
}

// Añadir una película nueva
async function addMovie() {
    const title = document.getElementById("movieTitle").value;
    const genre = document.getElementById("movieGenre").value;
    const year = document.getElementById("movieYear").value;
    
    const response = await fetch(`${apiBase}/addMovie`, {
        method: 'POST',
        headers: createHeaders(),
        body: JSON.stringify({ title, genre, year })
    });
    if (response.ok) {
        alert("¡Película añadida con éxito!");
        getMovies();
    } else {
        alert("Error al añadir la película.");
    }
}

// Rellenar formulario de actualización
function populateUpdateForm(id, title, genre, year) {
    document.getElementById("updateMovieId").value = id;
    document.getElementById("updateMovieTitle").value = title;
    document.getElementById("updateMovieGenre").value = genre;
    document.getElementById("updateMovieYear").value = year;
    document.getElementById("updateFormContainer").style.display = "block";
}

// Actualizar película
async function updateMovie() {
    const id = document.getElementById("updateMovieId").value;
    const title = document.getElementById("updateMovieTitle").value;
    const genre = document.getElementById("updateMovieGenre").value;
    const year = document.getElementById("updateMovieYear").value;

    const body = {};
    if (title) body.title = title;
    if (genre) body.genre = genre;
    if (year) body.year = year;

    const response = await fetch(`${apiBase}/updateMovie/${id}`, {
        method: "PUT",
        headers: createHeaders(),
        body: JSON.stringify(body)
    });
    if (response.ok) {
        alert("¡Película actualizada con éxito!");
        getMovies();
        cancelUpdate();
    } else {
        alert("Error al actualizar la película.");
    }
}

// Cancelar actualización
function cancelUpdate() {
    document.getElementById("updateFormContainer").style.display = "none";
}

// Eliminar película
async function deleteMovie(movieId) {
    const response = await fetch(`${apiBase}/deleteMovie/${movieId}`, {
        method: "DELETE",
        headers: createHeaders()
    });
    if (response.ok) {
        alert("¡Película eliminada con éxito!");
        getMovies();
    } else {
        alert("Error al eliminar la película.");
    }
}






// Get all characters
async function getCharacters() {
    const response = await fetch(`${apiBase}/getCharacters`, {
        headers: createHeaders()
    });
    const data = await response.json();
    const charactersTableBody = document.querySelector("#charactersTable tbody");
    charactersTableBody.innerHTML = "";
    data.forEach(character => {
        charactersTableBody.innerHTML += `
            <tr>
                <td>${character.id}</td>
                <td>${character.name}</td>
                <td>${character.role}</td>
                <td>${character.actor}</td>
                <td>${character.movie_title}</td>
                <td>
                    <button onclick="deleteCharacter(${character.id})">Eliminar</button>
                    <button onclick="populateCharacterUpdateForm(${character.id}, '${character.name}', '${character.actor}', '${character.role}', ${character.movie})">Actualizar</button>
                </td>
            </tr>`;
    });
}

// Add a new character
async function addCharacter() {
    const name = document.getElementById("characterName").value;
    const actor = document.getElementById("characterActor").value;
    const role = document.getElementById("characterRole").value;
    const movieId = document.getElementById("characterMovieId").value;
    
    const response = await fetch(`${apiBase}/addCharacter`, {
        method: "POST",
        headers: createHeaders(),
        body: JSON.stringify({ name, actor, role, movie: movieId })
    });
    if (response.ok) {
        alert("Character added successfully!");
        getCharacters();
    } else {
        alert("Error adding character!");
    }
}

// Delete a character
async function deleteCharacter(characterId) {
    const response = await fetch(`${apiBase}/deleteCharacter/${characterId}`, {
        method: "DELETE",
        headers: createHeaders()
    });
    if (response.ok) {
        alert("Character deleted successfully!");
        getCharacters();
    } else {
        alert("Error deleting character!");
    }
}

    // Mostrar formulario de actualización con datos del personaje
function populateCharacterUpdateForm(id, name, actor, role, movieId) {
    document.getElementById("updateCharacterForm").style.display = "block";
    document.getElementById("updateCharacterId").value = id;
    document.getElementById("updateCharacterName").value = name;
    document.getElementById("updateCharacterActor").value = actor;
    document.getElementById("updateCharacterRole").value = role;
    document.getElementById("updateCharacterMovieId").value = movieId;
}

// Ocultar formulario de actualización
function cancelUpdateCharacter() {
    document.getElementById("updateCharacterForm").style.display = "none";
    document.getElementById("updateCharacterId").value = "";
    document.getElementById("updateCharacterName").value = "";
    document.getElementById("updateCharacterActor").value = "";
    document.getElementById("updateCharacterRole").value = "";
    document.getElementById("updateCharacterMovieId").value = "";
}

// Actualizar personaje
async function updateCharacter() {
    const id = document.getElementById("updateCharacterId").value;
    const name = document.getElementById("updateCharacterName").value;
    const actor = document.getElementById("updateCharacterActor").value;
    const role = document.getElementById("updateCharacterRole").value;
    const movieId = document.getElementById("updateCharacterMovieId").value;

    // Crear objeto con solo los campos que tienen valores
    const updatedFields = {};
    if (name) updatedFields.name = name;
    if (actor) updatedFields.actor = actor;
    if (role) updatedFields.role = role;
    if (movieId) updatedFields.movie = movieId;

    const response = await fetch(`${apiBase}/updateCharacter/${id}`, {
        method: "PUT",
        headers:createHeaders(),
        body: JSON.stringify(updatedFields),
    });

    if (response.ok) {
        alert("¡Personaje actualizado con éxito!");
        cancelUpdateCharacter();
        getCharacters();
    } else {
        alert("Error al actualizar el personaje.");
    }
}
