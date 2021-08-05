n=int(input('Total no of list items: '))
list1=[]
for i in range(0,n):
                item=int(input('Enter the items:'))
                list1.append(item)
print('List is-:',list1)
s=int(input('Enter the item to search: '))
total_s=0
for i in range(0,n):
                if s==list1[i]:
                             total_s+=1
                print(s,'is present in the list',total_s,'times')
                else:
                                print(s,'is not in the list')
                                
