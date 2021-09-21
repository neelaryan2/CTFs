#!/bin/bash
for (( c=0; c<=27; c++ ))
do  
   wget --timeout=60 "http://maze.noobarmy.org/projects/justsomerandomfoldername/image-$c.png"
done
