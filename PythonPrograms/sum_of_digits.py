n=int(input('enter a no: '))
sum=0
for i in range(n): 
                sum=sum+n%10
                n=n//10
print(sum,'is sum of digits')
