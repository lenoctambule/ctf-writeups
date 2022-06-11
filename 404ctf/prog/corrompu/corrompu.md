# Corrompu

## Task

Here we are given corrupted base64 strings and we have to send them back uncorrupted in binary

## Process

We have to figure out what is wrong using the example : Rmх%hZуА*6KQ
First, we see that there are characters that are not base64 and then there is the thing that we don't see. If we convert this string to bytes  we get this :
```python
>>> a = 'Rmх%hZуА*6KQ'
>>> print( [ hex(ord(i)) for i in a ] )
['0x52', '0x6d', '0x445', '0x25', '0x68', '0x5a', '0x443', '0x410', '0x2a', '0x36', '0x4b', '0x51']
```
We see that there are cyrillic characters mixed up in there for example for the 'x' instead of 0x78 we get 0x445.

We know what we have to do :
1) Escape all the non base64 characters
2) Replace the cyrillic alphabet letters to their respective characters
3) Convert everything to binary
4) And there's one last step that you find out at the end which is that to get the flag we have to assemble into a file all the uncorrputed base64.

Here's my code to do all of that :

```python
from pwn import *
import string

host = 'challenge.404ctf.fr'
port = 30117 
connection = remote(host,port)

cyrillic_translit={0x410 : 'A', 0x430: 'a',
0x412: 'B', 0x432 : 'b',
0x421: 'C', 0x441 : 'c',
0x415: 'E', 0x435: 'e',
0x41a: 'K', 0x43a : 'k',
0x41c: 'M', 0x43c : 'm',
0x41d: 'H', 0x43d : 'h',
0x41e : 'O', 0x43e : 'o',
0x420 : 'P', 0x440 : 'p',
0x422 : 'T', 0x0442 : 't',
0x423 : 'y', 0x443 : 'y',
0x425 : 'X', 0x445 : 'x'}

f = open('output', 'wb')

b64_chrs = string.ascii_letters + '0123456789' + '+/'

print(b64_chrs)

def esc_nonascii(s):
    res = ""
    for i in s :
        if i in b64_chrs :
            res += i
    return res

def cyr_translit(s):
    res = ""
    for i in s :
        if ord(i) in cyrillic_translit.keys() :
            res += cyrillic_translit[ord(i)]
        else :
            res += i
    return res

def uncorrpt(s):
    a = esc_nonascii(cyr_translit(s))
    print(a)
    c = a + "=" * ( -len(a) % 4 )
    b64_bytes = base64.b64decode(c)
    f.write(b64_bytes)
    d = [ i for i in b64_bytes]
    b = [ bin(int(i))[2:].zfill(8) for i in d]
    return ''.join(b)

for i in range(6) :
    print(connection.recvline())

for i in range(250) : 
    print(connection.recvuntil(": "))
    line = connection.recvline().decode()
    connection.sendline(uncorrpt(line))
    print(connection.recvline())

print(connection.recv())
```
Then we get this [audio file](https://github.com/lenoctambule/ctf-writeups/blob/main/404ctf/prog/corrompu/output.mp3).

Flag : 404CTF{L4_B4S3_64_3FF1C4C3_M41S_C4PR1C13US3}