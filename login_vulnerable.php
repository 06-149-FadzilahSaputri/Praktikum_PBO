<?php
// Proses login
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $conn = new mysqli(hostname: 'localhost', username: 'root', password: '', database: 'sqli_demo_149');

    if ($conn->connect_error) {
        die("Koneksi gagal: " . $conn->connect_error);
    }

    $username = $_POST['username'];
    $password = $_POST['password'];

    // Query langsung dari input user (TIDAK AMAN)
    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";

    echo "<p><strong>Query yang dijalankan:</strong><br><code>$query</code></p>";

    $result = $conn->query($query);

    if ($result && $result->num_rows > 0) {
        echo "<h3>Login berhasil! Selamat datang, $username</h3>";
    } else {
        echo "<h3>Login gagal! Username atau password salah.</h3>";
    }

    $conn->close();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login Form - Demonstrasi SQL Injection</title>
</head>
<body>
    <h2>Form Login (Rentan terhadap SQL Injection)</h2>
    <form method="POST" action="">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>

        <label>Password:</label><br>
        <input type="text" name="password" required><br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
