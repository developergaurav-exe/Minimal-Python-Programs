#to find odd no and multiplat by 2
n=int(input('Total no of list items: '))
list1=[]
for i in range(0,n):
                item=int(input('Enter the items:'))
                list1.append(item)
print('list is',list1)
for j in range(0,n):
                if j%2==1:
                                list1[j]*=2
print('the list created is',list1)
