n=int(input('Total no of list items: '))
list1=[]
for i in range(0,n):
                item=int(input('Enter the items:'))
                list1.append(item)
print('the created list is',list1)
l=len(list1)
a=0
b=1
while a<l:
                if(list1[a]==list1[b]):
                                del (list1[b])
                                l=l-1
                b=b+1
print(list1)
                
