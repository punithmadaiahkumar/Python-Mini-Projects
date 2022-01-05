# Check Website Connectivity


### Tech Stack:
+ Python

### Libraries used:
+ csv
+ requests

###  Pre-requirements:
+ install csv and requests

### To execute the project:
+ Run check_connectivity.py

### Note: 
This directory contains a simple tool to check connectivity to a number of web sites.
+ The input file `websites.txt` should contain web site URLs, one per line.
+ The output file `website_status.csv` contains a two-column report with
+ the URL of each checked site and its status.
+ The script simply checks whether the web server returns a 200 status code.
+ The output file will be overwritten each time you run the tool.
+ This project uses the third-party library
[requests](https://requests.readthedocs.io/)
as well as the `csv` module from the Python standard library.
