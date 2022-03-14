"""
Find the first ten digit prime number in the sequence of numbers that make up pie
"""
import math
import json
from pprint import pprint

import sympy

pi = json.loads(open(r"pi.json", encoding="utf8").read())

piNew = ""
for x in pi:
    if x == " ":
        pass
    else:
        piNew += x


first = []
for x2 in range(len(piNew)):
    if sympy.isprime(int(piNew[x2:x2 + 10])):
        newTotal = 0
        for x3 in str(piNew[x2:x2 + 10]):
            newTotal += int(x3)
        if newTotal == 59:
            first.append(piNew[x2:x2 + 10])
            print(first[-1])
            print(x2, x2 + 10)
    else:
        pass

pprint(first[50])
