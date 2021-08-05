#default parameter programme
#1
def power(n=3,m=6):#default value dono mai dalna padega wrna nhi chalega
                pw=n**m
                return pw
a=int(input('Enter the number'))
b=int(input('Enter the number to which power is to be found:'))
res=power(a,b)
print('Answer is:',res)
print('Answer2,:',power(a))
print('Answer3:',power())
#2
def avg(n1,n2,n3):
                ag=(n1+n2+n3)/3
                return ag
n1=int(input('Enter the number1:'))
n2=int(input('Enter the number2:'))
n3=int(input('Enter the number3:'))
print('Average:',avg(n1,n2,n3))
#3
def max(n1,n2,n3):
                if n1>n2:
                         if n1>n3:
                                 l=n1
                         else:
                                 l=n3
                else:
                         if n2>n3:
                                 l=n2
                         else:
                                 l=n3
                                 return l
n1=int(input('Enter the number1:'))
n2=int(input('Enter the number2:'))
n3=int(input('Enter the number3:'))
print('largest no: ',max(n1,n2,n3))
                                
