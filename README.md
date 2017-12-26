# IP Calculator
Written on Python3
This programm calculates network mask, first, last, and broadcast addresses from user input.
The input is CIDR IP address with network mask.
For 192.168.1.1/20 the output looks like this:

IP address: 192.168.1.1
Network:
192      168      0        0       
11000000 10101000 00000001 00000001

Mask:
/20
255      255      240      0       
11111111 11111111 11110000 00000000

First host: 192.168.0.1
Last host:  192.168.15.254
Broadcast:  192.168.15.255
Maximum hosts: 4096

So, it's just easy way to make IP-calculator with Python3
