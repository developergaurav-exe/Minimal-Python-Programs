#Fibonacci Series 0112358
t=int(input('Enter the no of terms from the series: '))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
n=1
while (n<=(t-2)):
                c=a+b
                print(c,end=" ")
                a=b
                b=c
                n=n+1#loop variable to terminate loop
                
