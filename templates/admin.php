<!-- PHP code to establish connection with the localserver -->
<?php

// Username is root
$user = 'root';
$password = '';

// Database name is geeksforgeeks
$database = 'admission_form';

// Server is localhost with
// port number 3306
$servername='localhost';
$mysqli = mysqli_connect($servername, $user,
				$password, $database);

// Checking for connections
if (!$mysqli) {
	die('Could not connect to MySQL: ' .
		mysqli_error($mysqli));
}
else{
	echo"Connecting to Database";
}

?>
<!-- HTML code to display data in tabular format -->
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>GFG User Details</title>
	<!-- CSS FOR STYLING THE PAGE -->
	<style>
		table {
			margin: 0 auto;
			font-size: large;
			border: 1px solid black;
		}

		h1 {
			text-align: center;
			color: #006600;
			font-size: xx-large;
			font-family: 'Gill Sans', 'Gill Sans MT',
			' Calibri', 'Trebuchet MS', 'sans-serif';
		}

		td {
			background-color: #E4F5D4;
			border: 1px solid black;
		}

		th,
		td {
			font-weight: bold;
			border: 1px solid black;
			padding: 10px;
			text-align: center;
		}

		td {
			font-weight: lighter;
		}
	</style>
</head>

<body>
	<section>
		<h1>Admission Form</h1>
		<!-- TABLE CONSTRUCTION -->
		<table>
			<tr>
				<th>Form ID</th>
				<th>Father Name</th>
				<th>Mother Name</th>

			</tr>

			<?php
				// SQL query to select data from database
				$sql = "SELECT FORM_ID,FATHER_NAME,MOTHER_NAME FROM admission_form";
				$result = $mysqli->query($sql);
				$mysqli->close();
				while($rows=$result->fetch_assoc())
				{
			?>
			
			<tr>
				<td><?php echo $rows['FORM_ID'];?></td>
				<td><?php echo $rows['FATHER_NAME'];?></td>
				<td><?php echo $rows['MOTHER_NAME'];?></td>
			</tr>
			<?php 
				}
			?>
		</table>
	</section>
</body>

</html>
