#Question 6 pg-6.17
n=int(input('enter the no of students'))
dict1=dict()
for i in  range(1,n+1):
                name=input('enter the student name')
                per=input('enter the percentage: ')
                dict1[name]=[per]
print(dict1)
n1=input('enter the name you want to delete')
dict1.pop(n1)
print(dict1)
