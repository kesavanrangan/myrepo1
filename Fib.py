import sys

num = int(sys.argv[1])

a,b = 0,1

for i in range(num):
    print("\n---------{%d}--------\n",%(str(i+1)))
    print(a)
    a,b = b,a+b
