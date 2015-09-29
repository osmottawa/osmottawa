<?php
	$type="";
	if(isset($_GET["id"]))
	{
		if($_GET["id"]==="")
		{
			$type="NewUser";
		}
		else
		{
			$type=$_GET["id"];
		}
	}
	else
	{
		$type="NewUser";
	}

?>
<!DOCTYPE HTML>
<html>
	<head>
		<title>osmcanada - <?php if($type=="NewUser"){echo "New User";} ?></title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link href='http://fonts.googleapis.com/css?family=Oxygen:400,300,700' rel='stylesheet' type='text/css'>
		<!--[if lte IE 8]><script src="js/html5shiv.js"></script><![endif]-->
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-panels.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="css/skel-noscript.css" />
			<link rel="stylesheet" href="css/style.css" />
		</noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
		<!--[if lte IE 9]><link rel="stylesheet" href="css/ie/v9.css" /><![endif]-->
	</head>
	<body class="homepage">

	<!-- Header -->
		<div id="header">
			<div class="container">
					
				<!-- Logo -->
					<div id="logo">
						<h1><a href="#">OSMCanada</a></h1>
						<span>A community around OpenStreetMaps</span>
					</div>
				
				<!-- Nav -->
					<nav id="nav">
						<ul>
							<li><a href="index.html">Homepage</a></li>
                            <li class="active"><a href="tutorial.php?id=NewUser">Start Mapping</a></li>
							<li><a href="http://tasks.osmcanada.ca">Task Manager</a></li>
							<li><a href="http://www.meetup.com/openstreetmap-ottawa/">Events</a></li>
							<li><a href="about.html">About</a></li>
						</ul>
					</nav>

			</div>
		</div>
	<!-- Header -->
			
	<!-- Main -->
		<div id="main">
			<div class="container">
				   <?php
						if($type=="NewUser")
						{
							$html = <<< EOT
							<p>Anyone can change the data in OpenStreetMap itself and add new data. This step-by-step guide shows how to do it:</p><br/>
						<div class="row">
							<div id="sidebar" class="1u">
								<section>
									<img width="80" height="80" alt="(1)" src="images/1.png"></img>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<p>Visit <a href="http://www.openstreetmap.org/user/new" target="_blank">http://www.openstreetmap.org/user/new</a> and sign-up for an account.</p>
									<p>You can use any username. Note that it is public and all your edits are associated with it. Your e-mail address will not be shared, but other users can send you private messages that are forwarded to your e-mail address. Your password must be at least 8 characters long.</p>
								</section>
							</div>
							<div id="sidebar" class="3u">
								<section>
									<img height="400" width="393" alt="Sign-up" src="images/signup.png"></img>
								</section>
							</div>
						</div>
						<div class="row">
							<div id="sidebar" class="1u">
								<section>
									<img width="80" height="80" alt="(1)" src="images/2.png"></img>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<p>You should receive a <b>confirmation e-mail</b> with a link - click this link. You can now select your hometown by clicking on the map, so that others that can see who is active in the area.</p>
								</section>
							</div>
						</div>
						<div class="row">
							<div id="sidebar" class="1u">
								<section>
									<img width="80" height="80" alt="(1)" src="images/3.png"></img>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<p>Browse to <a href="http://www.openstreetmap.org" target="_blank">http://www.openstreetmap.org/</a> and choose <b>any part of the map</b> (for example, an area that has a mistake) and click on the <b>Edit</b> button (above).</p>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<img height="400" width="566" alt="Editing OSM" src="images/editosm.png"></img>
								</section>
							</div>
						</div>
						<div class="row">
							<div id="sidebar" class="1u">
								<section>
									<img width="80" height="80" alt="(1)" src="images/4.png"></img>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<p>The iD is currently the default editor on OpenStreetMap. When you launch it for the first time you can follow a <b>walkthrough</b> that will give you a quick tutorial on how to edit the map. You can also chose to skip the tutorial, but we highly recommend trying it out.</p>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<img height="400" width="566" alt="Beginning to edit OSM" src="images/editstart.png"></img>
								</section>
							</div>
						</div>
						<div class="row">
							<div id="sidebar" class="1u">
								<section>
									<img width="80" height="80" alt="(1)" src="images/dots.png"></img>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<p>Of course that was only a small start and there are many other ways to work with the OSM database. Offline editors(<a href="http://josm.openstreetmap.de/" target="_blank">JOSM</a>, <a href="http://wiki.openstreetmap.org/wiki/Merkaartor" target="_blank">Merkaartor</a>) offer more features than the iD browser, but must first be installed.</p>
								</section>
							</div>
							<div id="sidebar" class="5u">
								<section>
									<img height="400" width="541" alt="JOSM Editor" src="images/josm.png"></img>
								</section>
							</div>
						</div>
						
EOT;
							echo $html;
						}
				   ?>                 
			</div>
		</div>
	<!-- Main -->

	<!-- Footer -->
		<div id="footer">
			<div class="container">

			</div>
		</div>
	<!-- Footer -->

	<!-- Copyright -->
		<div id="copyright">
			<div class="container">
				Design: OSMCanada Team
			</div>
		</div>

	</body>
</html>