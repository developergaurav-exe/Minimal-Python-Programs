def prime():
                print('=======To Find Prime Number======= ')
                num=int(input('Enter Number: '))
                if num%10==0 or (num%10)%2==0:
                                print('This is not a Prime number')
                                prime()
                else:
                                print('This is a prime number')
                                prime()
prime()
