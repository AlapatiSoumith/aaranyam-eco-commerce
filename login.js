const username = document.getElementsById('loginId').value;
const password = document.getElementById('password').value;

document.getElementById('sellerId').addEventListener('click', async function() {
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const result = await response.json();

        if (response.ok && result.success) {
            alert('Login successful! Redirecting...');
            window.location.href = '/dashboard.html';
        } else {
            alert('Login failed: ' + result.message);
        }

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during login.');
    }
});

document.getElementById('buyerId').addEventListener('click', async function() {
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const result = await response.json();

        if (response.ok && result.success) {
            alert('Login successful! Redirecting...');
            window.location.href = '/dashboard.html';
        } else {
            alert('Login failed: ' + result.message);
        }

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during login.');
    }
});

document.getElementById('transporterId').addEventListener('click', async function() {
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const result = await response.json();

        if (response.ok && result.success) {
            alert('Login successful! Redirecting...');
            window.location.href = '/dashboard.html';
        } else {
            alert('Login failed: ' + result.message);
        }

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during login.');
    }
});