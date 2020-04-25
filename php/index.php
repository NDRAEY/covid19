<?php
$raw_data = shell_exec("bash data.sh");
$aray = preg_split('/<br[^>]*>/i',$raw_data);

echo($aray[0].' cases<p>');
echo($aray[1].' deaths');
?>

