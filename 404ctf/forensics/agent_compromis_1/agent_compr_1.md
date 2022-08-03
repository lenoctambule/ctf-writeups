# Agent Compromis 1

## Task

We have to find out what the attacker downloaded from a network capture.

## Process 

We can assume he downloaded from a browser so we just add this filter to get all the HTTP requests : 
```
http
```
And we scroll down we find a GET method HTTP request for a file named exfiltration.py.

![]( pics\cap1.PNG "")

Right after we get the response with the contents of the file inside and at the very end of it there is our flag. We save the file for later use because it'll be useful.

Flag : 404CTF{t3l3ch4rg3m3n7_b1z4rr3}
