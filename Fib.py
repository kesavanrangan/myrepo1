import sys
import datetime

num = int(sys.argv[1])

a,b = 0,1

for i in range(num):
    print("\n--------- Row: %d--------\n" %(i+1))
    print(a)
    a,b = b,a+b
    x = datetime.datetime.now()
    print(" \n\n")
    print(x.strftime("%H:%m:%S %b-%d-%Y"))

print("\n The file now ends here!!!")
