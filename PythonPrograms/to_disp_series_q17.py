#to display 1+(1+2)+(1+2+3)+(1+2+3.....n)
n=int(input('NO of terms you want to display:'))
sum2=0
for i in range(1,n):
                sum1=0
                for j in range(1,i+1):
                                sum1=sum1+j
                print('Sum is',sum1)
                sum2=sum2+sum1
print("=",sum2)
                
 
