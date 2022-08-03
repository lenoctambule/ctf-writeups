# Weak Signature : Tricking unsecure file signing

# Task

We have a remote server that executes a python script if it is signed.

# Process

Take a look at that part of the script :

```python
def checksum(data: bytes) -> int:
    # Sum the integer value of each byte and multiply the result by the length
    chksum = sum(data) * len(data)

    return chksum


def compute_signature(data: bytes, private_key: int, mod: int) -> int:
    # Compute the checksum
    chksum = checksum(data)
    # Sign it
    signature = pow(chksum, private_key, mod)

    return signature
```

The python script that signs those files just sums each byte and encrypts the sum using a private key that we don't have access to. But we have an already signed sample. And since it's just a sum, we can just copy the header of the file and make it so that the body of our file has the same sum hence the same signature as the already signed sample file.

We execute our [script](https://github.com/lenoctambule/ctf-writeups/blob/main/404ctf/crypto/weak_signature/rev-sign.py) send it to the server and voilà ! Our flag : 
```
404CTF{Th1s_Ch3cksum_W4s_Tr4sh}
```
