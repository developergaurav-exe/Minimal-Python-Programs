rows=int(input('Enter the number of rows: '))
asc=65
for i in range (1,rows+1):
                for j in range(1,i+1):
                    print (chr(asc),end=" ")
                print()
                asc=asc+1
