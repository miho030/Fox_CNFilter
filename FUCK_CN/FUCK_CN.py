#!/usr/bin/python
"""
CopyRight By 2019, Made by Nicht
> OpenSource GNU GPL.Ver3
"""

# import major Libs
from pyfiglet import Figlet
import os

# simple logo printing
f = Figlet(font='slant')
print(f.renderText('FUCK CHINA'))


cidr_old = ''
cidr_new = 'CN_ipv4-190420.txt'
number = 1

if cidr_old:
    with open(cidr_old) as f:
        for i, line in enumerate(f, start=1):
            if not line.startswith('#') or not line.strip():
                print('{} = {}'.format(i, line.strip()))
                os.system('ufw delete deny from {} to any'.format(line.strip()))
else:
    print("[-]", "file not specified")

if cidr_new:
    with open(cidr_new) as f:
        for i, line in enumerate(f, start=1):
            if not line.startswith('#') or not line.strip():
                print('{} = {}'.format(i, line.strip()))
                os.system('ufw insert {} deny from {} to any'.format(number, line.strip()))
else:
    print("[-]", "file not specified")
