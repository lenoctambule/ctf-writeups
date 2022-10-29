
# Reversing : Secure transfer

# Task

We are given 2 files : an executable and a packet capture of an exchange.

# Process

We launch it in ghidra and read the pseudo code to find out what is happening. And we find out that the file transfer happenned this way :

```
1) Sender sends length of data
2) Receiver receives and verifies length
3) Sender encrypts the data using AES-CBC and then sends it
4) Receiver receives and verifies that the length corresponds to the real size of the data
5) Receiver decrypts the data using AES-CBC
```

Then we look for the values of variables that interests us the most which are the initialization value and the key.

Finding the initialization value is straight forward :
```c
iv = "someinitialvalue"
```
The key is less straight forward but still easy to get. It's just a bunch of scrambled MOV instructions :
```asm
        001016d5 c6 45 d0 73     MOV        byte ptr [RBP + key], 's'
        001016d9 c6 45 d9 65     MOV        byte ptr [RBP + local_2f],'e'
        001016dd c6 45 d1 75     MOV        byte ptr [RBP + local_37],'u'
        001016e1 c6 45 d2 70     MOV        byte ptr [RBP + local_36],'p'
        001016e5 c6 45 e2 66     MOV        byte ptr [RBP + local_26],'f'
        001016e9 c6 45 e3 6f     MOV        byte ptr [RBP + local_25],'o'
        001016ed c6 45 e4 72     MOV        byte ptr [RBP + local_24],'r'
        001016f1 c6 45 e7 63     MOV        byte ptr [RBP + local_21],'c'
        001016f5 c6 45 da 74     MOV        byte ptr [RBP + local_2e],'t'
        001016f9 c6 45 db 6b     MOV        byte ptr [RBP + local_2d],'k'
        001016fd c6 45 eb 74     MOV        byte ptr [RBP + local_1d],'t'
        00101701 c6 45 ed 6f     MOV        byte ptr [RBP + local_1b],'o'
        00101705 c6 45 d6 65     MOV        byte ptr [RBP + local_32],'e'
        00101709 c6 45 d7 63     MOV        byte ptr [RBP + local_31],'c'
        0010170d c6 45 d5 73     MOV        byte ptr [RBP + local_33],'s'
        00101711 c6 45 e8 72     MOV        byte ptr [RBP + local_20],'r'
        00101715 c6 45 dd 79     MOV        byte ptr [RBP + local_2b],'y'
        00101719 c6 45 de 75     MOV        byte ptr [RBP + local_2a],'u'
        0010171d c6 45 df 73     MOV        byte ptr [RBP + local_29],'s'
        00101721 c6 45 ec 69     MOV        byte ptr [RBP + local_1c],'i'
        00101725 c6 45 e0 65     MOV        byte ptr [RBP + local_28],'e'
        00101729 c6 45 e1 64     MOV        byte ptr [RBP + local_27],'d'
        0010172d c6 45 e5 65     MOV        byte ptr [RBP + local_23],'e'
        00101731 c6 45 e9 79     MOV        byte ptr [RBP + local_1f],'y'
        00101735 c6 45 d8 72     MOV        byte ptr [RBP + local_30],'r'
        00101739 c6 45 d4 72     MOV        byte ptr [RBP + local_34],'r'
        0010173d c6 45 ea 70     MOV        byte ptr [RBP + local_1e],'p'
        00101741 c6 45 ef 21     MOV        byte ptr [RBP + local_19],'!'
        00101745 c6 45 ee 6e     MOV        byte ptr [RBP + local_1a],'n'
        00101749 c6 45 dc 65     MOV        byte ptr [RBP + local_2c],'e'
        0010174d c6 45 d3 65     MOV        byte ptr [RBP + local_35],'e'
        00101751 c6 45 e6 6e     MOV        byte ptr [RBP + local_22],'n'
```
Rewriting it into the right order, it gives us the key : 
```c
key="supersecretkeyusedforencryption!"
```
Finally, now that we know the inner workings of the program. We can decrypt 32bytes of data in packet no. 5 :

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

#key = b"setktiupncoecsryrforneyusedeerp!"
#key = b"seupforctktoecsryusiedeyrrp!neen"
key = b"supersecretkeyusedforencryption!"
iv = b"someinitialvalue"
ct = bytes.fromhex("5f558867993dccc99879f7ca39c5e406972f84a3a9dd5d48972421ff375cb18c")
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)
print(pt)
```

```
output : b'HTB{vryS3CuR3_F1L3_TR4nsf3r}\x04\x04\x04\x04'
```
