import sys

num = int(sys.argv[1])

a,b = 0,1

for i in range(num):
    print("\n--------- Row: %d--------\n" %(i+1))
    print(a)
    a,b = b,a+b
