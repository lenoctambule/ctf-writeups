# 8 vers 10 : Reading docs FTW

This one is full-on about reading documentation or videos about fiber optics.

## Task

We have intercepted a message sent by an Hallebarde member. We need to find out what he sent out.

## Process

So we are given a text file full of floating point numbers. The first thing I do in this case is drawing a graph of this using pyplot and this is the output we get :



This is a digital signal modulated by Amplitude-shift Keying. We can demodulate it by simply retrieving the local extremums for each period and using offsets to define if it represents a 0 or 1 :

```python
lines = open("8vers10.txt","r").readlines()
y = list()

for l in lines :
    y.append(float(l))

x = [ i for i in range(len(y)) ]

bin_l = []

for i in range(2, len(y)) :
    if y[i] < y[i-1] and y[i-1] > y[i-2] :
        if y[i-1] > 1.34 :
            bin_l.append(1)
        else :
            bin_l.append(0)
            
print(bin_l)
```

I'm scratching my head looking at those 0s and 1s, they don't seem to mean anything. So I decided to bring out the big guns : Google. I looked at the title because it doesn't really mean anything to me so I searched for "8 10 encoding"

And what we find is 8b/10b encoding used in fiber optics. From the Wikipedia page it says that it is *"a line code that maps 8-bit words to 10-bit symbols to achieve DC balance and bounded disparity, ... blablabla"* (I didn't get any of that).

![](./pics/bruh.jpg "Spikey round")

 But if we read a bit further we find something readable by mortals: 
 > *"the difference between the counts of ones and zeros in a string of at least 20 bits is no more than two, and that there are not more than five ones or zeros in a row"*
 
Our bits just matches that description. So we just need to decode it and for that we just import the encdec8b10b library and it'll do the job for us :

```python
bin = bin(int(''.join(map(str, bin_values)), 2) << 1)
flag = []
for i in range(2,len(bin)-1,10):
    byte = int(bin[i:i+10:1],2)
    ctrl, decoded = encdec.dec_8b10b(byte)
    flag.append(chr(decoded))

print(''.join(flag))
```
Execute the script and here it is our flag :
```sh
ubuntu@ubuntu-acer:~/ctf/misc$ python3 decode-8vers10.py
404CTF{d3C0d3r_l3_8b10b_c_f4c1l3}
```







