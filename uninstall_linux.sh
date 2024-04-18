#!usr/bin/bash

export userResponse=""

echo "Welcome to annon_install script"
echo "Annon search is a python script"
echo "Would you like to uninstall this (Y / N): ?"

read $userResponse
if [ $userResponse=="Y" ];then
rm -f /etc/annon_search/
echo "you selected Yes"
echo "Please wait..."
sleep 3 
echo "done"
echo "Note: if it does not delete then remove it manually"
else
echo "error"
fi
