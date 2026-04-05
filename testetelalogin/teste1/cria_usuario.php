<?php

require("connector.php");

if (isset($_POST['nome']) && isset($_POST['sobrenome'])) {

    $nome = $_POST['nome'];
    $sobrenome = $_POST['sobrenome'];

    $query = "INSERT INTO pessoa (nome, sobrenome) VALUES (:nome, :sobrenome)";

    $stmt = $pdo->prepare($query);
    $stmt->bindParam(':nome', $nome);
    $stmt->bindParam(':sobrenome', $sobrenome);
    $stmt->execute();

    header("Location: index.php?criado=sucesso");
}
