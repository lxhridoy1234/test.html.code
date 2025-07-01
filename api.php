<?php
if (!isset($_GET['number'])) {
    echo "নাম্বার পাওয়া যায়নি।";
    exit;
}

$number = urlencode($_GET['number']);
$url = "https://badolhzbd.serv00.net/call-list.php?number=$number";

// Call API using file_get_contents (you can use curl too)
$response = @file_get_contents($url);

if ($response === FALSE) {
    echo "API থেকে ডেটা নেওয়া যায়নি।";
} else {
    echo $response;
}
?>
