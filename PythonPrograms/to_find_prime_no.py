n=int(input('Enter the Number: '))
if n>1:
       for i in range(2,n):
                if n%i==0:
                    p=1
       if p==0:
                   print(n,' is the prime number')
       else:
                print(n,' is not a prime number')
else:
     print(n,'is not the prime number')
        
