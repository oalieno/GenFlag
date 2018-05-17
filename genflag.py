#!/usr/bin/env python3
import re
import sys
import string
import random

if len(sys.argv) != 2:
    print("USAGE : ./genflag.py FLAG{xxxxx}")
    exit(0)

flag = sys.argv[1]

candidates = {}

for c in string.ascii_lowercase:
    candidates[c] = set([c, c.upper()])
    candidates[c.upper()] = set([c, c.upper()])

for c in string.digits:
    candidates[c] = set([c])

def link(x, y):
    candidates[x].add(y)
    candidates[y].add(x)

link('o', '0')
link('O', '0')
link('l', '1')
link('e', '3')
link('a', '4')

m = re.match("(.*{)(.*)(})", flag)
if m:
    prefix, flag, postfix = m.group(1), m.group(2), m.group(3)
else:
    prefix, flag, postfix = '', flag, ''

result = ''
for c in flag:
    if c in string.ascii_letters + string.digits:
        result += random.sample(candidates[c], 1)[0]
    else:
        result += c

print(prefix + result + postfix)
