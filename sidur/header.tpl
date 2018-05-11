<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" type="text/css" href="/css/style.css">
  <title>Kvikmyndir</title>
</head>
<body>
  <div class="toppur">
    <form action="/leit" class="topp">
      <input type="text" name="leita" placeholder="Kvikmynd...">
      <input type="submit" value="Leita">
    </form>
    <div class="notandi">
      %if nafn:
        <h3>Notandi: <span class="ekkibold">{{nafn}}</span></h3>
      %end
    </div>
  </div>