import sys

num = int(sys.argv[0])

a,b = 0,1

for i in range(num):
    print(a)
    a,b = b,a+b
