<!DOCTYPE html>
<html>
<head>
    <title>Display Father and Mother Names</title>
</head>
<body>
    <h1>Father and Mother Names</h1>

    <?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "admission_form";

    // Create a connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check the connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
        echo "Working!". $conn->connect_error;
    }

    // Write SQL query to select Father Name and Mother Name
    $sql = "SELECT YEARS, MONTHS FROM ADMISSION_FORM";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<table border='1'>";
        echo "<tr><th>Father Name</th><th>Mother Name</th></tr>";
        while (1) {
            $row = $result->fetch_all();
            echo "<tr>";
            echo "<td>" . $row["YEARS"] . "</td>";
            echo "<td>" . $row["MONTHS"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No results found.";
    }

    // Close the database connection
    $conn->close();
    ?>
</body>
</html>
