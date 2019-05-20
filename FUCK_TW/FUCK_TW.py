#!/usr/bin/python

import os

cidr_old = ''
cidr_new = 'TW_ipv4-190420.txt'
number = 1

if cidr_old:
    with open(cidr_old) as f:
        for i, line in enumerate(f, start=1):
            if not line.startswith('#') or not line.strip():
                print('{} = {}'.format(i, line.strip()))
                os.system('ufw delete deny from {} to any'.format(line.strip()))
else:
    print('file not specified')

if cidr_new:
    with open(cidr_new) as f:
        for i, line in enumerate(f, start=1):
            if not line.startswith('#') or not line.strip():
                print('{} = {}'.format(i, line.strip()))
                os.system('ufw insert {} deny from {} to any'.format(number, line.strip()))
else:
  print('file not specified')