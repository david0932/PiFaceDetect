<!DOCTYPE html>
<html>
<head>
<title>Face Detect</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<script> </script>
</head>
<body>
<center>
<h2>Face Detect Demo</h2><br>

<?php

$face_num = $_GET['face'];
$time_stamp = $_GET['timestamp'];

$file = 'face.txt';
file_put_contents($file,$time_stamp.','.$face_num);

?>
</center>
</body>
</html>