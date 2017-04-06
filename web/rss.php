<?php header("Content-Type: application/xml; charset=UTF-8"); ?>
<?php 
$tmp = exec("python rss.py 31", $output, $ret_code);
$results =  json_decode($output[0],true);
$link = "http://www.gouget.com.br/tertulias/rss.php";
$now = date("D, d M Y H:i:s T");
?>
<?php krsort($results); ?>

<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
	<channel>
		<title>Tertúlia On-Line - Conscienciologia</title>
		<link>http://www.tertuliaconscienciologia.org</link>
		<atom:link href="<?php echo $link; ?>" rel="self" type="application/rss+xml" />
		<pubDate><?php echo $now; ?></pubDate>
		<language>pt-BR</language>
		
		<image><url>http://www.gouget.com.br/tertulias/tertuliarium.jpg</url></image>
		
	<?php foreach ($results as $key => $val ){ ?>
<item>
		<title><?php echo "Tertúlia ".$key." - ".$val[0]; ?></title>
		<?php $desc_data = "<b>Tertúlia:</b> ".$key."<br><b>Titulo:</b> ".$val[0]."<br><b>Especialidade:</b> ".$val[1]."<br><b>Data:</b> ".$val[3]; ?>
		<description><?php echo "<![CDATA[".nl2br($desc_data)."]]>" ?></description>
		<enclosure url="<?php
			echo "http://www.gouget.com.br/tertulias/".rawurlencode($val[2]); 
			?>"/>
</item>
	<?php } ?>
</channel>
</rss>
