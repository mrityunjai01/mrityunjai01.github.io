<?php
// the message
$msg = "<html>Hey, Please click this link for reseting your google password <a href =""> Reset </a>;

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("mj1190705@gmail.com","Password Reset",$msg);
?>