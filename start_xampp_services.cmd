echo checking if xampp is installed in c

if errorlevel then finish
dir C:\xampp\
echo ok i found it
echo attempting to start MYSQL server on xampp using port 3306
C:\xampp\mysql_start.bat
echo attempting to start apache http server on port 80
C:\xampp\apache_start.bat
echo done


:finish