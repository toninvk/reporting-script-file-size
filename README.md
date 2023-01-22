##### Week 2: Create a Reporting Script #####

First, import the os module with packages getsize, abspath and join to make the Python script traverse any path in the directory.

The first for loop walks through the directory and finds any files that include '.'. Next, the file names are joined with the path to get the full path. Finally, the full path is printed for the files in the directory.

Second, the scripts prints files that meet certain conditions:
(1) No more than 20 files
(2) Files larger  than a specific size in megabytes

(1) The second for loop in the script finds all files in the directory and, using a counter returns the first 20 files in the directory.
(2) The third (and last) for loop in the directory uses the getsize package to save the megabyte size of the files in the directory.
    Using an if statement, the script return all files smaller than 15000mb.
