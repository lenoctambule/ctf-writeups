
# Utilisateur suspicieux 

## Part 1

### Task

We need to investigate a discord bot that we find out to be Je suis un gentil humain#0364.

Seems like there's the command !chercher that let's you search inside a database. So by trial and error we find the flag with :
``` 
!chercher "UNION SELECT * FROM password#
```
Flag : 404CTF{D1sc0rd_&_injection_SQL}

## Part 2 

Here we gain access to the debugger which is a shell stripped out of alot of commands. We have echo so to print the contents of flag.txt without cat : 
```
$ echo "$(<flag.txt)"

```