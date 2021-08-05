n=int(input('Total no. of Subjects: '))
max_marks=int(input('Enter max marks:'))
max_marks=max_marks*n
list1=[]
for j in range(0,n):
                item=int(input('Enter the marks:'))
                list1.append(item)
print('list is:',list1) 
total=0
per=0
for i in range(0,len(list1)):
                total+=list1[i]
per=(total/max_marks)*100
print('Total Marks:',total)
print('Percentage:',per)
