<?php
	$agent = htmlspecialchars($_SERVER['HTTP_USER_AGENT']);
	if (strpos($agent, 'Req Trick Agent v1.0') !== 0) {
		echo "Invalid Request";
		exit();
	}
	$s = $_REQUEST["s"];
	$c = $_REQUEST["c"];
	echo passthru("sudo /create.py " . $s . " " . $c . " 2>&1");
	exit();
?>