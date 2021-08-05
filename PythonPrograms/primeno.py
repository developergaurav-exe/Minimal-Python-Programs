n=int(input('Enter a number: '))
if n>1:
        for i in range(2,n):
                if n%i==0:
                                print('It is not a prime number')
                                break
        else:
                print('IT is a prime number')
else:
                print('It is not a prime number')

                                
                                
