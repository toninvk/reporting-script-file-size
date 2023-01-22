#Week 2: Create a Reporting Script for File Sizes

#1. Create a new Github repository with a README and a single python file.
#2. Make your Python script accept an argument to traverse any path (don't hardcode the path!)

#Import packages
import os 
from os.path import abspath, join, getsize

# producing absolute paths
for top_dir, directories, files in os.walk('.'):
    for directory in directories:
        print(abspath(join(top_dir, directory)))
    for _file in files:
        print(abspath(join(top_dir, _file)))
    break

#Use different options in the script for reporting:
#Return no more than 20 files
count = 0
for top_dir, directories, files in os.walk('.'):
    for _file in files:
        print(_file)
        count +=1
    if count >= 19:
        break


#Return files larger  than a specific size in megabytes (15000mb)

for top_dir, directories, files in os.walk('.'):
    for _file in files:
        size = getsize(_file)
        if size >= 15000:
            print(_file)  

