#!/usr/bin/python
"""
CopyRight By 2019, Made by Nicht
> OpenSource GNU GPL.Ver3

"""
import os

cidr_old = ''
cidr_new = 'IN_ipv4-190520.txt'
number = 1

if cidr_old:
    with open(cidr_old) as f:
        for i, line in enumerate(f, start=1):
            if not line.startswith('#') or not line.strip():
                print('{} = {}'.format(i, line.strip()))
                os.system('iptables -D FUCKCN -p tcp -s {} -j DROP'.format(line.strip()))
else:
    print('file not specified')

if cidr_new:
    with open(cidr_new) as f:
        for i, line in enumerate(f, start=1):
            if not line.startswith('#') or not line.strip():
                print('{} = {}'.format(i, line.strip()))
                os.system('iptables -N FUCKCN')
                os.system('iptables -A FUCKCN -p tcp -s {} -j DROP'.format(number, line.strip()))
else:
  print('file not specified')
