#!usr/bin/bash

#main DIR

export fileDir="annon_search"

#end main DIR

#sub DIR

export sub_dir_db_main="annon_search/database/"
export sub_dir_crawler_open="annon_search/crawler_open_web/"
export sub_dir_crawler_dark="annon_search/crawler_dark_web/"
export sub_dir_lib="annon_search/lib/"
export sub_dir_src="annon_search/src/"
export sub_dir_static1="annon_search/static/css/"
export sub_dir_static2="annon_search/static/images/"



#end sub DIR

#begin copy path

export fileName="install_win.sh"
export fileMain="main.py"
export fileCrawl="web_test_scrapper.py"
export fileGen="generator.py"
export fileUnInstall="uninstall_win.sh"
export fileMem="buff.cpp"
export fileT="t.txt"
export fileEnv="trackerID.env"
export filegenator="genator.txt"
export fileC1="crawler_open_web/list.py"
export fileDB1="database/main_db.sql"
export fileDB2="database/search.sql"
export fileCSS="css/search.css"
export fileStart="start_server.py"
export fileToStart="start_xampp_services.cmd"

#end of copy path


if [ $fileName ]; then
echo  "Please wait while installing Annon script"
mkdir /C/annon_search/
mkdir /C/annon_search/templates/
mkdir /C/annon_search/static/
mkdir /C/annon_search/static/images/
mkdir /C/annon_search/static/css/
mkdir /C/annon_search/lib/
mkdir /C/annon_search/crawler_dark_web/
mkdir /C/annon_search/crawler_open_web/
mkdir /C/annon_search/lib/
mkdir /C/annon_search/src/

echo "installing...."
echo "copying annon_folder to C dir"
sleep 3
cp $fileMain /C/$fileDir/
sleep 3
cp $fileCrawl /C/$fileDir/
sleep 3
cp $fileGen /C/$fileDir/
sleep 3
cp $fileUnInstall /C/$fileDir/
sleep 3
cp $fileMem /C/$fileDir/
sleep 3
cp $fileT /C/$fileDir/
sleep 3
cp $fileEnv /C/$fileDir/
sleep 3
cp $filegenator /C/$fileDir/
sleep 3
cp $fileC1 /C/$fileDir/crawler_open_web/
sleep 3
cp $fileDB1 /C/$fileDir/database/
sleep 3
cp $fileDB2 /C/$fileDir/database/
sleep 3
cp $fileCSS /C/$fileDir/static/
sleep 3
cp $fileStart /C/$fileDir/
sleep 3
cp $fileToStart /C/$fileDir/
echo "Checking all files"
find /C/annon_search/*
sleep 3
echo the entire file system
#checking file system

find /C/$fileDir/
sleep 3
find /C/$fileDir/
sleep 3
find /C/$fileDir/
sleep 3
find /C/$fileDir/
sleep 3
find /C/$fileDir/
sleep 3
find /C/$fileDir/
sleep 3
find /C/$fileDir/
sleep 3
find /C/$fileDir/
sleep 3
find /C/$fileDir/crawler_open_web/
sleep 3
find /C/$fileDir/database/
sleep 3
find /C/$fileDir/database/
sleep 3
find /C/$fileDir/static/
sleep 3
find /C/$fileDir/

echo "all set!"
echo "Please run start_xampp_services.cmd to start MYSQL first before continuing"
echo "Now Open C folder and run start_server.py"
exit

fi