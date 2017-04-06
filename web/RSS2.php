<html>
    <head>
        <title>
            My page
        </title>
    </head>
    <body>
        <h1>
            Important website
        </h1>
<ul>
<?php
    $item='Everything is awesome!!';
    $tmp = exec("python rss2.py", $output, $ret_code);
    $arrlength = count($output);
    //echo $arrlength;
    //echo '<br>';
    //echo '====';
    for($x = 0; $x < $arrlength; $x++) {
    	echo "<li>" . $output[$x] . "</li>";
    	//echo "<br>";
    	}
    //echo '<br>====';

?>
</ul>
</body>
</html>
