n=int(input('enter the no of classes'))
dict1=dict()
for i in  range(1,n+1):
                cl=input('input enter the class name')
                cl_teacher=input('enter the class teacher name: ')
                dict1[cl]=[cl_teacher]
print(dict1)
