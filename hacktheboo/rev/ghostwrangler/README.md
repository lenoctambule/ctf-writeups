# Reversing : Ghost Wrangler

## Task

We get an executable for which we have to find out the contents of a string that is "censored".

## Process

We put it into ghidra and find this in the get_flag function :
```c
  for (local_c = 0; local_c < 40; local_c = local_c + 1) {
    *(byte *)((long)__s + (long)(int)local_c) = _[(int)local_c] ^ 0x13;
  }
```
Then we find out that _ variable points to string data which corresponds to : 
```
[GQh{'f}g wLqjLg{ Lt{#`g&L#uLpgu&Lc'&g2n%s
```
So now that we know that it is a xor cipher, the key is 0x13 and what the ciphertext is. We can do this to retrieve the flag :
```python
print("".join([chr(ord(i)^0x13) for i in "[GQh{'f}g wLqjLg{ Lt{#`g&L#uLpgu&Lc'&g2n%s"]))`
```
```
output : HTB{h4unt3d_by_th3_gh0st5_0f_ctf5_p45t!}6`
```