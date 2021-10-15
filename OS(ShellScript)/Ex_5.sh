#Write a Shell Scrip that compile all C fiiles in your home directory and create executable files .


#! /bin/sh
for F in *.c
do
gcc -o ${F%.c}".out" $F
echo File $F is successfully compiled.
done
