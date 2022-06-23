# Hackllebarde 2 : Memory Dump Forensics

## Task

There was a breach and we are given a memory dump to investigate for an URL, a malicious executable, an IP adress and a port number.

## Process

First, we look for a banner in our memory dump to try to figure out what OS the machine was running on using volatility 3.


```powershell
PS C:\Users\Ravaka\Desktop\volatility3> python vol.py -f ..\pentesting\weirdfiles\forensics\ransomware2\dumpmem.raw banners.Banners
Volatility 3 Framework 2.2.0
Progress:  100.00               PDB scanning finished
Offset  Banner

0x33af3a58      Linux version 5.4.0-107-generic (buildd@lcy02-amd64-070) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #121~18.04.1-Ubuntu SMP Thu Mar 24 17:21:33 UTC 2022 (Ubuntu 5.4.0-107.121~18.04.1-generic 5.4.174)
0x3b2001a0      Linux version 5.4.0-107-generic (buildd@lcy02-amd64-070) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #121~18.04.1-Ubuntu SMP Thu Mar 24 17:21:33 UTC 2022 (Ubuntu 5.4.0-107.121~18.04.1-generic 5.4.174)
0x3c196dd4      Linux version 5.4.0-107-generic (buildd@lcy02-amd64-070) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #121~18.04.1-Ubuntu SMP Thu Mar 24 17:21:33 UTC 2022 (Ubuntu 5.4.0-107.121~18.04.1-generic 5.4.174)
```

We need a Linux Kernel which version is 5.4.0-107 that has been compiled using gcc 7.5.0. So we replicate the same setup in virtual machine and use the kernel to retrieve the symbol and type information needed for the analysis of our memory dump.

To install the correct kernel :

```sh
$ sudo apt install linux-image-5.4.0-107
$ sudo apt install -y linux-headers-$(uname -r)
```

Then we install gcc and check if it's the right version :

```sh
$ sudo apt install gcc
$ gcc --version
gcc (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
```

Well it's all good !

We can now clone volatility 2 and head to the tools to create the profile.

```sh
$ cd volatility/tools/linux && make
```

With the file created we can now analyse the dump. First, we look for the IP adress and the port using :

```sh
$ python vol.py --profile=LinuxUbuntu_5_4_0-107-generic_profilex64 -f ../dumpmem.raw linux_netstat
```
We find a suspicious TCP connection.
```
TCP      192.168.61.2    :13598 192.168.61.137  :38088 ESTABLISHED                    nc/2647
```
From that we have 2 parts of our flag:
- Attackers IP Adress : 192.168.61.137
- Port used on the machine to exfiltrate data : 13598

Then we can look at the processes for our malicious executable :
```
$ python vol.py --profile=LinuxUbuntu_5_4_0-107-generic_profilex64 -f ../dumpmem.raw linux_psaux
```

We look and we find our malicious executable name :
```
2645   1000   1000   /usr/bin/python3 ./JeNeSuisPasDuToutUnFichierMalveillant        
```
Finally we need to find out the URL of a ressource the attacker accessed during the attack :
```
$ strings dumpmem.raw | grep 'http://'
```
And after getting Rick Rolled a few times we did it ! We found the last part of our flag which is a link to a hacking course : https://www.youtube.com/watch?v=3Kq1MIfTWCE


Flag : 404CTF{192.168.61.137:13598:JeNeSuisPasDuToutUnFichierMalveillant:https://www.youtube.com/watch?v=3Kq1MIfTWCE}

