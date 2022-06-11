# 128Code128 : Decoding Code 128

We are given base64 strings and converted we get pngs of barcodes encoded in Code 128 like the name of the challenge implies.

![](./pics/cbimage.png "cbimage.png")

If I sum up what this code does : 
1. It reads the base64 given by remote.
2. It converts it into an image stored temporarily as temp-img.png.
3. It reads the bits by reading the horizontal pixels. 
3. And finally decodes the code 128 using a text file that I extracted from Wikipedia's page table using this online [converter](https://www.convertcsv.com/html-table-to-csv.htm) as a conversion table and then I shift the resulting values by 32 to get the ASCII.

```python
import base64
from pwn import *
from PIL import Image

f = open("table128", "r")
l = f.readlines()
code128 = [ i.strip('\n\r') for i in l ]

def bitstring_to_bytes(s):
    hex_data = []
    for i in range(0,len(s)//11):
    	pos = i * 11
    	print(s[pos:pos+11:1])
    	hex_data.append(code128.index(s[pos:pos+11:1])+32)
    	
    str_data = ''.join([ chr(i) for i in hex_data ])
    return bytes(str_data, 'utf-8')


def code128reader(image):
    img = Image.open(image)
    pix = img.load()
    bin_values = ''
    for i in range(0,img.width,1):
        bin_values += str("1" if pix[i,2] == (0,0,0) else "0")
    print(bin_values)
    hex_values = bitstring_to_bytes(bin_values)
    return hex_values
    
def construct_img(b64_string):
    data_bytes = base64.b64decode(b64_string)
    with open("./temp-img.png", "wb") as png :
    	png.write(data_bytes)

if __name__ == "__main__":

    host = 'challenge.404ctf.fr'
    port = 30566
    conn = remote(host, port)
    
    print(conn.recvline())
    barcode = ''.join([ chr(i) for i in conn.recvline()])
    print(barcode)
    construct_img(barcode)
    mdp = code128reader("temp-img.png")
    print(conn.recv())
    print(mdp)
    conn.sendline(mdp)
    
    for i in range(127):
    	print(conn.recvline())
    	print(conn.recvline())
    	barcode = ''.join([ chr(i) for i in conn.recvline()])
    	print(barcode)
    	construct_img(barcode)
    	mdp = code128reader("temp-img.png")
    	print(conn.recv())
    	conn.sendline(mdp)
    	
    print(conn.recv())

```

Flag : 404CTF{W0w_c0d3_128_4_pLUs_4uCuN_s3cr3t_p0uR_t01}