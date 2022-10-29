from pwn import *
import json

proc = remote("161.35.33.243",32087)

print(proc.recv().decode())
print(proc.recv().decode())
proc.sendline(b'{"option":"3"}')
print(proc.recv().decode())
print(proc.recv().decode())
proc.sendline(b'{"modes": ["CTR"]}')
print(proc.recv().decode())
print(proc.recv().decode())
proc.sendline(b'{"option":"1"}')
ct_flag = json.loads(proc.recv().decode())['ciphertext']
print(proc.recv().decode())
p_known = b"this is known ciphertext i hope it works bc im very angry but a little bit longuer to be sure"
proc.sendline(b'{"option":"2"}')
print(proc.recv().decode())
proc.sendline(b'{"plaintext":"'+p_known+b'"}')
ct_known = json.loads(proc.recv().decode())['ciphertext']
print(proc.recv().decode())
proc.close()
blob = xor(bytes.fromhex(ct_known), bytes.fromhex(ct_flag))
p_flag = xor(blob, p_known)[:len(bytes.fromhex(ct_flag))].decode()
print(f'{p_flag=}')
