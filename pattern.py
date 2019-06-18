import sys

n = int(sys.argv[1])

for i in range(0,n):
    for j in range(0,i+1):
        print("* "),
    print("\r")

for i in range(n,0,-1):
    for j in range(i+1,0,-1):
        print("* "),
    print("\r")
