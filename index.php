<link rel="stylesheet" href="odometer-theme-car.css"/>
<script src="odometer.js"></script>

<?php
$raw_data = shell_exec("bash data.sh");
$aray = preg_split('/<br[^>]*>/i',$raw_data);
$coeff = str_replace(",","",$aray[0])/str_replace(",","",$aray[1]);

echo '<span id="counter">';
echo('<span class="odometer">'.$aray[0].'</span> cases<p>');
echo('<span class="odometer">'.$aray[1].'</span> deaths<p>');
if(isset($_GET['coeff'])) {
	echo('<span class="odometer">'.$coeff.'</span> coefficent');
}
echo '</span>';
?>
