# Research-Project
HTTP Bruteforcer
Beta is a HTTP Post Request Brute forcer, that recons a site page via a get request, and then builds a post request from supplied user input.

Usage and help:  
  beta.py [-h] [-target TARGETS [TARGETS ...]]
               [-user USERNAME [USERNAME ...]] [-pass PASSWORD [PASSWORD ...]]
               [-target_file TARGETFILE] [-user_file USERNAMEFILE]
               [-pass_file PASSWORDFILE]

An inherently broken HTTP POST Request Brute forcer.

optional arguments:
  -h, --help            show this help message and exit
  -target TARGETS [TARGETS ...], --targets TARGETS [TARGETS ...]
                        Please specify your target URL, for multiple use a
                        space delimitation.
  -user USERNAME [USERNAME ...], --username USERNAME [USERNAME ...]
                        Specify usernames for logging into the site. For
                        multiple use space delimitation
  -pass PASSWORD [PASSWORD ...], --password PASSWORD [PASSWORD ...]
                        Specify passwords for logging into the site. For
                        multiple use space delimitation
  -target_file TARGETFILE, --targetfile TARGETFILE
                        Specify the filepath to the target file. It must
                        contain url's of the target site, one per line
  -user_file USERNAMEFILE, --usernamefile USERNAMEFILE
                        Specify the filepath to the user file. It must contain
                        emails or username, one per line
  -pass_file PASSWORDFILE, --passwordfile PASSWORDFILE
                        Specify the filepath to the password file. It must
                        contain passwords, one per line

Common usage is beta.py -target -user -pass or beta.py -user_file -target_file
-pass_file

Basic HTTP Post Brute Forcing.


Please do pip install of the following dependencies (requests, cssselect, lxml) Coded in Python 3.7
