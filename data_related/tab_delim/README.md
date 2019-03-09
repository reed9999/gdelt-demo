# Directory `tab_delim` README
This directory is temporary, but I'm placing it in git to document my troubleshooting process.
I have some rather large files that were created on Hive on AWS EMR, when I sought to extract
some features about actor dyads and event codes.

I want to import the whole thing to MySQL but it chokes on the delimiter character. It was 
supposed to be tab-delimited, and MySQL is supposed to handle tab-delimited files, but it
doesn't work. (How?) The rogue delimiter shows up in vim as ^A.

To further spite me, MySQL now appears to work just fine on my tiny subset of a file, 
`original_delim.csv`. So I will try another one.


Note:For some reason I named the file where I replaced this character with my own tabs as
`conventional_spaces.csv` at first, but it should be.


