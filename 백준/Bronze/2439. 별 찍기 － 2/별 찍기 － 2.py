import sys

a = int(sys.stdin.readline())

for i in range(a):
        print(" "*(a - 1 - i) + "*"*(i + 1) + " ")