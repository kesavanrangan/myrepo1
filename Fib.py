import sys

num = int(sys.argv[1])

a,b = 0,1

for i in range(num):
    print(a)
    a,b = b,a+b
    print("\nDONE WITH THIS ROW\n")
    print("\nANOTHER ROW STARTS . . . . . \n")
