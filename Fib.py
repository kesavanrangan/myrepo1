num = int(input("Enter the number of fields: "))

a,b = 0,1

for i in range(num):
    print(a)
    a,b = b,a+b
    print("\nDONE WITH THIS ROW\n")
