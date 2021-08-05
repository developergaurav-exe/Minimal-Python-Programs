def fac(n=2):
                f=1
                for i in range(n):
                                f=f*(i+1)
                return f
n=int(input('enter no: '))
print('Factorial:',fac(n))
