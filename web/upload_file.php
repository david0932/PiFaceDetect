<?php
 
 $targetfolder = "uploads/";
 
 $targetfolder = $targetfolder . basename( $_FILES['file']['name']) ;
 
 if(is_file("$targetfolder")) {
unlink("$targetfolder");
}
 
if(move_uploaded_file($_FILES['file']['tmp_name'], $targetfolder))
 
 {
 
 echo "The file ". basename( $_FILES['file']['name']). " is uploaded";
 
 }
 
 else {
 
 echo "Problem uploading file";
 
 }
 
 ?>