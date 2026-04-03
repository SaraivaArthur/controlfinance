<?php

    $dbHost = "localhost";
    $dbUsername = "root";
    $dbPassword = "admin";
    $dbName = "login";
    $conexao = new mysqli($dbHost, $dbUsername, $dbPassword, $dbName);
if(isset($_POST['submit']))
{
    $login = $_POST['login'];
    $senha = $_POST['senha'];
}

    /*
    if($conexao->connect_error) 
    {
        echo "Erro";
    }
    else
    {
        echo "Conectado";
    }

        if(isse($_POST['submit']))
{
    print_r($_POST['login']);
    print_r('<br>');
    print_r($_POST['senha']);
}
    */

?>