# Write a Shell Script that accept a name from the user and Display whether is it file, directory or something else.

#! /bin/sh
read -p "Enter Your Name : " Name
echo "Entered Name : " $Name
echo "Directory of File : "
pwd
echo "Name of File :" $0
