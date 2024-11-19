let authToken = null;

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const loginMessage = document.getElementById('loginMessage');

    fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            localStorage.setItem('authToken', data.token);
            document.getElementById('loginContainer').classList.add('hidden');
            document.getElementById('logoutContainer').classList.remove('hidden');
            loginMessage.classList.add('hidden');
        } else {
            loginMessage.textContent = data.error || 'Error en el inicio de sesión';
            loginMessage.classList.remove('hidden');
        }
    })
    .catch(() => {
        loginMessage.textContent = 'Error al conectar con el servidor.';
        loginMessage.classList.remove('hidden');
    });
}

function logout() {
    const logoutMessage = document.getElementById('logoutMessage');
    const token = localStorage.getItem('authToken');

    fetch('/api/logout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`
        }
    })
    .then(response => {
        if (response.ok) {
            localStorage.removeItem('authToken');
            document.getElementById('logoutContainer').classList.add('hidden');
            document.getElementById('loginContainer').classList.remove('hidden');
            logoutMessage.classList.add('hidden');
        } else {
            logoutMessage.textContent = 'Error al cerrar sesión.';
            logoutMessage.classList.remove('hidden');
        }
    })
    .catch(() => {
        logoutMessage.textContent = 'Error al conectar con el servidor.';
        logoutMessage.classList.remove('hidden');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('authToken');
    if (token) {
        document.getElementById('loginContainer').classList.add('hidden');
        document.getElementById('logoutContainer').classList.remove('hidden');
    }
});
