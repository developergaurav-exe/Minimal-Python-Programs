total_even=0
total_odd=0
for i in range(1,11):
                num=int(input('enter the num: '))
if num%2==0:
                total_even=total_even+num
               
else:
                total_odd=total_odd+num
print('total of odd num: ',total_odd)
print('total of even num: ',total_even)
