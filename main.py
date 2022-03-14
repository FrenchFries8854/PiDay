"""
Find the first ten digit prime number in the sequence of numbers that make up pie
"""
import math
import json

import sympy

pi = json.loads(open(r"pi.json", encoding="utf8").read())

piNew = ""
for x in pi:
    if x == " ":
        pass
    else:
        piNew += x


first = ""
for x2 in range(len(piNew)):
    if sympy.isprime(int(piNew[x2:x2 + 10])):
        first = piNew[x2:x2 + 10]
        print(first)
        print(x2, x2 + 10)
        break
    else:
        pass

newTotal = 0
for x3 in first:
    newTotal += int(x3)
print(newTotal)