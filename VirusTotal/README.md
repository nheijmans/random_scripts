# VirusTotal API script
The script is build as a stand-alone tool that can be used from the CLI or
it can be imported by other scripts for automated analysis. The goal was to
keep it as simple as possible for the end-user so the script only has two 
commands: submit and search. The module will figure out what type of sample
you want to search or submit.

## Search
Currently the script allows you to search VirusTotal for three objects:
* Files
* Hashes (MD5, SHA-1 and SHA-256)
* URL's

### Examples
```
Search for a file:
python virustotal.py search /path/to/file/sample.exe

Search for a hash:
python virustotal.py search 28af9ab564f17fcf969a08450b61d6c7

Search for a URL:
python virustotal search http://www.google.nl
```
## Submit
To submit a file or a URL to VirusTotal you can use the submit command

### Examples
```
Submit a file:
python virustotal.py submit /path/to/file/sample.exe

Submit a URL:
python virustotal.py submit http://www.google.nl
```

## Features to build
* Search for a domain
* Search for a IP
* Post a comment
