<?php
require("connector.php");

$query = "SELECT * FROM pessoa";
$stmt = $pdo->prepare($query);
$stmt->execute();

$usuarios = $stmt->fetchAll();
?>

<h2>Usuários cadastrados:</h2>

<?php foreach ($usuarios as $user): ?>
    <p>
        Nome: <?= $user['nome'] ?> <br>
        Sobrenome: <?= $user['sobrenome'] ?>
    </p>
    <hr>
<?php endforeach; ?>