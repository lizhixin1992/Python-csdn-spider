# coding=utf-8

from scapy.all import *

conf.verb = 0

data = "111112131231231231231231"

p = IP(dst="220.181.111.188")/TCP()/data
r = sr1(p)
print(r.summary())