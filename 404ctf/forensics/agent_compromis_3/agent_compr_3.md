# Agent Compromis 2

## Task 

We have to reconstruct the files and we are warned that some packets may have been lost.

## Process

So just like before we study exfiltration.py and then use our understand to write a fairly simple python script that reconstructs those : 

```python
import csv


resp_data = []
def read_csv(file_name):
    res = []
    with open(file_name, newline='') as csvfile :
        respreader = csv.reader(csvfile, delimiter=",")
        for i in respreader :
            index = i[7].find("hallebarde.")
            if index != -1 or index != 0 :
                res.append(i[7][:index-1])
    return res


#print(resp_data)
def write_data(resp_data):
    file_n = 0
    i=0
    while i < len(resp_data) :
        if resp_data[i] == "626567696E" :
            print("Created file-"+str(file_n))
            out_f = open("file-"+str(file_n), "wb")
            file_n += 1
            j = i+1
            while resp_data[j] != "656E64" :
                out_f.write(bytes.fromhex(resp_data[j]))
                j += 1
            i = j
            out_f.close()
        i += 1

resp_data = read_csv('dns-responses.csv')
print(len(resp_data))
write_data(resp_data)

#req_data = read_csv('dns-req.csv')
#print(len(resp_data))
#write_data(req_data)
```

Finally, we find multiple files and all of them are there to bamboozle us except one : the pdf file (it's just named file-2 because I got extremely lazy while coding).

We check for corruption in the error file using qpdf tool and we find this :
```sh
$ qpdf --check file-2
WARNING: file-2: file is damaged
WARNING: file-2 (xref table, offset 9813): invalid xref entry (obj=13)
WARNING: file-2: Attempting to reconstruct cross-reference table
checking file-2
PDF Version: 1.6
File is not encrypted
File is not linearized
```

We check the cross ref table using an hex editor and there is indeed a missing line. 
```
xref
0 14
0000000000 65535 f
0000008983 00000 n
0000000019 00000 n
0000000252 00000 n
0000009152 00000 n
0000000272 00000 n
0000008026 00000 n
0000008047 00000 n
0000008237 00000 n
0000008640 00000 n
0000008896 928 00000 n
0000009251 00000 n
0000009348 00000 n
```
We can fix this by extrapolating and adding in the line manually which gives us this cross ref table :

```
xref
0 14
0000000000 65535 f
0000008983 00000 n
0000000019 00000 n
0000000252 00000 n
0000009152 00000 n
0000000272 00000 n
0000008026 00000 n
0000008047 00000 n
0000008237 00000 n
0000008640 00000 n
0000008896 00000 n
0000008928 00000 n
0000009251 00000 n
0000009348 00000 n
```

Then if we go look at object 11, we notice that it's location is off compared to what the cross ref table says. Moreover if we look at the object 10 right behind it, we notice that it's missing endobj and more. 

![](.\pics\cap1.PNG "")

From that we can easily extrapolate what the content was and repair it. We add in the missing part which is : 
```
 0 R >>[LF]endobj[LF][LF]
``` 
Afterwards the object number 11 is at the right place (starts at byte 8928 just like in the cross ref table) and it should look like this : 

![](.\pics\cap2.PNG "")

And finally we try to open it and here is our flag !

Flag : 404CTF{DNS_3xf1ltr4t10n_hallebarde}