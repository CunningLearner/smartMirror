<?php
	if(isset($_POST['username']) && isset($_POST['password']))
	{
		if($_POST['username']=="iot" && $_POST['password']=="iot")
		{
			session_start();
			$_SESSION['uid']="iot";
			header("LOCATION: ../dashboard3.php");                     #changed from "dashboard3.php" to "socketio_first.js" by me on 220916
		}
		else
		{
			echo "Login Error";
		}
	}
