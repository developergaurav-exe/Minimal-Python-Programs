n=int(input('Total no of list items: '))
list1=[]
for i in range(0,n):
                item=int(input('Enter the items:'))
                list1.append(item)
print('List is -',list1)
min=list1[0]
for j in range(0,n):
                if list1[i]<min:
                   min=list1[i]
print('Minimum value in this list is-',min)
